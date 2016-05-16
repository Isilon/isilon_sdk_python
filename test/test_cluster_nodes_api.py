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
from swagger_client.apis.cluster_nodes_api import ClusterNodesApi


class TestClusterNodesApi(unittest.TestCase):
    """ ClusterNodesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.cluster_nodes_api.ClusterNodesApi()

    def tearDown(self):
        pass

    def test_create_drives_drive_add_item(self):
        """
        Test case for create_drives_drive_add_item

        
        """
        pass

    def test_create_drives_drive_firmware_update_item(self):
        """
        Test case for create_drives_drive_firmware_update_item

        
        """
        pass

    def test_create_drives_drive_format_item(self):
        """
        Test case for create_drives_drive_format_item

        
        """
        pass

    def test_create_drives_drive_purpose_item(self):
        """
        Test case for create_drives_drive_purpose_item

        
        """
        pass

    def test_create_drives_drive_smartfail_item(self):
        """
        Test case for create_drives_drive_smartfail_item

        
        """
        pass

    def test_create_drives_drive_stopfail_item(self):
        """
        Test case for create_drives_drive_stopfail_item

        
        """
        pass

    def test_create_drives_drive_suspend_item(self):
        """
        Test case for create_drives_drive_suspend_item

        
        """
        pass

    def test_create_node_reboot_item(self):
        """
        Test case for create_node_reboot_item

        
        """
        pass

    def test_create_node_shutdown_item(self):
        """
        Test case for create_node_shutdown_item

        
        """
        pass

    def test_get_drives_drive_firmware(self):
        """
        Test case for get_drives_drive_firmware

        
        """
        pass

    def test_get_node_drive(self):
        """
        Test case for get_node_drive

        
        """
        pass

    def test_get_node_drives(self):
        """
        Test case for get_node_drives

        
        """
        pass

    def test_get_node_drives_purposelist(self):
        """
        Test case for get_node_drives_purposelist

        
        """
        pass

    def test_get_node_hardware(self):
        """
        Test case for get_node_hardware

        
        """
        pass

    def test_get_node_partitions(self):
        """
        Test case for get_node_partitions

        
        """
        pass

    def test_get_node_sensors(self):
        """
        Test case for get_node_sensors

        
        """
        pass

    def test_get_node_state(self):
        """
        Test case for get_node_state

        
        """
        pass

    def test_get_node_state_readonly(self):
        """
        Test case for get_node_state_readonly

        
        """
        pass

    def test_get_node_state_servicelight(self):
        """
        Test case for get_node_state_servicelight

        
        """
        pass

    def test_get_node_state_smartfail(self):
        """
        Test case for get_node_state_smartfail

        
        """
        pass

    def test_get_node_status(self):
        """
        Test case for get_node_status

        
        """
        pass

    def test_get_node_status_batterystatus(self):
        """
        Test case for get_node_status_batterystatus

        
        """
        pass

    def test_list_drives_drive_firmware_update(self):
        """
        Test case for list_drives_drive_firmware_update

        
        """
        pass

    def test_update_node_state_readonly(self):
        """
        Test case for update_node_state_readonly

        
        """
        pass

    def test_update_node_state_servicelight(self):
        """
        Test case for update_node_state_servicelight

        
        """
        pass

    def test_update_node_state_smartfail(self):
        """
        Test case for update_node_state_smartfail

        
        """
        pass


if __name__ == '__main__':
    unittest.main()