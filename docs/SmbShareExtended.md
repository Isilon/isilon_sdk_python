# SmbShareExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_based_enumeration** | **bool** | Only enumerate files and folders the requesting user has access to. | [optional] 
**access_based_enumeration_root_only** | **bool** | Access-based enumeration on only the root directory of the share. | [optional] 
**allow_delete_readonly** | **bool** | Allow deletion of read-only files in the share. | [optional] 
**allow_execute_always** | **bool** | Allows users to execute files they have read rights for. | [optional] 
**allow_variable_expansion** | **bool** | Allow automatic expansion of variables for home directories. | [optional] 
**auto_create_directory** | **bool** | Automatically create home directories. | [optional] 
**browsable** | **bool** | Share is visible in net view and the browse list. | [optional] 
**ca_timeout** | **int** | Persistent open timeout for the share. | [optional] 
**ca_write_integrity** | **str** | Specify the level of write-integrity on continuously available shares. | [optional] 
**change_notify** | **str** | Level of change notification alerts on the share. | [optional] 
**continuously_available** | **bool** | Specify if persistent opens are allowed on the share. | [optional] 
**create_permissions** | **str** | Create permissions for new files and directories in share. | [optional] 
**csc_policy** | **str** | Client-side caching policy for the shares. | [optional] 
**description** | **str** | Description for this SMB share. | [optional] 
**directory_create_mask** | **int** | Directory create mask bits. | [optional] 
**directory_create_mode** | **int** | Directory create mode bits. | [optional] 
**file_create_mask** | **int** | File create mask bits. | [optional] 
**file_create_mode** | **int** | File create mode bits. | [optional] 
**file_filter_extensions** | **list[str]** | Specifies the list of file extensions. | [optional] 
**file_filter_type** | **str** | Specifies if filter list is for deny or allow. Default is deny. | [optional] 
**file_filtering_enabled** | **bool** | Enables file filtering on this zone. | [optional] 
**hide_dot_files** | **bool** | Hide files and directories that begin with a period &#39;.&#39;. | [optional] 
**host_acl** | **list[str]** | An ACL expressing which hosts are allowed access. A deny clause must be the final entry. | [optional] 
**id** | **str** | Share ID. | 
**impersonate_guest** | **str** | Specify the condition in which user access is done as the guest account. | [optional] 
**impersonate_user** | **str** | User account to be used as guest account. | [optional] 
**inheritable_path_acl** | **bool** | Set the inheritable ACL on the share path. | [optional] 
**mangle_byte_start** | **int** | Specifies the wchar_t starting point for automatic byte mangling. | [optional] 
**mangle_map** | **list[str]** | Character mangle map. | [optional] 
**name** | **str** | Share name. | 
**ntfs_acl_support** | **bool** | Support NTFS ACLs on files and directories. | [optional] 
**oplocks** | **bool** | Support oplocks. | [optional] 
**path** | **str** | Path of share within /ifs. | 
**permissions** | [**list[SmbSharePermission]**](SmbSharePermission.md) | Specifies an ordered list of permission modifications. | [optional] 
**run_as_root** | [**list[GroupMember]**](GroupMember.md) | Allow account to run as root. | [optional] 
**strict_ca_lockout** | **bool** | Specifies if persistent opens would do strict lockout on the share. | [optional] 
**strict_flush** | **bool** | Handle SMB flush operations. | [optional] 
**strict_locking** | **bool** | Specifies whether byte range locks contend against SMB I/O. | [optional] 
**zid** | **int** | Numeric ID of the access zone which contains this SMB share | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


