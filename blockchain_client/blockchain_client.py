import os

from ecdsa import SigningKey, NIST192p
import Crypto.Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Cipher import AES, PKCS1_OAEP

import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, templates="../templates")

@app.route('/')
def index():
    return("why aren't you working")
    # return render_template('./index.html')




