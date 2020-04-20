# MappingUsersLookupMappingItemUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** |  | [optional] 
**dns_domain** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**email** | **str** | Specifies an Email address. | [optional] 
**enabled** | **bool** | Auth user is enabled. | 
**expired** | **bool** | Auth user is expired. | 
**expiry** | **int** | Epoch time at which the auth user will expire. | [optional] 
**gecos** | **str** | Sets GECOS value (usually full name). | [optional] 
**generated_gid** | **bool** |  | [optional] 
**generated_uid** | **bool** |  | [optional] 
**generated_upn** | **bool** |  | [optional] 
**gid** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**home_directory** | **str** | Specifies user&#39;s home directory. | [optional] 
**id** | **str** | The user or group ID. | 
**locked** | **bool** | Specifies if account is locked out. | 
**max_password_age** | **int** | The maximum age in seconds allowed for the password before it expires. | [optional] 
**member_of** | [**list[GroupMember]**](GroupMember.md) |  | [optional] 
**name** | **str** | A user or group name. | 
**on_disk_group_identity** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**on_disk_user_identity** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**password_expired** | **bool** | Specifies whether the password has expired. | 
**password_expires** | **bool** | Password is allowed to expire. | 
**password_expiry** | **int** | Specifies the time in epoch seconds the password will expire. | [optional] 
**password_last_set** | **int** | Specifies the last time the password was set. | [optional] 
**primary_group_sid** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**prompt_password_change** | **bool** | Prompts the user to change their password on next login. | 
**provider** | **str** | Specifies an authentication provider. | [optional] 
**sam_account_name** | **str** |  | [optional] 
**shell** | **str** | Sets path to user&#39;s shell. | [optional] 
**sid** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**type** | **str** |  | 
**uid** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**upn** | **str** | The user principal name. | [optional] 
**user_can_change_password** | **bool** | Specifies whether the user&#39;s password can be changed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


