#Description : Configuration file for Flask application including database URI settings

#Author : Govarthanahari N
#Version : Python 3.9.5
#Date : 10/04/2025

import os

#Class for setting up Flask app settings
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
