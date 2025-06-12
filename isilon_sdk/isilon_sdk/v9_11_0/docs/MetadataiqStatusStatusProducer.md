# MetadataiqStatusStatusProducer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changelistcreate_job_id** | **int** | The ChangelistCreate Job ID for the current snapid pair. | [optional] 
**end_time** | **int** | Time when the MetadataIQ current Producer Cycle ended.  | [optional] 
**error_count** | **int** | Number of errors encountered during the MetadataIQ current Producer Cycle. | [optional] 
**job_failures** | **int** | Consecutive failed jobs for the current snapid pair. | [optional] 
**new_snapshot_id** | **int** | The new snapshot ID of the current MetadataIQ cycle. | [optional] 
**new_snapshot_lock_id** | **int** | The new snapshot lock ID of the new snapshot from the current MetadataIQ cycle. | [optional] 
**old_snapshot_id** | **int** | The ID of the snapshot created at the start of the previous MetadataIQ cycle. First instance will be Invalid Snapid. | [optional] 
**old_snapshot_lock_id** | **int** | The lock ID of the snapshot created at the start of the previous MetadataIQ Cycle. First instance will be Invalid Lock ID. | [optional] 
**running_lnn** | **str** | The LNN on which the MetadataIQ Producer is currently running. | [optional] 
**start_time** | **int** | Time when the MetadataIQ current Producer Cycle started. Default is 0 (0 means never) | [optional] 
**state** | **str** | State of the MetadataIQ current Producer Cycle. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


