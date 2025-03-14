# Análisis de Satisfacción del Cliente

Este proyecto tiene como objetivo analizar la satisfacción del cliente utilizando datos de retroalimentación. Actualmente, muchas empresas tienen dificultades para comprender las opiniones de sus clientes y mejorar sus servicios de manera eficiente. Esto demuestra que la falta de análisis adecuados puede reducir la lealtad del cliente y afectar las ventas. Nuestra propuesta busca resolver este problema a través del uso de técnicas de Machine Learning y análisis de datos para identificar patrones en la satisfacción del cliente y sugerir mejoras basadas en estos hallazgos.

## Tabla de contenidos

1. [Nombre](#Nombre)
2. [Descripción](#descripción)
3. [Arquitectura](#Arquitectura)
4. [Proceso](#Proceso)
5. [Funcionalidades](#Funcionalidades)
6. [Estado del proyecto](#EstadoDelProyecto)
7. [Agradecimientos](#Agradecimientos)


* Nombre del proyecto

Análisis de Satisfacción del Cliente

* Breve descripción del proyecto -> Alguna imagen o gif que muestre el proyecto

Se presenta un modelo entrenado de IA que utiliza las caracteristicas brindadas para predecir el nivel de satisfaccion que tendra un cliente.

![alt text](/imgs/image.png)

* Arquitectura del proyecto + imagen

El modelo de IA utiliza diferentes tecnicas aprendidas durante el curso, dentro de las cuales estan:
    - Analisis y limpieza de datos
    - Generacion de datos artificales con KernelDensity
    - Escalado de datos con StandardScaler y OneHotEncoder
    - Reduccion de complejidad con PCA
    - Aplicacion de distintos modelos como RandomForest, GradientBoost y Redes Neuronales
    - Ensamblaje de modelos con VotingRegressor

![alt text](/imgs/image-1.png)   

* Proceso de desarrollo:

-Fuente del dataset

data = kagglehub.dataset_download("jahnavipaliwal/customer-feedback-and-satisfaction")
file_path = os.path.join(data, "customer_feedback_satisfaction.csv")

-Limpieza de datos (img que lo valide)

    - Validacion de datos null
    - Validacion de datos duplicados
    - Eliminar columnas innecesarias
    - Convertir variables categoricas a numericas
    - Escalar magnitudes para evitar sesgo 

![alt text](/imgs/image-2.png)

-Manejo excepciones/control errores

    - Se eliminan los posibles errores en la limpieza de los datos

![alt text](/imgs/image-3.png)

-Estadísticos (Valores, gráficos, …)

    - Se incluyen 7 analisis diferentes antes del procesamiento de los datos
    - Se realiza un analisis final de perdida al finalizar el entrenamiento de la IA

![alt text](/imgs/image-4.png)

* Funcionalidades extra:

Ejem 1: Integración del proyecto en una pág web
- Tecnología/Herramientas usadas …
- Arquitectura (img)

