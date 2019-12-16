import requests
import json

# Making a POST Request

# We need a path

# We need a json object to send

# Possibly headers, depending on the api

# Creating the json
dictionary_postcodes = {
    'postcodes' : ['EC2Y 5AS', 'E14 6GT', 'CT1 2EH']
}

json_body = json.dumps(dictionary_postcodes)
print(json_body)

# The url
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

# The headers
headers = {'Content-type' : 'application/json'}

# Making the requests
postcodes_post_response = requests.post(base_url+path, data=json_body, headers=headers)
print(postcodes_post_response.json())

results = postcodes_post_response.json()['result']

# for request in results:
#     print(request)