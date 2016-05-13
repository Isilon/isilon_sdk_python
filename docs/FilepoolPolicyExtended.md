# FilepoolPolicyExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**list[FilepoolDefaultPolicyDefaultPolicyAction]**](FilepoolDefaultPolicyDefaultPolicyAction.md) | A list of actions to be taken for matching files | [optional] 
**apply_order** | **int** | The order in which this policy should be applied (relative to other policies) | [optional] 
**description** | **str** | A description for this policy | [optional] 
**file_matching_pattern** | [**FilepoolPolicyFileMatchingPattern**](FilepoolPolicyFileMatchingPattern.md) | The file matching rules for this policy | [optional] 
**name** | **str** | A unique name for this policy | [optional] 
**birth_cluster_id** | **str** | The guid assigned to the cluster on which the account was created | [optional] 
**id** | **int** | A unique identifier for this policy | [optional] 
**state** | **str** | Indicates whether this policy is in a good state (\&quot;OK\&quot;) or disabled (\&quot;disabled\&quot;) | [optional] 
**state_details** | **str** | Gives further information to describe the state of this policy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


