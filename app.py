from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd

app = Flask(__name__)
CORS(app)

# Cargar el modelo al iniciar la API
try:
    model = joblib.load('modelo_entrenado.pkl')
    escalar = joblib.load('modelo_escalado.pkl')
    pca = joblib.load('modelo_pca.pkl')
    print("Modelo cargado correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    exit()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos de la solicitud
        #Se reciben las 9 caracteristicas iniciales
        data = request.json['data'] 
        columnas = ['Age','Gender','Country','Income','ProductQuality','ServiceQuality','PurchaseFrequency','FeedbackScore','LoyaltyLevel']
        
        #Procesar los datos recibidos antes de pasarlos al modelo
        df = pd.DataFrame([data], columns=columnas)

        #Escalar los datos tanto numericos como categoricos
        datos_escalados = escalar.transform(df) #18 caracteristicas

        #Aplicar PCA para reducir la complejidad (13 caracteristicas)
        datos_finales = pca.transform(datos_escalados)

        # Hacer la predicción
        prediction = model.predict(datos_finales)
        
        # Devolver la predicción como respuesta
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)