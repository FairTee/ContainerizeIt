#!/usr/bin/python3


from flask import Flask
from container_management import create_container, list_containers
from api_integration import fetch_data_from_api
from database_management import add_user, list_users, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

@app.route('/')
def hello():
    return 'Welcome to ContainerizeIt - One-click Docker Container Deployment!'

@app.route('/containers/create')
def create_container_route():
    # Example usage: /containers/create?image=<IMAGE_NAME>&name=<CONTAINER_NAME>
    image = request.args.get('image')
    name = request.args.get('name')
    return create_container(image, name)

@app.route('/containers/list')
def list_containers_route():
    return list_containers()

@app.route('/api/fetch')
def fetch_data_route():
    # Example usage: /api/fetch?url=<API_URL>
    url = request.args.get('url')
    return fetch_data_from_api(url)

@app.route('/users/add')
def add_user_route():
    # Example usage: /users/add?username=<USERNAME>&email=<EMAIL>
    username = request.args.get('username')
    email = request.args.get('email')
    return add_user(username, email)

@app.route('/users/list')
def list_users_route():
    return list_users()

if __name__ == '__main__':
    app.run(debug=True)
