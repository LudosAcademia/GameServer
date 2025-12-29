import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment variables


#the general config file of the server used for globably distruting variables throught the files
class Config:

    def get_secret():
        # get the path to secret
        path = os.getenv("SECRET_KEY")
        # Open the file in read mode
        file = open(path, "r")
        # Read the entire content of the file
        return file.read()
    
    #usually located outside of the 
    SECRET_KEY = get_secret()

    #database host: example: www.example.com or localhost
    DB_HOST = os.getenv("DB_HOST")
    #database user: example: root
    DB_USER = os.getenv("DB_USER")
    #database password: usually named root for the root user, but it is empty by default
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    #database name: example: test_db
    DB_NAME = os.getenv("DB_NAME")
    #database port: 
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    #app port: 
    APP_PORT = int(os.getenv("APP_PORT", 5000))