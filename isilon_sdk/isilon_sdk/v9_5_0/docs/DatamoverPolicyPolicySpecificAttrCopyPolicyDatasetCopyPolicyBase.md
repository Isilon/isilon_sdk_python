# DatamoverPolicyPolicySpecificAttrCopyPolicyDatasetCopyPolicyBase

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_account_id** | **str** | Account ID (local or remote DM system) where the policy should be created. This is an optional field, if not specified it will be set to the local account ID. | [optional] 
**copy_retention** | [**DatamoverBasePolicySrcDatasetRetention**](DatamoverBasePolicySrcDatasetRetention.md) |  | [optional] 
**new_tasks_account** | **str** | Account ID where to create all the tasks. This is an optional field, if not specified will be set to the local account ID. | [optional] 
**source_account_id** | **str** | Account ID of the source data storage. | [optional] 
**target_account_id** | **str** | Account ID of the target data storage. | [optional] 
**target_base_path** | **str** | Base path on the target storage system. | [optional] 
**target_dataset_type** | **str** | Dataset type from one of these: A file system on object store in a copy format, a file system on object store in a backup format or file on file dataset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


