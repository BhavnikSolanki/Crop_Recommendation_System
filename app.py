from platform import processor
from flask import Flask,request,render_template, redirect, session, url_for, flash
import numpy as np
import pandas as pd
import pickle as pickle
import joblib
import os
import csv

# creating flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Load the model using joblib
model = joblib.load('model')

# Check if the model is loaded correctly
if model:
    print("Model loaded successfully!")
else:
    print("Failed to load the model.")

user = 'User.csv'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        password = request.form['password']

        # Check credentials against CSV file
        with open(user, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    flash("Login successful", 'success')
                    return redirect(url_for('welcome'))
            flash("Invalid username or password", 'danger')
  
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if the CSV file exists, if not, create it and write the header
        file_exists = os.path.isfile(user)
        
        with open(user, mode='a', newline='') as file:
            writer = csv.writer(file)
            # Write the header only if the file is new
            if not file_exists:
                writer.writerow(['Username', 'Email', 'Password'])
            # Write the user's data
            writer.writerow([username, email, password])

        # Flash success message and redirect to login
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Handle password reset logic here
        flash('Password reset link has been sent to your email.', 'info')
        return redirect(url_for('login'))
    return render_template('forgot_password.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/input_page', methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        try:
            N = float(request.form['nitrogen'])
            P = float(request.form['phosphorus'])
            K = float(request.form['potassium'])
            soil = request.form['soil_type']
            rainfall = float(request.form['rainfall'])
            states = request.form['state']
            temp = float(request.form['temperature'])
            humidity = float(request.form['humidity'])
            ph = float(request.form['ph'])

            # Print form inputs
            print("Form Inputs:")
            print(f"Nitrogen: {N}")
            print(f"Phosphorus: {P}")
            print(f"Potassium: {K}")
            print(f"soil_type: {soil}")
            print(f"rainfall: {rainfall}")
            print(f'state: {states}')
            print(f"Temperature: {temp}")
            print(f"Humidity: {humidity}")
            print(f"pH: {ph}")

            # Handle missing session variables
            if None in [N, P, K, soil, states, rainfall, temp, humidity, ph]:
                flash("Missing session data. Please check your inputs.", "danger")
                return redirect(url_for('input_page'))

            # Map categorical features to indices
            # Replace these mappings with your actual mappings
            state_mapping = {
                'Andaman AND Nicobar': 0,
                'Andhra Pradesh ': 1,
                'Assam': 2,
                'Chattisgarh': 3,
                'Goa': 4,
                'Gujarat': 5,
                'Haryana': 6,
                'Himachal Pradesh': 7,
                'Jammu and Kashmir': 8,
                'Karnataka': 9,
                'Kerala': 10,
                'Madhya Pradesh': 11,
                'Maharashtra': 12,
                'Manipur': 13,
                'Meghalaya': 14,
                'Nagaland': 15,
                'Odisha': 16,
                'Pondicherry': 17,
                'Punjab': 18,
                'Rajasthan': 19,
                'Tamil Nadu': 20,
                'Telangana': 21,
                'Tripura': 22,
                'Uttar Pradesh': 23,
                'Uttrakhand': 24,
                'West Bengal': 25
            }

            soil_type_mapping = {'Dry': 0, 'Humid': 1, 'Wet': 2}
            print('state:',states)

           # state = state.upper
            print(states)            
            state_index = state_mapping.get(states, -1)  # -1 for unknown state
            
            soil_type_index = soil_type_mapping.get(soil, -1)  # -1 for unknown soil_type


            # Create a DataFrame for new data with numeric and categorical indices
            new_data = pd.DataFrame({
                    'N': [N],
                    'P': [P],
                    'K': [K],
                    'temp': [temp],
                    'humidity': [humidity],
                    'ph': [ph],
                    'rainfall': [rainfall],
                    'states': [state_index],
                    'soil': [soil_type_index],
                    #'weather': [0]  # Assuming a default index for 'weather'
                })

            print("New data for prediction:")
            print(new_data)
            print('new data shape',new_data.shape)
            print('new data type',new_data.dtypes)
            # Make prediction
            try:
                print('Attempting the prediction')
                prediction = model.predict(new_data)
                predicted_crop = prediction[0]

                print("Prediction:", predicted_crop)
                formatted_crop_name = predicted_crop.capitalize()

                recommended_crop = "{}".format(formatted_crop_name)
            
                return render_template('result.html', prediction=recommended_crop)
            except Exception as e:
                print("Error during prediction:", e)
                flash(f"Prediction error: {e}", "danger")
                return redirect(url_for('input_page'))

        except KeyError as e:
            print("KeyError: ", e)
            flash(f"Missing form field: {e}", "danger")
            return redirect(url_for('input_page'))

        except ValueError as e:
            print("ValueError: ", e)
            flash(f"Invalid input: {e}", "danger")
            return redirect(url_for('input_page'))

    return render_template('input_page.html')

@app.route('/result')
def result():
    return render_template('result.html')

# python main
if __name__ == '__main__':
    app.run(debug=True)