import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Flask Configuration
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'default-secret-key')
    
    # PostgreSQL Database Configuration
    DB_HOST = os.getenv('DB_HOST', 'postgres')
    DB_PORT = os.getenv('DB_PORT', '5432')
    DB_USER = os.getenv('DB_USER', 'pms_user')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'pms_password')
    DB_NAME = os.getenv('DB_NAME', 'pms_db')
    
    # Redis Cache Configuration
    REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
    REDIS_PORT = os.getenv('REDIS_PORT', '6379')
    
    # AI Model Storage Configuration
    AI_MODEL_PATH = os.getenv('AI_MODEL_PATH', '/app/models')