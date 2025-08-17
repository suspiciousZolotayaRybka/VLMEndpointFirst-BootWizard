'''
16 August 2025
Isaac Finehout
main.py
This .py file controls the program flow on port 5005
'''

from flask import Flask, render_template_string
import os
from flask_talisman import Talisman

bootWizardApp = Flask(__name__)

# Generate SECRET_KEY
bootWizardApp.config['SECRET_KEY'] = os.urandom(24)

# Enforce HTTPS and security headers
Talisman(bootWizardApp)

@bootWizardApp.route('/')
def hello():
    return render_template_string("<h1>hello world</h1>")

# Run the application with a signed certificate for HTTPS
if __name__ == "__main__":
    # TODO python automatically binds to LOCALHOST, change to production IP
    bootWizardApp.run(host="0.0.0.0", port=5005, ssl_context=('cert.pem', 'key.pem'))