from flask import Flask, request, render_template
import joblib

import pandas as pd

from flask import Flask

import joblib
print(joblib.__version__)


app = Flask(__name__)

# Load the model and vectorizers
model = joblib.load('budget_predictor_model.pkl')
tfidf_job_title = joblib.load('tfidf_job_title.pkl')
tfidf_company = joblib.load('tfidf_company.pkl')
tfidf_location = joblib.load('tfidf_location.pkl')

from flask import Flask

app = Flask(__name__)

try:
    @app.route('/')
    def home():
        return "Welcome to Flask App!"
except Exception as e:
    print(f"An error occurred: {e}")








@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        form_data = request.form
        data = {
            'job_title': str(form_data['job_title']),
            'company': str(form_data['company']),
            'location': str(form_data['location']),
            'link': str(form_data['link'])  # Include link for the output
        }


@app.route('/')
def home():
    return "Welcome to Flask!"

if __name__ == '__main__':
    app.run(debug=True)





