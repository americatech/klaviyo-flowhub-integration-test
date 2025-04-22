# This code can be used to call Klaviyo API endpoints using HTTP requests.
import requests
import json

def call_klaviyo_api_http(public_key, endpoint, hello_world_payload_as_dict):

    # Headers for a direct call on the endpoint
    headers = {
        'Content-Type': "application/json",
        'revision': "2023-08-15"
    }

    # move from a dictionary to a json
    hello_world_payload_as_json = json.dumps(hello_world_payload_as_dict)

    # execute the request
    response = requests.request("POST", 
                                endpoint, 
                                data=hello_world_payload_as_json, 
                                headers=headers, 
                                params={"company_id": public_key})

    print(response)
    print(response.reason)
    print(response.text)