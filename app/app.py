from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello! This is a simple web app."

@app.route('/print_path')
def print_path():
    path = request.path
    return f"The requested path is: {path}"

@app.route('/sessions/<sessionId>/refresh')
def returnPath(sessionId):
    path = request.path
    return f"Path is: {path}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
