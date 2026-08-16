import os


class Config:
    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "student_prediction")

    # MySQL / Aiven
    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_USER = os.getenv("MYSQL_USER", "avnadmin")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
    MYSQL_DB = os.getenv("MYSQL_DB", "student_prediction")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))

    # MySQL Cursor
    MYSQL_CURSORCLASS = "DictCursor"

    # Debug
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

    
