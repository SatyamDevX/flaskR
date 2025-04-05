from flask import Flask


app = Flask(__name__)

@app.route('/home')
@app.route('/')
def hello():
   return "hello, World!"