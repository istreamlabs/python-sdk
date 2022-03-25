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
from openapi_client.model.channel_packaging_content_protection_key_rotation import ChannelPackagingContentProtectionKeyRotation


class TestChannelPackagingContentProtectionKeyRotation(unittest.TestCase):
    """ChannelPackagingContentProtectionKeyRotation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testChannelPackagingContentProtectionKeyRotation(self):
        """Test ChannelPackagingContentProtectionKeyRotation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ChannelPackagingContentProtectionKeyRotation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
