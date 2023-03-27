# StoragepoolTierExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | **list[str]** | The names or IDs of the tier&#39;s children. | [optional] 
**id** | **int** | The system ID given to the tier. | 
**lnns** | **list[int]** | The nodes that are part of this tier. | 
**name** | **str** | The tier name. | 
**transfer_limit_pct** | **int** | Stop moving files to this tier when this limit is met | [optional] 
**transfer_limit_state** | **str** | How the transfer limit value is being applied | [optional] 
**usage** | [**StoragepoolNodepoolUsage**](StoragepoolNodepoolUsage.md) | Total pool usage. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


