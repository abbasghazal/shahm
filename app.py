from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome To Source shahm'


if __name__ == "__main__":
    app.run()
