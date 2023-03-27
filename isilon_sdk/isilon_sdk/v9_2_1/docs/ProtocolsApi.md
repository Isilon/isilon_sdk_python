# isilon_sdk.v9_2_1.ProtocolsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hdfs_crypto_encryption_zone**](ProtocolsApi.md#create_hdfs_crypto_encryption_zone) | **POST** /platform/7/protocols/hdfs/crypto/encryption-zones | 
[**create_hdfs_proxyuser**](ProtocolsApi.md#create_hdfs_proxyuser) | **POST** /platform/1/protocols/hdfs/proxyusers | 
[**create_hdfs_rack**](ProtocolsApi.md#create_hdfs_rack) | **POST** /platform/1/protocols/hdfs/racks | 
[**create_ndmp_settings_preferred_ip**](ProtocolsApi.md#create_ndmp_settings_preferred_ip) | **POST** /platform/4/protocols/ndmp/settings/preferred-ips | 
[**create_ndmp_settings_variable**](ProtocolsApi.md#create_ndmp_settings_variable) | **POST** /platform/3/protocols/ndmp/settings/variables/{NdmpSettingsVariableId} | 
[**create_ndmp_user**](ProtocolsApi.md#create_ndmp_user) | **POST** /platform/3/protocols/ndmp/users | 
[**create_nfs_alias**](ProtocolsApi.md#create_nfs_alias) | **POST** /platform/2/protocols/nfs/aliases | 
[**create_nfs_export**](ProtocolsApi.md#create_nfs_export) | **POST** /platform/4/protocols/nfs/exports | 
[**create_nfs_netgroup_check_item**](ProtocolsApi.md#create_nfs_netgroup_check_item) | **POST** /platform/3/protocols/nfs/netgroup/check | 
[**create_nfs_netgroup_flush_item**](ProtocolsApi.md#create_nfs_netgroup_flush_item) | **POST** /platform/3/protocols/nfs/netgroup/flush | 
[**create_nfs_netgroup_save_item**](ProtocolsApi.md#create_nfs_netgroup_save_item) | **POST** /platform/12/protocols/nfs/netgroup/save | 
[**create_nfs_nlm_sessions_check_item**](ProtocolsApi.md#create_nfs_nlm_sessions_check_item) | **POST** /platform/3/protocols/nfs/nlm/sessions-check | 
[**create_nfs_reload_item**](ProtocolsApi.md#create_nfs_reload_item) | **POST** /platform/3/protocols/nfs/reload | 
[**create_ntp_server**](ProtocolsApi.md#create_ntp_server) | **POST** /platform/3/protocols/ntp/servers | 
[**create_s3_bucket**](ProtocolsApi.md#create_s3_bucket) | **POST** /platform/12/protocols/s3/buckets | 
[**create_s3_key**](ProtocolsApi.md#create_s3_key) | **POST** /platform/10/protocols/s3/keys/{S3KeyId} | 
[**create_s3_mykey**](ProtocolsApi.md#create_s3_mykey) | **POST** /platform/10/protocols/s3/mykeys | 
[**create_smb_log_level_filter**](ProtocolsApi.md#create_smb_log_level_filter) | **POST** /platform/3/protocols/smb/log-level/filters | 
[**create_smb_share**](ProtocolsApi.md#create_smb_share) | **POST** /platform/7/protocols/smb/shares | 
[**create_swift_account**](ProtocolsApi.md#create_swift_account) | **POST** /platform/3/protocols/swift/accounts | 
[**delete_hdfs_fsimage_latest**](ProtocolsApi.md#delete_hdfs_fsimage_latest) | **DELETE** /platform/5/protocols/hdfs/fsimage/latest | 
[**delete_hdfs_inotify_stream**](ProtocolsApi.md#delete_hdfs_inotify_stream) | **DELETE** /platform/5/protocols/hdfs/inotify/stream | 
[**delete_hdfs_proxyuser**](ProtocolsApi.md#delete_hdfs_proxyuser) | **DELETE** /platform/1/protocols/hdfs/proxyusers/{HdfsProxyuserId} | 
[**delete_hdfs_rack**](ProtocolsApi.md#delete_hdfs_rack) | **DELETE** /platform/1/protocols/hdfs/racks/{HdfsRackId} | 
[**delete_ndmp_contexts_backup_by_id**](ProtocolsApi.md#delete_ndmp_contexts_backup_by_id) | **DELETE** /platform/3/protocols/ndmp/contexts/backup/{NdmpContextsBackupId} | 
[**delete_ndmp_contexts_bre_by_id**](ProtocolsApi.md#delete_ndmp_contexts_bre_by_id) | **DELETE** /platform/3/protocols/ndmp/contexts/bre/{NdmpContextsBreId} | 
[**delete_ndmp_contexts_restore_by_id**](ProtocolsApi.md#delete_ndmp_contexts_restore_by_id) | **DELETE** /platform/3/protocols/ndmp/contexts/restore/{NdmpContextsRestoreId} | 
[**delete_ndmp_dumpdate**](ProtocolsApi.md#delete_ndmp_dumpdate) | **DELETE** /platform/3/protocols/ndmp/dumpdates/{NdmpDumpdateId} | 
[**delete_ndmp_session**](ProtocolsApi.md#delete_ndmp_session) | **DELETE** /platform/3/protocols/ndmp/sessions/{NdmpSessionId} | 
[**delete_ndmp_settings_preferred_ip**](ProtocolsApi.md#delete_ndmp_settings_preferred_ip) | **DELETE** /platform/4/protocols/ndmp/settings/preferred-ips/{NdmpSettingsPreferredIpId} | 
[**delete_ndmp_settings_variable**](ProtocolsApi.md#delete_ndmp_settings_variable) | **DELETE** /platform/3/protocols/ndmp/settings/variables/{NdmpSettingsVariableId} | 
[**delete_ndmp_user**](ProtocolsApi.md#delete_ndmp_user) | **DELETE** /platform/3/protocols/ndmp/users/{NdmpUserId} | 
[**delete_nfs_alias**](ProtocolsApi.md#delete_nfs_alias) | **DELETE** /platform/2/protocols/nfs/aliases/{NfsAliasId} | 
[**delete_nfs_export**](ProtocolsApi.md#delete_nfs_export) | **DELETE** /platform/4/protocols/nfs/exports/{NfsExportId} | 
[**delete_nfs_nlm_session**](ProtocolsApi.md#delete_nfs_nlm_session) | **DELETE** /platform/3/protocols/nfs/nlm/sessions/{NfsNlmSessionId} | 
[**delete_ntp_server**](ProtocolsApi.md#delete_ntp_server) | **DELETE** /platform/3/protocols/ntp/servers/{NtpServerId} | 
[**delete_ntp_servers**](ProtocolsApi.md#delete_ntp_servers) | **DELETE** /platform/3/protocols/ntp/servers | 
[**delete_s3_bucket**](ProtocolsApi.md#delete_s3_bucket) | **DELETE** /platform/12/protocols/s3/buckets/{S3BucketId} | 
[**delete_s3_key**](ProtocolsApi.md#delete_s3_key) | **DELETE** /platform/10/protocols/s3/keys/{S3KeyId} | 
[**delete_s3_mykeys**](ProtocolsApi.md#delete_s3_mykeys) | **DELETE** /platform/10/protocols/s3/mykeys | 
[**delete_smb_log_level_filter**](ProtocolsApi.md#delete_smb_log_level_filter) | **DELETE** /platform/3/protocols/smb/log-level/filters/{SmbLogLevelFilterId} | 
[**delete_smb_log_level_filters**](ProtocolsApi.md#delete_smb_log_level_filters) | **DELETE** /platform/3/protocols/smb/log-level/filters | 
[**delete_smb_openfile**](ProtocolsApi.md#delete_smb_openfile) | **DELETE** /platform/1/protocols/smb/openfiles/{SmbOpenfileId} | 
[**delete_smb_session**](ProtocolsApi.md#delete_smb_session) | **DELETE** /platform/11/protocols/smb/sessions/{SmbSessionId} | 
[**delete_smb_sessions_computer_user**](ProtocolsApi.md#delete_smb_sessions_computer_user) | **DELETE** /platform/1/protocols/smb/sessions/{Computer}/{SmbSessionsComputerUser} | 
[**delete_smb_share**](ProtocolsApi.md#delete_smb_share) | **DELETE** /platform/7/protocols/smb/shares/{SmbShareId} | 
[**delete_smb_shares**](ProtocolsApi.md#delete_smb_shares) | **DELETE** /platform/7/protocols/smb/shares | 
[**delete_swift_account**](ProtocolsApi.md#delete_swift_account) | **DELETE** /platform/3/protocols/swift/accounts/{SwiftAccountId} | 
[**get_ftp_settings**](ProtocolsApi.md#get_ftp_settings) | **GET** /platform/3/protocols/ftp/settings | 
[**get_hdfs_crypto_settings**](ProtocolsApi.md#get_hdfs_crypto_settings) | **GET** /platform/7/protocols/hdfs/crypto/settings | 
[**get_hdfs_fsimage_job**](ProtocolsApi.md#get_hdfs_fsimage_job) | **GET** /platform/5/protocols/hdfs/fsimage/job | 
[**get_hdfs_fsimage_job_settings**](ProtocolsApi.md#get_hdfs_fsimage_job_settings) | **GET** /platform/5/protocols/hdfs/fsimage/job/settings | 
[**get_hdfs_fsimage_latest**](ProtocolsApi.md#get_hdfs_fsimage_latest) | **GET** /platform/5/protocols/hdfs/fsimage/latest | 
[**get_hdfs_fsimage_settings**](ProtocolsApi.md#get_hdfs_fsimage_settings) | **GET** /platform/5/protocols/hdfs/fsimage/settings | 
[**get_hdfs_inotify_settings**](ProtocolsApi.md#get_hdfs_inotify_settings) | **GET** /platform/5/protocols/hdfs/inotify/settings | 
[**get_hdfs_inotify_stream**](ProtocolsApi.md#get_hdfs_inotify_stream) | **GET** /platform/5/protocols/hdfs/inotify/stream | 
[**get_hdfs_log_level**](ProtocolsApi.md#get_hdfs_log_level) | **GET** /platform/12/protocols/hdfs/log-level | 
[**get_hdfs_proxyuser**](ProtocolsApi.md#get_hdfs_proxyuser) | **GET** /platform/1/protocols/hdfs/proxyusers/{HdfsProxyuserId} | 
[**get_hdfs_rack**](ProtocolsApi.md#get_hdfs_rack) | **GET** /platform/1/protocols/hdfs/racks/{HdfsRackId} | 
[**get_hdfs_ranger_plugin_settings**](ProtocolsApi.md#get_hdfs_ranger_plugin_settings) | **GET** /platform/4/protocols/hdfs/ranger-plugin/settings | 
[**get_hdfs_settings**](ProtocolsApi.md#get_hdfs_settings) | **GET** /platform/9/protocols/hdfs/settings | 
[**get_hdfs_settings_global**](ProtocolsApi.md#get_hdfs_settings_global) | **GET** /platform/11/protocols/hdfs/settings/global | 
[**get_http_settings**](ProtocolsApi.md#get_http_settings) | **GET** /platform/3/protocols/http/settings | 
[**get_ndmp_contexts_backup**](ProtocolsApi.md#get_ndmp_contexts_backup) | **GET** /platform/3/protocols/ndmp/contexts/backup | 
[**get_ndmp_contexts_backup_by_id**](ProtocolsApi.md#get_ndmp_contexts_backup_by_id) | **GET** /platform/3/protocols/ndmp/contexts/backup/{NdmpContextsBackupId} | 
[**get_ndmp_contexts_bre**](ProtocolsApi.md#get_ndmp_contexts_bre) | **GET** /platform/3/protocols/ndmp/contexts/bre | 
[**get_ndmp_contexts_bre_by_id**](ProtocolsApi.md#get_ndmp_contexts_bre_by_id) | **GET** /platform/3/protocols/ndmp/contexts/bre/{NdmpContextsBreId} | 
[**get_ndmp_contexts_restore**](ProtocolsApi.md#get_ndmp_contexts_restore) | **GET** /platform/3/protocols/ndmp/contexts/restore | 
[**get_ndmp_contexts_restore_by_id**](ProtocolsApi.md#get_ndmp_contexts_restore_by_id) | **GET** /platform/3/protocols/ndmp/contexts/restore/{NdmpContextsRestoreId} | 
[**get_ndmp_diagnostics**](ProtocolsApi.md#get_ndmp_diagnostics) | **GET** /platform/3/protocols/ndmp/diagnostics | 
[**get_ndmp_dumpdate**](ProtocolsApi.md#get_ndmp_dumpdate) | **GET** /platform/3/protocols/ndmp/dumpdates/{NdmpDumpdateId} | 
[**get_ndmp_logs**](ProtocolsApi.md#get_ndmp_logs) | **GET** /platform/3/protocols/ndmp/logs | 
[**get_ndmp_session**](ProtocolsApi.md#get_ndmp_session) | **GET** /platform/3/protocols/ndmp/sessions/{NdmpSessionId} | 
[**get_ndmp_sessions**](ProtocolsApi.md#get_ndmp_sessions) | **GET** /platform/3/protocols/ndmp/sessions | 
[**get_ndmp_settings_dmas**](ProtocolsApi.md#get_ndmp_settings_dmas) | **GET** /platform/3/protocols/ndmp/settings/dmas | 
[**get_ndmp_settings_global**](ProtocolsApi.md#get_ndmp_settings_global) | **GET** /platform/3/protocols/ndmp/settings/global | 
[**get_ndmp_settings_preferred_ip**](ProtocolsApi.md#get_ndmp_settings_preferred_ip) | **GET** /platform/4/protocols/ndmp/settings/preferred-ips/{NdmpSettingsPreferredIpId} | 
[**get_ndmp_settings_variable**](ProtocolsApi.md#get_ndmp_settings_variable) | **GET** /platform/3/protocols/ndmp/settings/variables/{NdmpSettingsVariableId} | 
[**get_ndmp_user**](ProtocolsApi.md#get_ndmp_user) | **GET** /platform/3/protocols/ndmp/users/{NdmpUserId} | 
[**get_nfs_alias**](ProtocolsApi.md#get_nfs_alias) | **GET** /platform/2/protocols/nfs/aliases/{NfsAliasId} | 
[**get_nfs_check**](ProtocolsApi.md#get_nfs_check) | **GET** /platform/2/protocols/nfs/check | 
[**get_nfs_export**](ProtocolsApi.md#get_nfs_export) | **GET** /platform/4/protocols/nfs/exports/{NfsExportId} | 
[**get_nfs_exports_summary**](ProtocolsApi.md#get_nfs_exports_summary) | **GET** /platform/2/protocols/nfs/exports-summary | 
[**get_nfs_log_level**](ProtocolsApi.md#get_nfs_log_level) | **GET** /platform/12/protocols/nfs/log-level | 
[**get_nfs_netgroup**](ProtocolsApi.md#get_nfs_netgroup) | **GET** /platform/3/protocols/nfs/netgroup | 
[**get_nfs_nlm_locks**](ProtocolsApi.md#get_nfs_nlm_locks) | **GET** /platform/2/protocols/nfs/nlm/locks | 
[**get_nfs_nlm_session**](ProtocolsApi.md#get_nfs_nlm_session) | **GET** /platform/3/protocols/nfs/nlm/sessions/{NfsNlmSessionId} | 
[**get_nfs_nlm_sessions**](ProtocolsApi.md#get_nfs_nlm_sessions) | **GET** /platform/3/protocols/nfs/nlm/sessions | 
[**get_nfs_nlm_waiters**](ProtocolsApi.md#get_nfs_nlm_waiters) | **GET** /platform/2/protocols/nfs/nlm/waiters | 
[**get_nfs_settings_export**](ProtocolsApi.md#get_nfs_settings_export) | **GET** /platform/2/protocols/nfs/settings/export | 
[**get_nfs_settings_global**](ProtocolsApi.md#get_nfs_settings_global) | **GET** /platform/12/protocols/nfs/settings/global | 
[**get_nfs_settings_zone**](ProtocolsApi.md#get_nfs_settings_zone) | **GET** /platform/2/protocols/nfs/settings/zone | 
[**get_ntp_server**](ProtocolsApi.md#get_ntp_server) | **GET** /platform/3/protocols/ntp/servers/{NtpServerId} | 
[**get_ntp_settings**](ProtocolsApi.md#get_ntp_settings) | **GET** /platform/3/protocols/ntp/settings | 
[**get_s3_bucket**](ProtocolsApi.md#get_s3_bucket) | **GET** /platform/12/protocols/s3/buckets/{S3BucketId} | 
[**get_s3_key**](ProtocolsApi.md#get_s3_key) | **GET** /platform/10/protocols/s3/keys/{S3KeyId} | 
[**get_s3_log_level**](ProtocolsApi.md#get_s3_log_level) | **GET** /platform/10/protocols/s3/log-level | 
[**get_s3_settings_global**](ProtocolsApi.md#get_s3_settings_global) | **GET** /platform/10/protocols/s3/settings/global | 
[**get_s3_settings_zone**](ProtocolsApi.md#get_s3_settings_zone) | **GET** /platform/12/protocols/s3/settings/zone | 
[**get_smb_log_level**](ProtocolsApi.md#get_smb_log_level) | **GET** /platform/12/protocols/smb/log-level | 
[**get_smb_log_level_filter**](ProtocolsApi.md#get_smb_log_level_filter) | **GET** /platform/3/protocols/smb/log-level/filters/{SmbLogLevelFilterId} | 
[**get_smb_openfiles**](ProtocolsApi.md#get_smb_openfiles) | **GET** /platform/1/protocols/smb/openfiles | 
[**get_smb_sessions**](ProtocolsApi.md#get_smb_sessions) | **GET** /platform/11/protocols/smb/sessions | 
[**get_smb_settings_global**](ProtocolsApi.md#get_smb_settings_global) | **GET** /platform/7/protocols/smb/settings/global | 
[**get_smb_settings_share**](ProtocolsApi.md#get_smb_settings_share) | **GET** /platform/7/protocols/smb/settings/share | 
[**get_smb_settings_zone**](ProtocolsApi.md#get_smb_settings_zone) | **GET** /platform/6/protocols/smb/settings/zone | 
[**get_smb_share**](ProtocolsApi.md#get_smb_share) | **GET** /platform/7/protocols/smb/shares/{SmbShareId} | 
[**get_smb_shares_summary**](ProtocolsApi.md#get_smb_shares_summary) | **GET** /platform/1/protocols/smb/shares-summary | 
[**get_snmp_settings**](ProtocolsApi.md#get_snmp_settings) | **GET** /platform/5/protocols/snmp/settings | 
[**get_ssh_settings**](ProtocolsApi.md#get_ssh_settings) | **GET** /platform/8/protocols/ssh/settings | 
[**get_swift_account**](ProtocolsApi.md#get_swift_account) | **GET** /platform/3/protocols/swift/accounts/{SwiftAccountId} | 
[**list_hdfs_crypto_encryption_zones**](ProtocolsApi.md#list_hdfs_crypto_encryption_zones) | **GET** /platform/7/protocols/hdfs/crypto/encryption-zones | 
[**list_hdfs_proxyusers**](ProtocolsApi.md#list_hdfs_proxyusers) | **GET** /platform/1/protocols/hdfs/proxyusers | 
[**list_hdfs_racks**](ProtocolsApi.md#list_hdfs_racks) | **GET** /platform/1/protocols/hdfs/racks | 
[**list_ndmp_settings_preferred_ips**](ProtocolsApi.md#list_ndmp_settings_preferred_ips) | **GET** /platform/4/protocols/ndmp/settings/preferred-ips | 
[**list_ndmp_users**](ProtocolsApi.md#list_ndmp_users) | **GET** /platform/3/protocols/ndmp/users | 
[**list_nfs_aliases**](ProtocolsApi.md#list_nfs_aliases) | **GET** /platform/2/protocols/nfs/aliases | 
[**list_nfs_exports**](ProtocolsApi.md#list_nfs_exports) | **GET** /platform/4/protocols/nfs/exports | 
[**list_ntp_servers**](ProtocolsApi.md#list_ntp_servers) | **GET** /platform/3/protocols/ntp/servers | 
[**list_s3_buckets**](ProtocolsApi.md#list_s3_buckets) | **GET** /platform/12/protocols/s3/buckets | 
[**list_s3_mykeys**](ProtocolsApi.md#list_s3_mykeys) | **GET** /platform/10/protocols/s3/mykeys | 
[**list_smb_log_level_filters**](ProtocolsApi.md#list_smb_log_level_filters) | **GET** /platform/3/protocols/smb/log-level/filters | 
[**list_smb_shares**](ProtocolsApi.md#list_smb_shares) | **GET** /platform/7/protocols/smb/shares | 
[**list_swift_accounts**](ProtocolsApi.md#list_swift_accounts) | **GET** /platform/3/protocols/swift/accounts | 
[**update_ftp_settings**](ProtocolsApi.md#update_ftp_settings) | **PUT** /platform/3/protocols/ftp/settings | 
[**update_hdfs_crypto_settings**](ProtocolsApi.md#update_hdfs_crypto_settings) | **PUT** /platform/7/protocols/hdfs/crypto/settings | 
[**update_hdfs_fsimage_job_settings**](ProtocolsApi.md#update_hdfs_fsimage_job_settings) | **PUT** /platform/5/protocols/hdfs/fsimage/job/settings | 
[**update_hdfs_fsimage_settings**](ProtocolsApi.md#update_hdfs_fsimage_settings) | **PUT** /platform/5/protocols/hdfs/fsimage/settings | 
[**update_hdfs_inotify_settings**](ProtocolsApi.md#update_hdfs_inotify_settings) | **PUT** /platform/5/protocols/hdfs/inotify/settings | 
[**update_hdfs_log_level**](ProtocolsApi.md#update_hdfs_log_level) | **PUT** /platform/12/protocols/hdfs/log-level | 
[**update_hdfs_proxyuser**](ProtocolsApi.md#update_hdfs_proxyuser) | **PUT** /platform/1/protocols/hdfs/proxyusers/{HdfsProxyuserId} | 
[**update_hdfs_rack**](ProtocolsApi.md#update_hdfs_rack) | **PUT** /platform/1/protocols/hdfs/racks/{HdfsRackId} | 
[**update_hdfs_ranger_plugin_settings**](ProtocolsApi.md#update_hdfs_ranger_plugin_settings) | **PUT** /platform/4/protocols/hdfs/ranger-plugin/settings | 
[**update_hdfs_settings**](ProtocolsApi.md#update_hdfs_settings) | **PUT** /platform/9/protocols/hdfs/settings | 
[**update_hdfs_settings_global**](ProtocolsApi.md#update_hdfs_settings_global) | **PUT** /platform/11/protocols/hdfs/settings/global | 
[**update_http_settings**](ProtocolsApi.md#update_http_settings) | **PUT** /platform/3/protocols/http/settings | 
[**update_ndmp_diagnostics**](ProtocolsApi.md#update_ndmp_diagnostics) | **PUT** /platform/3/protocols/ndmp/diagnostics | 
[**update_ndmp_settings_global**](ProtocolsApi.md#update_ndmp_settings_global) | **PUT** /platform/3/protocols/ndmp/settings/global | 
[**update_ndmp_settings_preferred_ip**](ProtocolsApi.md#update_ndmp_settings_preferred_ip) | **PUT** /platform/4/protocols/ndmp/settings/preferred-ips/{NdmpSettingsPreferredIpId} | 
[**update_ndmp_settings_variable**](ProtocolsApi.md#update_ndmp_settings_variable) | **PUT** /platform/3/protocols/ndmp/settings/variables/{NdmpSettingsVariableId} | 
[**update_ndmp_user**](ProtocolsApi.md#update_ndmp_user) | **PUT** /platform/3/protocols/ndmp/users/{NdmpUserId} | 
[**update_nfs_alias**](ProtocolsApi.md#update_nfs_alias) | **PUT** /platform/2/protocols/nfs/aliases/{NfsAliasId} | 
[**update_nfs_export**](ProtocolsApi.md#update_nfs_export) | **PUT** /platform/4/protocols/nfs/exports/{NfsExportId} | 
[**update_nfs_log_level**](ProtocolsApi.md#update_nfs_log_level) | **PUT** /platform/12/protocols/nfs/log-level | 
[**update_nfs_netgroup**](ProtocolsApi.md#update_nfs_netgroup) | **PUT** /platform/3/protocols/nfs/netgroup | 
[**update_nfs_settings_export**](ProtocolsApi.md#update_nfs_settings_export) | **PUT** /platform/2/protocols/nfs/settings/export | 
[**update_nfs_settings_global**](ProtocolsApi.md#update_nfs_settings_global) | **PUT** /platform/12/protocols/nfs/settings/global | 
[**update_nfs_settings_zone**](ProtocolsApi.md#update_nfs_settings_zone) | **PUT** /platform/2/protocols/nfs/settings/zone | 
[**update_ntp_server**](ProtocolsApi.md#update_ntp_server) | **PUT** /platform/3/protocols/ntp/servers/{NtpServerId} | 
[**update_ntp_settings**](ProtocolsApi.md#update_ntp_settings) | **PUT** /platform/3/protocols/ntp/settings | 
[**update_s3_bucket**](ProtocolsApi.md#update_s3_bucket) | **PUT** /platform/12/protocols/s3/buckets/{S3BucketId} | 
[**update_s3_log_level**](ProtocolsApi.md#update_s3_log_level) | **PUT** /platform/10/protocols/s3/log-level | 
[**update_s3_settings_global**](ProtocolsApi.md#update_s3_settings_global) | **PUT** /platform/10/protocols/s3/settings/global | 
[**update_s3_settings_zone**](ProtocolsApi.md#update_s3_settings_zone) | **PUT** /platform/12/protocols/s3/settings/zone | 
[**update_smb_log_level**](ProtocolsApi.md#update_smb_log_level) | **PUT** /platform/12/protocols/smb/log-level | 
[**update_smb_settings_global**](ProtocolsApi.md#update_smb_settings_global) | **PUT** /platform/7/protocols/smb/settings/global | 
[**update_smb_settings_share**](ProtocolsApi.md#update_smb_settings_share) | **PUT** /platform/7/protocols/smb/settings/share | 
[**update_smb_settings_zone**](ProtocolsApi.md#update_smb_settings_zone) | **PUT** /platform/6/protocols/smb/settings/zone | 
[**update_smb_share**](ProtocolsApi.md#update_smb_share) | **PUT** /platform/7/protocols/smb/shares/{SmbShareId} | 
[**update_snmp_settings**](ProtocolsApi.md#update_snmp_settings) | **PUT** /platform/5/protocols/snmp/settings | 
[**update_ssh_settings**](ProtocolsApi.md#update_ssh_settings) | **PUT** /platform/8/protocols/ssh/settings | 
[**update_swift_account**](ProtocolsApi.md#update_swift_account) | **PUT** /platform/3/protocols/swift/accounts/{SwiftAccountId} | 


# **create_hdfs_crypto_encryption_zone**
> CreateResponse create_hdfs_crypto_encryption_zone(hdfs_crypto_encryption_zone, zone=zone)



Turn an empty directory into an Encryption Zone.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_crypto_encryption_zone = isilon_sdk.v9_2_1.HdfsCryptoEncryptionZone() # HdfsCryptoEncryptionZone | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.create_hdfs_crypto_encryption_zone(hdfs_crypto_encryption_zone, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_hdfs_crypto_encryption_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_crypto_encryption_zone** | [**HdfsCryptoEncryptionZone**](HdfsCryptoEncryptionZone.md)|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hdfs_proxyuser**
> CreateResponse create_hdfs_proxyuser(hdfs_proxyuser, zone=zone)



Create a new HDFS proxyuser.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_proxyuser = isilon_sdk.v9_2_1.HdfsProxyuserCreateParams() # HdfsProxyuserCreateParams | 
zone = 'zone_example' # str | Access zone which contains HDFS proxyuser. (optional)

try:
    api_response = api_instance.create_hdfs_proxyuser(hdfs_proxyuser, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_hdfs_proxyuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_proxyuser** | [**HdfsProxyuserCreateParams**](HdfsProxyuserCreateParams.md)|  | 
 **zone** | **str**| Access zone which contains HDFS proxyuser. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hdfs_rack**
> CreateResponse create_hdfs_rack(hdfs_rack, zone=zone)



Create a new HDFS rack.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_rack = isilon_sdk.v9_2_1.HdfsRackCreateParams() # HdfsRackCreateParams | 
zone = 'zone_example' # str | Access zone which contains HDFS rack. (optional)

try:
    api_response = api_instance.create_hdfs_rack(hdfs_rack, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_hdfs_rack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_rack** | [**HdfsRackCreateParams**](HdfsRackCreateParams.md)|  | 
 **zone** | **str**| Access zone which contains HDFS rack. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ndmp_settings_preferred_ip**
> Empty create_ndmp_settings_preferred_ip(ndmp_settings_preferred_ip)



Create a preferred ip preference.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_preferred_ip = isilon_sdk.v9_2_1.NdmpSettingsPreferredIpCreateParams() # NdmpSettingsPreferredIpCreateParams | 

try:
    api_response = api_instance.create_ndmp_settings_preferred_ip(ndmp_settings_preferred_ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_ndmp_settings_preferred_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_preferred_ip** | [**NdmpSettingsPreferredIpCreateParams**](NdmpSettingsPreferredIpCreateParams.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ndmp_settings_variable**
> Empty create_ndmp_settings_variable(ndmp_settings_variable, ndmp_settings_variable_id)



Create a preferred NDMP environment variable.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_variable = isilon_sdk.v9_2_1.NdmpSettingsVariableCreateParams() # NdmpSettingsVariableCreateParams | 
ndmp_settings_variable_id = 'ndmp_settings_variable_id_example' # str | Create a preferred NDMP environment variable.

try:
    api_response = api_instance.create_ndmp_settings_variable(ndmp_settings_variable, ndmp_settings_variable_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_ndmp_settings_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_variable** | [**NdmpSettingsVariableCreateParams**](NdmpSettingsVariableCreateParams.md)|  | 
 **ndmp_settings_variable_id** | **str**| Create a preferred NDMP environment variable. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ndmp_user**
> Empty create_ndmp_user(ndmp_user)



Created a new user.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_user = isilon_sdk.v9_2_1.NdmpUserCreateParams() # NdmpUserCreateParams | 

try:
    api_response = api_instance.create_ndmp_user(ndmp_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_ndmp_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_user** | [**NdmpUserCreateParams**](NdmpUserCreateParams.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_alias**
> CreateNfsAliasResponse create_nfs_alias(nfs_alias, zone=zone)



Create a new NFS alias.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_alias = isilon_sdk.v9_2_1.NfsAliasCreateParams() # NfsAliasCreateParams | 
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.create_nfs_alias(nfs_alias, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_alias** | [**NfsAliasCreateParams**](NfsAliasCreateParams.md)|  | 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**CreateNfsAliasResponse**](CreateNfsAliasResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_export**
> CreateQuotaReportResponse create_nfs_export(nfs_export, force=force, ignore_bad_auth=ignore_bad_auth, ignore_bad_paths=ignore_bad_paths, ignore_conflicts=ignore_conflicts, ignore_unresolvable_hosts=ignore_unresolvable_hosts, zone=zone)



Create a new NFS export.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_export = isilon_sdk.v9_2_1.NfsExportCreateParams() # NfsExportCreateParams | 
force = true # bool | If true, the export will be created even if it conflicts with another export. (optional)
ignore_bad_auth = true # bool | Ignore invalid users. (optional)
ignore_bad_paths = true # bool | Ignore nonexistent or otherwise bad paths. (optional)
ignore_conflicts = true # bool | Ignore conflicts with existing exports. (optional)
ignore_unresolvable_hosts = true # bool | Ignore unresolvable hosts. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.create_nfs_export(nfs_export, force=force, ignore_bad_auth=ignore_bad_auth, ignore_bad_paths=ignore_bad_paths, ignore_conflicts=ignore_conflicts, ignore_unresolvable_hosts=ignore_unresolvable_hosts, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export** | [**NfsExportCreateParams**](NfsExportCreateParams.md)|  | 
 **force** | **bool**| If true, the export will be created even if it conflicts with another export. | [optional] 
 **ignore_bad_auth** | **bool**| Ignore invalid users. | [optional] 
 **ignore_bad_paths** | **bool**| Ignore nonexistent or otherwise bad paths. | [optional] 
 **ignore_conflicts** | **bool**| Ignore conflicts with existing exports. | [optional] 
 **ignore_unresolvable_hosts** | **bool**| Ignore unresolvable hosts. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**CreateQuotaReportResponse**](CreateQuotaReportResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_netgroup_check_item**
> Empty create_nfs_netgroup_check_item(nfs_netgroup_check_item, host=host)



Update the NFS netgroups in the cache.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_netgroup_check_item = isilon_sdk.v9_2_1.Empty() # Empty | 
host = 'host_example' # str | IP address of node to update. If unspecified, the local nodes cache is updated. (optional)

try:
    api_response = api_instance.create_nfs_netgroup_check_item(nfs_netgroup_check_item, host=host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_netgroup_check_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_netgroup_check_item** | [**Empty**](Empty.md)|  | 
 **host** | **str**| IP address of node to update. If unspecified, the local nodes cache is updated. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_netgroup_flush_item**
> Empty create_nfs_netgroup_flush_item(nfs_netgroup_flush_item, host=host)



Flush the NFS netgroups in the cache.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_netgroup_flush_item = isilon_sdk.v9_2_1.Empty() # Empty | 
host = 'host_example' # str | IP address of node to flush. If unspecified, all nodes on the cluster are flushed. (optional)

try:
    api_response = api_instance.create_nfs_netgroup_flush_item(nfs_netgroup_flush_item, host=host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_netgroup_flush_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_netgroup_flush_item** | [**Empty**](Empty.md)|  | 
 **host** | **str**| IP address of node to flush. If unspecified, all nodes on the cluster are flushed. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_netgroup_save_item**
> Empty create_nfs_netgroup_save_item(nfs_netgroup_save_item, host=host)



Save the NFS netgroups in the cache.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_netgroup_save_item = isilon_sdk.v9_2_1.Empty() # Empty | 
host = 'host_example' # str | IP address of node to save. If unspecified, all nodes on the cluster are saved. (optional)

try:
    api_response = api_instance.create_nfs_netgroup_save_item(nfs_netgroup_save_item, host=host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_netgroup_save_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_netgroup_save_item** | [**Empty**](Empty.md)|  | 
 **host** | **str**| IP address of node to save. If unspecified, all nodes on the cluster are saved. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_nlm_sessions_check_item**
> CreateNfsNlmSessionsCheckItemResponse create_nfs_nlm_sessions_check_item(nfs_nlm_sessions_check_item, cluster_ip=cluster_ip, zone=zone)



Perform an active scan for lost NFSv3 locks.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_nlm_sessions_check_item = isilon_sdk.v9_2_1.Empty() # Empty | 
cluster_ip = 'cluster_ip_example' # str | An IP address for which NSM has client records (optional)
zone = 'zone_example' # str | Represents an extant auth zone (optional)

try:
    api_response = api_instance.create_nfs_nlm_sessions_check_item(nfs_nlm_sessions_check_item, cluster_ip=cluster_ip, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_nlm_sessions_check_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_nlm_sessions_check_item** | [**Empty**](Empty.md)|  | 
 **cluster_ip** | **str**| An IP address for which NSM has client records | [optional] 
 **zone** | **str**| Represents an extant auth zone | [optional] 

### Return type

[**CreateNfsNlmSessionsCheckItemResponse**](CreateNfsNlmSessionsCheckItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_reload_item**
> Empty create_nfs_reload_item(nfs_reload_item, zone=zone)



Reload default NFS export configuration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_reload_item = isilon_sdk.v9_2_1.Empty() # Empty | 
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.create_nfs_reload_item(nfs_reload_item, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_reload_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_reload_item** | [**Empty**](Empty.md)|  | 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ntp_server**
> Empty create_ntp_server(ntp_server)



Create an NTP server entry.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ntp_server = isilon_sdk.v9_2_1.NtpServerCreateParams() # NtpServerCreateParams | 

try:
    api_response = api_instance.create_ntp_server(ntp_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_ntp_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_server** | [**NtpServerCreateParams**](NtpServerCreateParams.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_s3_bucket**
> CreateResponse create_s3_bucket(s3_bucket, zone=zone)



Create a new bucket.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_bucket = isilon_sdk.v9_2_1.S3BucketCreateParams() # S3BucketCreateParams | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.create_s3_bucket(s3_bucket, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_bucket** | [**S3BucketCreateParams**](S3BucketCreateParams.md)|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_s3_key**
> CreateS3KeyResponse create_s3_key(s3_key, s3_key_id, force=force, zone=zone)



Generate a new secret key/access ID for given user.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_key = isilon_sdk.v9_2_1.S3Key() # S3Key | 
s3_key_id = 's3_key_id_example' # str | Generate a new secret key/access ID for given user.
force = true # bool | Forces to create new key. (optional)
zone = 'zone_example' # str | Specifies access zone containing user. (optional)

try:
    api_response = api_instance.create_s3_key(s3_key, s3_key_id, force=force, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_s3_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_key** | [**S3Key**](S3Key.md)|  | 
 **s3_key_id** | **str**| Generate a new secret key/access ID for given user. | 
 **force** | **bool**| Forces to create new key. | [optional] 
 **zone** | **str**| Specifies access zone containing user. | [optional] 

### Return type

[**CreateS3KeyResponse**](CreateS3KeyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_s3_mykey**
> CreateS3KeyResponse create_s3_mykey(s3_mykey, force=force)



Generate a new secret key/access ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_mykey = isilon_sdk.v9_2_1.S3Key() # S3Key | 
force = true # bool | Forces to create new key. (optional)

try:
    api_response = api_instance.create_s3_mykey(s3_mykey, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_s3_mykey: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_mykey** | [**S3Key**](S3Key.md)|  | 
 **force** | **bool**| Forces to create new key. | [optional] 

### Return type

[**CreateS3KeyResponse**](CreateS3KeyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_smb_log_level_filter**
> CreateSmbLogLevelFilterResponse create_smb_log_level_filter(smb_log_level_filter)



Add an SMB log filter.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_log_level_filter = isilon_sdk.v9_2_1.SmbLogLevelFilter() # SmbLogLevelFilter | 

try:
    api_response = api_instance.create_smb_log_level_filter(smb_log_level_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_smb_log_level_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_log_level_filter** | [**SmbLogLevelFilter**](SmbLogLevelFilter.md)|  | 

### Return type

[**CreateSmbLogLevelFilterResponse**](CreateSmbLogLevelFilterResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_smb_share**
> CreateSmbShareResponse create_smb_share(smb_share, zone=zone)



Create a new share.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_share = isilon_sdk.v9_2_1.SmbShareCreateParams() # SmbShareCreateParams | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.create_smb_share(smb_share, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_share** | [**SmbShareCreateParams**](SmbShareCreateParams.md)|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**CreateSmbShareResponse**](CreateSmbShareResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_swift_account**
> Empty create_swift_account(swift_account, zone=zone)



Create a new Swift account

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
swift_account = isilon_sdk.v9_2_1.SwiftAccount() # SwiftAccount | 
zone = 'zone_example' # str | Access zone which contains Swift account. (optional)

try:
    api_response = api_instance.create_swift_account(swift_account, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_swift_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swift_account** | [**SwiftAccount**](SwiftAccount.md)|  | 
 **zone** | **str**| Access zone which contains Swift account. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hdfs_fsimage_latest**
> delete_hdfs_fsimage_latest(zone=zone)



Delete the latest HDFS FSImage, if there is one.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains HDFS FSImage. (optional)

try:
    api_instance.delete_hdfs_fsimage_latest(zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_hdfs_fsimage_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains HDFS FSImage. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hdfs_inotify_stream**
> delete_hdfs_inotify_stream(zone=zone)



Delete all collected events, this has the effect of resetting the stream. Note that this may cause clients reading INotify to fail. The clients that want to track metadata changes may resume reading from INotify stream after updating filesystem metadata from other sources, like HDFS FSImage.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which exposes HDFS INotify. (optional)

try:
    api_instance.delete_hdfs_inotify_stream(zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_hdfs_inotify_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which exposes HDFS INotify. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hdfs_proxyuser**
> delete_hdfs_proxyuser(hdfs_proxyuser_id, zone=zone)



Delete an HDFS proxyuser.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_proxyuser_id = 'hdfs_proxyuser_id_example' # str | Delete an HDFS proxyuser.
zone = 'zone_example' # str | Access zone which contains HDFS proxyuser. (optional)

try:
    api_instance.delete_hdfs_proxyuser(hdfs_proxyuser_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_hdfs_proxyuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_proxyuser_id** | **str**| Delete an HDFS proxyuser. | 
 **zone** | **str**| Access zone which contains HDFS proxyuser. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hdfs_rack**
> delete_hdfs_rack(hdfs_rack_id, zone=zone)



Delete the HDFS rack.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_rack_id = 'hdfs_rack_id_example' # str | Delete the HDFS rack.
zone = 'zone_example' # str | Access zone which contains HDFS rack. (optional)

try:
    api_instance.delete_hdfs_rack(hdfs_rack_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_hdfs_rack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_rack_id** | **str**| Delete the HDFS rack. | 
 **zone** | **str**| Access zone which contains HDFS rack. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndmp_contexts_backup_by_id**
> delete_ndmp_contexts_backup_by_id(ndmp_contexts_backup_id)



Delete a backup context

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_contexts_backup_id = 'ndmp_contexts_backup_id_example' # str | Delete a backup context

try:
    api_instance.delete_ndmp_contexts_backup_by_id(ndmp_contexts_backup_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ndmp_contexts_backup_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_contexts_backup_id** | **str**| Delete a backup context | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndmp_contexts_bre_by_id**
> delete_ndmp_contexts_bre_by_id(ndmp_contexts_bre_id)



Delete a NDMP BRE context

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_contexts_bre_id = 'ndmp_contexts_bre_id_example' # str | Delete a NDMP BRE context

try:
    api_instance.delete_ndmp_contexts_bre_by_id(ndmp_contexts_bre_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ndmp_contexts_bre_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_contexts_bre_id** | **str**| Delete a NDMP BRE context | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndmp_contexts_restore_by_id**
> delete_ndmp_contexts_restore_by_id(ndmp_contexts_restore_id)



Delete a restore context

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_contexts_restore_id = 'ndmp_contexts_restore_id_example' # str | Delete a restore context

try:
    api_instance.delete_ndmp_contexts_restore_by_id(ndmp_contexts_restore_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ndmp_contexts_restore_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_contexts_restore_id** | **str**| Delete a restore context | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndmp_dumpdate**
> delete_ndmp_dumpdate(ndmp_dumpdate_id, level=level)



Delete dumpdates entries of a specified path.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_dumpdate_id = 'ndmp_dumpdate_id_example' # str | Delete dumpdates entries of a specified path.
level = 56 # int | Level is an input from 0 to 10. (optional)

try:
    api_instance.delete_ndmp_dumpdate(ndmp_dumpdate_id, level=level)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ndmp_dumpdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_dumpdate_id** | **str**| Delete dumpdates entries of a specified path. | 
 **level** | **int**| Level is an input from 0 to 10. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndmp_session**
> delete_ndmp_session(ndmp_session_id, lnn=lnn)



Delete the ndmp session.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_session_id = 'ndmp_session_id_example' # str | Delete the ndmp session.
lnn = 'lnn_example' # str | Logical node number. (optional)

try:
    api_instance.delete_ndmp_session(ndmp_session_id, lnn=lnn)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ndmp_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_session_id** | **str**| Delete the ndmp session. | 
 **lnn** | **str**| Logical node number. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndmp_settings_preferred_ip**
> delete_ndmp_settings_preferred_ip(ndmp_settings_preferred_ip_id)



Delete a preferred ip preference.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_preferred_ip_id = 'ndmp_settings_preferred_ip_id_example' # str | Delete a preferred ip preference.

try:
    api_instance.delete_ndmp_settings_preferred_ip(ndmp_settings_preferred_ip_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ndmp_settings_preferred_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_preferred_ip_id** | **str**| Delete a preferred ip preference. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndmp_settings_variable**
> delete_ndmp_settings_variable(ndmp_settings_variable_id, name=name)



Delete preferred environment variable entries

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_variable_id = 'ndmp_settings_variable_id_example' # str | Delete preferred environment variable entries
name = 'name_example' # str | Name of the variable to delete. (optional)

try:
    api_instance.delete_ndmp_settings_variable(ndmp_settings_variable_id, name=name)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ndmp_settings_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_variable_id** | **str**| Delete preferred environment variable entries | 
 **name** | **str**| Name of the variable to delete. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ndmp_user**
> delete_ndmp_user(ndmp_user_id)



Delete the user.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_user_id = 'ndmp_user_id_example' # str | Delete the user.

try:
    api_instance.delete_ndmp_user(ndmp_user_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ndmp_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_user_id** | **str**| Delete the user. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_alias**
> delete_nfs_alias(nfs_alias_id, zone=zone)



Delete the export.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_alias_id = 'nfs_alias_id_example' # str | Delete the export.
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.delete_nfs_alias(nfs_alias_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_nfs_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_alias_id** | **str**| Delete the export. | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_export**
> delete_nfs_export(nfs_export_id, zone=zone)



Delete the export.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_export_id = 'nfs_export_id_example' # str | Delete the export.
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.delete_nfs_export(nfs_export_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export_id** | **str**| Delete the export. | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_nlm_session**
> delete_nfs_nlm_session(nfs_nlm_session_id, cluster_ip=cluster_ip, refresh=refresh, zone=zone)



Delete all lock state for this host.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_nlm_session_id = 'nfs_nlm_session_id_example' # str | Delete all lock state for this host.
cluster_ip = 'cluster_ip_example' # str | An IP address for which NSM has client records (optional)
refresh = true # bool | if set to true, the client will be given a chance to reclaim its locks before they are destroyed (optional)
zone = 'zone_example' # str | Represents an extant auth zone (optional)

try:
    api_instance.delete_nfs_nlm_session(nfs_nlm_session_id, cluster_ip=cluster_ip, refresh=refresh, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_nfs_nlm_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_nlm_session_id** | **str**| Delete all lock state for this host. | 
 **cluster_ip** | **str**| An IP address for which NSM has client records | [optional] 
 **refresh** | **bool**| if set to true, the client will be given a chance to reclaim its locks before they are destroyed | [optional] 
 **zone** | **str**| Represents an extant auth zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ntp_server**
> delete_ntp_server(ntp_server_id)



Delete an NTP server entry.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ntp_server_id = 'ntp_server_id_example' # str | Delete an NTP server entry.

try:
    api_instance.delete_ntp_server(ntp_server_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ntp_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_server_id** | **str**| Delete an NTP server entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ntp_servers**
> delete_ntp_servers()



Delete all NTP server entries.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_instance.delete_ntp_servers()
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_ntp_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_s3_bucket**
> delete_s3_bucket(s3_bucket_id, zone=zone)



Delete the bucket.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_bucket_id = 's3_bucket_id_example' # str | Delete the bucket.
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.delete_s3_bucket(s3_bucket_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_bucket_id** | **str**| Delete the bucket. | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_s3_key**
> delete_s3_key(s3_key_id, zone=zone)



Delete secret key information for given user.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_key_id = 's3_key_id_example' # str | Delete secret key information for given user.
zone = 'zone_example' # str | Specifies access zone containing user. (optional)

try:
    api_instance.delete_s3_key(s3_key_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_s3_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_key_id** | **str**| Delete secret key information for given user. | 
 **zone** | **str**| Specifies access zone containing user. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_s3_mykeys**
> delete_s3_mykeys()



Delete secret key information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_instance.delete_s3_mykeys()
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_s3_mykeys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_log_level_filter**
> delete_smb_log_level_filter(smb_log_level_filter_id)



Delete log filter.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_log_level_filter_id = 'smb_log_level_filter_id_example' # str | Delete log filter.

try:
    api_instance.delete_smb_log_level_filter(smb_log_level_filter_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_log_level_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_log_level_filter_id** | **str**| Delete log filter. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_log_level_filters**
> delete_smb_log_level_filters(level=level)



Delete existing SMB log filters.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
level = 'level_example' # str | Valid SMB logging levels (optional)

try:
    api_instance.delete_smb_log_level_filters(level=level)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_log_level_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **level** | **str**| Valid SMB logging levels | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_openfile**
> delete_smb_openfile(smb_openfile_id)



Close the file in the SMB server.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_openfile_id = 'smb_openfile_id_example' # str | Close the file in the SMB server.

try:
    api_instance.delete_smb_openfile(smb_openfile_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_openfile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_openfile_id** | **str**| Close the file in the SMB server. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_session**
> delete_smb_session(smb_session_id)



Close the SMB session.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_session_id = 'smb_session_id_example' # str | Close the SMB session.

try:
    api_instance.delete_smb_session(smb_session_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_session_id** | **str**| Close the SMB session. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_sessions_computer_user**
> delete_smb_sessions_computer_user(smb_sessions_computer_user, computer)



Close the SMB session.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_sessions_computer_user = 'smb_sessions_computer_user_example' # str | Close the SMB session.
computer = 'computer_example' # str | 

try:
    api_instance.delete_smb_sessions_computer_user(smb_sessions_computer_user, computer)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_sessions_computer_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_sessions_computer_user** | **str**| Close the SMB session. | 
 **computer** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_share**
> delete_smb_share(smb_share_id, zone=zone)



Delete the share.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_share_id = 'smb_share_id_example' # str | Delete the share.
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.delete_smb_share(smb_share_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_share_id** | **str**| Delete the share. | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_shares**
> delete_smb_shares()



Delete multiple smb shares.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_instance.delete_smb_shares()
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_shares: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_swift_account**
> delete_swift_account(swift_account_id, zone=zone)



Delete a Swift account.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
swift_account_id = 'swift_account_id_example' # str | Delete a Swift account.
zone = 'zone_example' # str | Access zone which contains Swift account. (optional)

try:
    api_instance.delete_swift_account(swift_account_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_swift_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swift_account_id** | **str**| Delete a Swift account. | 
 **zone** | **str**| Access zone which contains Swift account. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ftp_settings**
> FtpSettings get_ftp_settings()



Retrieve the FTP settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_ftp_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ftp_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FtpSettings**](FtpSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_crypto_settings**
> HdfsCryptoSettings get_hdfs_crypto_settings(zone=zone)



Retrieve HDFS crypto settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.get_hdfs_crypto_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_crypto_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**HdfsCryptoSettings**](HdfsCryptoSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_fsimage_job**
> HdfsFsimageJob get_hdfs_fsimage_job(zone=zone)



Retrieve current HDFS FSImage job information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains job information. (optional)

try:
    api_response = api_instance.get_hdfs_fsimage_job(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_fsimage_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains job information. | [optional] 

### Return type

[**HdfsFsimageJob**](HdfsFsimageJob.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_fsimage_job_settings**
> HdfsFsimageJobSettings get_hdfs_fsimage_job_settings(zone=zone)



Retrieve HDFS FSImage job properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains job settings. (optional)

try:
    api_response = api_instance.get_hdfs_fsimage_job_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_fsimage_job_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains job settings. | [optional] 

### Return type

[**HdfsFsimageJobSettings**](HdfsFsimageJobSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_fsimage_latest**
> HdfsFsimageLatest get_hdfs_fsimage_latest(zone=zone)



Retrieve the latest HDFS FSImage information, if there is one.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains HDFS FSImage. (optional)

try:
    api_response = api_instance.get_hdfs_fsimage_latest(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_fsimage_latest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains HDFS FSImage. | [optional] 

### Return type

[**HdfsFsimageLatest**](HdfsFsimageLatest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_fsimage_settings**
> HdfsFsimageSettings get_hdfs_fsimage_settings(zone=zone)



Retrieve HDFS FSImage properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains FSImage settings. (optional)

try:
    api_response = api_instance.get_hdfs_fsimage_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_fsimage_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains FSImage settings. | [optional] 

### Return type

[**HdfsFsimageSettings**](HdfsFsimageSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_inotify_settings**
> HdfsInotifySettings get_hdfs_inotify_settings(zone=zone)



Retrieve HDFS INotify properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains INotify settings. (optional)

try:
    api_response = api_instance.get_hdfs_inotify_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_inotify_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains INotify settings. | [optional] 

### Return type

[**HdfsInotifySettings**](HdfsInotifySettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_inotify_stream**
> HdfsInotifyStream get_hdfs_inotify_stream(zone=zone)



Retrieve information about the collection and availability of HDFS INotify edit events.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which exposes HDFS INotify. (optional)

try:
    api_response = api_instance.get_hdfs_inotify_stream(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_inotify_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which exposes HDFS INotify. | [optional] 

### Return type

[**HdfsInotifyStream**](HdfsInotifyStream.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_log_level**
> HdfsLogLevel get_hdfs_log_level()



Retrieve the HDFS service log-level.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_hdfs_log_level()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_log_level: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HdfsLogLevel**](HdfsLogLevel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_proxyuser**
> HdfsProxyusers get_hdfs_proxyuser(hdfs_proxyuser_id, zone=zone)



View the proxyuser.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_proxyuser_id = 'hdfs_proxyuser_id_example' # str | View the proxyuser.
zone = 'zone_example' # str | Access zone which contains HDFS proxyuser. (optional)

try:
    api_response = api_instance.get_hdfs_proxyuser(hdfs_proxyuser_id, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_proxyuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_proxyuser_id** | **str**| View the proxyuser. | 
 **zone** | **str**| Access zone which contains HDFS proxyuser. | [optional] 

### Return type

[**HdfsProxyusers**](HdfsProxyusers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_rack**
> HdfsRacks get_hdfs_rack(hdfs_rack_id, zone=zone)



Retrieve the HDFS rack.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_rack_id = 'hdfs_rack_id_example' # str | Retrieve the HDFS rack.
zone = 'zone_example' # str | Access zone which contains HDFS rack. (optional)

try:
    api_response = api_instance.get_hdfs_rack(hdfs_rack_id, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_rack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_rack_id** | **str**| Retrieve the HDFS rack. | 
 **zone** | **str**| Access zone which contains HDFS rack. | [optional] 

### Return type

[**HdfsRacks**](HdfsRacks.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_ranger_plugin_settings**
> HdfsRangerPluginSettings get_hdfs_ranger_plugin_settings(zone=zone)



Retrieve HDFS ranger-plugin properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains HDFS ranger-plugin settings. (optional)

try:
    api_response = api_instance.get_hdfs_ranger_plugin_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_ranger_plugin_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains HDFS ranger-plugin settings. | [optional] 

### Return type

[**HdfsRangerPluginSettings**](HdfsRangerPluginSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_settings**
> HdfsSettings get_hdfs_settings(zone=zone)



Retrieve HDFS properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains HDFS settings. (optional)

try:
    api_response = api_instance.get_hdfs_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains HDFS settings. | [optional] 

### Return type

[**HdfsSettings**](HdfsSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_settings_global**
> HdfsSettingsGlobal get_hdfs_settings_global()



Retrieve HDFS global settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_hdfs_settings_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_settings_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HdfsSettingsGlobal**](HdfsSettingsGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_http_settings**
> HttpSettings get_http_settings()



Retrieve HTTP properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_http_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_http_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HttpSettings**](HttpSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_contexts_backup**
> NdmpContextsBackupExtended get_ndmp_contexts_backup(limit=limit, resume=resume)



Get List of NDMP Backup Contexts.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_ndmp_contexts_backup(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_contexts_backup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NdmpContextsBackupExtended**](NdmpContextsBackupExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_contexts_backup_by_id**
> NdmpContextsBackup get_ndmp_contexts_backup_by_id(ndmp_contexts_backup_id)



View a NDMP backup context

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_contexts_backup_id = 'ndmp_contexts_backup_id_example' # str | View a NDMP backup context

try:
    api_response = api_instance.get_ndmp_contexts_backup_by_id(ndmp_contexts_backup_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_contexts_backup_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_contexts_backup_id** | **str**| View a NDMP backup context | 

### Return type

[**NdmpContextsBackup**](NdmpContextsBackup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_contexts_bre**
> NdmpContextsBreExtended get_ndmp_contexts_bre(limit=limit, resume=resume)



Get list of NDMP BRE Contexts.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_ndmp_contexts_bre(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_contexts_bre: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NdmpContextsBreExtended**](NdmpContextsBreExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_contexts_bre_by_id**
> NdmpContextsBre get_ndmp_contexts_bre_by_id(ndmp_contexts_bre_id)



View a NDMP BRE context

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_contexts_bre_id = 'ndmp_contexts_bre_id_example' # str | View a NDMP BRE context

try:
    api_response = api_instance.get_ndmp_contexts_bre_by_id(ndmp_contexts_bre_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_contexts_bre_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_contexts_bre_id** | **str**| View a NDMP BRE context | 

### Return type

[**NdmpContextsBre**](NdmpContextsBre.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_contexts_restore**
> NdmpContextsBackupExtended get_ndmp_contexts_restore(limit=limit, resume=resume)



Get List of NDMP Restore Contexts.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_ndmp_contexts_restore(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_contexts_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NdmpContextsBackupExtended**](NdmpContextsBackupExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_contexts_restore_by_id**
> NdmpContextsBackup get_ndmp_contexts_restore_by_id(ndmp_contexts_restore_id)



View a NDMP restore context

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_contexts_restore_id = 'ndmp_contexts_restore_id_example' # str | View a NDMP restore context

try:
    api_response = api_instance.get_ndmp_contexts_restore_by_id(ndmp_contexts_restore_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_contexts_restore_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_contexts_restore_id** | **str**| View a NDMP restore context | 

### Return type

[**NdmpContextsBackup**](NdmpContextsBackup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_diagnostics**
> NdmpDiagnostics get_ndmp_diagnostics()



List ndmp diagnostics settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_ndmp_diagnostics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_diagnostics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NdmpDiagnostics**](NdmpDiagnostics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_dumpdate**
> NdmpDumpdates get_ndmp_dumpdate(ndmp_dumpdate_id, dir=dir, level=level, limit=limit, path=path, resume=resume, sort=sort)



List of dumpdates entries.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_dumpdate_id = 'ndmp_dumpdate_id_example' # str | List of dumpdates entries.
dir = 'dir_example' # str | The direction of the sort. (optional)
level = 56 # int | Filter by dumpdate level. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
path = 'path_example' # str | Filter by file path. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_ndmp_dumpdate(ndmp_dumpdate_id, dir=dir, level=level, limit=limit, path=path, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_dumpdate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_dumpdate_id** | **str**| List of dumpdates entries. | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **level** | **int**| Filter by dumpdate level. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **path** | **str**| Filter by file path. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**NdmpDumpdates**](NdmpDumpdates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_logs**
> NdmpLogs get_ndmp_logs(lnn=lnn, page=page, pagesize=pagesize)



Get NDMP logs

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
lnn = 'lnn_example' # str | Logical node number. (optional)
page = 56 # int | The page number of the NDMP logs file. (optional)
pagesize = 56 # int | The page size of each page of the NDMP log file. (optional)

try:
    api_response = api_instance.get_ndmp_logs(lnn=lnn, page=page, pagesize=pagesize)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **str**| Logical node number. | [optional] 
 **page** | **int**| The page number of the NDMP logs file. | [optional] 
 **pagesize** | **int**| The page size of each page of the NDMP log file. | [optional] 

### Return type

[**NdmpLogs**](NdmpLogs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_session**
> NdmpSessions get_ndmp_session(ndmp_session_id, lnn=lnn)



Retrieve the ndmp session.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_session_id = 'ndmp_session_id_example' # str | Retrieve the ndmp session.
lnn = 'lnn_example' # str | Logical node number. (optional)

try:
    api_response = api_instance.get_ndmp_session(ndmp_session_id, lnn=lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_session_id** | **str**| Retrieve the ndmp session. | 
 **lnn** | **str**| Logical node number. | [optional] 

### Return type

[**NdmpSessions**](NdmpSessions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_sessions**
> NdmpSessionsExtended get_ndmp_sessions(consolidate=consolidate, limit=limit, node=node, resume=resume, session=session)



List all ndmp sessions.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
consolidate = true # bool | Combine sessions in the same context. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
node = 'node_example' # str | Only return sessions of the node. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
session = 'session_example' # str | Only return the specified session. (optional)

try:
    api_response = api_instance.get_ndmp_sessions(consolidate=consolidate, limit=limit, node=node, resume=resume, session=session)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **consolidate** | **bool**| Combine sessions in the same context. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **node** | **str**| Only return sessions of the node. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **session** | **str**| Only return the specified session. | [optional] 

### Return type

[**NdmpSessionsExtended**](NdmpSessionsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_settings_dmas**
> NdmpSettingsDmas get_ndmp_settings_dmas()



List of supported dma vendors.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_ndmp_settings_dmas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_settings_dmas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NdmpSettingsDmas**](NdmpSettingsDmas.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_settings_global**
> NdmpSettingsGlobal get_ndmp_settings_global()



List global ndmp settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_ndmp_settings_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_settings_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NdmpSettingsGlobal**](NdmpSettingsGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_settings_preferred_ip**
> NdmpSettingsPreferredIps get_ndmp_settings_preferred_ip(ndmp_settings_preferred_ip_id)



Get one preference by id.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_preferred_ip_id = 'ndmp_settings_preferred_ip_id_example' # str | Get one preference by id.

try:
    api_response = api_instance.get_ndmp_settings_preferred_ip(ndmp_settings_preferred_ip_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_settings_preferred_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_preferred_ip_id** | **str**| Get one preference by id. | 

### Return type

[**NdmpSettingsPreferredIps**](NdmpSettingsPreferredIps.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_settings_variable**
> NdmpSettingsVariables get_ndmp_settings_variable(ndmp_settings_variable_id, limit=limit, path=path, resume=resume)



List of preferred environment variables.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_variable_id = 'ndmp_settings_variable_id_example' # str | List of preferred environment variables.
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
path = 'path_example' # str | Return variables of the path. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_ndmp_settings_variable(ndmp_settings_variable_id, limit=limit, path=path, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_settings_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_variable_id** | **str**| List of preferred environment variables. | 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **path** | **str**| Return variables of the path. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NdmpSettingsVariables**](NdmpSettingsVariables.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ndmp_user**
> NdmpUsers get_ndmp_user(ndmp_user_id)



Retrieve the user.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_user_id = 'ndmp_user_id_example' # str | Retrieve the user.

try:
    api_response = api_instance.get_ndmp_user(ndmp_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ndmp_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_user_id** | **str**| Retrieve the user. | 

### Return type

[**NdmpUsers**](NdmpUsers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_alias**
> NfsAliases get_nfs_alias(nfs_alias_id, check=check, scope=scope, zone=zone)



Retrieve export information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_alias_id = 'nfs_alias_id_example' # str | Retrieve export information.
check = true # bool | Check for conflicts when viewing alias. (optional)
scope = 'scope_example' # str | When specified as 'effective', or not specified, all fields are returned. When specified as 'user', only fields with non-default values are shown. When specified as 'default', the original values are returned. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_alias(nfs_alias_id, check=check, scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_alias_id** | **str**| Retrieve export information. | 
 **check** | **bool**| Check for conflicts when viewing alias. | [optional] 
 **scope** | **str**| When specified as &#39;effective&#39;, or not specified, all fields are returned. When specified as &#39;user&#39;, only fields with non-default values are shown. When specified as &#39;default&#39;, the original values are returned. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsAliases**](NfsAliases.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_check**
> NfsCheckExtended get_nfs_check(ignore_bad_auth=ignore_bad_auth, ignore_bad_paths=ignore_bad_paths, ignore_unresolvable_hosts=ignore_unresolvable_hosts, zone=zone)



Retrieve NFS export validation information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ignore_bad_auth = true # bool | Ignore invalid users. (optional)
ignore_bad_paths = true # bool | Ignore nonexistent or otherwise bad paths. (optional)
ignore_unresolvable_hosts = true # bool | Ignore unresolvable hosts. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_check(ignore_bad_auth=ignore_bad_auth, ignore_bad_paths=ignore_bad_paths, ignore_unresolvable_hosts=ignore_unresolvable_hosts, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ignore_bad_auth** | **bool**| Ignore invalid users. | [optional] 
 **ignore_bad_paths** | **bool**| Ignore nonexistent or otherwise bad paths. | [optional] 
 **ignore_unresolvable_hosts** | **bool**| Ignore unresolvable hosts. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsCheckExtended**](NfsCheckExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_export**
> NfsExports get_nfs_export(nfs_export_id, scope=scope, zone=zone)



Retrieve export information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_export_id = 'nfs_export_id_example' # str | Retrieve export information.
scope = 'scope_example' # str | When specified as 'effective', or not specified, all fields are returned. When specified as 'user', only fields with non-default values are shown. When specified as 'default', the original values are returned. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_export(nfs_export_id, scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export_id** | **str**| Retrieve export information. | 
 **scope** | **str**| When specified as &#39;effective&#39;, or not specified, all fields are returned. When specified as &#39;user&#39;, only fields with non-default values are shown. When specified as &#39;default&#39;, the original values are returned. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsExports**](NfsExports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_exports_summary**
> NfsExportsSummary get_nfs_exports_summary(zone=zone)



Retrieve NFS export summary information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_exports_summary(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_exports_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsExportsSummary**](NfsExportsSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_log_level**
> NfsLogLevel get_nfs_log_level()



Get the current NFS service logging level.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_nfs_log_level()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_log_level: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NfsLogLevel**](NfsLogLevel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_netgroup**
> NfsNetgroup get_nfs_netgroup(host=host)



Get the current NFS netgroup cache settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
host = 'host_example' # str | Host to retrieve netgroup cache settings from. (optional)

try:
    api_response = api_instance.get_nfs_netgroup(host=host)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_netgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host** | **str**| Host to retrieve netgroup cache settings from. | [optional] 

### Return type

[**NfsNetgroup**](NfsNetgroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_nlm_locks**
> NfsNlmLocks get_nfs_nlm_locks(client=client, client_id=client_id, created=created, dir=dir, limit=limit, lin=lin, path=path, resume=resume, sort=sort)



List all NLM locks.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
client = 'client_example' # str | Filter locks by the specified client host name and IP address. (optional)
client_id = 'client_id_example' # str | Filter locks by the specified client ID. (optional)
created = 'created_example' # str | Return locks created after the specified unix epoch time. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
lin = 'lin_example' # str | Filter locks by the specified LIN in /ifs that is locked. (optional)
path = 'path_example' # str | Filter locks by the specified path under /ifs. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_nfs_nlm_locks(client=client, client_id=client_id, created=created, dir=dir, limit=limit, lin=lin, path=path, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_nlm_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**| Filter locks by the specified client host name and IP address. | [optional] 
 **client_id** | **str**| Filter locks by the specified client ID. | [optional] 
 **created** | **str**| Return locks created after the specified unix epoch time. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **lin** | **str**| Filter locks by the specified LIN in /ifs that is locked. | [optional] 
 **path** | **str**| Filter locks by the specified path under /ifs. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**NfsNlmLocks**](NfsNlmLocks.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_nlm_session**
> NfsNlmSessions get_nfs_nlm_session(nfs_nlm_session_id, cluster_ip=cluster_ip, zone=zone)



Retrieve all lock state for a single client.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_nlm_session_id = 'nfs_nlm_session_id_example' # str | Retrieve all lock state for a single client.
cluster_ip = 'cluster_ip_example' # str | An IP address for which NSM has client records (optional)
zone = 'zone_example' # str | Represents an extant auth zone (optional)

try:
    api_response = api_instance.get_nfs_nlm_session(nfs_nlm_session_id, cluster_ip=cluster_ip, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_nlm_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_nlm_session_id** | **str**| Retrieve all lock state for a single client. | 
 **cluster_ip** | **str**| An IP address for which NSM has client records | [optional] 
 **zone** | **str**| Represents an extant auth zone | [optional] 

### Return type

[**NfsNlmSessions**](NfsNlmSessions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_nlm_sessions**
> NfsNlmSessionsExtended get_nfs_nlm_sessions(dir=dir, ip=ip, limit=limit, sort=sort, zone=zone)



List all NSM clients (optionally filtered by either zone or IP)

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
ip = 'ip_example' # str | An IP address for which NSM has client records (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
zone = 'zone_example' # str | Represents an extant auth zone (optional)

try:
    api_response = api_instance.get_nfs_nlm_sessions(dir=dir, ip=ip, limit=limit, sort=sort, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_nlm_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **ip** | **str**| An IP address for which NSM has client records | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **zone** | **str**| Represents an extant auth zone | [optional] 

### Return type

[**NfsNlmSessionsExtended**](NfsNlmSessionsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_nlm_waiters**
> NfsNlmWaiters get_nfs_nlm_waiters(dir=dir, limit=limit, resume=resume, sort=sort)



List all NLM lock waiters.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_nfs_nlm_waiters(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_nlm_waiters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**NfsNlmWaiters**](NfsNlmWaiters.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_settings_export**
> NfsSettingsExport get_nfs_settings_export(scope=scope, zone=zone)



Retrieve export information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_settings_export(scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_settings_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsSettingsExport**](NfsSettingsExport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_settings_global**
> NfsSettingsGlobal get_nfs_settings_global()



Retrieve the NFS configuration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_nfs_settings_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_settings_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NfsSettingsGlobal**](NfsSettingsGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_settings_zone**
> NfsSettingsZone get_nfs_settings_zone(zone=zone)



Retrieve the NFS server settings for this zone.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_settings_zone(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_settings_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsSettingsZone**](NfsSettingsZone.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ntp_server**
> NtpServers get_ntp_server(ntp_server_id)



Retrieve one NTP server.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ntp_server_id = 'ntp_server_id_example' # str | Retrieve one NTP server.

try:
    api_response = api_instance.get_ntp_server(ntp_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ntp_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_server_id** | **str**| Retrieve one NTP server. | 

### Return type

[**NtpServers**](NtpServers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ntp_settings**
> NtpSettings get_ntp_settings()



Retrieve the NTP settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_ntp_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ntp_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NtpSettings**](NtpSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_bucket**
> S3Buckets get_s3_bucket(s3_bucket_id, zone=zone)



Retrieve bucket.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_bucket_id = 's3_bucket_id_example' # str | Retrieve bucket.
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.get_s3_bucket(s3_bucket_id, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_bucket_id** | **str**| Retrieve bucket. | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**S3Buckets**](S3Buckets.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_key**
> S3Keys get_s3_key(s3_key_id, zone=zone)



Get access ID information for given user.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_key_id = 's3_key_id_example' # str | Get access ID information for given user.
zone = 'zone_example' # str | Specifies access zone containing user. (optional)

try:
    api_response = api_instance.get_s3_key(s3_key_id, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_s3_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_key_id** | **str**| Get access ID information for given user. | 
 **zone** | **str**| Specifies access zone containing user. | [optional] 

### Return type

[**S3Keys**](S3Keys.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_log_level**
> S3LogLevel get_s3_log_level()



Get the current S3 service logging level.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_s3_log_level()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_s3_log_level: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**S3LogLevel**](S3LogLevel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_settings_global**
> S3SettingsGlobal get_s3_settings_global()



Retrieve global S3 bucket settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_s3_settings_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_s3_settings_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**S3SettingsGlobal**](S3SettingsGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_s3_settings_zone**
> S3SettingsZone get_s3_settings_zone(zone=zone)



Retrieve the S3 bucket settings for this zone.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_s3_settings_zone(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_s3_settings_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone | [optional] 

### Return type

[**S3SettingsZone**](S3SettingsZone.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_log_level**
> SmbLogLevel get_smb_log_level()



Get the current SMB logging level.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_smb_log_level()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_log_level: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SmbLogLevel**](SmbLogLevel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_log_level_filter**
> SmbLogLevelFilters get_smb_log_level_filter(smb_log_level_filter_id)



View log filter.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_log_level_filter_id = 'smb_log_level_filter_id_example' # str | View log filter.

try:
    api_response = api_instance.get_smb_log_level_filter(smb_log_level_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_log_level_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_log_level_filter_id** | **str**| View log filter. | 

### Return type

[**SmbLogLevelFilters**](SmbLogLevelFilters.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_openfiles**
> SmbOpenfiles get_smb_openfiles(dir=dir, limit=limit, resume=resume, sort=sort)



List open files.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | Order results by this field. Default is id. (optional)

try:
    api_response = api_instance.get_smb_openfiles(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_openfiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| Order results by this field. Default is id. | [optional] 

### Return type

[**SmbOpenfiles**](SmbOpenfiles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_sessions**
> ProtocolsSmbSessions get_smb_sessions(limit=limit, lnn=lnn, lnn_skip=lnn_skip, resume=resume)



List open SMB sessions.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
lnn = 'lnn_example' # str | The node to fetch open sessions from. (optional)
lnn_skip = 'lnn_skip_example' # str | When parameter lnn=all, don't fetch open session info from this node. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_smb_sessions(limit=limit, lnn=lnn, lnn_skip=lnn_skip, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **lnn** | **str**| The node to fetch open sessions from. | [optional] 
 **lnn_skip** | **str**| When parameter lnn&#x3D;all, don&#39;t fetch open session info from this node. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**ProtocolsSmbSessions**](ProtocolsSmbSessions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_settings_global**
> SmbSettingsGlobal get_smb_settings_global(scope=scope)



List all settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_smb_settings_global(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**SmbSettingsGlobal**](SmbSettingsGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_settings_share**
> SmbSettingsShare get_smb_settings_share(scope=scope, zone=zone)



List all settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.get_smb_settings_share(scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_settings_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**SmbSettingsShare**](SmbSettingsShare.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_settings_zone**
> SmbSettingsZone get_smb_settings_zone(scope=scope, zone=zone)



List all settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
zone = 'zone_example' # str | Name of the access zone (optional)

try:
    api_response = api_instance.get_smb_settings_zone(scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_settings_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **zone** | **str**| Name of the access zone | [optional] 

### Return type

[**SmbSettingsZone**](SmbSettingsZone.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_share**
> SmbShares get_smb_share(smb_share_id, resolve_names=resolve_names, scope=scope, zone=zone)



Retrieve share.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_share_id = 'smb_share_id_example' # str | Retrieve share.
resolve_names = true # bool | If true, resolve group and user names in personas. (optional)
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.get_smb_share(smb_share_id, resolve_names=resolve_names, scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_share_id** | **str**| Retrieve share. | 
 **resolve_names** | **bool**| If true, resolve group and user names in personas. | [optional] 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**SmbShares**](SmbShares.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_shares_summary**
> SmbSharesSummary get_smb_shares_summary(zone=zone)



Return summary information about shares.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.get_smb_shares_summary(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_shares_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**SmbSharesSummary**](SmbSharesSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snmp_settings**
> SnmpSettings get_snmp_settings()



Retrieve the SNMP settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_snmp_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_snmp_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnmpSettings**](SnmpSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssh_settings**
> SshSettings get_ssh_settings()



ssh settings

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_ssh_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_ssh_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SshSettings**](SshSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_swift_account**
> SwiftAccounts get_swift_account(swift_account_id, zone=zone)



List a swift account.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
swift_account_id = 'swift_account_id_example' # str | List a swift account.
zone = 'zone_example' # str | Access zone which contains Swift account. (optional)

try:
    api_response = api_instance.get_swift_account(swift_account_id, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_swift_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swift_account_id** | **str**| List a swift account. | 
 **zone** | **str**| Access zone which contains Swift account. | [optional] 

### Return type

[**SwiftAccounts**](SwiftAccounts.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hdfs_crypto_encryption_zones**
> HdfsCryptoEncryptionZones list_hdfs_crypto_encryption_zones(dir=dir, limit=limit, resume=resume, sort=sort, zone=zone)



Retrieve a list of Encryption Zones.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.list_hdfs_crypto_encryption_zones(dir=dir, limit=limit, resume=resume, sort=sort, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_hdfs_crypto_encryption_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**HdfsCryptoEncryptionZones**](HdfsCryptoEncryptionZones.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hdfs_proxyusers**
> HdfsProxyusers list_hdfs_proxyusers(dir=dir, limit=limit, resume=resume, zone=zone)



List all proxyusers.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
zone = 'zone_example' # str | Access zone which contains HDFS proxyusers. (optional)

try:
    api_response = api_instance.list_hdfs_proxyusers(dir=dir, limit=limit, resume=resume, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_hdfs_proxyusers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **zone** | **str**| Access zone which contains HDFS proxyusers. | [optional] 

### Return type

[**HdfsProxyusers**](HdfsProxyusers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hdfs_racks**
> HdfsRacksExtended list_hdfs_racks(dir=dir, limit=limit, resume=resume, zone=zone)



List all racks.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
zone = 'zone_example' # str | Access zone which contains HDFS racks. (optional)

try:
    api_response = api_instance.list_hdfs_racks(dir=dir, limit=limit, resume=resume, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_hdfs_racks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **zone** | **str**| Access zone which contains HDFS racks. | [optional] 

### Return type

[**HdfsRacksExtended**](HdfsRacksExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ndmp_settings_preferred_ips**
> NdmpSettingsPreferredIpsExtended list_ndmp_settings_preferred_ips(limit=limit, resume=resume, scope=scope)



Get list of preferences.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
scope = 'scope_example' # str | Either cluster or a network subnet defined in OneFS. (optional)

try:
    api_response = api_instance.list_ndmp_settings_preferred_ips(limit=limit, resume=resume, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_ndmp_settings_preferred_ips: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **scope** | **str**| Either cluster or a network subnet defined in OneFS. | [optional] 

### Return type

[**NdmpSettingsPreferredIpsExtended**](NdmpSettingsPreferredIpsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ndmp_users**
> NdmpUsersExtended list_ndmp_users()



List all ndmp administrators.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.list_ndmp_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_ndmp_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NdmpUsersExtended**](NdmpUsersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nfs_aliases**
> NfsAliasesExtended list_nfs_aliases(check=check, dir=dir, limit=limit, resume=resume, sort=sort, zone=zone)



List all NFS aliases.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
check = true # bool | Check for conflicts when listing aliases. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.list_nfs_aliases(check=check, dir=dir, limit=limit, resume=resume, sort=sort, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check** | **bool**| Check for conflicts when listing aliases. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsAliasesExtended**](NfsAliasesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nfs_exports**
> NfsExportsExtended list_nfs_exports(check=check, dir=dir, limit=limit, offset=offset, path=path, resume=resume, scope=scope, sort=sort, zone=zone)



List all NFS exports.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
check = true # bool | Check for conflicts when listing exports. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
offset = 56 # int | The position of the first item returned for a paginated query within the full result set. (optional)
path = 'path_example' # str | If specified, only exports that explicitly reference at least one of the given paths will be returned. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
scope = 'scope_example' # str | When specified as 'effective', or not specified, all fields are returned. When specified as 'user', only fields with non-default values are shown. When specified as 'default', the original values are returned. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. Default is id. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.list_nfs_exports(check=check, dir=dir, limit=limit, offset=offset, path=path, resume=resume, scope=scope, sort=sort, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check** | **bool**| Check for conflicts when listing exports. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **offset** | **int**| The position of the first item returned for a paginated query within the full result set. | [optional] 
 **path** | **str**| If specified, only exports that explicitly reference at least one of the given paths will be returned. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **scope** | **str**| When specified as &#39;effective&#39;, or not specified, all fields are returned. When specified as &#39;user&#39;, only fields with non-default values are shown. When specified as &#39;default&#39;, the original values are returned. | [optional] 
 **sort** | **str**| The field that will be used for sorting. Default is id. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsExportsExtended**](NfsExportsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ntp_servers**
> NtpServersExtended list_ntp_servers(dir=dir, limit=limit, resume=resume, sort=sort)



List all NTP servers.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_ntp_servers(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_ntp_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**NtpServersExtended**](NtpServersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_s3_buckets**
> S3BucketsExtended list_s3_buckets(dir=dir, limit=limit, owner=owner, resume=resume, sort=sort, zone=zone)



List all buckets.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
owner = 'owner_example' # str | Specifies the name of the owner. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.list_s3_buckets(dir=dir, limit=limit, owner=owner, resume=resume, sort=sort, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_s3_buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **owner** | **str**| Specifies the name of the owner. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**S3BucketsExtended**](S3BucketsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_s3_mykeys**
> CreateS3KeyResponse list_s3_mykeys()



Get user secret key information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.list_s3_mykeys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_s3_mykeys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateS3KeyResponse**](CreateS3KeyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_smb_log_level_filters**
> SmbLogLevelFilters list_smb_log_level_filters(dir=dir, level=level, sort=sort)



Get the current SMB log filters.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
level = 'level_example' # str | Valid SMB logging levels (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_smb_log_level_filters(dir=dir, level=level, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_smb_log_level_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **level** | **str**| Valid SMB logging levels | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**SmbLogLevelFilters**](SmbLogLevelFilters.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_smb_shares**
> SmbSharesExtended list_smb_shares(dir=dir, limit=limit, resolve_names=resolve_names, resume=resume, scope=scope, sort=sort, zone=zone)



List all shares.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resolve_names = true # bool | If true, resolve group and user names in personas. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.list_smb_shares(dir=dir, limit=limit, resolve_names=resolve_names, resume=resume, scope=scope, sort=sort, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_smb_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resolve_names** | **bool**| If true, resolve group and user names in personas. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**SmbSharesExtended**](SmbSharesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_swift_accounts**
> SwiftAccountsExtended list_swift_accounts(zone=zone)



List all swift accounts.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains Swift accounts. (optional)

try:
    api_response = api_instance.list_swift_accounts(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_swift_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains Swift accounts. | [optional] 

### Return type

[**SwiftAccountsExtended**](SwiftAccountsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ftp_settings**
> update_ftp_settings(ftp_settings)



Modify the FTP settings. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ftp_settings = isilon_sdk.v9_2_1.FtpSettingsExtended() # FtpSettingsExtended | 

try:
    api_instance.update_ftp_settings(ftp_settings)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ftp_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ftp_settings** | [**FtpSettingsExtended**](FtpSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_crypto_settings**
> update_hdfs_crypto_settings(hdfs_crypto_settings, zone=zone)



Modify HDFS crypto settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_crypto_settings = isilon_sdk.v9_2_1.HdfsCryptoSettingsSettings() # HdfsCryptoSettingsSettings | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.update_hdfs_crypto_settings(hdfs_crypto_settings, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_crypto_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_crypto_settings** | [**HdfsCryptoSettingsSettings**](HdfsCryptoSettingsSettings.md)|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_fsimage_job_settings**
> update_hdfs_fsimage_job_settings(hdfs_fsimage_job_settings, zone=zone)



Modify HDFS FSImage job properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_fsimage_job_settings = isilon_sdk.v9_2_1.HdfsFsimageJobSettingsSettings() # HdfsFsimageJobSettingsSettings | 
zone = 'zone_example' # str | Access zone which contains job settings. (optional)

try:
    api_instance.update_hdfs_fsimage_job_settings(hdfs_fsimage_job_settings, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_fsimage_job_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_fsimage_job_settings** | [**HdfsFsimageJobSettingsSettings**](HdfsFsimageJobSettingsSettings.md)|  | 
 **zone** | **str**| Access zone which contains job settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_fsimage_settings**
> update_hdfs_fsimage_settings(hdfs_fsimage_settings, zone=zone)



Modify HDFS FSImage properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_fsimage_settings = isilon_sdk.v9_2_1.HdfsFsimageSettingsSettings() # HdfsFsimageSettingsSettings | 
zone = 'zone_example' # str | Access zone which contains FSImage settings. (optional)

try:
    api_instance.update_hdfs_fsimage_settings(hdfs_fsimage_settings, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_fsimage_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_fsimage_settings** | [**HdfsFsimageSettingsSettings**](HdfsFsimageSettingsSettings.md)|  | 
 **zone** | **str**| Access zone which contains FSImage settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_inotify_settings**
> update_hdfs_inotify_settings(hdfs_inotify_settings, zone=zone)



Modify HDFS INotify properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_inotify_settings = isilon_sdk.v9_2_1.HdfsInotifySettingsSettings() # HdfsInotifySettingsSettings | 
zone = 'zone_example' # str | Access zone which contains INotify settings. (optional)

try:
    api_instance.update_hdfs_inotify_settings(hdfs_inotify_settings, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_inotify_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_inotify_settings** | [**HdfsInotifySettingsSettings**](HdfsInotifySettingsSettings.md)|  | 
 **zone** | **str**| Access zone which contains INotify settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_log_level**
> update_hdfs_log_level(hdfs_log_level)



Modify the HDFS service log-level.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_log_level = isilon_sdk.v9_2_1.HdfsLogLevel() # HdfsLogLevel | 

try:
    api_instance.update_hdfs_log_level(hdfs_log_level)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_log_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_log_level** | [**HdfsLogLevel**](HdfsLogLevel.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_proxyuser**
> update_hdfs_proxyuser(hdfs_proxyuser, hdfs_proxyuser_id, zone=zone)



Modify an HDFS proxyuser.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_proxyuser = isilon_sdk.v9_2_1.Empty() # Empty | 
hdfs_proxyuser_id = 'hdfs_proxyuser_id_example' # str | Modify an HDFS proxyuser.
zone = 'zone_example' # str | Access zone which contains HDFS proxyuser. (optional)

try:
    api_instance.update_hdfs_proxyuser(hdfs_proxyuser, hdfs_proxyuser_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_proxyuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_proxyuser** | [**Empty**](Empty.md)|  | 
 **hdfs_proxyuser_id** | **str**| Modify an HDFS proxyuser. | 
 **zone** | **str**| Access zone which contains HDFS proxyuser. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_rack**
> update_hdfs_rack(hdfs_rack, hdfs_rack_id, zone=zone)



Modify the HDFS rack

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_rack = isilon_sdk.v9_2_1.HdfsRack() # HdfsRack | 
hdfs_rack_id = 'hdfs_rack_id_example' # str | Modify the HDFS rack
zone = 'zone_example' # str | Access zone which contains HDFS rack. (optional)

try:
    api_instance.update_hdfs_rack(hdfs_rack, hdfs_rack_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_rack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_rack** | [**HdfsRack**](HdfsRack.md)|  | 
 **hdfs_rack_id** | **str**| Modify the HDFS rack | 
 **zone** | **str**| Access zone which contains HDFS rack. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_ranger_plugin_settings**
> update_hdfs_ranger_plugin_settings(hdfs_ranger_plugin_settings, zone=zone)



Modify HDFS ranger-plugin properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_ranger_plugin_settings = isilon_sdk.v9_2_1.HdfsRangerPluginSettingsSettings() # HdfsRangerPluginSettingsSettings | 
zone = 'zone_example' # str | Access zone which contains HDFS ranger-plugin settings. (optional)

try:
    api_instance.update_hdfs_ranger_plugin_settings(hdfs_ranger_plugin_settings, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_ranger_plugin_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_ranger_plugin_settings** | [**HdfsRangerPluginSettingsSettings**](HdfsRangerPluginSettingsSettings.md)|  | 
 **zone** | **str**| Access zone which contains HDFS ranger-plugin settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_settings**
> update_hdfs_settings(hdfs_settings, zone=zone)



Modify HDFS properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_settings = isilon_sdk.v9_2_1.HdfsSettingsSettings() # HdfsSettingsSettings | 
zone = 'zone_example' # str | Access zone which contains HDFS settings. (optional)

try:
    api_instance.update_hdfs_settings(hdfs_settings, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_settings** | [**HdfsSettingsSettings**](HdfsSettingsSettings.md)|  | 
 **zone** | **str**| Access zone which contains HDFS settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_settings_global**
> update_hdfs_settings_global(hdfs_settings_global)



Modify HDFS global settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
hdfs_settings_global = isilon_sdk.v9_2_1.HdfsSettingsGlobalGlobalSettings() # HdfsSettingsGlobalGlobalSettings | 

try:
    api_instance.update_hdfs_settings_global(hdfs_settings_global)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_settings_global** | [**HdfsSettingsGlobalGlobalSettings**](HdfsSettingsGlobalGlobalSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_http_settings**
> update_http_settings(http_settings)



Modify HTTP properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
http_settings = isilon_sdk.v9_2_1.HttpSettingsSettings() # HttpSettingsSettings | 

try:
    api_instance.update_http_settings(http_settings)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_http_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **http_settings** | [**HttpSettingsSettings**](HttpSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ndmp_diagnostics**
> update_ndmp_diagnostics(ndmp_diagnostics)



Modify ndmp diagnostics settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_diagnostics = isilon_sdk.v9_2_1.NdmpDiagnosticsDiagnostics() # NdmpDiagnosticsDiagnostics | 

try:
    api_instance.update_ndmp_diagnostics(ndmp_diagnostics)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ndmp_diagnostics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_diagnostics** | [**NdmpDiagnosticsDiagnostics**](NdmpDiagnosticsDiagnostics.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ndmp_settings_global**
> update_ndmp_settings_global(ndmp_settings_global)



Modify one or more settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_global = isilon_sdk.v9_2_1.NdmpSettingsGlobalGlobal() # NdmpSettingsGlobalGlobal | 

try:
    api_instance.update_ndmp_settings_global(ndmp_settings_global)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ndmp_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_global** | [**NdmpSettingsGlobalGlobal**](NdmpSettingsGlobalGlobal.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ndmp_settings_preferred_ip**
> update_ndmp_settings_preferred_ip(ndmp_settings_preferred_ip, ndmp_settings_preferred_ip_id)



Modify a preferred ip preference.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_preferred_ip = isilon_sdk.v9_2_1.NdmpSettingsPreferredIp() # NdmpSettingsPreferredIp | 
ndmp_settings_preferred_ip_id = 'ndmp_settings_preferred_ip_id_example' # str | Modify a preferred ip preference.

try:
    api_instance.update_ndmp_settings_preferred_ip(ndmp_settings_preferred_ip, ndmp_settings_preferred_ip_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ndmp_settings_preferred_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_preferred_ip** | [**NdmpSettingsPreferredIp**](NdmpSettingsPreferredIp.md)|  | 
 **ndmp_settings_preferred_ip_id** | **str**| Modify a preferred ip preference. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ndmp_settings_variable**
> update_ndmp_settings_variable(ndmp_settings_variable, ndmp_settings_variable_id, name=name)



Modify or create a NDMP preferred environment variable.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_settings_variable = isilon_sdk.v9_2_1.NdmpSettingsVariable() # NdmpSettingsVariable | 
ndmp_settings_variable_id = 'ndmp_settings_variable_id_example' # str | Modify or create a NDMP preferred environment variable.
name = 'name_example' # str | Name of the variable to modify. (optional)

try:
    api_instance.update_ndmp_settings_variable(ndmp_settings_variable, ndmp_settings_variable_id, name=name)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ndmp_settings_variable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_settings_variable** | [**NdmpSettingsVariable**](NdmpSettingsVariable.md)|  | 
 **ndmp_settings_variable_id** | **str**| Modify or create a NDMP preferred environment variable. | 
 **name** | **str**| Name of the variable to modify. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ndmp_user**
> update_ndmp_user(ndmp_user, ndmp_user_id)



Modify the user

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ndmp_user = isilon_sdk.v9_2_1.NdmpUser() # NdmpUser | 
ndmp_user_id = 'ndmp_user_id_example' # str | Modify the user

try:
    api_instance.update_ndmp_user(ndmp_user, ndmp_user_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ndmp_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ndmp_user** | [**NdmpUser**](NdmpUser.md)|  | 
 **ndmp_user_id** | **str**| Modify the user | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_alias**
> update_nfs_alias(nfs_alias, nfs_alias_id, zone=zone)



Modify the alias. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_alias = isilon_sdk.v9_2_1.NfsAlias() # NfsAlias | 
nfs_alias_id = 'nfs_alias_id_example' # str | Modify the alias. All input fields are optional, but one or more must be supplied.
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.update_nfs_alias(nfs_alias, nfs_alias_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_alias** | [**NfsAlias**](NfsAlias.md)|  | 
 **nfs_alias_id** | **str**| Modify the alias. All input fields are optional, but one or more must be supplied. | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_export**
> update_nfs_export(nfs_export, nfs_export_id, force=force, ignore_bad_auth=ignore_bad_auth, ignore_bad_paths=ignore_bad_paths, ignore_conflicts=ignore_conflicts, ignore_unresolvable_hosts=ignore_unresolvable_hosts, zone=zone)



Modify the export. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_export = isilon_sdk.v9_2_1.NfsExport() # NfsExport | 
nfs_export_id = 'nfs_export_id_example' # str | Modify the export. All input fields are optional, but one or more must be supplied.
force = true # bool | If true, the export will be updated even if that change conflicts with another export. (optional)
ignore_bad_auth = true # bool | Ignore invalid users. (optional)
ignore_bad_paths = true # bool | Ignore nonexistent or otherwise bad paths. (optional)
ignore_conflicts = true # bool | Ignore conflicts with existing exports. (optional)
ignore_unresolvable_hosts = true # bool | Ignore unresolvable hosts. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.update_nfs_export(nfs_export, nfs_export_id, force=force, ignore_bad_auth=ignore_bad_auth, ignore_bad_paths=ignore_bad_paths, ignore_conflicts=ignore_conflicts, ignore_unresolvable_hosts=ignore_unresolvable_hosts, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export** | [**NfsExport**](NfsExport.md)|  | 
 **nfs_export_id** | **str**| Modify the export. All input fields are optional, but one or more must be supplied. | 
 **force** | **bool**| If true, the export will be updated even if that change conflicts with another export. | [optional] 
 **ignore_bad_auth** | **bool**| Ignore invalid users. | [optional] 
 **ignore_bad_paths** | **bool**| Ignore nonexistent or otherwise bad paths. | [optional] 
 **ignore_conflicts** | **bool**| Ignore conflicts with existing exports. | [optional] 
 **ignore_unresolvable_hosts** | **bool**| Ignore unresolvable hosts. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_log_level**
> update_nfs_log_level(nfs_log_level)



Set the current NFS service logging level.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_log_level = isilon_sdk.v9_2_1.NfsLogLevel() # NfsLogLevel | 

try:
    api_instance.update_nfs_log_level(nfs_log_level)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_log_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_log_level** | [**NfsLogLevel**](NfsLogLevel.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_netgroup**
> update_nfs_netgroup(nfs_netgroup, host=host)



Modify the current NFS netgroup settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_netgroup = isilon_sdk.v9_2_1.NfsNetgroup() # NfsNetgroup | 
host = 'host_example' # str | Host to retrieve netgroup cache settings for. (optional)

try:
    api_instance.update_nfs_netgroup(nfs_netgroup, host=host)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_netgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_netgroup** | [**NfsNetgroup**](NfsNetgroup.md)|  | 
 **host** | **str**| Host to retrieve netgroup cache settings for. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_settings_export**
> update_nfs_settings_export(nfs_settings_export, zone=zone)



Modify the default values for NFS exports. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_settings_export = isilon_sdk.v9_2_1.NfsSettingsExportSettings() # NfsSettingsExportSettings | 
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.update_nfs_settings_export(nfs_settings_export, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_settings_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_settings_export** | [**NfsSettingsExportSettings**](NfsSettingsExportSettings.md)|  | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_settings_global**
> update_nfs_settings_global(nfs_settings_global)



Modify the default values for NFS exports. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_settings_global = isilon_sdk.v9_2_1.NfsSettingsGlobalSettings() # NfsSettingsGlobalSettings | 

try:
    api_instance.update_nfs_settings_global(nfs_settings_global)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_settings_global** | [**NfsSettingsGlobalSettings**](NfsSettingsGlobalSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_settings_zone**
> update_nfs_settings_zone(nfs_settings_zone, zone=zone)



Modify the NFS server settings for this zone.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
nfs_settings_zone = isilon_sdk.v9_2_1.NfsSettingsZoneSettings() # NfsSettingsZoneSettings | 
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.update_nfs_settings_zone(nfs_settings_zone, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_settings_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_settings_zone** | [**NfsSettingsZoneSettings**](NfsSettingsZoneSettings.md)|  | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ntp_server**
> update_ntp_server(ntp_server, ntp_server_id)



Modify the key value for an NTP server.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ntp_server = isilon_sdk.v9_2_1.NtpServer() # NtpServer | 
ntp_server_id = 'ntp_server_id_example' # str | Modify the key value for an NTP server.

try:
    api_instance.update_ntp_server(ntp_server, ntp_server_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ntp_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_server** | [**NtpServer**](NtpServer.md)|  | 
 **ntp_server_id** | **str**| Modify the key value for an NTP server. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ntp_settings**
> update_ntp_settings(ntp_settings)



Modify the NTP settings. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ntp_settings = isilon_sdk.v9_2_1.NtpSettingsSettings() # NtpSettingsSettings | 

try:
    api_instance.update_ntp_settings(ntp_settings)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ntp_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ntp_settings** | [**NtpSettingsSettings**](NtpSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_s3_bucket**
> update_s3_bucket(s3_bucket, s3_bucket_id, zone=zone)



Modify bucket. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_bucket = isilon_sdk.v9_2_1.S3Bucket() # S3Bucket | 
s3_bucket_id = 's3_bucket_id_example' # str | Modify bucket. All input fields are optional, but one or more must be supplied.
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.update_s3_bucket(s3_bucket, s3_bucket_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_s3_bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_bucket** | [**S3Bucket**](S3Bucket.md)|  | 
 **s3_bucket_id** | **str**| Modify bucket. All input fields are optional, but one or more must be supplied. | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_s3_log_level**
> update_s3_log_level(s3_log_level)



Set the current S3 service logging level.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_log_level = isilon_sdk.v9_2_1.S3LogLevel() # S3LogLevel | 

try:
    api_instance.update_s3_log_level(s3_log_level)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_s3_log_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_log_level** | [**S3LogLevel**](S3LogLevel.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_s3_settings_global**
> update_s3_settings_global(s3_settings_global)



Modify global S3 bucket settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_settings_global = isilon_sdk.v9_2_1.S3SettingsGlobalSettings() # S3SettingsGlobalSettings | 

try:
    api_instance.update_s3_settings_global(s3_settings_global)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_s3_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_settings_global** | [**S3SettingsGlobalSettings**](S3SettingsGlobalSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_s3_settings_zone**
> update_s3_settings_zone(s3_settings_zone, zone=zone)



Modify the S3 bucket settings for this zone.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
s3_settings_zone = isilon_sdk.v9_2_1.S3SettingsZoneSettings() # S3SettingsZoneSettings | 
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.update_s3_settings_zone(s3_settings_zone, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_s3_settings_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s3_settings_zone** | [**S3SettingsZoneSettings**](S3SettingsZoneSettings.md)|  | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smb_log_level**
> update_smb_log_level(smb_log_level)



Set the current SMB logging level.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_log_level = isilon_sdk.v9_2_1.SmbLogLevel() # SmbLogLevel | 

try:
    api_instance.update_smb_log_level(smb_log_level)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_smb_log_level: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_log_level** | [**SmbLogLevel**](SmbLogLevel.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smb_settings_global**
> update_smb_settings_global(smb_settings_global)



Modify one or more settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_settings_global = isilon_sdk.v9_2_1.SmbSettingsGlobalExtended() # SmbSettingsGlobalExtended | 

try:
    api_instance.update_smb_settings_global(smb_settings_global)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_smb_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_settings_global** | [**SmbSettingsGlobalExtended**](SmbSettingsGlobalExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smb_settings_share**
> update_smb_settings_share(smb_settings_share, zone=zone)



Modify one or more settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_settings_share = isilon_sdk.v9_2_1.SmbSettingsShareExtended() # SmbSettingsShareExtended | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.update_smb_settings_share(smb_settings_share, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_smb_settings_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_settings_share** | [**SmbSettingsShareExtended**](SmbSettingsShareExtended.md)|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smb_settings_zone**
> update_smb_settings_zone(smb_settings_zone, zone=zone)



Modify one or more settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_settings_zone = isilon_sdk.v9_2_1.SmbSettingsZoneSettings() # SmbSettingsZoneSettings | 
zone = 'zone_example' # str | Name of the access zone (optional)

try:
    api_instance.update_smb_settings_zone(smb_settings_zone, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_smb_settings_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_settings_zone** | [**SmbSettingsZoneSettings**](SmbSettingsZoneSettings.md)|  | 
 **zone** | **str**| Name of the access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smb_share**
> update_smb_share(smb_share, smb_share_id, zone=zone)



Modify share. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
smb_share = isilon_sdk.v9_2_1.SmbShare() # SmbShare | 
smb_share_id = 'smb_share_id_example' # str | Modify share. All input fields are optional, but one or more must be supplied.
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.update_smb_share(smb_share, smb_share_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_share** | [**SmbShare**](SmbShare.md)|  | 
 **smb_share_id** | **str**| Modify share. All input fields are optional, but one or more must be supplied. | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snmp_settings**
> update_snmp_settings(snmp_settings)



Modify the SNMP settings. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
snmp_settings = isilon_sdk.v9_2_1.SnmpSettingsExtended() # SnmpSettingsExtended | 

try:
    api_instance.update_snmp_settings(snmp_settings)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_snmp_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_settings** | [**SnmpSettingsExtended**](SnmpSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ssh_settings**
> update_ssh_settings(ssh_settings)



ssh settings

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ssh_settings = isilon_sdk.v9_2_1.SshSettingsSettings() # SshSettingsSettings | 

try:
    api_instance.update_ssh_settings(ssh_settings)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_ssh_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_settings** | [**SshSettingsSettings**](SshSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_swift_account**
> update_swift_account(swift_account, swift_account_id, zone=zone)



Modify a Swift account

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.ProtocolsApi(isilon_sdk.v9_2_1.ApiClient(configuration))
swift_account = isilon_sdk.v9_2_1.SwiftAccount() # SwiftAccount | 
swift_account_id = 'swift_account_id_example' # str | Modify a Swift account
zone = 'zone_example' # str | Access zone which contains Swift account. (optional)

try:
    api_instance.update_swift_account(swift_account, swift_account_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_swift_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **swift_account** | [**SwiftAccount**](SwiftAccount.md)|  | 
 **swift_account_id** | **str**| Modify a Swift account | 
 **zone** | **str**| Access zone which contains Swift account. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

