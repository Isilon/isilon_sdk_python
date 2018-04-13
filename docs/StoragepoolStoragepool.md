# StoragepoolStoragepool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_enable_l3** | **bool** | Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives. | 
**children** | **list[str]** | The names or IDs of the pool&#39;s children. | [optional] 
**health_flags** | **list[str]** | An array of containing any health issues with this pool.  If the pool is healthy, the list is empty.  Only appears on &#39;nodepool&#39; type storagepools. | [optional] 
**id** | **int** | The system ID given to the pool. | 
**l3** | **bool** | Use SSDs in this node pool for L3 cache. | 
**l3_status** | **str** | &#39;storage&#39; if the &#39;l3&#39; option is disabled. If the l3 option is enabled, &#39;migrating&#39; if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, &#39;l3&#39;. | 
**lnns** | **list[int]** | The nodes that are part of this pool. | 
**manual** | **bool** | Whether or not the node pool is manually managed. | [optional] 
**name** | **str** | The pool name. | 
**protection_policy** | **str** | The underlying protection policy. | [optional] 
**type** | **str** | The pool type. | 
**usage** | [**StoragepoolTierUsage**](StoragepoolTierUsage.md) | Total pool usage. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


