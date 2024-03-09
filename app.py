''' 
    Activate.ps1 is not digitally signed.
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

    Create env
    py -3 -m venv venv

    Activate env
    venv\scripts\activate

    To install packages simply type
    pip install <package-name>

    Run Flask
    python -m flask run
    In browser type: 
        http://127.0.0.1:5000/
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"