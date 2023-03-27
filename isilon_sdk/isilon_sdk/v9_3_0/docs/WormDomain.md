# WormDomain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autocommit_offset** | **int** | Specifies the autocommit time period for the domain in seconds.  After a file is in the domain without being modified for the specified time period, the file is automatically committed. If this parameter is set to null, there is no autocommit time, and files must be committed manually. | [optional] 
**default_retention** | **str** |  | [optional] 
**exclusions** | [**list[WormDomainExclusion]**](WormDomainExclusion.md) | A list of directories excluded from WORM protection. In a POST/PUT request this collection specifies the directories that the user wishes to create SmartLock exclusion directories on underneath this SmartLock directory. In a GET request this collection specifies all of the exclusion directories that exist underneath this SmartLock directory. | [optional] 
**max_retention** | **str** |  | [optional] 
**min_retention** | **str** |  | [optional] 
**override_date** | **int** | Specifies the override retention date for the domain. If this date is later than the retention date for any committed file, the file will remain protected until the override retention date. | [optional] 
**privileged_delete** | **str** | When this value is set to &#39;on&#39;, files in this domain can be deleted through the privileged delete feature. If this value is set to &#39;disabled&#39;, privileged file deletes are permanently disabled and cannot be turned on again. | [optional] 
**set_pending_delete** | **bool** | If true, the domain is irreversibly marked for deletion. This is used for compliance domains and allows compliance store directories to be deleted, while disallowing the creation or committing of new/existing files. | [optional] 
**type** | **str** | Specifies whether the domain is an enterprise domain or a compliance domain. Compliance domains can not be created on enterprise clusters. Enterprise and compliance domains can be created on compliance clusters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


