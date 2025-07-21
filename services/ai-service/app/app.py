from flask import Flask
from flask_cors import CORS
from .config import Config
import logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Register blueprints
    from .controllers.inventory_controller import inventory_bp
    from .controllers.prescription_controller import prescription_bp
    
    app.register_blueprint(inventory_bp, url_prefix='/api/ai/inventory')
    app.register_blueprint(prescription_bp, url_prefix='/api/ai/prescription')
    
    return app