from config import domain, api_path, username, password
import json
import requests
from requests.auth import HTTPBasicAuth

rest_api = "/posts"

url = "http://"+ domain + "/"+ api_path + rest_api

'''
From this doc https://github.com/rmccue/WP-API/blob/master/docs/routes.md
It said the post object should be

Content-Type: application/json
{"post_title":"Hello World!","post_content":"Content"}

But it doesn't work for me. I have to dig in the code and found that I have to use
the payload as the line below.

I will find more about attribute that I can use to create new post.
'''

payload =  {"title":"Hello Request","content_raw":"Natty Content", "status":"publish"}
headers = {'content-type': 'application/json'}


r = requests.post(url, auth=HTTPBasicAuth(username, password), data=json.dumps(payload), headers=headers)
print r.text

