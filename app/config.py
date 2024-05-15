import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    AZURE_SUBSCRIPTION_KEY = os.environ.get('AZURE_SUBSCRIPTION_KEY')
    AZURE_ENDPOINT = os.environ.get('AZURE_ENDPOINT')
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
