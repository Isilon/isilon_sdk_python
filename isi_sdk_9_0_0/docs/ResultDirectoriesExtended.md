# ResultDirectoriesExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_count** | **int** | User attribute count. | 
**begin_time** | **int** | Unix Epoch time of start of results collection job. | 
**dir_depth** | **int** | Directory depth. | 
**dir_usage** | [**ResultDirectoriesDirUsageExtended**](ResultDirectoriesDirUsageExtended.md) | Disk usage by the current directory. | 
**path_parts** | **list[str]** | Directory path information from root to current directory. | 
**total_usage** | [**ResultDirectoriesTotalUsage**](ResultDirectoriesTotalUsage.md) | Disk usage from root. | 
**usage_data** | [**list[ResultDirectoriesUsageDataItem]**](ResultDirectoriesUsageDataItem.md) | Disk usage for all of immediate children of the current directory. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


