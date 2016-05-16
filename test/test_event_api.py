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
from swagger_client.apis.event_api import EventApi


class TestEventApi(unittest.TestCase):
    """ EventApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.event_api.EventApi()

    def tearDown(self):
        pass

    def test_create_event_alert_condition(self):
        """
        Test case for create_event_alert_condition

        
        """
        pass

    def test_create_event_channel(self):
        """
        Test case for create_event_channel

        
        """
        pass

    def test_create_event_event(self):
        """
        Test case for create_event_event

        
        """
        pass

    def test_delete_event_alert_condition(self):
        """
        Test case for delete_event_alert_condition

        
        """
        pass

    def test_delete_event_alert_conditions(self):
        """
        Test case for delete_event_alert_conditions

        
        """
        pass

    def test_delete_event_channel(self):
        """
        Test case for delete_event_channel

        
        """
        pass

    def test_get_event_alert_condition(self):
        """
        Test case for get_event_alert_condition

        
        """
        pass

    def test_get_event_categories(self):
        """
        Test case for get_event_categories

        
        """
        pass

    def test_get_event_category(self):
        """
        Test case for get_event_category

        
        """
        pass

    def test_get_event_channel(self):
        """
        Test case for get_event_channel

        
        """
        pass

    def test_get_event_eventgroup_definition(self):
        """
        Test case for get_event_eventgroup_definition

        
        """
        pass

    def test_get_event_eventgroup_definitions(self):
        """
        Test case for get_event_eventgroup_definitions

        
        """
        pass

    def test_get_event_eventgroup_occurrence(self):
        """
        Test case for get_event_eventgroup_occurrence

        
        """
        pass

    def test_get_event_eventgroup_occurrences(self):
        """
        Test case for get_event_eventgroup_occurrences

        
        """
        pass

    def test_get_event_eventlist(self):
        """
        Test case for get_event_eventlist

        
        """
        pass

    def test_get_event_eventlists(self):
        """
        Test case for get_event_eventlists

        
        """
        pass

    def test_get_event_settings(self):
        """
        Test case for get_event_settings

        
        """
        pass

    def test_list_event_alert_conditions(self):
        """
        Test case for list_event_alert_conditions

        
        """
        pass

    def test_list_event_channels(self):
        """
        Test case for list_event_channels

        
        """
        pass

    def test_update_event_alert_condition(self):
        """
        Test case for update_event_alert_condition

        
        """
        pass

    def test_update_event_channel(self):
        """
        Test case for update_event_channel

        
        """
        pass

    def test_update_event_eventgroup_occurrence(self):
        """
        Test case for update_event_eventgroup_occurrence

        
        """
        pass

    def test_update_event_eventgroup_occurrences(self):
        """
        Test case for update_event_eventgroup_occurrences

        
        """
        pass

    def test_update_event_settings(self):
        """
        Test case for update_event_settings

        
        """
        pass


if __name__ == '__main__':
    unittest.main()