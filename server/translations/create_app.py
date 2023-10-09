from flask import Flask, Response, make_response, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)


def create_app() -> Flask:

    with app.app_context():

        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
        )
        app.config['APPLICATION_ROOT'] = '/translations'

        @app.route('/test1')
        def index1() -> Response:
            return make_response({'message': 'Translations home page3'}, 200)

        @app.route('/test2')
        def index2() -> Response:
            return make_response({'message': 'Translations home page4'}, 200)

        return app
