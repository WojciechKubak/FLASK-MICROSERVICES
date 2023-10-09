from flask import Flask, Response, make_response, request
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)


# https://stackoverflow.com/questions/67737069/how-to-host-a-flask-app-on-a-subfolder-url-prefix-with-nginx
@app.errorhandler(404)
def page_not_found(error):
    return 'This route does not exist {}'.format(request.url), 404


def create_app() -> Flask:

    with app.app_context():

        app.wsgi_app = ProxyFix(
            app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
        )

        @app.route('/test1')
        def index1() -> Response:
            return make_response({'message': 'Articles home page1'}, 200)

        @app.route('/test2')
        def index2() -> Response:
            return make_response({'message': 'Articles home page2'}, 200)

        return app
