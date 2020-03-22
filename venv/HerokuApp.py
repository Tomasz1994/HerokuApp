from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
    return '<h1>Moja strona na Heroku</h1>'