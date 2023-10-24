from infrastructure.api.configuration import article_service
from flask_restful import Resource, reqparse
from flask import Response, make_response
from datetime import datetime


class ArticleResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str)
    parser.add_argument('content', type=str)
    parser.add_argument('category_id', type=int)
    parser.add_argument('publication_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'))

    def post(self) -> Response:
        try:
            article = article_service.add_article(ArticleResource.parser.parse_args())
            return make_response(article.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class ArticleIdResource(Resource):

    def get(self, id_: int) -> Response:
        try:
            article = article_service.get_article_by_id(id_)
            return make_response(article.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def put(self, id_: int) -> Response:
        ...

    def delete(self, id_: int) -> Response:
        try:
            article_id = article_service.delete_article(id_)
            return make_response(f'Successfully deleted article with id: {article_id}', 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


# todo (1):
"""
    Zakładam, że wszystkie Resource'y, nawet te proste powinny przechodzić przez warstwę domeny, 
    a co za tym idzie mieć swój domenowy odpowiednik serwisu? Chodzi mi o to, że dla prostych route'ów, które
    nie potrzebują nic więcej, oprócz zapisania do bazy generuje to masę dodatkowego kodu.
"""


class CategoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=True)
    parser.add_argument('description', type=str)

    def get(self, id_: int) -> Response:
        ...

    def post(self) -> Response:
        ...

    def put(self, name: str) -> Response:
        ...

    def delete(self, id_: int) -> Response:
        ...


class TagResource(Resource):
    ...


class ArticleTagResource(Resource):
    ...
