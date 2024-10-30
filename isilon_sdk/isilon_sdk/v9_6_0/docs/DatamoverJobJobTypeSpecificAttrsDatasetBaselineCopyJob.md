# DatamoverJobJobTypeSpecificAttrsDatasetBaselineCopyJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_dataset_on_target** | **bool** | Target dataset creation flag. True if dataset should be created on target, false otherwise. | [optional] 
**dataset_id** | **int** | The unique dataset identifier. | [optional] 
**new_tasks_account** | **str** | Account where to create task. | [optional] 
**retention** | [**DatamoverBasePolicySrcDatasetRetention**](DatamoverBasePolicySrcDatasetRetention.md) |  | [optional] 
**source_account_id** | **str** | Account ID of the source storage system. | [optional] 
**source_base_path** | **str** | Filesystem source base path. | [optional] 
**source_subpaths** | **list[str]** | Set of filesystem paths relative to base path. | [optional] 
**statistics** | [**DatamoverJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics**](DatamoverJobJobTypeSpecificAttrsDatasetBaselineCopyJobStatistics.md) | Baseline copy job statistics. | [optional] 
**target_account_id** | **str** | Account ID of the target storage system. | [optional] 
**target_base_path** | **str** | Target base path. | [optional] 
**target_dataset_type** | **str** | Dataset type on target. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


