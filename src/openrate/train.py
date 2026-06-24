import pandas as pd
import yaml

import mlflow
import mlflow.sklearn

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


def evaluate_model(model_name, model, model_params, X_train, X_test, y_train, y_test):
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)

        metrics = {
            "model": model_name,
            "accuracy": accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred),
            "recall": recall_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred),
        }

        mlflow.log_params(model_params)
        mlflow.log_metrics({
            "accuracy": metrics["accuracy"],
            "precision": metrics["precision"],
            "recall": metrics["recall"],
            "f1_score": metrics["f1_score"],
        })

        mlflow.sklearn.log_model(
            sk_model=model,
            name=model_name.lower().replace(" ", "_"),
        )

        print(f"\n===== {model_name} =====")
        print(f"Accuracy : {metrics['accuracy']:.4f}")
        print(f"Precision: {metrics['precision']:.4f}")
        print(f"Recall   : {metrics['recall']:.4f}")
        print(f"F1 Score : {metrics['f1_score']:.4f}")

        return metrics


with open("params.yaml", "r") as file:
    params = yaml.safe_load(file)

mlflow.set_tracking_uri(params["mlflow"]["tracking_uri"])
mlflow.set_experiment(params["mlflow"]["experiment_name"])

data = pd.read_csv(params["data"]["processed_path"])

X = data.drop(columns=["target_opened"])
y = data["target_opened"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=params["split"]["test_size"],
    random_state=params["split"]["random_state"],
)

logistic_params = params["models"]["logistic_regression"]
random_forest_params = params["models"]["random_forest"]

models = [
    (
        "Logistic Regression",
        LogisticRegression(
            max_iter=logistic_params["max_iter"],
            random_state=logistic_params["random_state"],
        ),
        logistic_params,
    ),
    (
        "Random Forest",
        RandomForestClassifier(
            n_estimators=random_forest_params["n_estimators"],
            max_depth=random_forest_params["max_depth"],
            random_state=random_forest_params["random_state"],
        ),
        random_forest_params,
    ),
]

results = []

for model_name, model, model_params in models:
    metrics = evaluate_model(
        model_name,
        model,
        model_params,
        X_train,
        X_test,
        y_train,
        y_test,
    )
    results.append(metrics)

results_df = pd.DataFrame(results)
results_df.to_csv("outputs/model_metrics.csv", index=False)

best_model = results_df.sort_values(by="f1_score", ascending=False).iloc[0]

print("\n===== Mejor modelo =====")
print(f"Modelo seleccionado: {best_model['model']}")
print(f"F1 Score: {best_model['f1_score']:.4f}")