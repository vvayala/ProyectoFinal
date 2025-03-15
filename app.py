from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


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
        #Se reciben las 9 caracteristicas iniciales
        #Procesar los datos recibidos antes de pasarlos al modelo
        #Escalar los datos tanto numericos como categoricos
        escalado = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), ['Age','Income','ProductQuality','ServiceQuality','PurchaseFrequency']),
                ('cat', OneHotEncoder(), ['Gender', 'Country','FeedbackScore','LoyaltyLevel'])
            ])

        #Ajustarlos al modelo (18 caracteristicas)
        X = escalado.fit_transform(data)

        #Aplicar PCA para reducir la complejidad (13 caracteristicas)
        pca = PCA(n_components=0.95)  # Retener el 95% de la varianza
        X_final_pca = pca.fit_transform(X)

        # Hacer la predicción
        prediction = model.predict([X_final_pca])
        
        # Devolver la predicción como respuesta
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)