# NdmpContextsBackupContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context_expiration_time** | **int** | Context expiration time | [optional] 
**context_id** | **str** | Context ID | [optional] 
**id** | **str** | Unique display id. | [optional] 
**lead_session_id** | **str** | The leading session in the backup or restore | [optional] 
**multistream** | **bool** | Indicating a multi-stream backup or restore operation | [optional] 
**path** | **str** | The directory of the backup. This is not applicable to restore contexts. | [optional] 
**sessions** | [**list[NdmpContextsBackupContextSession]**](NdmpContextsBackupContextSession.md) |  | [optional] 
**snapid** | **int** | Snapshot ID reserved for the context. This is not applicable to restore contexts. | [optional] 
**start_time** | **int** | Context creation time | [optional] 
**status** | **str** | Whether the context is active. | [optional] 
**total_sessions** | **int** | The number of sessions in the context | [optional] 
**type** | **str** | Type of context; It can be bre, backup, and restore | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


