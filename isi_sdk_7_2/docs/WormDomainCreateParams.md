# WormDomainCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autocommit_offset** | **int** | The autocommit time period in seconds for the domain.  After a file exists in this domain without being modified for the specified time period, the file is automatically committed the next time the file is accessed.  If null, there is no autocommit time so files must be manually committed. | [optional] 
**default_retention** | **str** |  | [optional] 
**max_retention** | **str** |  | [optional] 
**min_retention** | **str** |  | [optional] 
**override_date** | **int** | Override retention date for the domain.  If this date is later than any committed file&#39;s own retention date, that file will remain protected beyond its own retention date until this date. | [optional] 
**privileged_delete** | **str** | If &#39;on&#39;, files in this domain can be deleted using the privileged delete feature.  Otherwise, they can&#39;t be deleted even with privileged delete.  If &#39;disabled&#39;, privileged file deletes are permanently disabled and cannot be turned back on again. | [optional] 
**type** | **str** | Whether this is an enterprise domain or this is a compliance domain. Compliance domains may not be created on enterprise clusters. Enterprise and compliance domains may be created on compliance clusters. | [optional] 
**path** | **str** | Root path of this domain.  Files in this directory and all sub-directories will be protected. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


