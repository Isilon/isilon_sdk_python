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
from swagger_client.apis.audit_api import AuditApi


class TestAuditApi(unittest.TestCase):
    """ AuditApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.audit_api.AuditApi()

    def tearDown(self):
        pass

    def test_create_audit_topic(self):
        """
        Test case for create_audit_topic

        
        """
        pass

    def test_delete_audit_topic(self):
        """
        Test case for delete_audit_topic

        
        """
        pass

    def test_get_audit_settings(self):
        """
        Test case for get_audit_settings

        
        """
        pass

    def test_get_audit_topic(self):
        """
        Test case for get_audit_topic

        
        """
        pass

    def test_get_settings_global(self):
        """
        Test case for get_settings_global

        
        """
        pass

    def test_list_audit_topics(self):
        """
        Test case for list_audit_topics

        
        """
        pass

    def test_update_audit_settings(self):
        """
        Test case for update_audit_settings

        
        """
        pass

    def test_update_audit_topic(self):
        """
        Test case for update_audit_topic

        
        """
        pass

    def test_update_settings_global(self):
        """
        Test case for update_settings_global

        
        """
        pass


if __name__ == '__main__':
    unittest.main()