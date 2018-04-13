# ProvidersLocalIdParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | If true, enables authentication and identity management through the authentication provider. | [optional] 
**create_home_directory** | **bool** | Automatically creates the home directory on the first login. | [optional] 
**home_directory_template** | **str** | Specifies the path to the home directory template. | [optional] 
**lockout_duration** | **int** | Specifies the length of time in seconds that an account will be inaccessible after multiple failed login attempts. | [optional] 
**lockout_threshold** | **int** | Specifies the number of failed login attempts necessary before an account is locked. | [optional] 
**lockout_window** | **int** | Specifies the duration of time in seconds in which the number of failed attempts set in the &#39;lockout_threshold&#39; parameter must be made before an account is locked. | [optional] 
**login_shell** | **str** | Specifies the login shell path. | [optional] 
**machine_name** | **str** | Specifies the domain for this provider through which users and groups are qualified. | [optional] 
**max_password_age** | **int** | Specifies the maximum password age in seconds. | [optional] 
**min_password_age** | **int** | Specifies the minimum password age in seconds. | [optional] 
**min_password_length** | **int** | Specifies the minimum password length. | [optional] 
**name** | **str** | Specifies the local provider name. | [optional] 
**password_complexity** | **list[str]** | Specifies the conditions required for a password. | [optional] 
**password_history_length** | **int** | Specifies the number of previous passwords to store. | [optional] 
**password_prompt_time** | **int** | Specifies the time in seconds remaining before a user will be prompted for a password change. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


