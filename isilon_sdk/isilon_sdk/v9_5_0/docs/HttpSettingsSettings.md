# HttpSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control** | **bool** | Enable Access Control Authentication for HTTP service. | [optional] 
**basic_authentication** | **bool** | Enable Basic Authentication for HTTP service. | [optional] 
**dav** | **bool** | Enable DAV specification for HTTP service. | [optional] 
**enable_access_log** | **bool** | Enable HTTP access logging for HTTP service. | [optional] 
**httpd_controlpath_redirect** | **bool** | Enable or disable WebUI redirect to HTTP service. | [optional] 
**https** | **bool** | Use HTTPS transport for HTTP service. | [optional] 
**inactive_timeout** | **int** | Get the HTTP RequestReadTimeout directive from both WebUI and HTTP service. | 
**integrated_authentication** | **bool** | Enable Integrated Authentication for HTTP service. | [optional] 
**server_root** | **str** | Document root directory for HTTP service. Must be within /ifs. | [optional] 
**service** | **str** | Enable/disable the HTTP service or redirect to WebUI or disabled BasicFileAccess. | [optional] 
**service_timeout** | **int** | Get the HTTP Timeout directive from Apache. Value 0 means service timeout is disabled. | 
**session_max_age** | **int** | Get the HTTP SessionMaxAge directive from both WebUI and HTTP service. | 
**webhdfs_ran_https_port** | **int** | Configure Data Services Port for HTTP service. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


