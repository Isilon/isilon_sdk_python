# SmbSettingsShareSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_based_enumeration** | **bool** | Only enumerate files and folders the requesting user has access to. | [optional] 
**access_based_enumeration_root_only** | **bool** | Access-based enumeration on only the root directory of the share. | [optional] 
**allow_delete_readonly** | **bool** | Allow deletion of read-only files in the share. | [optional] 
**allow_execute_always** | **bool** | Allows users to execute files they have read rights for. | [optional] 
**change_notify** | **str** | Specify level of change notification alerts on the share. | [optional] 
**create_permissions** | **str** | Set the create permissions for new files and directories in share. | [optional] 
**csc_policy** | **str** | Client-side caching policy for the shares. | [optional] 
**directory_create_mask** | **int** | Unix umask or mode bits. | [optional] 
**directory_create_mode** | **int** | Unix umask or mode bits. | [optional] 
**file_create_mask** | **int** | Unix umask or mode bits. | [optional] 
**file_create_mode** | **int** | Unix umask or mode bits. | [optional] 
**hide_dot_files** | **bool** | Hide files and directories that begin with a period &#39;.&#39;. | [optional] 
**host_acl** | **list[str]** | An ACL expressing which hosts are allowed access. A deny clause must be the final entry. | [optional] 
**impersonate_guest** | **str** | Specify the condition in which user access is done as the guest account. | [optional] 
**impersonate_user** | **str** | User account to be used as guest account. | [optional] 
**mangle_byte_start** | **int** | Specifies the wchar_t starting point for automatic byte mangling. | [optional] 
**mangle_map** | **list[str]** | Character mangle map. | [optional] 
**ntfs_acl_support** | **bool** | Support NTFS ACLs on files and directories. | [optional] 
**oplocks** | **bool** | Allow oplock requests. | [optional] 
**strict_flush** | **bool** | Handle SMB flush operations. | [optional] 
**strict_locking** | **bool** | Specifies whether byte range locks contend against SMB I/O. | [optional] 
**zone** | **str** | Name of the access zone in which to update settings | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


