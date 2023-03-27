# DatamoverBasePolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_account_id** | **str** | Account ID (local or remote DM system) where the policy should be created. | [optional] 
**briefcase** | **str** | An opaque container for storing additional data in this object, e.g. key-value pairs | [optional] 
**enabled** | **bool** | True: policy is enabled, False: otherwise. | [optional] 
**name** | **str** | A user provided base policy name. | [optional] 
**new_tasks_account** | **str** | Account of the system to create tasks on. This overrides the default task affinity. | [optional] 
**override_list** | **list[str]** | The list of fields which will override a concrete policy. | [optional] 
**priority** | **str** | The relative priority of the policy. | [optional] 
**schedule** | [**DatamoverBasePolicySchedule**](DatamoverBasePolicySchedule.md) | The schedule of the policy- start time, recurrence, specific date-times. | [optional] 
**source_account_id** | **str** | Account ID of the source data storage. | [optional] 
**source_base_path** | **str** | Filesystem base path on source DM system which has the directories/files for which dataset has to be created. | [optional] 
**source_subpaths** | **list[str]** | Set of filesystem paths relative to base path. | [optional] 
**src_dataset_retention** | [**DatamoverBasePolicySrcDatasetRetention**](DatamoverBasePolicySrcDatasetRetention.md) |  | [optional] 
**target_account_id** | **str** | Account ID of the target data storage. | [optional] 
**target_base_path** | **str** | Filesystem base path on target DM syestem which has the directories/files for which dataset has to be created. | [optional] 
**tgt_dataset_retention** | [**DatamoverBasePolicySrcDatasetRetention**](DatamoverBasePolicySrcDatasetRetention.md) |  | [optional] 
**version** | **int** | Version number of the config store when this object was edited. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


