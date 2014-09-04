rest_tools
======

# Description:
This is a module to interact with REST APIs using Python Requests and JSON.

# HTTP GET:
<pre>
>>> from rest_tools import *
>>> j = rest_get("http://www.fakeapi.com/api/v2/info/")
>>> print(j)
{u'version': u'2.0', u'response': [{u'info1': None, u'info2': "something" }]}
</pre>

# HTTP PUSH (with basic authentication):
<pre>
>>> from rest_tools import *
>>> username = "test"
>>> passwd = "test"
>>> payload = { 
...             "DeviceId": "d07bb3fb-351b-4cf6-8770-f83b66a1a0", 
...             "role": "Server", 
...             "roleSource": "manual"
...             } 
>>> rest_put("http://www.fakeapi.com/api/v2/device/", payload, username, passwd)
{u'version': u'2.0', u'response': u'Number of records updated for role [d07bb3fb-351b-4cf6-8770-f83b66a1a0]'}
</pre>