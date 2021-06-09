from flask import Blueprint, render_template, abort, jsonify, request
from flasgger import swag_from
from api.model.database import db
from api.model.fruit_model import FruitModel
from api.schema.fruit_schema import FruitSchema

api = Blueprint('api', __name__)

fruit_schema = FruitSchema()
fruits_schema = FruitSchema(many=True)


@api.route('/fruits/template')
@swag_from('../doc/fruits-template.yml')
def get_all_in_web():
    data = FruitModel.get_all()
    return render_template('fruit.html', fruits=data)


@api.route('/fruits')
@swag_from('../doc/fruits.yml')
def get_all():
    data = FruitModel.get_all()
    return fruits_schema.jsonify(data)


@api.route('/fruits/<int:id>')
@swag_from('../doc/fruit-get.yml')
def get_by_id(id):
    fruit = FruitModel.get_by_id(id)
    return fruit_schema.dump(fruit)


@api.route('/fruits', methods=['POST'])
@swag_from('../doc/fruit-post.yml')
def save():
    if request.is_json and 'name' in request.get_json():
        payload = request.get_json()
        new_fruit = FruitModel(name=payload['name'])
        new_fruit.save()
        resp = fruit_schema.dump(new_fruit)
        return resp, 201
    else:
        abort(400)


@api.route('/fruits/<int:id>', methods=['PATCH'])
@swag_from('../doc/fruit-patch.yml')
def update(id):
    if request.is_json and 'name' in request.get_json():
        fruit = FruitModel.get_by_id(id)
        if fruit:
            payload = request.get_json()
            fruit.name = payload['name']
            fruit.update()
            return fruit_schema.dump(fruit)
        else:
            abort(404)
    else:
        abort(400)


@api.route('/fruits/<int:id>', methods=['DELETE'])
@swag_from('../doc/fruit-delete.yml')
def delete(id):
    fruit = FruitModel.get_by_id(id)
    if fruit:
        fruit.delete()
        return '', 204
    else:
        abort(404)
