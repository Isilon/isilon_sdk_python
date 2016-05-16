# StoragepoolNodepoolExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**l3** | **bool** | Use SSDs in this node pool for L3 cache. | [optional] 
**lnns** | **list[int]** | The nodes that are part of this node pool. | [optional] 
**name** | **str** | The node pool name. | [optional] 
**protection_policy** | **str** | The node pool protection policy. | [optional] 
**tier** | **str** | The name or ID of the node pool&#39;s tier, if it is in a tier. | [optional] 
**can_enable_l3** | **bool** | Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives. | 
**id** | **int** | The system ID given to the node pool. | 
**l3_status** | **str** | &#39;storage&#39; if the &#39;l3&#39; option is disabled. If the l3 option is enabled, &#39;migrating&#39; if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, &#39;l3&#39;. | 
**manual** | **bool** | Whether or not the node pool is manually managed. | 
**usage** | [**StoragepoolTierUsage**](StoragepoolTierUsage.md) | Total pool usage. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


