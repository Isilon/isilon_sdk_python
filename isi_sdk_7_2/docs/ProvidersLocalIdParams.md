# ProvidersLocalIdParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Enables use of provider for authentication as well as identity. | [optional] 
**create_home_directory** | **bool** | Automatically create home directory on first login. | [optional] 
**home_directory_template** | **str** | Specifies home directory template path. | [optional] 
**lockout_duration** | **int** | Sets length of time in seconds that an account will be inaccessible after multiple failed login attempts. | [optional] 
**lockout_threshold** | **int** | Sets the number of failed login attempts necessary for an account to be locked out. | [optional] 
**lockout_window** | **int** | Sets the time in seconds in which lockout_threshold failed attempts must be made for an account to be locked out. | [optional] 
**login_shell** | **str** | Sets login shell path. | [optional] 
**machine_name** | **str** | Specifies domain used to qualify user and group names for this provider. | [optional] 
**max_password_age** | **int** | Sets maximum password age in seconds. | [optional] 
**min_password_age** | **int** | Sets minimum password age in seconds. | [optional] 
**min_password_length** | **int** | Sets minimum password length. | [optional] 
**name** | **str** | Specifies local provider name. | [optional] 
**password_complexity** | **list[str]** | List of cases required in a password. Options are lowercase, uppercase, numeric and symbol | [optional] 
**password_history_length** | **int** | The number of previous passwords to store. | [optional] 
**password_prompt_time** | **int** | Specifies time in seconds remaining before prompting for password change. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


