from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    print('Metodo create app')
    app = Flask(__name__)
    CORS(app)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # Import models to ensure they are registered with SQLAlchemy
    from .models import URL  
    db.init_app(app)
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    migrate.init_app(app, db)

    from app.routes import shorten_url, redirect_url
    app.add_url_rule('/shorten', 'shorten_url', shorten_url, methods=['POST'])
    app.add_url_rule('/<short_url>', 'redirect_url', redirect_url, methods=['GET'])

    return app