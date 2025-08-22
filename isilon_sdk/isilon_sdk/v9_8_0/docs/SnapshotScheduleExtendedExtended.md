# SnapshotScheduleExtendedExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | Alias name to create for each snapshot. | [optional] 
**duration** | **int** | Time in seconds added to creation time to construction expiration time. | [optional] 
**id** | **int** | The system ID given to the schedule. | [optional] 
**name** | **str** | The schedule name. | [optional] 
**next_run** | **int** | Unix Epoch time of next snapshot to be created. | [optional] 
**next_snapshot** | **str** | Formatted name (see pattern) of next snapshot to be created. | [optional] 
**path** | **str** | The /ifs path snapshotted. | [optional] 
**pattern** | **str** | Pattern expanded with strftime to create snapshot names. | [optional] 
**schedule** | **str** | The isidate compatible natural language description of the schedule. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


