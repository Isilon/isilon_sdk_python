# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_9_0_0
from isi_sdk_9_0_0.api.ipmi_api import IpmiApi  # noqa: E501
from isi_sdk_9_0_0.rest import ApiException


class TestIpmiApi(unittest.TestCase):
    """IpmiApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_9_0_0.api.ipmi_api.IpmiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_config_feature(self):
        """Test case for get_config_feature

        """
        pass

    def test_get_config_features(self):
        """Test case for get_config_features

        """
        pass

    def test_get_config_network(self):
        """Test case for get_config_network

        """
        pass

    def test_get_config_node(self):
        """Test case for get_config_node

        """
        pass

    def test_get_config_nodes(self):
        """Test case for get_config_nodes

        """
        pass

    def test_get_config_settings(self):
        """Test case for get_config_settings

        """
        pass

    def test_get_config_user(self):
        """Test case for get_config_user

        """
        pass

    def test_update_config_feature(self):
        """Test case for update_config_feature

        """
        pass

    def test_update_config_network(self):
        """Test case for update_config_network

        """
        pass

    def test_update_config_settings(self):
        """Test case for update_config_settings

        """
        pass

    def test_update_config_user(self):
        """Test case for update_config_user

        """
        pass


if __name__ == '__main__':
    unittest.main()