# SettingsGlobalGlobalSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alloc_retries** | **int** | Sets number of times to retry an ID allocation before failing. | [optional] 
**cache_cred_lifetime** | **int** | Sets length of time in seconds to cache credential responses from the ID mapper. | [optional] 
**cache_id_lifetime** | **int** | Sets length of time in seconds to cache ID responses from the ID mapper. | [optional] 
**gid_range_enabled** | **bool** | Enables use of a fixed range for allocating GIDs. | [optional] 
**gid_range_max** | **int** | Specifies ending number for allocating GIDs. | [optional] 
**gid_range_min** | **int** | Specifies starting number for allocating GIDs. | [optional] 
**gid_range_next** | **int** | Specifies the next GID to be allocated. | [optional] 
**group_uid** | **int** |  | [optional] 
**load_providers** | **list[str]** |  | [optional] 
**min_mapped_rid** | **int** |  | [optional] 
**null_gid** | **int** |  | [optional] 
**null_uid** | **int** |  | [optional] 
**on_disk_identity** | **str** | Specifies type of identity stored on disk. | [optional] 
**rpc_block_time** | **int** |  | [optional] 
**rpc_max_requests** | **int** |  | [optional] 
**rpc_timeout** | **int** |  | [optional] 
**send_ntlmv2** | **bool** | Specifies whether to send NTLMv2 responses. | [optional] 
**space_replacement** | **str** | Sets space replacement. | [optional] 
**system_gid_threshold** | **int** |  | [optional] 
**system_uid_threshold** | **int** |  | [optional] 
**uid_range_enabled** | **bool** | Uses a fixed range for allocating UIDs. | [optional] 
**uid_range_max** | **int** | Specifies ending number for allocating UIDs. | [optional] 
**uid_range_min** | **int** | Specifies starting number for allocating UIDs. | [optional] 
**uid_range_next** | **int** | Specifies the next UID to be allocated. | [optional] 
**unknown_gid** | **int** | Specifies GID to use for the unknown (anonymous) group. | [optional] 
**unknown_uid** | **int** | Specifies UID to use for the unknown (anonymous) user. | [optional] 
**workgroup** | **str** | Sets NetBIOS workgroup/domain. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


