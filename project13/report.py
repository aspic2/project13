import requests
from requests.auth import HTTPBasicAuth
import re
from os import getcwd
import time
import json

import secrets

main_directory = getcwd() + "/.."
api_key = secrets.sas_api_key
base_path = secrets.sas_base_path


class Report(object):
    """Unfinished object to hold all reporting data.
    Holds reports parameters and retrieved reporting data.
    """

    def __init__(self, request_dict, is3rdPartyAdvertiser=False):
        self.Advertiser = request_dict.get('advertiser')
        self.startDate = request_dict.get('startDate')
        self.endDate = request_dict.get('endDate')

        self.is3rdPartyAdvertiser = is3rdPartyAdvertiser

        # This may end up being a dictionary or a report subclass.
        self.parameters = {}
        self.sas = None



class SASReport(Report):

    def __init__(self, request_dict):
        super(self, SASReport).__init__(request_dict)
        self.job_id = None
        self.campaign = request_dict.get('campaign')
        # TODO is request_dict.get('flights') currently an iterable?
        self.flights = [x for x in request_dict.get('flights')]
        self.report_data = None

    def pull_report(self):
        self.assemble_parameters()
        prefix = base_path + "/reports/performance_report.xml"
        self.report_data = requests.get(
            prefix, params=self.params, auth=HTTPBasicAuth(api_key, ''))
        print("data's URL")
        print(self.report_data.url)
        self.job_id = self.get_job_id()
        return self

    def assemble_parameters(self):
        pass


    def get_job_id(self):
        decoded_content = self.report_data.content.decode("utf-8")
        start = decoded_content.index("<JobId>")
        end = decoded_content.index("</JobId>")
        jobId = decoded_content[start + len("<JobId>"):end]
        print("Job ID = ", jobId)
        return jobId
