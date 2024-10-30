# ChangelistEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atime** | [**ChangelistEntryAtime**](ChangelistEntryAtime.md) |  | [optional] 
**btime** | [**ChangelistEntryAtime**](ChangelistEntryAtime.md) |  | [optional] 
**change_types** | **list[str]** | The types of change for this entry. | [optional] 
**ctime** | [**ChangelistEntryAtime**](ChangelistEntryAtime.md) |  | [optional] 
**data_pool** | **int** | The data disk pool ID of the file associated with the entry. | 
**diff_regions** | [**list[ChangelistsChangelistDiffRegionsDiffRegion]**](ChangelistsChangelistDiffRegionsDiffRegion.md) | Changed regions of the file | [optional] 
**file_type** | **str** | Type of file. | 
**gid** | **int** | The Group ID defined flags of the file associated with the entry. | 
**id** | **str** | The ID of the changelist entry. | 
**lin** | **int** | The LIN number of the file associated with the entry. | 
**metadata_pool** | **int** | The metadata disk pool ID of the file associated with the entry. | 
**mtime** | [**ChangelistEntryAtime**](ChangelistEntryAtime.md) |  | [optional] 
**num_diff_regions** | **int** | Number of changed regions stored in the diff_regions array. A value of 4294967295 indicates that diff_regions contains a truncated list of changed regions, and a full list must be obtained from another handler. | [optional] 
**parent_lin** | **int** | The Parent LIN number of the file associated with the entry. | 
**path** | **str** | The relative path to the file associated with the entry. | 
**physical_size** | **int** | The physical size of the file associated with the entry. | 
**size** | **int** | The size of the file associated with the entry. | 
**uid** | **int** | The User ID flags of the file associated with the entry. | 
**user_flags** | **list[str]** | The user defined flags of the file associated with the entry. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


