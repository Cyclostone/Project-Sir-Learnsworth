from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Route for the login page (index)
@app.route('/')
def home():
    return render_template('index.html')  # Render the login page

# Route for the homepage after login
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')  # Render the homepage

# Route for the 'Get Started' page
@app.route('/get-started')
def get_started():
    return render_template('get-started.html')  # Render the get started page

# Route for the 'Quiz' page
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')  # Render the quiz page

# Example route for running model logic
@app.route('/run-model', methods=['POST'])
def run_model():
    # Add logic here to run your model using the form input or data
    user_input = request.form['user_input']
    # Use the model to make a prediction, process data, etc.
    response = f"Processed input: {user_input}"  # Replace with actual processing
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
