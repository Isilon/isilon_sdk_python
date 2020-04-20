# SmbSettingsGlobalExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_based_share_enum** | **bool** | Only enumerate files and folders the requesting user has access to. | [optional] 
**audit_fileshare** | **str** | Specify level of file share audit events to log. | [optional] 
**audit_global_sacl** | [**list[SmbSettingsGlobalSettingsAuditGlobalSaclItem]**](SmbSettingsGlobalSettingsAuditGlobalSaclItem.md) | List of permissions to audit. | [optional] 
**audit_logon** | **str** | Specify the level of logon audit events to log. | [optional] 
**dot_snap_accessible_child** | **bool** | Allow access to .snapshot directories in share subdirectories. | [optional] 
**dot_snap_accessible_root** | **bool** | Allow access to the .snapshot directory in the root of the share. | [optional] 
**dot_snap_visible_child** | **bool** | Show .snapshot directories in share subdirectories. | [optional] 
**dot_snap_visible_root** | **bool** | Show the .snapshot directory in the root of a share. | [optional] 
**enable_security_signatures** | **bool** | Indicates whether the server supports signed SMB packets. | [optional] 
**guest_user** | **str** | Specifies the fully-qualified user to use for guest access. | [optional] 
**ignore_eas** | **bool** | Specify whether to ignore EAs on files. | [optional] 
**onefs_cpu_multiplier** | **int** | Specify the number of OneFS driver worker threads per CPU. | [optional] 
**onefs_num_workers** | **int** | Set the maximum number of OneFS driver worker threads. | [optional] 
**require_security_signatures** | **bool** | Indicates whether the server requires signed SMB packets. | [optional] 
**server_string** | **str** | Provides a description of the server. | [optional] 
**service** | **bool** | Specify whether service is enabled. | [optional] 
**srv_cpu_multiplier** | **int** | Specify the number of SRV service worker threads per CPU. | [optional] 
**srv_num_workers** | **int** | Set the maximum number of SRV service worker threads. | [optional] 
**support_multichannel** | **bool** | Support multichannel. | [optional] 
**support_netbios** | **bool** | Support NetBIOS. | [optional] 
**support_smb2** | **bool** | Support the SMB2 protocol on the server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


