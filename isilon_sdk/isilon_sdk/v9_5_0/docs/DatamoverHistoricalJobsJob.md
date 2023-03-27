# DatamoverHistoricalJobsJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Job ID. | [optional] 
**job_control_request** | **str** | Job control request. | [optional] 
**job_end_time** | **int** | The time in seconds past the epoch | [optional] 
**job_policy_id** | **int** | Policy ID associated with this job. | [optional] 
**job_priority** | **str** | The relative priority of the job. | [optional] 
**job_start_time** | **int** | The time in seconds past the epoch | [optional] 
**job_state** | **str** | Job state | [optional] 
**job_state_flags** | **int** | This shows if job has some failure and failure code/info: DM_JOB_HAS_NO_FAILURE &#x3D; 0, DM_JOB_FAILURE_ENCOUNTERED &#x3D; 1, DM_JOB_CANNOT_COMPLETE &#x3D; 2, DM_JOB_ALREADY_RUNNING &#x3D; 4. | [optional] 
**job_type_specific_attrs** | [**DatamoverHistoricalJobsJobJobTypeSpecificAttrs**](DatamoverHistoricalJobsJobJobTypeSpecificAttrs.md) | Job type specific attributes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


