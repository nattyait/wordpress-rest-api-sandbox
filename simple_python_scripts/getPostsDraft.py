from config import domain, api_path
import json
import requests

rest_api = "/posts?filter[post_status]=draft"
url = "http://"+ domain + "/"+ api_path + rest_api
r = requests.get(url)
print r.json()