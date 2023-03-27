# SnapshotWritableWritableItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** | The Unix Epoch time the writable snapshot was created. | 
**dst_path** | **str** | The user supplied /ifs path of writable snapshot. | 
**id** | **int** | The system ID given to the writable snapshot. This is useful for debugging. | 
**log_size** | **int** | The sum in bytes of logical size of files in this writable snapshot. | 
**phys_size** | **int** | The amount of storage in bytes used to store this writable snapshot. | 
**src_id** | **int** | The system ID of the user supplied source snapshot. This is useful for debugging. | 
**src_path** | **str** | The /ifs path of user supplied source snapshot. This will be null for writable snapshots pending delete. | [optional] 
**src_snap** | **str** | The user supplied source snapshot name or ID. This will be null for writable snapshots pending delete. | [optional] 
**state** | **str** | Writable Snapshot state. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


