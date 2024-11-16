import joblib
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# render home page


@ app.route('/')
def home():
    title = 'Harvestify - Home'
    return render_template('Home_1.html', title=title)

# render crop recommendation form page


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Harvestify - Crop Recommendation'
    return render_template('Index.html', title=title)

# render crop recommendation result page

@ app.route('/form', methods=['POST'])
def brain():
    title = 'Harvestify - Crop Recommendation'
    Nitrogen=float(request.form['Nitrogen'])
    Phosphorus=float(request.form['Phosphorus'])
    Potassium=float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['Ph'])
    Rainfall=float(request.form['Rainfall']) 

    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
        model = joblib.load('crop_app')
        arr = [values]
        acc = model.predict(arr)
        # print(acc)
        return render_template('prediction.html', prediction=str(acc))
    else:
        return "Sorry...  Error in entered values in the form Please check the values and fill it again"


# ===============================================================================================

if __name__ == '__main__':
    app.run(debug=True)
