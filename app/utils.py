import openai
import requests
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from flask import current_app
from app import config

# Configuration de l'API OpenAI
openai.api_key = config.Config.OPENAI_API_KEY
chatgpt_model_name = "gpt-3.5-turbo" 


def generate_prompt(prompt):
    response = openai.chat.completions.create(
        model=chatgpt_model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()

def analyze_image(image_path):
    subscription_key = current_app.config['AZURE_SUBSCRIPTION_KEY']
    endpoint = current_app.config['AZURE_ENDPOINT']
    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    local_image = open(image_path, "rb")
    analysis = computervision_client.analyze_image_in_stream(local_image, visual_features=["Description", "Objects"])
    return analysis

def process_image(image_path, prompt):
    # Analyser l'image avec Azure Computer Vision
    analysis = analyze_image(image_path)
    
    # Générer la description basée sur l'analyse
    description = ' '.join([caption.text for caption in analysis.description.captions])
    prompt = f"{description}. {prompt}"
    
    # Utiliser DALL·E pour générer une nouvelle image basée sur le prompt
    openai.api_key = current_app.config['OPENAI_API_KEY']
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']

    # Télécharger l'image générée par DALL·E
    image_response = requests.get(image_url)
    image_filename = os.path.join('app/static/uploads', 'result_image.png')
    with open(image_filename, 'wb') as f:
        f.write(image_response.content)

    return 'result_image.png'