# Predicción de Open Rate con MLOps

## Integrantes

* Najhery Soler
* Laura Medina

---

## Descripción del proyecto

Este proyecto implementa un flujo básico de MLOps para predecir si un usuario abrirá o no una notificación push.

La solución incluye:

* Generación de datos.
* Preparación de datos.
* Entrenamiento y comparación de modelos.
* Seguimiento de experimentos con MLflow.
* Versionamiento de datos mediante DVC.

---

## Objetivo

Construir un flujo de trabajo reproducible y trazable para entrenar, comparar y documentar modelos de clasificación orientados a la predicción del Open Rate de notificaciones push.

---

## Tecnologías utilizadas

* Python 3.13
* Poetry
* DVC
* MLflow
* Pandas
* Scikit-learn
* Git
* GitHub

---

## Estructura del proyecto

```text
MLOpsMaestria/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│
├── src/
│   └── openrate/
│       ├── generate_data.py
│       ├── prepare_data.py
│       └── train.py
│
├── dvc.yaml
├── dvc.lock
├── params.yaml
├── pyproject.toml
├── poetry.lock
├── README.md
└── TEAM.md
```

---

## Instalación

### Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd MLOpsMaestria
```

### Instalar dependencias

```bash
poetry install --no-root
```

---

## Comandos principales

### Recuperar datos versionados con DVC

```bash
dvc pull
```

> Nota: este comando requiere un almacenamiento remoto configurado en DVC. En esta implementación académica no se configuró un repositorio remoto, por lo que los datos se generan localmente mediante el pipeline definido en `dvc.yaml`.

### Ejecutar el pipeline completo

```bash
dvc repro
```

Este comando ejecuta automáticamente:

1. Generación de datos.
2. Preparación de datos.
3. Entrenamiento de modelos.
4. Generación de métricas.

### Ejecutar el entrenamiento manualmente

```bash
poetry run python src/openrate/train.py
```

### Visualizar experimentos con MLflow

```bash
poetry run mlflow ui
```

Luego abrir en el navegador:

```text
http://127.0.0.1:5000
```

---

## Modelos implementados

### Logistic Regression

Modelo lineal utilizado como línea base para clasificación binaria.

### Random Forest

Modelo basado en árboles de decisión utilizado para comparar su desempeño frente al modelo base.

---

## Parámetros de configuración

Los parámetros de entrenamiento y división de datos se encuentran centralizados en:

```text
params.yaml
```

Esto permite modificar la configuración del experimento sin alterar el código fuente.

---

## Métricas evaluadas

Los modelos son comparados mediante las siguientes métricas:

* Accuracy
* Precision
* Recall
* F1 Score

La selección del mejor modelo se realiza utilizando el valor de F1 Score.

---

## Seguimiento de experimentos

Se utiliza MLflow para registrar:

* Nombre del modelo.
* Parámetros utilizados.
* Métricas obtenidas.
* Comparación de experimentos.

---

## Versionamiento de datos

El proyecto utiliza DVC para garantizar la reproducibilidad del flujo de trabajo.

Archivos principales:

* `dvc.yaml`
* `dvc.lock`

---

## Resultados

Durante las pruebas realizadas se entrenaron y compararon los modelos Logistic Regression y Random Forest para la predicción de apertura de notificaciones push.

El modelo con mejor desempeño es seleccionado automáticamente con base en el valor obtenido de F1 Score y sus resultados son almacenados para su posterior análisis.
