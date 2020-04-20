# AuthUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Specifies an Email address. | [optional] 
**enabled** | **bool** | Auth user is enabled. | [optional] 
**expiry** | **int** | Epoch time at which the auth user will expire. | [optional] 
**gecos** | **str** | Sets GECOS value (usually full name). | [optional] 
**home_directory** | **str** | Specifies user&#39;s home directory. | [optional] 
**password** | **str** | Changes user&#39;s password. | [optional] 
**password_expires** | **bool** | Specifies whether the password expires. | [optional] 
**primary_group** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**prompt_password_change** | **bool** | Prompts the user to change their password on next login. | [optional] 
**shell** | **str** | Specifies the user&#39;s shell. | [optional] 
**sid** | **str** | A security identifier. | [optional] 
**uid** | **int** | A numeric user identifier. | [optional] 
**unlock** | **bool** | Unlocks the user&#39;s account if locked. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


