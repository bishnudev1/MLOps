from flask import Flask, render_template, request
import pickle

app = Flask(__name__)


model = pickle.load(open('models/height_ridge_model.pkl', 'rb'))

scale = pickle.load(open('models/scaler.pkl', 'rb'))


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        weight = float(request.form['weight'])
        print(f"Gender: {gender}, Weight: {weight}")

        new_scaled_data = scale.transform([[gender, weight]])

        prediction = model.predict(new_scaled_data)

        print(f"Prediction: {prediction}")

        # // inch to feet also getting first number after decimal

        result = prediction[0]

        height_in_feet = result / 12

        return render_template('home.html', result=round(height_in_feet,2))
    return render_template('home.html')

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)