"""
    iStreamPlanet Channels API

    This API provides a way to list, create, and run channels.  Channels consist of inputs (ingest), transcoding settings like codecs and bitrates, and outputs (publishing).  List calls use cursor-based pagination with [RFC 5988](https://tools.ietf.org/html/rfc5988) Link headers. Clients *should* read this header and follow the next link to read all pages of results.   # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: support@istreamplanet.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.channel_publishing_closed_caption_streams import ChannelPublishingClosedCaptionStreams
from openapi_client.model.channel_publishing_live2vod import ChannelPublishingLive2vod
from openapi_client.model.channel_publishing_publications import ChannelPublishingPublications
globals()['ChannelPublishingClosedCaptionStreams'] = ChannelPublishingClosedCaptionStreams
globals()['ChannelPublishingLive2vod'] = ChannelPublishingLive2vod
globals()['ChannelPublishingPublications'] = ChannelPublishingPublications
from openapi_client.model.channel_publishing import ChannelPublishing


class TestChannelPublishing(unittest.TestCase):
    """ChannelPublishing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChannelPublishing(self):
        """Test ChannelPublishing"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChannelPublishing()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()