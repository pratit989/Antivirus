from __future__ import print_function
from os import remove

from pprint import pprint

import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException

# Configure API key authorization: Apikey
configuration = cloudmersive_virus_api_client.Configuration()
configuration.api_key['Apikey'] = str(input('Enter your API key.'))
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))


def scan(input_file='EICAR TEST FILE.txt'):
    try:
        # Scan a file for viruses
        api_response = api_instance.scan_file(input_file)
        pprint(api_response)
        # Uncomment the 2 lines below to enable automatic virus delete
        # if "'clean_result': False" in str(api_response):
        # remove(input_file)
    except ApiException as e:
        print("Exception when calling ScanApi->scan_file: %s\n" % e)
