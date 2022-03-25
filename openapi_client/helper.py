from openapi_client import *
from openapi_client.api.channels_api import ChannelsApi
from openapi_client.api.sources_api import SourcesApi
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
import requests, json
import urllib3
urllib3.disable_warnings()

def get_access_token(client_id, client_secret, organization):
    auth = HTTPBasicAuth(client_id, client_secret)
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    audience = 'https://platform.dtc.istreamplanet.net/' + organization
    token = oauth.fetch_token(token_url='https://istreamplanet.auth0.com/oauth/token', auth=auth, audience=audience)
    token_payload = client.token
    access_token = token_payload['access_token']
    return(access_token)

def create_client_config(access_token):
    new_config = Configuration()
    new_config.access_token = access_token
    new_config.api_key_prefix = 'Bearer '
    new_config.verify_ssl = False
    new_client = ApiClient(new_config)
    channels = ChannelsApi(new_client)
    return channels

# function to loop through summary2 list and return channel ids
def list_channel_ids(summaries):
    for s in summaries._data_store.values():
        for i in s:
            for k,v in i._data_store.items():
                print(i['id'])
