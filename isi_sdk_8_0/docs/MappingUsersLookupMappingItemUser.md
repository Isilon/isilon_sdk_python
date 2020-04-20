# MappingUsersLookupMappingItemUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** | Specifies the distinguished name for the user. | [optional] 
**dns_domain** | **str** | Specifies the DNS domain. | [optional] 
**domain** | **str** | Specifies the domain that the object is part of. | [optional] 
**email** | **str** | Specifies an email address. | [optional] 
**enabled** | **bool** | True, if the authenticated user is enabled. | 
**expired** | **bool** | True, if the authenticated user has expired. | 
**expiry** | **int** | Specifies the Unix Epoch time at which the authenticated user will expire. | [optional] 
**gecos** | **str** | Specifies the GECOS value, which is usually the full name. | [optional] 
**generated_gid** | **bool** | True, if the GID was generated. | [optional] 
**generated_uid** | **bool** | True, if the UID was generated. | [optional] 
**generated_upn** | **bool** | True, if the UPN was generated. | [optional] 
**gid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**home_directory** | **str** | Specifies a home directory for the user. | [optional] 
**id** | **str** | Specifies the user or group ID. | 
**locked** | **bool** | If true, indicates that the account is locked. | 
**max_password_age** | **int** | Specifies the maximum time in seconds allowed before the password expires. | [optional] 
**member_of** | [**list[GroupMember]**](GroupMember.md) |  | [optional] 
**name** | **str** | Specifies a user or group name. | 
**on_disk_group_identity** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**on_disk_user_identity** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**password_expired** | **bool** | If true, the password has expired. | 
**password_expires** | **bool** | If true, the password is allowed to expire. | 
**password_expiry** | **int** | Specifies the time in Unix Epoch seconds that the password will expire. | [optional] 
**password_last_set** | **int** | Specifies the last time the password was set. | [optional] 
**primary_group_sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**prompt_password_change** | **bool** | Prompts the user to change their password at the next login. | 
**provider** | **str** | Specifies the authentication provider that the object belongs to. | [optional] 
**sam_account_name** | **str** | Specifies a user or group name. | [optional] 
**shell** | **str** | Specifies a path to the shell for the user. | [optional] 
**sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**type** | **str** | Specifies the object type. | 
**uid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**upn** | **str** | Specifies a principal name for the user. | [optional] 
**user_can_change_password** | **bool** | Specifies whether the password for the user can be changed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


