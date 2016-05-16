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
from swagger_client.apis.cloud_api import CloudApi


class TestCloudApi(unittest.TestCase):
    """ CloudApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.cloud_api.CloudApi()

    def tearDown(self):
        pass

    def test_create_cloud_access_item(self):
        """
        Test case for create_cloud_access_item

        
        """
        pass

    def test_create_cloud_account(self):
        """
        Test case for create_cloud_account

        
        """
        pass

    def test_create_cloud_job(self):
        """
        Test case for create_cloud_job

        
        """
        pass

    def test_create_cloud_pool(self):
        """
        Test case for create_cloud_pool

        
        """
        pass

    def test_create_settings_encryption_key_item(self):
        """
        Test case for create_settings_encryption_key_item

        
        """
        pass

    def test_create_settings_reporting_eula_item(self):
        """
        Test case for create_settings_reporting_eula_item

        
        """
        pass

    def test_delete_cloud_access_guid(self):
        """
        Test case for delete_cloud_access_guid

        
        """
        pass

    def test_delete_cloud_account(self):
        """
        Test case for delete_cloud_account

        
        """
        pass

    def test_delete_cloud_pool(self):
        """
        Test case for delete_cloud_pool

        
        """
        pass

    def test_delete_settings_reporting_eula(self):
        """
        Test case for delete_settings_reporting_eula

        
        """
        pass

    def test_get_cloud_access_guid(self):
        """
        Test case for get_cloud_access_guid

        
        """
        pass

    def test_get_cloud_account(self):
        """
        Test case for get_cloud_account

        
        """
        pass

    def test_get_cloud_job(self):
        """
        Test case for get_cloud_job

        
        """
        pass

    def test_get_cloud_jobs_file(self):
        """
        Test case for get_cloud_jobs_file

        
        """
        pass

    def test_get_cloud_pool(self):
        """
        Test case for get_cloud_pool

        
        """
        pass

    def test_get_cloud_settings(self):
        """
        Test case for get_cloud_settings

        
        """
        pass

    def test_list_cloud_access(self):
        """
        Test case for list_cloud_access

        
        """
        pass

    def test_list_cloud_accounts(self):
        """
        Test case for list_cloud_accounts

        
        """
        pass

    def test_list_cloud_jobs(self):
        """
        Test case for list_cloud_jobs

        
        """
        pass

    def test_list_cloud_pools(self):
        """
        Test case for list_cloud_pools

        
        """
        pass

    def test_list_settings_reporting_eula(self):
        """
        Test case for list_settings_reporting_eula

        
        """
        pass

    def test_update_cloud_account(self):
        """
        Test case for update_cloud_account

        
        """
        pass

    def test_update_cloud_job(self):
        """
        Test case for update_cloud_job

        
        """
        pass

    def test_update_cloud_pool(self):
        """
        Test case for update_cloud_pool

        
        """
        pass

    def test_update_cloud_settings(self):
        """
        Test case for update_cloud_settings

        
        """
        pass


if __name__ == '__main__':
    unittest.main()