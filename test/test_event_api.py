# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 7
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_2_0
from isi_sdk_8_2_0.api.event_api import EventApi  # noqa: E501
from isi_sdk_8_2_0.rest import ApiException


class TestEventApi(unittest.TestCase):
    """EventApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_2_0.api.event_api.EventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_event_alert_condition(self):
        """Test case for create_event_alert_condition

        """
        pass

    def test_create_event_channel(self):
        """Test case for create_event_channel

        """
        pass

    def test_create_event_event(self):
        """Test case for create_event_event

        """
        pass

    def test_delete_event_alert_condition(self):
        """Test case for delete_event_alert_condition

        """
        pass

    def test_delete_event_alert_conditions(self):
        """Test case for delete_event_alert_conditions

        """
        pass

    def test_delete_event_channel(self):
        """Test case for delete_event_channel

        """
        pass

    def test_get_event_alert_condition(self):
        """Test case for get_event_alert_condition

        """
        pass

    def test_get_event_categories(self):
        """Test case for get_event_categories

        """
        pass

    def test_get_event_category(self):
        """Test case for get_event_category

        """
        pass

    def test_get_event_channel(self):
        """Test case for get_event_channel

        """
        pass

    def test_get_event_eventgroup_definition(self):
        """Test case for get_event_eventgroup_definition

        """
        pass

    def test_get_event_eventgroup_definitions(self):
        """Test case for get_event_eventgroup_definitions

        """
        pass

    def test_get_event_eventgroup_occurrence(self):
        """Test case for get_event_eventgroup_occurrence

        """
        pass

    def test_get_event_eventgroup_occurrences(self):
        """Test case for get_event_eventgroup_occurrences

        """
        pass

    def test_get_event_eventlist(self):
        """Test case for get_event_eventlist

        """
        pass

    def test_get_event_eventlists(self):
        """Test case for get_event_eventlists

        """
        pass

    def test_get_event_settings(self):
        """Test case for get_event_settings

        """
        pass

    def test_list_event_alert_conditions(self):
        """Test case for list_event_alert_conditions

        """
        pass

    def test_list_event_channels(self):
        """Test case for list_event_channels

        """
        pass

    def test_update_event_alert_condition(self):
        """Test case for update_event_alert_condition

        """
        pass

    def test_update_event_channel(self):
        """Test case for update_event_channel

        """
        pass

    def test_update_event_eventgroup_occurrence(self):
        """Test case for update_event_eventgroup_occurrence

        """
        pass

    def test_update_event_eventgroup_occurrences(self):
        """Test case for update_event_eventgroup_occurrences

        """
        pass

    def test_update_event_settings(self):
        """Test case for update_event_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
