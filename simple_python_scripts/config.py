domain = 'PLEASE PUT YOUR SITE DOMAIN' #for example, public-api.wordpress.com
api_path = 'PLEASE PUT API PATH' #for example, if self-hosted, it might be "wp-json.php".

#authentication for API
username = "YOUR USERNAME"
password = "YOUR PASSWORD"

try:
    from local_config import *
except ImportError, e:
    if str(e) != 'No module named local_settings':
        raise e