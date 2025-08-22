# MpaRequestExtendedExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Name of privileged action | [optional] 
**action_payload** | [**list[MpaRequestActionPayloadItem]**](MpaRequestActionPayloadItem.md) | set of key/value pairs for privileged action payload | [optional] 
**created_by** | **str** |  | [optional] 
**creation_time** | **int** | Unix epoch time format. | [optional] 
**id** | **str** | Unique ID of MPA request. | [optional] 
**last_update_time** | **int** | Unix epoch time format. | [optional] 
**request_for** | **str** |  | [optional] 
**resource_ids** | **list[str]** | List of resources IDs requested for approval; optional. | [optional] 
**resource_type** | **str** | Type of resource requested for approval; optional. | [optional] 
**service** | **str** | Name of service or component in system that owns the privileged action | [optional] 
**status** | **str** | status of MPA request | [optional] 
**system_created** | **bool** | A privileged action approval request was created by the system. | 
**zone_id** | **int** | Zone id of MPA request created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


