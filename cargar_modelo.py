import joblib

# Cargar el modelo desde el archivo .pkl
try:
    model = joblib.load('modelo_entrenado.pkl')
    print("Modelo cargado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

# Datos de prueba (ajusta esto según las características de tu modelo)
input_data = [[5.1, 3.5, 1.4, 0.2, 4.0, 5.0, 6.0, 8.5, 9.5, 6.4, 1.0, 7.3, 8.3]]  # Ejemplo de datos de entrada

# Función para hacer predicciones
try:
    prediction = model.predict(input_data)
    print(f"Predicción: {prediction}")
except Exception as e:
    print(f"Error al hacer la predicción: {e}")