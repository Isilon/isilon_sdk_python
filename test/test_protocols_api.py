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
from swagger_client.apis.protocols_api import ProtocolsApi


class TestProtocolsApi(unittest.TestCase):
    """ ProtocolsApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.protocols_api.ProtocolsApi()

    def tearDown(self):
        pass

    def test_create_hdfs_proxyuser(self):
        """
        Test case for create_hdfs_proxyuser

        
        """
        pass

    def test_create_hdfs_rack(self):
        """
        Test case for create_hdfs_rack

        
        """
        pass

    def test_create_ndmp_user(self):
        """
        Test case for create_ndmp_user

        
        """
        pass

    def test_create_nfs_aliase(self):
        """
        Test case for create_nfs_aliase

        
        """
        pass

    def test_create_nfs_export(self):
        """
        Test case for create_nfs_export

        
        """
        pass

    def test_create_nfs_netgroup_check_item(self):
        """
        Test case for create_nfs_netgroup_check_item

        
        """
        pass

    def test_create_nfs_netgroup_flush_item(self):
        """
        Test case for create_nfs_netgroup_flush_item

        
        """
        pass

    def test_create_nfs_nlm_sessions_check_item(self):
        """
        Test case for create_nfs_nlm_sessions_check_item

        
        """
        pass

    def test_create_nfs_reload_item(self):
        """
        Test case for create_nfs_reload_item

        
        """
        pass

    def test_create_ntp_server(self):
        """
        Test case for create_ntp_server

        
        """
        pass

    def test_create_smb_log_level_filter(self):
        """
        Test case for create_smb_log_level_filter

        
        """
        pass

    def test_create_smb_share(self):
        """
        Test case for create_smb_share

        
        """
        pass

    def test_create_swift_account(self):
        """
        Test case for create_swift_account

        
        """
        pass

    def test_delete_hdfs_proxyuser(self):
        """
        Test case for delete_hdfs_proxyuser

        
        """
        pass

    def test_delete_hdfs_rack(self):
        """
        Test case for delete_hdfs_rack

        
        """
        pass

    def test_delete_ndmp_user(self):
        """
        Test case for delete_ndmp_user

        
        """
        pass

    def test_delete_nfs_aliase(self):
        """
        Test case for delete_nfs_aliase

        
        """
        pass

    def test_delete_nfs_export(self):
        """
        Test case for delete_nfs_export

        
        """
        pass

    def test_delete_nfs_nlm_session(self):
        """
        Test case for delete_nfs_nlm_session

        
        """
        pass

    def test_delete_ntp_server(self):
        """
        Test case for delete_ntp_server

        
        """
        pass

    def test_delete_ntp_servers(self):
        """
        Test case for delete_ntp_servers

        
        """
        pass

    def test_delete_smb_log_level_filter(self):
        """
        Test case for delete_smb_log_level_filter

        
        """
        pass

    def test_delete_smb_log_level_filters(self):
        """
        Test case for delete_smb_log_level_filters

        
        """
        pass

    def test_delete_smb_openfile(self):
        """
        Test case for delete_smb_openfile

        
        """
        pass

    def test_delete_smb_session(self):
        """
        Test case for delete_smb_session

        
        """
        pass

    def test_delete_smb_sessions_computer_user(self):
        """
        Test case for delete_smb_sessions_computer_user

        
        """
        pass

    def test_delete_smb_share(self):
        """
        Test case for delete_smb_share

        
        """
        pass

    def test_delete_smb_shares(self):
        """
        Test case for delete_smb_shares

        
        """
        pass

    def test_delete_swift_account(self):
        """
        Test case for delete_swift_account

        
        """
        pass

    def test_get_ftp_settings(self):
        """
        Test case for get_ftp_settings

        
        """
        pass

    def test_get_hdfs_log_level(self):
        """
        Test case for get_hdfs_log_level

        
        """
        pass

    def test_get_hdfs_proxyuser(self):
        """
        Test case for get_hdfs_proxyuser

        
        """
        pass

    def test_get_hdfs_rack(self):
        """
        Test case for get_hdfs_rack

        
        """
        pass

    def test_get_hdfs_settings(self):
        """
        Test case for get_hdfs_settings

        
        """
        pass

    def test_get_http_settings(self):
        """
        Test case for get_http_settings

        
        """
        pass

    def test_get_ndmp_contexts_bre(self):
        """
        Test case for get_ndmp_contexts_bre

        
        """
        pass

    def test_get_ndmp_diagnostics(self):
        """
        Test case for get_ndmp_diagnostics

        
        """
        pass

    def test_get_ndmp_logs(self):
        """
        Test case for get_ndmp_logs

        
        """
        pass

    def test_get_ndmp_sessions(self):
        """
        Test case for get_ndmp_sessions

        
        """
        pass

    def test_get_ndmp_settings_global(self):
        """
        Test case for get_ndmp_settings_global

        
        """
        pass

    def test_get_ndmp_user(self):
        """
        Test case for get_ndmp_user

        
        """
        pass

    def test_get_nfs_aliase(self):
        """
        Test case for get_nfs_aliase

        
        """
        pass

    def test_get_nfs_check(self):
        """
        Test case for get_nfs_check

        
        """
        pass

    def test_get_nfs_export(self):
        """
        Test case for get_nfs_export

        
        """
        pass

    def test_get_nfs_exports_summary(self):
        """
        Test case for get_nfs_exports_summary

        
        """
        pass

    def test_get_nfs_log_level(self):
        """
        Test case for get_nfs_log_level

        
        """
        pass

    def test_get_nfs_netgroup(self):
        """
        Test case for get_nfs_netgroup

        
        """
        pass

    def test_get_nfs_nlm_locks(self):
        """
        Test case for get_nfs_nlm_locks

        
        """
        pass

    def test_get_nfs_nlm_session(self):
        """
        Test case for get_nfs_nlm_session

        
        """
        pass

    def test_get_nfs_nlm_sessions(self):
        """
        Test case for get_nfs_nlm_sessions

        
        """
        pass

    def test_get_nfs_nlm_waiters(self):
        """
        Test case for get_nfs_nlm_waiters

        
        """
        pass

    def test_get_nfs_settings_export(self):
        """
        Test case for get_nfs_settings_export

        
        """
        pass

    def test_get_nfs_settings_global(self):
        """
        Test case for get_nfs_settings_global

        
        """
        pass

    def test_get_nfs_settings_zone(self):
        """
        Test case for get_nfs_settings_zone

        
        """
        pass

    def test_get_ntp_server(self):
        """
        Test case for get_ntp_server

        
        """
        pass

    def test_get_ntp_settings(self):
        """
        Test case for get_ntp_settings

        
        """
        pass

    def test_get_smb_log_level(self):
        """
        Test case for get_smb_log_level

        
        """
        pass

    def test_get_smb_log_level_filter(self):
        """
        Test case for get_smb_log_level_filter

        
        """
        pass

    def test_get_smb_openfiles(self):
        """
        Test case for get_smb_openfiles

        
        """
        pass

    def test_get_smb_sessions(self):
        """
        Test case for get_smb_sessions

        
        """
        pass

    def test_get_smb_settings_global(self):
        """
        Test case for get_smb_settings_global

        
        """
        pass

    def test_get_smb_settings_share(self):
        """
        Test case for get_smb_settings_share

        
        """
        pass

    def test_get_smb_share(self):
        """
        Test case for get_smb_share

        
        """
        pass

    def test_get_smb_shares_summary(self):
        """
        Test case for get_smb_shares_summary

        
        """
        pass

    def test_get_snmp_settings(self):
        """
        Test case for get_snmp_settings

        
        """
        pass

    def test_get_swift_account(self):
        """
        Test case for get_swift_account

        
        """
        pass

    def test_list_hdfs_proxyusers(self):
        """
        Test case for list_hdfs_proxyusers

        
        """
        pass

    def test_list_hdfs_racks(self):
        """
        Test case for list_hdfs_racks

        
        """
        pass

    def test_list_ndmp_users(self):
        """
        Test case for list_ndmp_users

        
        """
        pass

    def test_list_nfs_aliases(self):
        """
        Test case for list_nfs_aliases

        
        """
        pass

    def test_list_nfs_exports(self):
        """
        Test case for list_nfs_exports

        
        """
        pass

    def test_list_ntp_servers(self):
        """
        Test case for list_ntp_servers

        
        """
        pass

    def test_list_smb_log_level_filters(self):
        """
        Test case for list_smb_log_level_filters

        
        """
        pass

    def test_list_smb_shares(self):
        """
        Test case for list_smb_shares

        
        """
        pass

    def test_list_swift_accounts(self):
        """
        Test case for list_swift_accounts

        
        """
        pass

    def test_update_ftp_settings(self):
        """
        Test case for update_ftp_settings

        
        """
        pass

    def test_update_hdfs_log_level(self):
        """
        Test case for update_hdfs_log_level

        
        """
        pass

    def test_update_hdfs_proxyuser(self):
        """
        Test case for update_hdfs_proxyuser

        
        """
        pass

    def test_update_hdfs_rack(self):
        """
        Test case for update_hdfs_rack

        
        """
        pass

    def test_update_hdfs_settings(self):
        """
        Test case for update_hdfs_settings

        
        """
        pass

    def test_update_http_settings(self):
        """
        Test case for update_http_settings

        
        """
        pass

    def test_update_ndmp_diagnostics(self):
        """
        Test case for update_ndmp_diagnostics

        
        """
        pass

    def test_update_ndmp_settings_global(self):
        """
        Test case for update_ndmp_settings_global

        
        """
        pass

    def test_update_ndmp_user(self):
        """
        Test case for update_ndmp_user

        
        """
        pass

    def test_update_nfs_aliase(self):
        """
        Test case for update_nfs_aliase

        
        """
        pass

    def test_update_nfs_export(self):
        """
        Test case for update_nfs_export

        
        """
        pass

    def test_update_nfs_log_level(self):
        """
        Test case for update_nfs_log_level

        
        """
        pass

    def test_update_nfs_netgroup(self):
        """
        Test case for update_nfs_netgroup

        
        """
        pass

    def test_update_nfs_settings_export(self):
        """
        Test case for update_nfs_settings_export

        
        """
        pass

    def test_update_nfs_settings_global(self):
        """
        Test case for update_nfs_settings_global

        
        """
        pass

    def test_update_nfs_settings_zone(self):
        """
        Test case for update_nfs_settings_zone

        
        """
        pass

    def test_update_ntp_server(self):
        """
        Test case for update_ntp_server

        
        """
        pass

    def test_update_ntp_settings(self):
        """
        Test case for update_ntp_settings

        
        """
        pass

    def test_update_smb_log_level(self):
        """
        Test case for update_smb_log_level

        
        """
        pass

    def test_update_smb_settings_global(self):
        """
        Test case for update_smb_settings_global

        
        """
        pass

    def test_update_smb_settings_share(self):
        """
        Test case for update_smb_settings_share

        
        """
        pass

    def test_update_smb_share(self):
        """
        Test case for update_smb_share

        
        """
        pass

    def test_update_snmp_settings(self):
        """
        Test case for update_snmp_settings

        
        """
        pass

    def test_update_swift_account(self):
        """
        Test case for update_swift_account

        
        """
        pass


if __name__ == '__main__':
    unittest.main()