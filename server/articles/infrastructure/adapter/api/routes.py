from flask_restful import Resource, reqparse
from flask import Response


class ArticleResource(Resource):
    ...


class CategoryResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, nullable=True)
    parser.add_argument('description', type=str)

    def get(self, id_: int) -> Response:
        ...

    def post(self, name: str) -> Response:
        ...

    def put(self, name: str) -> Response:
        ...

    def delete(self, id_: int) -> Response:
        ...


class TagResource(Resource):
    ...


class ArticleTagResource(Resource):
    ...
