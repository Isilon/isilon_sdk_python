# ProvidersDuoSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autopush** | **bool** | Specifies if Duo automatically sends a push login request to the users phone. | 
**enabled** | **bool** | Specifies if the Duo provider is enabled. | 
**failmode** | **str** | Specifies if Duo will fail \&quot;safe\&quot; (allow access) or \&quot;secure\&quot; (deny access) on configuration or service errors. | 
**fallback_local_ip** | **bool** | Specifies if Duo will report the server IP if the client IP cannot be detected. | 
**groups** | **str** | Specifies a list of groups Duo is required for (default is all groups). | 
**host** | **str** | Specifies the API hostname. | 
**http_proxy** | **str** | Specifies the HTTP proxy to use. | 
**https_timeout** | **int** | Specifies the number of seconds to wait for HTTPS responses from Duo Security. | 
**ikey** | **str** | Specifies the integration key. | 
**prompts** | **int** | Specifies the maximum number of authentication prompts to display (1-3 default is 3). | 
**pushinfo** | **bool** | Specifies to include information in the Duo Push message. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


