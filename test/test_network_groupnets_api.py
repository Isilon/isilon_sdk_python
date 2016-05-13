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
from swagger_client.apis.network_groupnets_api import NetworkGroupnetsApi


class TestNetworkGroupnetsApi(unittest.TestCase):
    """ NetworkGroupnetsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.network_groupnets_api.NetworkGroupnetsApi()

    def tearDown(self):
        pass

    def test_create_groupnet_subnet(self):
        """
        Test case for create_groupnet_subnet

        
        """
        pass

    def test_create_subnets_subnet_pool(self):
        """
        Test case for create_subnets_subnet_pool

        
        """
        pass

    def test_delete_groupnet_subnet(self):
        """
        Test case for delete_groupnet_subnet

        
        """
        pass

    def test_delete_subnets_subnet_pool(self):
        """
        Test case for delete_subnets_subnet_pool

        
        """
        pass

    def test_get_groupnet_subnet(self):
        """
        Test case for get_groupnet_subnet

        
        """
        pass

    def test_get_subnets_subnet_pool(self):
        """
        Test case for get_subnets_subnet_pool

        
        """
        pass

    def test_list_groupnet_subnets(self):
        """
        Test case for list_groupnet_subnets

        
        """
        pass

    def test_list_subnets_subnet_pools(self):
        """
        Test case for list_subnets_subnet_pools

        
        """
        pass

    def test_update_groupnet_subnet(self):
        """
        Test case for update_groupnet_subnet

        
        """
        pass

    def test_update_subnets_subnet_pool(self):
        """
        Test case for update_subnets_subnet_pool

        
        """
        pass


if __name__ == '__main__':
    unittest.main()