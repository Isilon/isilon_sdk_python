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
from swagger_client.apis.cluster_api import ClusterApi


class TestClusterApi(unittest.TestCase):
    """ ClusterApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.cluster_api.ClusterApi()

    def tearDown(self):
        pass

    def test_create_cluster_add_node_item(self):
        """
        Test case for create_cluster_add_node_item

        
        """
        pass

    def test_get_cluster_config(self):
        """
        Test case for get_cluster_config

        
        """
        pass

    def test_get_cluster_email(self):
        """
        Test case for get_cluster_email

        
        """
        pass

    def test_get_cluster_identity(self):
        """
        Test case for get_cluster_identity

        
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

    def test_get_cluster_nodes_available(self):
        """
        Test case for get_cluster_nodes_available

        
        """
        pass

    def test_get_cluster_owner(self):
        """
        Test case for get_cluster_owner

        
        """
        pass

    def test_get_cluster_statfs(self):
        """
        Test case for get_cluster_statfs

        
        """
        pass

    def test_get_cluster_time(self):
        """
        Test case for get_cluster_time

        
        """
        pass

    def test_get_cluster_timezone(self):
        """
        Test case for get_cluster_timezone

        
        """
        pass

    def test_get_cluster_version(self):
        """
        Test case for get_cluster_version

        
        """
        pass

    def test_get_timezone_region(self):
        """
        Test case for get_timezone_region

        
        """
        pass

    def test_get_timezone_settings(self):
        """
        Test case for get_timezone_settings

        
        """
        pass

    def test_update_cluster_email(self):
        """
        Test case for update_cluster_email

        
        """
        pass

    def test_update_cluster_identity(self):
        """
        Test case for update_cluster_identity

        
        """
        pass

    def test_update_cluster_node(self):
        """
        Test case for update_cluster_node

        
        """
        pass

    def test_update_cluster_owner(self):
        """
        Test case for update_cluster_owner

        
        """
        pass

    def test_update_cluster_time(self):
        """
        Test case for update_cluster_time

        
        """
        pass

    def test_update_cluster_timezone(self):
        """
        Test case for update_cluster_timezone

        
        """
        pass

    def test_update_timezone_settings(self):
        """
        Test case for update_timezone_settings

        
        """
        pass


if __name__ == '__main__':
    unittest.main()