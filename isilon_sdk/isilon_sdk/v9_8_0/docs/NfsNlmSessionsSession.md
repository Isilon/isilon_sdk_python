# NfsNlmSessionsSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_ip** | **str** | An IP address for which NSM has client records | [optional] 
**delegates** | **list[int]** |  | [optional] 
**host_type** | **str** | The sort of host that this entry represents | [optional] 
**hostname** | **str** | The host being monitored | [optional] 
**id** | **str** | Session ID | [optional] 
**is_active** | **bool** | Whether or not the client is actively being monitored | [optional] 
**last_modified** | **int** | Unix time in seconds that the client was last modified (monitored or unmonitored) | [optional] 
**notify_attempts_remaining** | **int** | Number of times we will attempt to notify this client before giving up | [optional] 
**notify_error** | **str** | Last error received attempting to notify this client | [optional] 
**notify_last_attempt** | **int** | Unix time in seconds when we last attempted to notify this clients | [optional] 
**zone** | **str** | Access zone name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


