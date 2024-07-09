from flask import Flask, request, render_template
import os
import sys
from src.exception import CustomException
from src.pipelines.predict_pipelines import PredictPipeline,CustomData


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    else:
        try:
            data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=int(request.form.get('writing_score')),
            writing_score=int(request.form.get('reading_score'))

            )   
            pred_df=data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline=PredictPipeline()
            print("Mid Prediction")
            results=predict_pipeline.predict(pred_df)
            print("after Prediction")
            return render_template('index.html',results=results[0])
        except CustomException as e:
            return render_template('index.html',results=e.error_message)



if __name__ == "__main__":
    app.run(port=5000, debug=True)