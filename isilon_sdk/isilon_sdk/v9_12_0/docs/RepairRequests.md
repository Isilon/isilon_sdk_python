# RepairRequests

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_trigger** | **bool** | If the repair action should be automatically triggered upon a failure. | 
**end_time** | **int** | The time in seconds since the UNIX epoch at which request was completed. | [optional] 
**error** | **str** | Error message for a failed repair. | [optional] 
**item_id** | **str** | The ID of the healthcheck item. | 
**nodes** | [**list[RepairRequestsNode]**](RepairRequestsNode.md) |  | [optional] 
**queue_time** | **int** | The time in seconds since the UNIX epoch at which request was queued. | 
**repair_id** | **str** | The ID of the repair request. | 
**result** | **str** | The result of a repair. | [optional] 
**scope** | **str** | The scope of the repair. | [optional] 
**source_id** | **str** | The ID of the source of the request. | 
**source_type** | **str** | The source type of the request. | 
**start_time** | **int** | The time in seconds since the UNIX epoch at which request was started. | [optional] 
**status** | **str** | Status of a particular repair. | [optional] 
**task_id** | **str** | The ID of the repair task. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


