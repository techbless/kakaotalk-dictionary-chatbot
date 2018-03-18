"""
This script runs the Interactive application using a development server.
"""

from os import environ
from Interactive import app

if __name__ == '__main__':
    app.run(host="0.0.0.0")
