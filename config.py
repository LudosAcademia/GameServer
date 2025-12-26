import os
from dotenv import load_dotenv

load_dotenv()  # loads .env into environment variables

class Config:

    def get_secret():
        # get the path to secret
        path = os.getenv("SECRET_KEY")
        # Open the file in read mode
        file = open(path, "r")
        # Read the entire content of the file
        return file.read()
    
    SECRET_KEY = get_secret()

    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = int(os.getenv("DB_PORT", 3306))

    APP_PORT = int(os.getenv("APP_PORT", 5000))