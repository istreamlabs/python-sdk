from openapi_client.helper import *
import sys, os

# add the organization you would like to view e.g. istreamplant-internal
ORGANIZATION = "ORGANIZATION"

access_token = get_access_token(os.getenv('ISP_CLIENT_ID'), os.getenv('ISP_SECRET_ID'), ORGANIZATION)
channels = create_client_config(access_token)
summaries = channels.list_channels()

list_channel_ids(summaries)
