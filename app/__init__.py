from flask import Flask

from app.webhook.routes import webhook
from app.extensions import mongo

# Creating our flask app
def create_app():

    app = Flask(__name__)
    mongo.init_app(app, uri="mongodb://admin:admin@localhost:27017/techstax?authSource=admin")

    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
