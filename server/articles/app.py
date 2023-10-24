from infrastructure.api.routes import ArticleResource
from config import get_config
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, Response, make_response
from flask_restful import Api
import logging

app = Flask(__name__)


def create_app() -> Flask:

    logging.basicConfig(level=logging.INFO)

    with app.app_context():

        app.config.from_object(get_config())

        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
        )

        api = Api(app)
        api.add_resource(ArticleResource, '/')

        @app.route('/')
        def index() -> Response:
            return make_response({'message': 'Articles home page'}, 200)

        return app
