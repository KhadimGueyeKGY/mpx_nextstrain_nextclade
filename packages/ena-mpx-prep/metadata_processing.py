#!/usr/bin/env python

__author__ = 'Nadim Rahman'

import datetime, io, re, requests, subprocess
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from requests.auth import HTTPBasicAuth


ena_searches = {
    'sequence': {'search_fields': ['country', 'collection_date', 'host', 'strain', 'isolate', 'first_public', 'collected_by'], 'query': 'tax_tree(10244) AND country="*" AND collection_date="*"', 'result_type': 'sequence', 'data_portal': 'ena'},
}
format = 'fasta'

class retrieve_data:
    def __init__(self, ena_search, username="", password=""):
        self.ena_search = ena_search        # A dictionary of that includes: query and result type (to search), data portal (to search in) and search fields to return
        self.username = username
        self.password = password
        self.BASE_PORTAL_API_SEARCH_URL = 'https://www.ebi.ac.uk/ena/portal/api/search'
        self.ena_headers = {
            'accept': '*/*',
        }       # Define headers for the requests

    def req(URL, headers, params, user="", password=""):
        """
        Run a request and retrieve the output
        :param URL: URL used for the search
        :param headers: Headers to be used in the search
        :param params: Parameters for the request
        :param user: Username (only if authentication required)
        :param password: Username password (only if authentication required)
        :return: A response object with the results of the search
        """
        if user == "":
            # If a username was not provided
            response = requests.get(URL, headers=headers, params=params)  # No authentication required in the query
        else:
            # If a username was provided
            response = requests.get(URL, headers=headers, params=params,
                                    auth=HTTPBasicAuth(user, password))  # Authentication required in the query
            print(response.url)
        return response

    def build_request_params(**kwargs):
        """
        Build parameters for the request search
        :param query_url: query URL to use in the search
        :param start: starting point for results to be retrieved
        :return: A tuple of tuples of the parameters to be used in the request search
        """
        search_params = {}
        for key, value in kwargs.items():
            if type(value) is list:
                search_params[key] = ",".join(value)
            else:
                search_params[key] = value
        return search_params

    
    def coordinate_retrieval(self):
        """
        Run the retrieval of ENA data
        :return: Data frame
        """
        today = datetime.date.today()
        date = today.strftime('%d%m%Y')
        print('> Running data request... [{}]'.format(datetime.datetime.now()))
        if 'authentication' in self.ena_search.keys():
            # If there is an authentication flag for the result type to search for
            self.ena_search_params = retrieve_data.build_request_params(dataPortal=self.ena_search['data_portal'],
                                                          fields=self.ena_search['search_fields'],
                                                          result=self.ena_search['result_type'],
                                                          dccDataOnly=True,
                                                          limit=0)  # Create the parameter tuple
            print(self.ena_search_params)
            self.ena_search_result = retrieve_data.req(self.BASE_PORTAL_API_SEARCH_URL, self.ena_headers, self.ena_search_params, self.username, self.password)
        else:
            self.ena_search_params = retrieve_data.build_request_params(dataPortal=self.ena_search['data_portal'],
                                                          fields=self.ena_search['search_fields'],
                                                          query=self.ena_search['query'],
                                                          result=self.ena_search['result_type'],
                                                          excludeAccessions='LC722946',
                                                          limit=0)
            print(self.ena_search_params)
            self.ena_search_result = retrieve_data.req(self.BASE_PORTAL_API_SEARCH_URL, self.ena_headers, self.ena_search_params)      # Search the query
        self.ena_results = pd.read_csv(io.StringIO(self.ena_search_result.content.decode('UTF-8')), sep="\t")      # Save results in a dataframe
        output_file = 'data/ENA_Search.tsv'.format(self.ena_search['result_type'], date)
        self.ena_results.to_csv(output_file, sep="\t", index=False)      # Save search results to a dataframe
        

if __name__ == '__main__':
    for key, value in ena_searches.items():
        data_retrieval = retrieve_data(ena_searches[key])     # Instantiate class with information
        ena_results = data_retrieval.coordinate_retrieval()

    # ena_results = pd.read_csv('ENA_Search_sequence_07092022.tsv', sep="\t")       # Temp: for bug fixing

    