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
from isi_sdk_9_0_0.api.upgrade_api import UpgradeApi  # noqa: E501
from isi_sdk_9_0_0.rest import ApiException


class TestUpgradeApi(unittest.TestCase):
    """UpgradeApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_9_0_0.api.upgrade_api.UpgradeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cluster_add_remaining_node(self):
        """Test case for create_cluster_add_remaining_node

        """
        pass

    def test_create_cluster_archive_item(self):
        """Test case for create_cluster_archive_item

        """
        pass

    def test_create_cluster_assess_item(self):
        """Test case for create_cluster_assess_item

        """
        pass

    def test_create_cluster_commit_item(self):
        """Test case for create_cluster_commit_item

        """
        pass

    def test_create_cluster_firmware_assess_item(self):
        """Test case for create_cluster_firmware_assess_item

        """
        pass

    def test_create_cluster_firmware_upgrade_item(self):
        """Test case for create_cluster_firmware_upgrade_item

        """
        pass

    def test_create_cluster_patch_abort_item(self):
        """Test case for create_cluster_patch_abort_item

        """
        pass

    def test_create_cluster_patch_patch(self):
        """Test case for create_cluster_patch_patch

        """
        pass

    def test_create_cluster_pause_item(self):
        """Test case for create_cluster_pause_item

        """
        pass

    def test_create_cluster_resume_item(self):
        """Test case for create_cluster_resume_item

        """
        pass

    def test_create_cluster_retry_last_action_item(self):
        """Test case for create_cluster_retry_last_action_item

        """
        pass

    def test_create_cluster_rollback_item(self):
        """Test case for create_cluster_rollback_item

        """
        pass

    def test_create_cluster_upgrade_item(self):
        """Test case for create_cluster_upgrade_item

        """
        pass

    def test_delete_cluster_patch_patch(self):
        """Test case for delete_cluster_patch_patch

        """
        pass

    def test_get_cluster_firmware_device(self):
        """Test case for get_cluster_firmware_device

        """
        pass

    def test_get_cluster_firmware_progress(self):
        """Test case for get_cluster_firmware_progress

        """
        pass

    def test_get_cluster_firmware_status(self):
        """Test case for get_cluster_firmware_status

        """
        pass

    def test_get_cluster_node(self):
        """Test case for get_cluster_node

        """
        pass

    def test_get_cluster_nodes(self):
        """Test case for get_cluster_nodes

        """
        pass

    def test_get_cluster_patch_patch(self):
        """Test case for get_cluster_patch_patch

        """
        pass

    def test_get_upgrade_cluster(self):
        """Test case for get_upgrade_cluster

        """
        pass

    def test_list_cluster_patch_patches(self):
        """Test case for list_cluster_patch_patches

        """
        pass

    def test_update_cluster_unblock(self):
        """Test case for update_cluster_unblock

        """
        pass

    def test_update_cluster_upgrade(self):
        """Test case for update_cluster_upgrade

        """
        pass


if __name__ == '__main__':
    unittest.main()
