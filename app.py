from __future__ import unicode_literals
from flask import Flask, render_template, request, redirect, url_for
import requests
from applied_ml import get_score
import time
import os
import json


#
# app = Flask(__name__)
#
#
# @app.route('/')
# def landing_page():
#
#     return render_template('index.html')
#
#
# @app.route('/fetch_toxicity', methods=['GET', 'POST'])
# def stream_data():
#     """ Utilize model to evaluate toxicity of text and return score """
#     # Get text from user
#     # NOTE: uncertain if split on space is needed
#     text = request.args.get('text').split(' ')
#
#
#     toxicity_score = get_score(text)
#
#     return toxicity_score




if __name__ == "__main__":

    text = 'I love dogs. I love cats. I like humans'.split(' ')
    text = 'I hate dogs. I hate cats. I hate humans'.split(' ')
    toxicity_score = get_score(text)

    print(toxicity_score)
    # app.run(debug=True, port=5000)
