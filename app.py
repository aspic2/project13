"""Run the flask app from here"""

# DCM STUFF
import random
import sys
import time
from os import getcwd
import json

# TODO: ADD dfareporting_utils to project
#import dfareporting_utils
#from oauth2client import client
from flask import Flask, redirect, render_template

from project13.sas import SAS

app = Flask(__name__)

#TODO: ADD adv.json to project
#Dictionary of all advertisers and their corresponding 3rd party data
advertiser_data = json.load(open(getcwd() + "/resources/adv.json", 'r'))

@app.route("/report/new")
def build_report():
    # TODO: These vars should be outside of function.
    # TODO: they do not need to be reloaded after every call to this page
    client_xml = getcwd() + "/resources/advertisers.xml"
    advertisers = list(advertiser_data.keys())
    return render_template("report.html", advertisers=advertisers)

@app.route("/report")
def run_report():
    sas_report = SAS()
    # test values
    results = sas_report.get_list_of("campaigns", "2018")
    return render_template("results.html", results=results)

# TODO: maybe make this two parts? pass in object, then query?
@app.route("/get/<query>/")
def get(query):
    #query = request.args.get('query')
    #query = "fid"
    length = None
    advertisers = "null"
    if query:
        length = len(query)
        advertisers = SAS().get_list_of("advertisers", query)
    return advertisers

#TODO: clean up redirect routes
@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def not_found_route(path):
    return redirect('/report/new')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
