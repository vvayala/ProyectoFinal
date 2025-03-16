# Análisis de Satisfacción del Cliente

Muchas empresas enfrentan dificultades para interpretar la satisfacción de sus clientes, afectando la experiencia del consumidor y en consecuencia, las ventas de sus negocios. Valora+ resuelve este problema mediante el uso de inteligencia artificial y aprendizaje automático para analizar datos y detectar patrones en la satisfacción del cliente. Proporcionamos información accionable que ayuda a las empresas a mejorar sus servicios, fortalecer la fidelidad de los clientes y fomentar el crecimiento sostenible.

## Tabla de contenidos

1. [Nombre](#Nombre)
2. [Descripción](#descripción)
3. [Arquitectura](#Arquitectura)
4. [Proceso](#Proceso)
5. [Funcionalidades](#Funcionalidades)
6. [Estado del proyecto](#EstadoDelProyecto)
7. [Agradecimientos](#Agradecimientos)


* Nombre del proyecto

Valora+
Análisis de Satisfacción del Cliente con IA: Soluciones Basadas en Datos

* Breve descripción del proyecto -> Alguna imagen o gif que muestre el proyecto

En la sección de galería, se incluyen gráficos interactivos que facilitan la visualización de tendencias, patrones y relaciones clave identificadas en los datos recopilados. Estos recursos permiten una comprensión más profunda y accesible de la información analizada. Asimismo, ponemos a disposición un modelo predictivo avanzado, entrenado mediante técnicas de inteligencia artificial. Este modelo es capaz de prever el nivel de satisfacción del cliente en función de las características proporcionadas, ofreciendo una herramienta poderosa para la toma de decisiones estratégicas basadas en datos.

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
    - Utilizacion de try/catch en el sitio web

![alt text](/imgs/image-3.png)

-Estadísticos (Valores, gráficos, …)

    - Se incluyen 7 analisis diferentes antes del procesamiento de los datos
    - Se realiza un analisis final de perdida al finalizar el entrenamiento de la IA

![alt text](/imgs/image-4.png)

* Funcionalidades extra:

Se ha creado un sitio web que incluye:
- Informacion sobre el proyecto  
- Galeria de analisis
- Prediccion de satisfaccion

En la creacion del sitio web se ha utilizado html, css y js.

![alt text](/imgs/image-5.png)