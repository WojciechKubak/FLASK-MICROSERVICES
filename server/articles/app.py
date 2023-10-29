from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask, Response, make_response

app = Flask(__name__)


def create_app() -> Flask:

    with app.app_context():

        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
        )

        @app.route('/')
        def index() -> Response:
            return make_response({'message': 'Articles home page'}, 200)

        # test comment 2

        return app
