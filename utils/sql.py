import psycopg2
from psycopg2 import Error
import yaml
import json

class Fruit(dict):
    def __init__(self, id, name):
        dict.__init__(self, id=id, name=name)

db = yaml.load(open('db.yaml'))

def getConnection():
    try:
        return psycopg2.connect(user = db['pg_user'],
                                    password = db['pg_pass'],
                                    host = db['pg_host'],
                                    port = db['pg_port'],
                                    database = db['pg_db'])
    except Exception as e:
        print('Error in connection to PostgreSQL', e)

def closeResources(connection, cursor):
    if (connection):
        cursor.close()
        connection.close()
        print('PostgreSQL connection is closed')

def getAllData():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, name FROM fruit ORDER BY name ASC;')
        data = cursor.fetchall()
        fruitNames = []
        for f in data:
            fruit = Fruit(f[0], f[1])
            fruitNames.append(fruit)
        return fruitNames
    except Exception as e:
        print('Error in connection to PostgreSQL', e)
    finally:
        closeResources(connection, cursor)

def getById(id):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute('SELECT id, name FROM fruit WHERE id=%s', id)
        data = cursor.fetchone()
        return Fruit(data[0], data[1])
    except Exception as e:
        print('Error in connection to PostgreSQL', e)
    finally:
        closeResources(connection, cursor)

def getMaxId():
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute('SELECT MAX(id) FROM fruit;')
        data = cursor.fetchone()
        return data[0]
    except Exception as e:
        print('Error in connection to PostgreSQL', e)
    finally:
        closeResources(connection, cursor)

def saveData(newFruit):
    try:
        newId = getMaxId() + 1
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO fruit VALUES(%s,%s)', (newId, newFruit))
        connection.commit()
    except Exception as e:
        print('Error in connection to PostgreSQL', e)
    finally:
        closeResources(connection, cursor)