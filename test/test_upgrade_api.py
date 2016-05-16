# coding: utf-8

"""
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.upgrade_api import UpgradeApi


class TestUpgradeApi(unittest.TestCase):
    """ UpgradeApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.upgrade_api.UpgradeApi()

    def tearDown(self):
        pass

    def test_create_cluster_add_remaining_node(self):
        """
        Test case for create_cluster_add_remaining_node

        
        """
        pass

    def test_create_cluster_archive_item(self):
        """
        Test case for create_cluster_archive_item

        
        """
        pass

    def test_create_cluster_assess_item(self):
        """
        Test case for create_cluster_assess_item

        
        """
        pass

    def test_create_cluster_commit_item(self):
        """
        Test case for create_cluster_commit_item

        
        """
        pass

    def test_create_cluster_firmware_assess_item(self):
        """
        Test case for create_cluster_firmware_assess_item

        
        """
        pass

    def test_create_cluster_firmware_upgrade_item(self):
        """
        Test case for create_cluster_firmware_upgrade_item

        
        """
        pass

    def test_create_cluster_patch_abort_item(self):
        """
        Test case for create_cluster_patch_abort_item

        
        """
        pass

    def test_create_cluster_retry_last_action_item(self):
        """
        Test case for create_cluster_retry_last_action_item

        
        """
        pass

    def test_create_cluster_rollback_item(self):
        """
        Test case for create_cluster_rollback_item

        
        """
        pass

    def test_create_cluster_upgrade_item(self):
        """
        Test case for create_cluster_upgrade_item

        
        """
        pass

    def test_get_cluster_firmware_progress(self):
        """
        Test case for get_cluster_firmware_progress

        
        """
        pass

    def test_get_cluster_firmware_status(self):
        """
        Test case for get_cluster_firmware_status

        
        """
        pass

    def test_get_cluster_node(self):
        """
        Test case for get_cluster_node

        
        """
        pass

    def test_get_cluster_nodes(self):
        """
        Test case for get_cluster_nodes

        
        """
        pass

    def test_get_upgrade_cluster(self):
        """
        Test case for get_upgrade_cluster

        
        """
        pass

    def test_update_cluster_upgrade(self):
        """
        Test case for update_cluster_upgrade

        
        """
        pass


if __name__ == '__main__':
    unittest.main()