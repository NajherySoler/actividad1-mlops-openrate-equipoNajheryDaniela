import pandas as pd
 
input_path = "data/raw/openrate_mock.csv"
output_path = "data/processed/openrate_processed.csv"
 
data = pd.read_csv(input_path)
 
categorical_columns = [
    "site",
    "campaign_type",
    "device_os",
    "day_of_week",
    "segment"
]
 
data_processed = pd.get_dummies(
    data,
    columns=categorical_columns,
    drop_first=True
)
 
data_processed.to_csv(output_path, index=False)
 
print("Datos preparados correctamente en data/processed/openrate_processed.csv")
print(data_processed.head())