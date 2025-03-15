from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

# Cargar el modelo al iniciar la API
try:
    model = joblib.load('modelo_entrenado.pkl')
    print("Modelo cargado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos de la solicitud
        data = request.json['data']
        
        # Hacer la predicción
        prediction = model.predict([data])
        
        # Devolver la predicción como respuesta
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)