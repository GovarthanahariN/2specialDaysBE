#Description : Defines the User model and initializes the SQLAlchemy database connection

#Author : Govarthanahari N
#Version : Python 3.9.5
#Date : 10/04/2025

from flask_sqlalchemy import SQLAlchemy

#Initialize SQLAlchemy instance
db =SQLAlchemy()

#User model for the 'users' table
class User(db.Model):
    __tablename__ ='users'
    id =db.Column(db.Integer,primary_key=True)
    name =db.Column(db.String(100),nullable=False)
    email =db.Column(db.String(100),nullable=False, unique=True)
    mobile =db.Column(db.String(15),nullable=False)
