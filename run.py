# from app import views
from views import app
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()