# Actividad 2 – Pipeline y Control de Calidad Básico

## Estudiante

Catalina Valderrama Martínez

## Docente

Ing. Martha Susana Contreras Ortiz

## Asignatura

Seminario de Grado II

## Descripción


El objetivo es complementar la línea base reproducible desarrollada en la Actividad 1, implementando un pipeline automatizado para ejecutar la validación de los datos y el entrenamiento del modelo.

Además, se agregan controles básicos de calidad de datos y un contrato de datos que sirva como base para futuras etapas de despliegue.

## Objetivos

- Automatizar el flujo de entrenamiento del modelo.
- Validar la calidad de los datos antes del entrenamiento.
- Definir un contrato de datos en formato JSON.
- Mantener la trazabilidad y reproducibilidad de los experimentos mediante MLflow.
- Generar el REadMe para que cualquier usuario pueda reproducirlo desde cero.



# Estructura del Proyecto

- train.py 
- validate_data.py 
- pipeline.py 
- data_contract.json
- requirements.txt 
- mlflow.db


# Tecnologías utilizadas

- Python
- Scikit-Learn
- MLflow 
- Visual Studio Code 


# Dataset utilizado
Para este laboratorio se utiliza el dataset Iris incluido dentro de Scikit-Learn. 
 
 Características utilizadas: 
 - sepal_length - sepal_width 
 - petal_length 
 - petal_width
 - Variable objetivo: - species (target) 


## Crear entorno virtual Abrir la terminal y ejecutar: 

py -m venv venv o  python -m venv venv
