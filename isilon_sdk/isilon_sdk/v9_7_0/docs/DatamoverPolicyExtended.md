# DatamoverPolicyExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_policy_id** | **int** | Policy ID associated with this job. | [optional] 
**briefcase** | **str** | An opaque container for storing additional data in this object, e.g. key-value pairs | [optional] 
**disabled_by_dm** | **bool** | This flag indicates if policy has been disabled by the datamover system. This flag is set to true when a job for the given policy is cancelled | [optional] 
**enabled** | **bool** | True: policy is enabled, False: otherwise. | 
**id** | **int** | The unique policy identifier. | [optional] 
**name** | **str** | A user provided policy name. | 
**parent_exec_policy_id** | **int** | If a valid policy ID, then a job for this policy will be scheduled immediately after the parent policy job completes. This is optional field | [optional] 
**policy_specific_attr** | [**DatamoverPolicyPolicySpecificAttrExtended**](DatamoverPolicyPolicySpecificAttrExtended.md) |  | [optional] 
**priority** | **str** | The relative priority of the policy. | 
**run_now** | **bool** | Execute the policy immediately instead of waiting for it to run as scheduled. | [optional] 
**schedule** | [**DatamoverBasePolicySchedule**](DatamoverBasePolicySchedule.md) | The schedule of the policy- start time, recurrence, specific date-times. | [optional] 
**validity** | **bool** | Whether the policy is valid. | [optional] 
**version** | **int** | Version number of the config store when this object was edited. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


