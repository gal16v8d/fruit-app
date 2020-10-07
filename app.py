from flask import Flask, render_template, abort, jsonify, request, make_response
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
Bootstrap(app)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

import models
import schemas

fruit_schema = schemas.FruitSchema()
fruits_schema = schemas.FruitSchema(many=True)

@app.route('/fruits/template')
def getAllInWeb():
    data = models.FruitModel.query.all()
    return render_template('fruit.html', fruits=data)

@app.route('/fruits')
def getAll():
    data = models.FruitModel.query.all() 
    return fruits_schema.jsonify(data)

@app.route('/fruits/<int:id>')
def getById(id):
    data = models.FruitModel.query.get_or_404(id)
    return fruit_schema.jsonify(data)

@app.route('/fruits', methods=['POST'])
def save():
    if request.is_json and 'name' in request.get_json():
        payload = request.get_json()
        new_fruit = models.FruitModel(name=payload['name'])
        db.session.add(new_fruit)
        db.session.commit()
        storedData = db.session.query(models.FruitModel).filter(models.FruitModel.name == payload['name'])
        return fruit_schema.jsonify(storedData, 201)
    else:
        abort(400)

@app.route('/fruits/<int:id>', methods=['PATCH'])
def update(id):
    if request.is_json and 'name' in request.get_json():
        fruit = models.FruitModel.query.get_or_404(id)
        payload = request.get_json()
        fruit.name = payload['name']
        db.session.commit()
        return fruit_schema.jsonify(fruit)
    else:
        abort(400) 

@app.route('/fruits/<int:id>', methods=['DELETE'])
def delete(id):
    fruit = db.session.query(models.FruitModel).filter(models.FruitModel.id == id).first()
    if fruit:
        db.session.delete(fruit)
        db.session.commit()
        response = make_response('', 204)
        response.mimetype = app.config['JSONIFY_MIMETYPE']
        return response
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)