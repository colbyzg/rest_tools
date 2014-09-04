import json

try:
	import requests
except ImportError:
	print("request module not installed - try 'pip install requests'")

# Simple HTTP GET
def rest_get(url, user="", passwd=""):
	if len(user) > 1 and len(passwd) > 1:
		auth = HTTPBasicAuth(user,passwd)
		r = requests.get(url, auth=auth)
	else:
		r = requests.get(url)
	j = json.loads(r.content)
	return j

# Sending JSON data with an HTTP PUT
def rest_put(url, payload, user="", passwd=""):
	my_headers = {'Content-type': 'application/json'}
	if len(user) > 1 and len(passwd) > 1:
		auth = HTTPBasicAuth(user,passwd)
		r = requests.put(url, data=json.dumps(payload), auth=auth, headers=my_headers)
	else:
		r = requests.put(url, data=json.dumps(payload), headers=my_headers)
	j = json.loads(r.content)
	return j