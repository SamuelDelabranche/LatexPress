from flask import Flask
from .routes import bp

def createApp():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    with app.app_context():
        app.register_blueprint(bp)
    
    return app
