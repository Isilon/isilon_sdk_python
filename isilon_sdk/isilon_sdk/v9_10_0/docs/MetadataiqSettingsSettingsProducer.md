# MetadataiqSettingsSettingsProducer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changelist_job_retries** | **int** | Number of additional times, after the first failure, that MetadataIQ retries the ChangelistCreate job on a given pair of snapshots. Default is 2. | [optional] 
**changelist_job_tolerable_pause_hours** | **int** | Amount of time the Metadataiq system tolerates a MetadataIQ-driven ChangelistCreate job being paused, in hours, before warning. Default is 24. | [optional] 
**changelist_job_tolerable_state_request_failures** | **int** | Number of times the Metadataiq System can fail to get the ChangelistCreate job&#39;s status before it gives up. Default is 720. | [optional] 
**path** | **str** |  | [optional] 
**schedule** | **str** | Schedule at which a metadata cycle of analysis and upload occurs. The syntax must be isi-date compatible. Default is &#39;&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


