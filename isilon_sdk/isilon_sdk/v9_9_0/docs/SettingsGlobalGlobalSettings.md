# SettingsGlobalGlobalSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alloc_retries** | **int** | Specifies the number of times to retry an ID allocation before failing. | [optional] 
**concurrent_session_limit** | **int** | Specifies the total number of concurrent administrative sessions. | [optional] 
**default_ldap_tls_revocation_check_level** | **str** | This setting controls the default behavior of the certificate revocation checking algorithm when the LDAP provider is presented with a digital certificate by an LDAP server. | [optional] 
**failed_login_delay_time** | **int** | Specifies the delay in seconds following a failed login/authentication attempt. | [optional] 
**gid_range_enabled** | **bool** | If true, allocates GIDs from a fixed range. | [optional] 
**gid_range_max** | **int** | Specifies the ending number for a fixed range from which GIDs are allocated. | [optional] 
**gid_range_min** | **int** | Specifies the starting number for a fixed range from which GIDs are allocated. | [optional] 
**gid_range_next** | **int** | Specifies the next GID to allocate. | [optional] 
**group_uid** | **int** | Specifies the user iD for a group when requested by the kernel. | [optional] 
**load_providers** | **list[str]** | Specifies which providers are loaded by the authentication daemon (lsassd). | [optional] 
**min_mapped_rid** | **int** | Starts the RID in the local domain to map a UID and a GID. | [optional] 
**null_gid** | **int** | Specifies an alternative GID when the kernel is unable to retrieve a GID for a persona. | [optional] 
**null_uid** | **int** | Specifies an alternative UID when the kernel is unable to retrieve a UID for a persona. | [optional] 
**on_disk_identity** | **str** | Specifies the type of identity that is stored on disk. | [optional] 
**rpc_block_time** | **int** | Specifies the minimum amount of time in milliseconds to wait before performing an oprestart. | [optional] 
**rpc_max_requests** | **int** | Specifies the maximum number of outstanding RPC requests. | [optional] 
**rpc_timeout** | **int** | Specifies the maximum amount of time in seconds to wait for an idmap response. | [optional] 
**send_ntlmv2** | **bool** | If true, sends NTLMv2 responses. | [optional] 
**space_replacement** | **str** | Specifies the space replacement character. | [optional] 
**system_gid_threshold** | **int** | Specifies the minimum GID to attempt to look up in the idmap database. | [optional] 
**system_uid_threshold** | **int** | Specifies the minimum UID to attempt to look up in the idmap database. | [optional] 
**uid_range_enabled** | **bool** | If true, allocates UIDs from a fixed range. | [optional] 
**uid_range_max** | **int** | Specifies the ending number for a fixed range from which UIDs are allocated. | [optional] 
**uid_range_min** | **int** | Specifies the starting number for a fixed range from which UIDs are allocated. | [optional] 
**uid_range_next** | **int** | Specifies the next UID to allocate. | [optional] 
**unknown_gid** | **int** | Specifies the GID for the unknown (anonymous) group. | [optional] 
**unknown_uid** | **int** | Specifies the UID for the unknown (anonymous) user. | [optional] 
**user_object_cache_size** | **int** | Specifies the maximum size (in bytes) of the security object cache in the authentication daemon. | [optional] 
**workgroup** | **str** | Specifies the NetBIOS workgroup or domain. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


