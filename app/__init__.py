from flask import Flask

def create_app():
    app = Flask(__name__)

    # Charger la configuration
    app.config.from_object('app.config.Config')

    # Enregistrer les routes
    from app.routes import main
    app.register_blueprint(main)

    return app