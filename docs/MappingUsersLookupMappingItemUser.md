# MappingUsersLookupMappingItemUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** | Specifies the distinguished name for the user. | 
**dns_domain** | **str** | Specifies the DNS domain. | 
**domain** | **str** | Specifies the domain that the object is part of. | 
**email** | **str** | Specifies an email address. | 
**enabled** | **bool** | True, if the authenticated user is enabled. | 
**expired** | **bool** | True, if the authenticated user has expired. | 
**expiry** | **int** | Specifies the Unix Epoch time at which the authenticated user will expire. | 
**gecos** | **str** | Specifies the GECOS value, which is usually the full name. | 
**generated_gid** | **bool** | True, if the GID was generated. | 
**generated_uid** | **bool** | True, if the UID was generated. | 
**generated_upn** | **bool** | True, if the UPN was generated. | 
**gid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | 
**home_directory** | **str** | Specifies a home directory for the user. | 
**id** | **str** | Specifies the user or group ID. | 
**locked** | **bool** | If true, indicates that the account is locked. | 
**max_password_age** | **int** | Specifies the maximum time in seconds allowed before the password expires. | 
**member_of** | [**list[GroupMember]**](GroupMember.md) |  | 
**name** | **str** | Specifies a user or group name. | 
**on_disk_group_identity** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | 
**on_disk_user_identity** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | 
**password_expired** | **bool** | If true, the password has expired. | 
**password_expires** | **bool** | If true, the password is allowed to expire. | 
**password_expiry** | **int** | Specifies the time in Unix Epoch seconds that the password will expire. | 
**password_last_set** | **int** | Specifies the last time the password was set. | 
**primary_group_sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | 
**prompt_password_change** | **bool** | Prompts the user to change their password at the next login. | 
**provider** | **str** | Specifies the authentication provider that the object belongs to. | 
**sam_account_name** | **str** | Specifies a user or group name. | 
**shell** | **str** | Specifies a path to the shell for the user. | 
**sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | 
**type** | **str** | Specifies the object type. | 
**uid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | 
**upn** | **str** | Specifies a principal name for the user. | 
**user_can_change_password** | **bool** | Specifies whether the password for the user can be changed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


