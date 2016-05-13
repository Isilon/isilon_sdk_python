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
from swagger_client.apis.antivirus_api import AntivirusApi


class TestAntivirusApi(unittest.TestCase):
    """ AntivirusApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.antivirus_api.AntivirusApi()

    def tearDown(self):
        pass

    def test_create_antivirus_policy(self):
        """
        Test case for create_antivirus_policy

        
        """
        pass

    def test_create_antivirus_scan_item(self):
        """
        Test case for create_antivirus_scan_item

        
        """
        pass

    def test_create_antivirus_server(self):
        """
        Test case for create_antivirus_server

        
        """
        pass

    def test_delete_antivirus_policies(self):
        """
        Test case for delete_antivirus_policies

        
        """
        pass

    def test_delete_antivirus_policy(self):
        """
        Test case for delete_antivirus_policy

        
        """
        pass

    def test_delete_antivirus_server(self):
        """
        Test case for delete_antivirus_server

        
        """
        pass

    def test_delete_antivirus_servers(self):
        """
        Test case for delete_antivirus_servers

        
        """
        pass

    def test_delete_reports_scan(self):
        """
        Test case for delete_reports_scan

        
        """
        pass

    def test_delete_reports_scans(self):
        """
        Test case for delete_reports_scans

        
        """
        pass

    def test_get_antivirus_policy(self):
        """
        Test case for get_antivirus_policy

        
        """
        pass

    def test_get_antivirus_quarantine_path(self):
        """
        Test case for get_antivirus_quarantine_path

        
        """
        pass

    def test_get_antivirus_server(self):
        """
        Test case for get_antivirus_server

        
        """
        pass

    def test_get_antivirus_settings(self):
        """
        Test case for get_antivirus_settings

        
        """
        pass

    def test_get_reports_scan(self):
        """
        Test case for get_reports_scan

        
        """
        pass

    def test_get_reports_scans(self):
        """
        Test case for get_reports_scans

        
        """
        pass

    def test_get_reports_threat(self):
        """
        Test case for get_reports_threat

        
        """
        pass

    def test_get_reports_threats(self):
        """
        Test case for get_reports_threats

        
        """
        pass

    def test_list_antivirus_policies(self):
        """
        Test case for list_antivirus_policies

        
        """
        pass

    def test_list_antivirus_servers(self):
        """
        Test case for list_antivirus_servers

        
        """
        pass

    def test_update_antivirus_policy(self):
        """
        Test case for update_antivirus_policy

        
        """
        pass

    def test_update_antivirus_quarantine_path(self):
        """
        Test case for update_antivirus_quarantine_path

        
        """
        pass

    def test_update_antivirus_server(self):
        """
        Test case for update_antivirus_server

        
        """
        pass

    def test_update_antivirus_settings(self):
        """
        Test case for update_antivirus_settings

        
        """
        pass


if __name__ == '__main__':
    unittest.main()