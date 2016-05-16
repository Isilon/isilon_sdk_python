# WormDomainCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autocommit_offset** | **int** | Specifies the autocommit time period for the domain in seconds.  After a file is in the domain without being modified for the specified time period, the file is automatically committed. If this parameter is set to null, there is no autocommit time, and files must be committed manually. | [optional] 
**default_retention** | **int** | Specifies the default amount of time, in seconds, that a file in this domain will be protected for. The default retention period is applied if no retention date is manually set on the file. This parameter can also be set to &#39;forever&#39;, &#39;use_min&#39; (which applies the &#39;min_retention&#39; option), or &#39;use_max&#39; (which applies the &#39;max_retention&#39; option). | [optional] 
**max_retention** | **int** | Specifies the maximum amount of time, in seconds, that a file in this domain will be protected. This setting will override the retention period of any file committed with a longer retention period. If this parameter is set to null, an infinite length retention period is set. | [optional] 
**min_retention** | **int** | Specifies the minimum amount of time, in seconds, that a file in this domain will be protected. This setting will override the retention period of any file committed with a shorter retention period. If this parameter is set to null, this minimum value is not enforced. This parameter can also be set to &#39;forever&#39;. | [optional] 
**override_date** | **int** | Specifies the override retention date for the domain. If this date is later than the retention date for any committed file, the file will remain protected until the override retention date. | [optional] 
**privileged_delete** | **str** | When this value is set to &#39;on&#39;, files in this domain can be deleted through the privileged delete feature. If this value is set to &#39;disabled&#39;, privileged file deletes are permanently disabled and cannot be turned on again. | [optional] 
**type** | **str** | Specifies whether the domain is an enterprise domain or a compliance domain. Compliance domains can not be created on enterprise clusters. Enterprise and compliance domains can be created on compliance clusters. | [optional] 
**path** | **str** | Specifies the root path of this domain. Files in this directory and all sub-directories will be protected. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


