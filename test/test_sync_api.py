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
from swagger_client.apis.sync_api import SyncApi


class TestSyncApi(unittest.TestCase):
    """ SyncApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.sync_api.SyncApi()

    def tearDown(self):
        pass

    def test_create_sync_job(self):
        """
        Test case for create_sync_job

        
        """
        pass

    def test_create_sync_policy(self):
        """
        Test case for create_sync_policy

        
        """
        pass

    def test_create_sync_reports_rotate_item(self):
        """
        Test case for create_sync_reports_rotate_item

        
        """
        pass

    def test_create_sync_rule(self):
        """
        Test case for create_sync_rule

        
        """
        pass

    def test_delete_sync_policies(self):
        """
        Test case for delete_sync_policies

        
        """
        pass

    def test_delete_sync_policy(self):
        """
        Test case for delete_sync_policy

        
        """
        pass

    def test_delete_sync_rule(self):
        """
        Test case for delete_sync_rule

        
        """
        pass

    def test_delete_sync_rules(self):
        """
        Test case for delete_sync_rules

        
        """
        pass

    def test_delete_target_policy(self):
        """
        Test case for delete_target_policy

        
        """
        pass

    def test_get_history_cpu(self):
        """
        Test case for get_history_cpu

        
        """
        pass

    def test_get_history_file(self):
        """
        Test case for get_history_file

        
        """
        pass

    def test_get_history_network(self):
        """
        Test case for get_history_network

        
        """
        pass

    def test_get_history_worker(self):
        """
        Test case for get_history_worker

        
        """
        pass

    def test_get_sync_job(self):
        """
        Test case for get_sync_job

        
        """
        pass

    def test_get_sync_license(self):
        """
        Test case for get_sync_license

        
        """
        pass

    def test_get_sync_policy(self):
        """
        Test case for get_sync_policy

        
        """
        pass

    def test_get_sync_report(self):
        """
        Test case for get_sync_report

        
        """
        pass

    def test_get_sync_reports(self):
        """
        Test case for get_sync_reports

        
        """
        pass

    def test_get_sync_rule(self):
        """
        Test case for get_sync_rule

        
        """
        pass

    def test_get_sync_settings(self):
        """
        Test case for get_sync_settings

        
        """
        pass

    def test_get_target_policies(self):
        """
        Test case for get_target_policies

        
        """
        pass

    def test_get_target_policy(self):
        """
        Test case for get_target_policy

        
        """
        pass

    def test_get_target_report(self):
        """
        Test case for get_target_report

        
        """
        pass

    def test_get_target_reports(self):
        """
        Test case for get_target_reports

        
        """
        pass

    def test_list_sync_jobs(self):
        """
        Test case for list_sync_jobs

        
        """
        pass

    def test_list_sync_policies(self):
        """
        Test case for list_sync_policies

        
        """
        pass

    def test_list_sync_reports_rotate(self):
        """
        Test case for list_sync_reports_rotate

        
        """
        pass

    def test_list_sync_rules(self):
        """
        Test case for list_sync_rules

        
        """
        pass

    def test_update_sync_job(self):
        """
        Test case for update_sync_job

        
        """
        pass

    def test_update_sync_policy(self):
        """
        Test case for update_sync_policy

        
        """
        pass

    def test_update_sync_rule(self):
        """
        Test case for update_sync_rule

        
        """
        pass

    def test_update_sync_settings(self):
        """
        Test case for update_sync_settings

        
        """
        pass


if __name__ == '__main__':
    unittest.main()