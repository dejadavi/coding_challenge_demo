from .settings import retry_behaviour
import logging
import flask
from flask import Response
from flask_marshmallow import Marshmallow
from requests import Session
from requests.adapters import HTTPAdapter

app = flask.Flask("user_profiles_api")
logger = flask.logging.create_logger(app)
logger.setLevel(logging.INFO)
ma = Marshmallow(app)

##Adding our routes only after out Marshmallow
#middleware has been added to the app
#We could also create a factory function
#and expose that in routes/__init__.py but this is 
#a small app and more transparent

from .routes import health_check_blueprint, get_github_profile_blueprint\
    , get_bitbucket_profile_blueprint

app.register_blueprint(health_check_blueprint)
app.register_blueprint(get_github_profile_blueprint)
app.register_blueprint(get_bitbucket_profile_blueprint)
