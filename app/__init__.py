try:
    from flask import Flask
except:
    print("could not import Flask from flask")

app = Flask(__name__)

from app import script