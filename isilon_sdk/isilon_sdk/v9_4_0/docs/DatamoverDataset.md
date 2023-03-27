# DatamoverDataset

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset_base_path** | **str** |  | [optional] 
**dataset_creation_time** | **int** | The time when the dataset is created. The time in seconds past the epoch | [optional] 
**dataset_expiry_action** | **str** | The action to be taken after dataset expiry. | [optional] 
**dataset_global_id** | [**DatamoverDatasetDatasetGlobalId**](DatamoverDatasetDatasetGlobalId.md) | The globally unique identifier of dataset. | [optional] 
**dataset_retention_period** | **int** | The time when dataset will expire which is calculated based upon dataset creation time plus dataset retention period specified for the dataset. It is the time in seconds past the epoch | [optional] 
**dataset_state** | **str** | The state of dataset. | [optional] 
**dataset_subpaths** | **list[str]** | Set of filesystem paths relative to base path. | [optional] 
**dataset_type** | **str** | Dataset type from one of these: A file system on object store in a copy format, a file system on object store in a backup format or file on file dataset. | [optional] 
**id** | **int** | The locally unique dataset identifier. | [optional] 
**snapshot_path** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


