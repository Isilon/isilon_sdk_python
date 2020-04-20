# WormDomainExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autocommit_offset** | **int** | The autocommit time period in seconds for the domain.  After a file exists in this domain without being modified for the specified time period, the file is automatically committed the next time the file is accessed.  If null, there is no autocommit time so files must be manually committed. | [optional] 
**default_retention** | **str** |  | [optional] 
**max_retention** | **str** |  | [optional] 
**min_retention** | **str** |  | [optional] 
**override_date** | **int** | Override retention date for the domain.  If this date is later than any committed file&#39;s own retention date, that file will remain protected beyond its own retention date until this date. | [optional] 
**privileged_delete** | **str** | If &#39;on&#39;, files in this domain can be deleted using the privileged delete feature.  Otherwise, they can&#39;t be deleted even with privileged delete.  If &#39;disabled&#39;, privileged file deletes are permanently disabled and cannot be turned back on again. | 
**type** | **str** | Whether this is an enterprise domain or this is a compliance domain. Compliance domains may not be created on enterprise clusters. Enterprise and compliance domains may be created on compliance clusters. | 
**id** | **int** | System-assigned ID of this protection domain. | 
**incomplete** | **bool** | If true, OneFS is still in the process of creating this domain and it is not yet preventing files from being modified or deleted.  If false, the domain is fully created and operational. | 
**lin** | **int** | Logical inode number (LIN) for the root of this domain. | 
**max_modifies** | **int** | Maximum number of times a WORM domain can be modified over its lifetime. | 
**path** | **str** | Root path of this domain.  Files in this directory and all sub-directories will be protected. | 
**total_modifies** | **int** | The number of times this domain has been modified (had its domain attributes changed) so far.  A WORM domain can be modified a fixed number of times over its lifetime defined by max_modifies. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


