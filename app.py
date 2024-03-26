from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to ContainerizeIt - One-click Docker Container Deployment!'

if __name__ == '__main__':
    app.run(debug=True)
