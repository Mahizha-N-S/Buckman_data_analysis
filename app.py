from joblib import load
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the saved Random Forest model
loaded_rf_clf = load('random_forest_model.joblib')

mapping={5: "Don't Want to Reveal", 4: 'Above 26%', 1: '16% to 20%', 2: '21% to 25%', 6: 'Upto 5%', 0: '11% to 15%', 3: '6% to 10%'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user inputs from the form
    knowledge_sharemarket = int(request.form['knowledge_sharemarket'])
    knowledge_investment = int(request.form['knowledge_investment'])
    awareness_source = int(request.form['awareness_source'])
    household_income = int(request.form['household_income'])

    # Make a prediction using the trained model
    prediction = loaded_rf_clf.predict([[knowledge_sharemarket, knowledge_investment, awareness_source, household_income]])

# Print the prediction
    print("Prediction:", prediction)
    print("My Recommendation is that you invest in range:",mapping[int(prediction)])
    prediction=f"My Recommendation is that you invest in range:{mapping[int(prediction)]}"
    return prediction

if __name__ == '__main__':
    app.run(debug=True)
