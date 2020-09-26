from flask import Flask, render_template, abort
from flask_bootstrap import Bootstrap
from flask import jsonify
import utils.sql

app = Flask(__name__)
Bootstrap(app)

@app.route('/template')
def templateLoad():
    fruits = utils.sql.getAllData()
    return render_template('fruit.html', fruits=fruits)

@app.route('/')
def loadAll():
    return jsonify(utils.sql.getAllData())

@app.route('/<id>')
def loadById(id):
    data = utils.sql.getById(id)
    if (data):
        return jsonify(data)
    else:
        abort(404)
        

if __name__ == '__main__':
    #app.run(debug=True, port=5001)
    app.run()