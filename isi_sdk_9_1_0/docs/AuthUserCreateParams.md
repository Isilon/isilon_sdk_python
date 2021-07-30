# AuthUserCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Specifies an email address for the user. | [optional] 
**enabled** | **bool** | If true, the authenticated user is enabled. | [optional] 
**expiry** | **int** | Specifies the Unix Epoch time when the auth user will expire. | [optional] 
**gecos** | **str** | Specifies the GECOS value, which is usually the full name. | [optional] 
**home_directory** | **str** | Specifies a home directory for the user. | [optional] 
**password** | **str** | Changes the password for the user. | [optional] 
**password_expires** | **bool** | If true, the password should expire. | [optional] 
**primary_group** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**prompt_password_change** | **bool** | If true, prompts the user to change their password at the next login. | [optional] 
**shell** | **str** | Specifies the shell for the user. | [optional] 
**sid** | **str** | Specifies a security identifier. | [optional] 
**uid** | **int** | Specifies a numeric user identifier. | [optional] 
**unlock** | **bool** | If true, the user account should be unlocked. | [optional] 
**name** | **str** | Specifies a user name. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


