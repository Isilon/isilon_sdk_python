# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_9_1_0
from isi_sdk_9_1_0.api.upgrade_cluster_api import UpgradeClusterApi  # noqa: E501
from isi_sdk_9_1_0.rest import ApiException


class TestUpgradeClusterApi(unittest.TestCase):
    """UpgradeClusterApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_9_1_0.api.upgrade_cluster_api.UpgradeClusterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_nodes_node_patch_sync_item(self):
        """Test case for create_nodes_node_patch_sync_item

        """
        pass

    def test_get_nodes_node_firmware_device(self):
        """Test case for get_nodes_node_firmware_device

        """
        pass

    def test_get_nodes_node_firmware_status(self):
        """Test case for get_nodes_node_firmware_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
