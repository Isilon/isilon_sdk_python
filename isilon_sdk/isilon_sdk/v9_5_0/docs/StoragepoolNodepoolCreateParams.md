# StoragepoolNodepoolCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assess** | **bool** | Test that the action is possible | [optional] 
**l3** | **bool** | Use SSDs in this node pool for L3 cache. | [optional] 
**lnns** | **list[int]** | The node membership change requested for this node pool. | 
**name** | **str** | The node pool name. | 
**node_type_ids** | **list[int]** | The node types that are part of this pool. | [optional] 
**protection_policy** | **str** | The node pool protection policy. | [optional] 
**tier** | **str** | The name or ID of the node pool&#39;s tier, if it is in a tier. | [optional] 
**transfer_limit_pct** | **int** | Stop moving files to this nodepool when this limit is met | [optional] 
**transfer_limit_state** | **str** | How the transfer limit value is being applied | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


