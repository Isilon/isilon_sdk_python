# CloudJobExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_time** | **int** | The time at which the job was completed (if applicable) | [optional] 
**create_time** | **int** | The time at which the job was created | [optional] 
**description** | **str** | A brief description of the job contents | [optional] 
**effective_state** | **str** | The effective state of the job (e.g,. the combination of operation_state and job_state) | [optional] 
**files** | [**CloudJobFiles**](CloudJobFiles.md) | The files and filters addressed by this job | [optional] 
**id** | **int** | The job&#39;s ID | [optional] 
**job_engine_job** | [**CloudJobJobEngineJob**](CloudJobJobEngineJob.md) | Information about the related job engine job if there is one | [optional] 
**job_state** | **str** | The current state of the job | [optional] 
**operation_state** | **str** | The current state of the operation associated with the job | [optional] 
**state_change_time** | **int** | The last time at which the job state changed | [optional] 
**type** | **str** | The type of cloud action to be performed by this job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


