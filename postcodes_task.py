import requests
import json

# A programme to requests 3 postcodes to get information:

# User input - can be edited to allow input requests
postcode_1 = "SW193AT"
postcode_2 = "N51EY"
postcode_3 = "NR23LE"
info_1 = "nuts"
info_2 = "admin_district"
info_3 = "ccg"

# ["SW193AT","N51EY","NR23LE"]

# Setup - 3 postcodes to request for:
dictionary_postcodes = {
    'postcodes' : [postcode_1, postcode_2, postcode_3]
}


# Converting dictionary to string using JSON library
json_body = json.dumps(dictionary_postcodes)

# The url
base_url = 'http://api.postcodes.io/'
path = 'postcodes/'

# The headers
headers = {'Content-type' : 'application/json'}

# Executing requests
postcodes_post_response = requests.post(base_url+path, data=json_body, headers=headers)

# Output
results = postcodes_post_response.json()['result']
    ## Using a for loop to get dictionary out of the list
counter = 1
for request in results:
    print("\nPostcode", counter, "request:  ", request['result']['postcode'])
    print("nuts -->", request['result'][info_1])
    print("admin district -->", request['result'][info_2])
    print("ccg -->", request['result'][info_3])
    counter += 1

