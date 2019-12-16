import requests
# Get requests
# Do not have a body (JSON)
# They have a base url, path and arguments

base_url = 'http://api.postcodes.io/'
path = 'postcodes/'
arguments = 'E146GT'

request_response = requests.get(base_url+path+arguments)
print(request_response)
print(type(request_response))

# Turning a Request to dictionary --> use .json()

dictionary_response = request_response.json()
print(dictionary_response)
print(type(dictionary_response))

