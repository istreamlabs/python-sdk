"""
    iStreamPlanet Channels API

    This API provides a way to list, create, and run channels.  Channels consist of inputs (ingest), transcoding settings like codecs and bitrates, and outputs (publishing).  List calls use cursor-based pagination with [RFC 5988](https://tools.ietf.org/html/rfc5988) Link headers. Clients *should* read this header and follow the next link to read all pages of results.   # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: support@istreamplanet.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.channel_operations_api import ChannelOperationsApi  # noqa: E501


class TestChannelOperationsApi(unittest.TestCase):
    """ChannelOperationsApi unit test stubs"""

    def setUp(self):
        self.api = ChannelOperationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clear_dvr_window(self):
        """Test case for clear_dvr_window

        Clear DVR Window  # noqa: E501
        """
        pass

    def test_get_signals(self):
        """Test case for get_signals

        Get Signals  # noqa: E501
        """
        pass

    def test_insert_id3(self):
        """Test case for insert_id3

        Insert ID3  # noqa: E501
        """
        pass

    def test_insert_scte35(self):
        """Test case for insert_scte35

        Insert SCTE-35  # noqa: E501
        """
        pass

    def test_preview_image(self):
        """Test case for preview_image

        Get Preview Image  # noqa: E501
        """
        pass

    def test_program_end(self):
        """Test case for program_end

        Program End  # noqa: E501
        """
        pass

    def test_program_start(self):
        """Test case for program_start

        Program Start  # noqa: E501
        """
        pass

    def test_signal(self):
        """Test case for signal

        Generic Signal  # noqa: E501
        """
        pass

    def test_slate_in(self):
        """Test case for slate_in

        Slate in  # noqa: E501
        """
        pass

    def test_slate_out(self):
        """Test case for slate_out

        Slate out  # noqa: E501
        """
        pass

    def test_splice_end(self):
        """Test case for splice_end

        Splice Insert End  # noqa: E501
        """
        pass

    def test_splice_start(self):
        """Test case for splice_start

        Splice Insert Start  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()