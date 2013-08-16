Simple Python Scripts for Wordpress Rest API
===

- Before using it, please look at config.py. You need to configure the variables here correctly before start using the scripts.

- In case you don't want to push the credential to config.py, please create your own local_config.py and configure variables:

```
domain = 'PLEASE PUT YOUR SITE DOMAIN' #for example, public-api.wordpress.com
api_path = 'PLEASE PUT API PATH' #for example, if self-hosted, it might be "wp-json.php".

#authentication for API
username = "YOUR USERNAME"
password = "YOUR PASSWORD"
```

- Please also install library in setup.pip

```
pip install -r setup.pip
```

getPosts.py
---
API path: /posts  
*(my absolute URL path look like: http://xxx.selfhostedwordpress.com/wp-json.php/posts)*  
Method: GET  
Response: JSON data of all posts in http://xxx.selfhostedwordpress.com  

getPost.py
---
Under construction

getPostsDraft.py
---
Under construction

getPostsWithString.py
---
Under construction

newPost.py
---
Under construction




Read more for the JSON Rest API plugin here https://github.com/rmccue/WP-API/blob/master/docs/routes.md


