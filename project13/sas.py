"""Module to hold all the SAS methods."""

import secrets

class SAS(object):

    def __init__(self):
        self.api_key = secrets.sas_api_key
        self.base_path = secrets.sas_base_path
        self.url = ""


    def build_url(self):
        """Add on all the subdirectories you need."""
        self.url = self.base_path
        return self
