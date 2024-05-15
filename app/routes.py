from flask import Flask, Blueprint, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import openai
import requests
from app.utils import generate_prompt, process_image

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'prompt' not in request.form:
        return redirect(url_for('main.home'))

    file = request.files['file']
    prompt = request.form['prompt']

    # Sauvegarder le fichier et traiter l'image
    filename = secure_filename(file.filename)
    filepath = os.path.join('app/static/uploads', filename)
    file.save(filepath)

    # Générer le prompt et l'image modifiée
    result_prompt = generate_prompt(prompt)
    result_image = process_image(filepath, result_prompt)

    return render_template('result.html', prompt=result_prompt, image_path=result_image)