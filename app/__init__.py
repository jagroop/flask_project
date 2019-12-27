from flask import Flask
import datetime

app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import pages, auth

# Load the config file
app.config.from_object('config')

@app.context_processor
def inject_now():
    now = datetime.datetime.now()
    return {'now': now.year}