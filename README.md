Instalación y ejecución
1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd MLOpsMaestria
2. Instalar dependencias
poetry install --no-root
3. Recuperar datos versionados con DVC
dvc pull
Nota: este comando requiere tener configurado el almacenamiento remoto de DVC.
4. Ejecutar el pipeline completo
dvc repro
Este comando ejecuta las siguientes etapas:
Generación de datos.
Preparación de datos.
Entrenamiento de modelos.
Generación de métricas.
5. Ejecutar el entrenamiento manualmente
poetry run python src/openrate/train.py
6. Visualizar experimentos en MLflow
poetry run mlflow ui
Abrir en el navegador:
http://127.0.0.1:5000
 
https://chatgpt.com/share/6a3b563f-a4b0-83e9-a6f4-a9d139a2dcf9
Echa un vistazo a este chat
Alguna persona pensó que te gustaría ver este chat.
 
Predicción de Open Rate con MLOps
Integrantes
Najhery Soler
Laura Medina
[Nombre del tercer integrante]
Descripción del proyecto
Este proyecto implementa un flujo básico de MLOps para predecir si un usuario abrirá o no una notificación push.
La solución incluye generación de datos, preparación de datos, entrenamiento y comparación de modelos de clasificación, seguimiento de experimentos con MLflow y versionamiento de datos mediante DVC.
Objetivo
Construir un flujo de trabajo reproducible y trazable para entrenar, comparar y documentar modelos de clasificación orientados a la predicción del Open Rate de notificaciones push.
Tecnologías utilizadas
Python 3.13
Poetry
DVC
MLflow
Pandas
Scikit-learn
Git
GitHub
Estructura del proyecto
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
Instalación
Clonar el repositorio:
git clone <URL_DEL_REPOSITORIO>
cd MLOpsMaestria
Instalar dependencias:
poetry install --no-root
Comandos principales
Recuperar datos versionados con DVC
dvc pull
Nota: Este comando requiere un almacenamiento remoto configurado en DVC. En esta implementación académica no se configuró un repositorio remoto, por lo que los datos se generan localmente mediante el pipeline definido en dvc.yaml.
Ejecutar el pipeline completo
dvc repro
Este comando ejecuta automáticamente:
Generación de datos.
Preparación de datos.
Entrenamiento de modelos.
Generación de métricas.
Ejecutar el entrenamiento manualmente
poetry run python src/openrate/train.py
Visualizar experimentos con MLflow
poetry run mlflow ui
Luego abrir en el navegador:
http://127.0.0.1:5000
Modelos implementados
Logistic Regression
Modelo lineal utilizado como línea base para clasificación binaria.
Random Forest
Modelo basado en árboles de decisión utilizado para comparar su desempeño frente al modelo base.
Parámetros de configuración
Los parámetros de entrenamiento y división de datos se encuentran centralizados en:
params.yaml
Esto permite modificar la configuración del experimento sin alterar el código fuente.
Métricas evaluadas
Los modelos son comparados mediante las siguientes métricas:
Accuracy
Precision
Recall
F1 Score
La selección del mejor modelo se realiza utilizando el valor de F1 Score.
Seguimiento de experimentos
Se utiliza MLflow para registrar:
Nombre del modelo.
Parámetros utilizados.
Métricas obtenidas.
Comparación de experimentos.
Versionamiento de datos
El proyecto utiliza DVC para garantizar la reproducibilidad del flujo de trabajo.
Archivos principales:
dvc.yaml
dvc.lock
Resultados
Durante las pruebas realizadas se entrenaron y compararon los modelos Logistic Regression y Random Forest para la predicción de apertura de notificaciones push.
El modelo con mejor desempeño es seleccionado automáticamente con base en el valor obtenido de F1 Score y sus resultados son almacenados para su posterior análisis.
 