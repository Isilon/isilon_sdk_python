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
from swagger_client.apis.storagepool_api import StoragepoolApi


class TestStoragepoolApi(unittest.TestCase):
    """ StoragepoolApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.storagepool_api.StoragepoolApi()

    def tearDown(self):
        pass

    def test_create_compatibilities_class_active_item(self):
        """
        Test case for create_compatibilities_class_active_item

        
        """
        pass

    def test_create_compatibilities_ssd_active_item(self):
        """
        Test case for create_compatibilities_ssd_active_item

        
        """
        pass

    def test_create_storagepool_nodepool(self):
        """
        Test case for create_storagepool_nodepool

        
        """
        pass

    def test_create_storagepool_tier(self):
        """
        Test case for create_storagepool_tier

        
        """
        pass

    def test_delete_compatibilities_class_active_by_id(self):
        """
        Test case for delete_compatibilities_class_active_by_id

        
        """
        pass

    def test_delete_compatibilities_ssd_active_by_id(self):
        """
        Test case for delete_compatibilities_ssd_active_by_id

        
        """
        pass

    def test_delete_storagepool_nodepool(self):
        """
        Test case for delete_storagepool_nodepool

        
        """
        pass

    def test_delete_storagepool_tier(self):
        """
        Test case for delete_storagepool_tier

        
        """
        pass

    def test_delete_storagepool_tiers(self):
        """
        Test case for delete_storagepool_tiers

        
        """
        pass

    def test_get_compatibilities_class_active_by_id(self):
        """
        Test case for get_compatibilities_class_active_by_id

        
        """
        pass

    def test_get_compatibilities_class_available(self):
        """
        Test case for get_compatibilities_class_available

        
        """
        pass

    def test_get_compatibilities_ssd_active_by_id(self):
        """
        Test case for get_compatibilities_ssd_active_by_id

        
        """
        pass

    def test_get_compatibilities_ssd_available(self):
        """
        Test case for get_compatibilities_ssd_available

        
        """
        pass

    def test_get_storagepool_nodepool(self):
        """
        Test case for get_storagepool_nodepool

        
        """
        pass

    def test_get_storagepool_settings(self):
        """
        Test case for get_storagepool_settings

        
        """
        pass

    def test_get_storagepool_status(self):
        """
        Test case for get_storagepool_status

        
        """
        pass

    def test_get_storagepool_storagepools(self):
        """
        Test case for get_storagepool_storagepools

        
        """
        pass

    def test_get_storagepool_suggested_protection_nid(self):
        """
        Test case for get_storagepool_suggested_protection_nid

        
        """
        pass

    def test_get_storagepool_tier(self):
        """
        Test case for get_storagepool_tier

        
        """
        pass

    def test_get_storagepool_unprovisioned(self):
        """
        Test case for get_storagepool_unprovisioned

        
        """
        pass

    def test_list_compatibilities_class_active(self):
        """
        Test case for list_compatibilities_class_active

        
        """
        pass

    def test_list_compatibilities_ssd_active(self):
        """
        Test case for list_compatibilities_ssd_active

        
        """
        pass

    def test_list_storagepool_nodepools(self):
        """
        Test case for list_storagepool_nodepools

        
        """
        pass

    def test_list_storagepool_tiers(self):
        """
        Test case for list_storagepool_tiers

        
        """
        pass

    def test_update_compatibilities_ssd_active_by_id(self):
        """
        Test case for update_compatibilities_ssd_active_by_id

        
        """
        pass

    def test_update_storagepool_nodepool(self):
        """
        Test case for update_storagepool_nodepool

        
        """
        pass

    def test_update_storagepool_settings(self):
        """
        Test case for update_storagepool_settings

        
        """
        pass

    def test_update_storagepool_tier(self):
        """
        Test case for update_storagepool_tier

        
        """
        pass


if __name__ == '__main__':
    unittest.main()