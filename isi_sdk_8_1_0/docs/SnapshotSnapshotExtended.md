# SnapshotSnapshotExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Alias name to create for this snapshot. If null, remove any alias. | [optional] 
**expires** | **int** | The Unix Epoch time the snapshot will expire and be eligible for automatic deletion. | [optional] 
**name** | **str** | The user or system supplied snapshot name. This will be null for snapshots pending delete. | [optional] 
**created** | **int** | The Unix Epoch time the snapshot was created. | 
**has_locks** | **bool** | True if the snapshot has one or more locks present see, see the locks subresource of a snapshot for a list of locks. | 
**id** | **int** | The system ID given to the snapshot. This is useful for tracking the status of delete pending snapshots. | 
**path** | **str** | The /ifs path snapshotted. | [optional] 
**pct_filesystem** | **float** | Percentage of /ifs used for storing this snapshot. | 
**pct_reserve** | **float** | Percentage of configured snapshot reserved used for storing this snapshot. | 
**schedule** | **str** | The name of the schedule used to create this snapshot, if applicable. | [optional] 
**shadow_bytes** | **int** | The amount of shadow bytes referred to by this snapshot. | 
**size** | **int** | The amount of storage in bytes used to store this snapshot. | 
**state** | **str** | Snapshot state. | 
**target_id** | **int** | The ID of the snapshot pointed to if this is an alias. | [optional] 
**target_name** | **str** | The name of the snapshot pointed to if this is an alias. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


