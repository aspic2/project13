"""Module to hold all the SAS methods."""

import sensitive
import requests

class SAS(object):

    def __init__(self):
        self.api_key = sensitive.sas_api_key
        self.base_path = sensitive.sas_base_path
        self.url = ""


    def build_url(self):
        """Add on all the subdirectories you need."""
        self.url = self.base_path
        return self


    def get_list_of(self, objects, search_term):
        """This will be the ajax method for auto-filling the web form
        It needs to be able to retrieve advertisers, campaigns, and
        flights/placements.
        """
        # Construct a url and send as request
        url = self.base_path + "/" + objects + ".xml"
        params = { "search[name_like]": search_term }


        response = requests.get(url, params=params, auth=(self.api_key, ''))
        # TODO: parse the content to retrieve name and ID
        print("The URL = ", response.url)
        print(response.content)
        return response.content
