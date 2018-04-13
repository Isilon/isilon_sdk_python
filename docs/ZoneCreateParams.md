# ZoneCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_auth_providers** | **bool** | Use all authentication providers available. | [optional] 
**alternate_system_provider** | **str** | Alternate system provider. | [optional] 
**audit_failure** | **list[str]** | List of failed operations to audit. | [optional] 
**audit_success** | **list[str]** | List of successful operations to audit. | [optional] 
**auth_providers** | **list[str]** | List of authentication providers used on this zone. | [optional] 
**cache_size** | **int** | Specifies the maximum size of zone in-memory cache. | [optional] 
**create_path** | **bool** | Create path if it does not exist. | [optional] 
**hdfs_ambari_namenode** | **str** | The SmartConnect name of this cluster that will be used for the HDFS service. | [optional] 
**hdfs_ambari_server** | **str** | A valid hostname, FQDN, IPv4, or IPv6 string of the Ambari server. | [optional] 
**hdfs_authentication** | **str** | Authentication type for HDFS protocol. | [optional] 
**hdfs_odp_version** | **str** | ODP stack repository version number. | [optional] 
**hdfs_root_directory** | **str** | Root directory for HDFS protocol. | [optional] 
**home_directory_umask** | **int** | Permissions set on auto-created user home directories. | [optional] 
**ifs_restricted** | [**list[GroupMember]**](GroupMember.md) | User restrictions for this zone. | [optional] 
**map_untrusted** | **str** | Maps untrusted domains to this NetBIOS domain during authentication. | [optional] 
**name** | **str** | Zone name. | 
**netbios_name** | **str** | NetBIOS name. | [optional] 
**path** | **str** | zone path. | [optional] 
**protocol_audit_enabled** | **bool** | Indicates whether I/O auditing is set on this zone. | [optional] 
**skeleton_directory** | **str** | Skeleton directory for user home directories. | [optional] 
**syslog_audit_events** | **list[str]** | List of audit operations to forward to syslog. | [optional] 
**syslog_forwarding_enabled** | **bool** | Enable syslog forwarding of zone audit events. | [optional] 
**system_provider** | **str** | System provider. | [optional] 
**user_mapping_rules** | **list[str]** | Current ID mapping rules. | [optional] 
**webhdfs_enabled** | **bool** | Indicates whether WebHDFS is enabled on this zone. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


