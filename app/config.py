import os

class Config:
    SECRET_KEY = os.environ.get('50792435eb1b1b90e09a170ee60bc9864e6a8051e6e76f0d') or 'you-will-never-guess'
    AZURE_SUBSCRIPTION_KEY = os.environ.get('81f1a4bc58cd455aa975842b8a6fc0d5')
    AZURE_ENDPOINT = os.environ.get('https://vision-finall.cognitiveservices.azure.com/')
    OPENAI_API_KEY = os.environ.get('sk-proj-C6joKkEq0v0OFGZJyb2aT3BlbkFJr1yyhwMpXH7RCAPKzc0b')
