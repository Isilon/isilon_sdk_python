# MappingUsersLookupMappingItemUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_when_inactive** | **bool** | The user account will be disabled when inactive beyond a period of time. | [optional] 
**dn** | **str** |  | [optional] 
**dns_domain** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**enabled** | **bool** | True, if the authenticated user is enabled. | 
**expired** | **bool** | True, if the authenticated user has expired. | 
**expiry** | **int** |  | [optional] 
**gecos** | **str** |  | [optional] 
**generated_gid** | **bool** | True, if the GID was generated. | [optional] 
**generated_uid** | **bool** | True, if the UID was generated. | [optional] 
**generated_upn** | **bool** | True, if the UPN was generated. | [optional] 
**gid** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**home_directory** | **str** |  | [optional] 
**id** | **str** | Specifies the user or group ID. | 
**last_logon** | **int** |  | [optional] 
**locked** | **bool** | If true, indicates that the account is locked. | 
**max_password_age** | **int** | Specifies the maximum time in seconds allowed before the password expires. | [optional] 
**member_of** | [**list[AuthAccessAccessItemFileGroup]**](AuthAccessAccessItemFileGroup.md) |  | [optional] 
**name** | **str** | Specifies a user or group name. | 
**object_history** | [**list[AuthGroupObjectHistoryItem]**](AuthGroupObjectHistoryItem.md) |  | [optional] 
**on_disk_group_identity** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**on_disk_user_identity** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**password_expired** | **bool** | If true, the password has expired. | 
**password_expires** | **bool** | If true, the password is allowed to expire. | 
**password_expiry** | **int** |  | [optional] 
**password_last_set** | **int** |  | [optional] 
**primary_group_sid** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**prompt_password_change** | **bool** | Prompts the user to change their password at the next login. | 
**provider** | **str** |  | [optional] 
**sam_account_name** | **str** |  | [optional] 
**shell** | **str** |  | [optional] 
**sid** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**ssh_public_keys** | **list[str]** | Specifies the user&#39;s LDAP SSH Public Key. | [optional] 
**type** | **str** | Specifies the object type. | 
**uid** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**upn** | **str** |  | [optional] 
**user_can_change_password** | **bool** | Specifies whether the password for the user can be changed. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


