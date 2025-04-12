#Description : A Flask API that allows submitting user data (name, email, phone) to a database using SQLAlchemy and supports CORS.

#Author : Govarthanahari N
#Version : Python 3.9.5
#Date : 11/04/2025

# Import necessary libraries
from flask import Flask, request, jsonify 
from flask_cors import CORS  
from dotenv import load_dotenv 
load_dotenv()  #Load .env file containing sensitive data (e.g., database URL)

import os  
from config import Config  
from models import db, User  

#Initialize Flask app
app = Flask(__name__) 
app.config.from_object(Config) 

#Initialize the database with the app context
db.init_app(app)  

#Allowing cross-origin requests
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is working!"})  

#Route for submitting user data
@app.route('/submit', methods=['POST']) 
def submit_form():
    data = request.json  
    print("Received data:", data)  

    #From the received JSON data
    name = data.get('name')
    email = data.get('email')  
    mobile = data.get('phone')  

    #Validate
    if not name or not email or not mobile: 
        return jsonify({'error': 'Missing field'}), 400  

    try:
        #Create and store the user data in the database
        user = User(name=name, email=email, mobile=mobile) 
        db.session.add(user)  
        db.session.commit() 
        return jsonify({'message': 'User data saved successfully!'}), 201 
    except Exception as e:
        
        db.session.rollback()  
        return jsonify({'error': str(e)}), 500 

#Run the Flask app when the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  
