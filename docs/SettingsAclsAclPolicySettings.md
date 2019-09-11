# SettingsAclsAclPolicySettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | **str** | Access checks (chmod, chown). | [optional] 
**calcmode** | **str** | Displayed mode bits. | [optional] 
**calcmode_group** | **str** | Approximate group mode bits when ACL exists. | [optional] 
**calcmode_owner** | **str** | Approximate owner mode bits when ACL exists. | [optional] 
**calcmode_traverse** | **str** | Require traverse rights in order to traverse directories with existing ACLs. | [optional] 
**chmod** | **str** | chmod on files with existing ACLs. | [optional] 
**chmod_007** | **str** | chmod (007) on files with existing ACLs. | [optional] 
**chmod_inheritable** | **str** | ACLs created on directories by UNIX chmod. | [optional] 
**chown** | **str** | chown/chgrp on files with existing ACLs. | [optional] 
**create_over_smb** | **str** | ACL creation over SMB. | [optional] 
**dos_attr** | **str** |  Read only DOS attribute. | [optional] 
**group_owner_inheritance** | **str** | Group owner inheritance. | [optional] 
**rwx** | **str** | Treatment of &#39;rwx&#39; permissions. | [optional] 
**synthetic_denies** | **str** | Synthetic &#39;deny&#39; ACEs. | [optional] 
**utimes** | **str** | Access check (utimes) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


