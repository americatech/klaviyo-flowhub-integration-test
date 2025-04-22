from klaviyo_api import KlaviyoAPI
from api_call_http import call_klaviyo_api_http

import json
import requests

hello_world_payload_as_dict = {'data':
    {
        "type": "event",
        "attributes":
            {
                "profile": {
                    'email': 'julie.rodriguez@klaviyo-demo.com'
                },
                "metric": {
                    "name": 'Hello World'
                },
                "properties": {'Field_1': 'True', 
                               'Field_2': '20', 
                               'Field_3': 'string'
                },
                "time": '2022-09-20T14:33:49+00:00'
            }
    }
}

def get_klaviyo_data_http(api_key, endpoint):
    klaviyo = KlaviyoAPI('', max_delay=60, max_retries=3)


# Main function to run the script
def main():

    print('Getting Klaviyo data from Klaviyo API')
    user_input = int(input("Select '1' for using http or '2' for using the SDK:"))

    # Loop user_input to ensure user selected the right value, or prompt again
    while user_input != 1 and user_input != 2:
        user_input = int(input("Please try again! Select '1' for using http or '2' for using the SDK:"))

    # Load configuration from JSON file
    with open('/json/config.json', 'r') as config_file:
        config = json.load(config_file)

    # Extract API key and endpoint from the configuration
    public_api_key = config['public_api_key']
    endpoint = config['endpoint']

    if user_input == '1':
        # Use the http api call
        call_klaviyo_api_http(public_api_key, endpoint, hello_world_payload_as_dict)
    elif user_input == '2':
        # Use the SDK api call
        klaviyo = KlaviyoAPI('', max_delay=60, max_retries=3)
        klaviyo.Client.create_client_event(public_api_key, hello_world_payload_as_dict)

