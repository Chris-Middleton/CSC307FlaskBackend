from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random


app = Flask(__name__)
CORS(app)


users = {
    'users_list' :
    [
        {
            'id' : 'xyz789',
            'name' : 'Charlie',
            'job': 'Janitor',
        },
        {
            'id' : 'abc123',
            'name': 'Mac',
            'job': 'Bouncer',
        },
        {
            'id' : 'ppp222',
            'name': 'Mac',
            'job': 'Professor',
        },
        {
            'id' : 'yat999',
            'name': 'Dee',
            'job': 'Aspring actress',
        },
        {
            'id' : 'zap555',
            'name': 'Dennis',
            'job': 'Bartender',
        }
    ]
}





@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/users/<id>')
def get_user(id):
    if id :
        for user in users['users_list']:
            if user['id'] == id:
                return user
        return ({})
    return users
   


@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
    if request.method == 'GET':
        search_job = request.args.get('job')
        search_username = request.args.get('name')
        if search_username and search_job:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username and user['job'] == search_job:
                    subdict['users_list'].append(user)
            return subdict
        elif search_username:
            subdict = {'users_list' : []}
            for user in users['users_list']:
                if user['name'] == search_username:
                    subdict['users_list'].append(user)
            return subdict
        return users
    elif request.method == 'POST':
        userToAdd = request.get_json()
        userToAdd['id'] = uniqueID(users['users_list'])
        users['users_list'].append(userToAdd)
        resp = jsonify(userToAdd)
        resp.status_code = 201 #optionally, you can always set a response code. 
        # 200 is the default code for a normal response
        return resp
    elif request.method == 'DELETE':
        userToDelete = request.get_json()
        try:
            users['users_list'].remove(userToDelete)
        except:
            resp = jsonify(success=False)
            resp.status_code = 404
            return resp
        resp = jsonify(success=True)
        resp.status_code = 204
        return resp

def uniqueID(usersList):
    id = random.randint(0,10000)
    for user in usersList:
        if user['id'] == id:
            return uniqueID(usersList)
    return id

