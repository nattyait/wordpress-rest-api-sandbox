from config import domain, api_path
import json
import requests
from requests.auth import HTTPBasicAuth


username = "natty"
password = "TheNatty69"

rest_api = "/posts"

url = "http://"+ domain + "/"+ api_path + rest_api
#payload = {"post_title":"Hello World!","post_content":"Content"}
payload =  {"title":"Hello Request","content_raw":"Natty Content", "status":"publish"}
headers = {'content-type': 'application/json'}


r = requests.post(url, auth=HTTPBasicAuth(username, password), data=json.dumps(payload), headers=headers)
print r.text

