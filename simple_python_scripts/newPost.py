from config import domain, api_path, username, password
import json
import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

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

---- payload to use ----
ID: for update
parent: Use for page
date: don't know yet how to parse it here
author: don't know yet how to parse it here
menu_order: User for page
password: any string,
ping_status: open|closed
slug: string

---- can't pass tru json yet ----
sticky: don't know yet how to parse it here

---- not yet implement ----
terms
Post thumbnail
post_meta

Schema is here.. but what I can use is not that matched with the document. Need to research more.
https://github.com/rmccue/WP-API/blob/master/docs/schema.json
'''

payload =  {"title":"Hello Request",
			"content_raw":"Natty Content", 
			"status":"publish", #"draft","pending","private","publish","trash" (draft is default if no value set)
			"excerpt_raw": "This is excerpt",
			"type": "post",
			"name":"hello-hello",
			"comment_status":"closed", # open|closed|registered_only
			}
headers = {'content-type': 'application/json'}

print json.dumps(payload)

r = requests.post(url, auth=HTTPBasicAuth(username, password), data=json.dumps(payload), headers=headers)
print r.text

