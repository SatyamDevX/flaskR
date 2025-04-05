import os

from flaskR import create_app  # Now it should work

app = create_app()

@app.route('/home')
def helloo():
   return "create app using application factory function then importing it into app.py file ."