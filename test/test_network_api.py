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
from swagger_client.apis.network_api import NetworkApi


class TestNetworkApi(unittest.TestCase):
    """ NetworkApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.network_api.NetworkApi()

    def tearDown(self):
        pass

    def test_create_dnscache_flush_item(self):
        """
        Test case for create_dnscache_flush_item

        
        """
        pass

    def test_create_network_groupnet(self):
        """
        Test case for create_network_groupnet

        
        """
        pass

    def test_create_network_sc_rebalance_all_item(self):
        """
        Test case for create_network_sc_rebalance_all_item

        
        """
        pass

    def test_delete_network_groupnet(self):
        """
        Test case for delete_network_groupnet

        
        """
        pass

    def test_get_network_dnscache(self):
        """
        Test case for get_network_dnscache

        
        """
        pass

    def test_get_network_external(self):
        """
        Test case for get_network_external

        
        """
        pass

    def test_get_network_groupnet(self):
        """
        Test case for get_network_groupnet

        
        """
        pass

    def test_get_network_interfaces(self):
        """
        Test case for get_network_interfaces

        
        """
        pass

    def test_get_network_pools(self):
        """
        Test case for get_network_pools

        
        """
        pass

    def test_get_network_rules(self):
        """
        Test case for get_network_rules

        
        """
        pass

    def test_get_network_subnets(self):
        """
        Test case for get_network_subnets

        
        """
        pass

    def test_list_network_groupnets(self):
        """
        Test case for list_network_groupnets

        
        """
        pass

    def test_update_network_dnscache(self):
        """
        Test case for update_network_dnscache

        
        """
        pass

    def test_update_network_external(self):
        """
        Test case for update_network_external

        
        """
        pass

    def test_update_network_groupnet(self):
        """
        Test case for update_network_groupnet

        
        """
        pass


if __name__ == '__main__':
    unittest.main()