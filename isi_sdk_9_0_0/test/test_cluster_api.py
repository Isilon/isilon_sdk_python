# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_9_0_0
from isi_sdk_9_0_0.api.cluster_api import ClusterApi  # noqa: E501
from isi_sdk_9_0_0.rest import ApiException


class TestClusterApi(unittest.TestCase):
    """ClusterApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_9_0_0.api.cluster_api.ClusterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_cluster_add_node_item(self):
        """Test case for create_cluster_add_node_item

        """
        pass

    def test_create_diagnostics_gather_start_item(self):
        """Test case for create_diagnostics_gather_start_item

        """
        pass

    def test_create_diagnostics_gather_stop_item(self):
        """Test case for create_diagnostics_gather_stop_item

        """
        pass

    def test_create_diagnostics_netlogger_start_item(self):
        """Test case for create_diagnostics_netlogger_start_item

        """
        pass

    def test_create_diagnostics_netlogger_stop_item(self):
        """Test case for create_diagnostics_netlogger_stop_item

        """
        pass

    def test_get_cluster_config(self):
        """Test case for get_cluster_config

        """
        pass

    def test_get_cluster_email(self):
        """Test case for get_cluster_email

        """
        pass

    def test_get_cluster_external_ips(self):
        """Test case for get_cluster_external_ips

        """
        pass

    def test_get_cluster_identity(self):
        """Test case for get_cluster_identity

        """
        pass

    def test_get_cluster_internal_networks(self):
        """Test case for get_cluster_internal_networks

        """
        pass

    def test_get_cluster_node(self):
        """Test case for get_cluster_node

        """
        pass

    def test_get_cluster_nodes(self):
        """Test case for get_cluster_nodes

        """
        pass

    def test_get_cluster_nodes_available(self):
        """Test case for get_cluster_nodes_available

        """
        pass

    def test_get_cluster_owner(self):
        """Test case for get_cluster_owner

        """
        pass

    def test_get_cluster_statfs(self):
        """Test case for get_cluster_statfs

        """
        pass

    def test_get_cluster_time(self):
        """Test case for get_cluster_time

        """
        pass

    def test_get_cluster_timezone(self):
        """Test case for get_cluster_timezone

        """
        pass

    def test_get_cluster_version(self):
        """Test case for get_cluster_version

        """
        pass

    def test_get_diagnostics_gather(self):
        """Test case for get_diagnostics_gather

        """
        pass

    def test_get_diagnostics_gather_settings(self):
        """Test case for get_diagnostics_gather_settings

        """
        pass

    def test_get_diagnostics_gather_status(self):
        """Test case for get_diagnostics_gather_status

        """
        pass

    def test_get_diagnostics_netlogger(self):
        """Test case for get_diagnostics_netlogger

        """
        pass

    def test_get_diagnostics_netlogger_settings(self):
        """Test case for get_diagnostics_netlogger_settings

        """
        pass

    def test_get_diagnostics_netlogger_status(self):
        """Test case for get_diagnostics_netlogger_status

        """
        pass

    def test_get_timezone_region(self):
        """Test case for get_timezone_region

        """
        pass

    def test_get_timezone_settings(self):
        """Test case for get_timezone_settings

        """
        pass

    def test_update_cluster_email(self):
        """Test case for update_cluster_email

        """
        pass

    def test_update_cluster_identity(self):
        """Test case for update_cluster_identity

        """
        pass

    def test_update_cluster_internal_networks(self):
        """Test case for update_cluster_internal_networks

        """
        pass

    def test_update_cluster_node(self):
        """Test case for update_cluster_node

        """
        pass

    def test_update_cluster_owner(self):
        """Test case for update_cluster_owner

        """
        pass

    def test_update_cluster_time(self):
        """Test case for update_cluster_time

        """
        pass

    def test_update_cluster_timezone(self):
        """Test case for update_cluster_timezone

        """
        pass

    def test_update_cluster_update_lnns(self):
        """Test case for update_cluster_update_lnns

        """
        pass

    def test_update_diagnostics_gather_settings(self):
        """Test case for update_diagnostics_gather_settings

        """
        pass

    def test_update_diagnostics_netlogger_settings(self):
        """Test case for update_diagnostics_netlogger_settings

        """
        pass

    def test_update_timezone_settings(self):
        """Test case for update_timezone_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
