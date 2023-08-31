import os, socket
from flask import Flask
from flask_healthz import healthz
from flask_healthz import HealthError

app = Flask(__name__)
app.register_blueprint(healthz, url_prefix="/healthz")

@app.route('/hostname')
def hostname():
    return socket.gethostname()

@app.route('/author')
def author():
    return os.getenv("AUTHOR")

@app.route('/id')
def id():
    return os.getenv("UID")

def printok():
    print("Everything is fine")

def liveness():
    try:
        printok()
    except Exception:
        raise HealthError("Can't connect to the file")

def readiness():
    try:
        printok()
    except Exception:
        raise HealthError("Can't connect to the file")

app.config.update(
    HEALTHZ = {
        "live": "app.liveness",
        "ready": "app.readiness",
    }
)
