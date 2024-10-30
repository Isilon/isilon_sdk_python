# NetworkGroupnet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_wildcard_subdomains** | **bool** | If enabled, SmartConnect treats subdomains of known dns zones as the known dns zone. This is required for S3 Virtual Host domains. Defaults to True. | [optional] 
**description** | **str** | A description of the groupnet. | [optional] 
**dns_cache_enabled** | **bool** | DNS caching is enabled or disabled. | [optional] 
**dns_options** | **list[str]** | List of DNS resolver options. | [optional] 
**dns_search** | **list[str]** | List of DNS search suffixes. | [optional] 
**dns_servers** | **list[str]** | List of Domain Name Server IP addresses. | [optional] 
**name** | **str** | The name of the groupnet. | [optional] 
**server_side_dns_search** | **bool** | Enable or disable appending nodes DNS search  list to client DNS inquiries directed at SmartConnect service IP. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


