from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')  # Assuming your main HTML file is index.html

# Example route for running model logic
@app.route('/run-model', methods=['POST'])
def run_model():
    # Add logic here to run your model using the form input or data
    user_input = request.form['user_input']
    # Use the model to make a prediction, process data, etc.
    # response = model.predict(user_input) or any processing
    response = f"Processed input: {user_input}"  # Replace with actual processing
    return response

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)