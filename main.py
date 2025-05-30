import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the trained model
model = joblib.load('crop_app.pkl')  # Ensure you're loading the correct updated model

@ app.route('/')
def home():
    title = 'Harvestify - Home'
    return render_template('Home_1.html', title=title)

@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Harvestify - Crop Recommendation'
    return render_template('Index.html', title=title)

@ app.route('/form', methods=['POST'])
def brain():
    title = 'Harvestify - Crop Recommendation'

    # Get user inputs from the form
    Nitrogen = float(request.form['Nitrogen'])
    Phosphorus = float(request.form['Phosphorus'])
    Potassium = float(request.form['Potassium'])
    Temperature = float(request.form['Temperature'])
    Humidity = float(request.form['Humidity'])
    Rainfall = float(request.form['Rainfall'])  
    Ph = float(request.form['Ph'])

    # Correct the feature order
    values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Rainfall, Ph]

    # Validate input ranges
    if 0 < Ph <= 14 and Temperature < 100 and Humidity > 0:
        # Convert values into a DataFrame with correct column names
        feature_names = ["N", "P", "K", "temperature", "humidity", "rainfall", "ph"]
        arr_df = pd.DataFrame([values], columns=feature_names)

        # Predict the crop
        acc = model.predict(arr_df)

        return render_template('prediction.html', prediction=str(acc[0]))  # Extract the string value
    else:
        return "Sorry... Error in entered values. Please check the form and try again."

if __name__ == '__main__':
    app.run(debug=True)
