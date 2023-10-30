from infrastructure.api.configuration import article_service, category_service
from flask_restful import Resource, reqparse
from flask import Response, make_response
from datetime import datetime


class ArticleResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str)
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('publication_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'))

    def post(self) -> Response:
        try:
            article = article_service.add_article(ArticleResource.parser.parse_args())
            return make_response(article.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class ArticleIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, nullable=False)
    parser.add_argument('content', type=str)
    parser.add_argument('category_id', type=int, nullable=False)
    parser.add_argument('publication_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'))

    def get(self, id_: int) -> Response:
        try:
            article = article_service.get_article_by_id(id_)
            return make_response(article.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def put(self, id_: int) -> Response:
        try:
            article = article_service.update_article(ArticleIdResource.parser.parse_args() | {'id': id_})
            return make_response(article.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def delete(self, id_: int) -> Response:
        try:
            article_id = article_service.delete_article(id_)
            return make_response(f'Successfully deleted article with id: {article_id}', 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class CategoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str)

    def post(self) -> Response:
        try:
            category = category_service.add_category(CategoryResource.parser.parse_args())
            return make_response(category.to_json(), 201)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class CategoryIdResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=False)
    parser.add_argument('description', type=str)

    def get(self, id_: int) -> Response:
        try:
            category = category_service.get_category_by_id(id_)
            return make_response(category.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def put(self, id_: int) -> Response:
        try:
            category = category_service.update_category(CategoryIdResource.parser.parse_args() | {'id': id_})
            return make_response(category.to_json(), 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)

    def delete(self, id_: int) -> Response:
        try:
            category_id = category_service.delete_category(id_)
            return make_response(f'Successfully deleted category with id: {category_id}', 200)
        except ValueError as e:
            return make_response({'message': e.args[0]}, 400)


class TagResource(Resource):
    ...


class ArticleTagResource(Resource):
    ...
