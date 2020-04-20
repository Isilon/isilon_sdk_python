# JobJobExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_state** | **str** | State to which the job is transitioning; if control_state is identical to state, the job&#39;s state is stable. | [optional] 
**create_time** | **int** | The time the job was queued, in seconds since the epoch. | 
**current_phase** | **int** | The current phase of the job. | [optional] 
**description** | **str** | A text representation of the job. | [optional] 
**end_time** | **int** | The time the job ended, in seconds since the Epoch. | [optional] 
**human_desc** | **str** | A helpful human-readable description of the job | 
**id** | **int** | The ID of the job. | 
**impact** | **str** | The current impact of the job. | 
**participants** | **list[int]** | The set of devids working on the job. | [optional] 
**paths** | **list[str]** | Paths for which the job was queued. | [optional] 
**policy** | **str** | Current impact policy of the job. | 
**priority** | **int** | Current priority of the job; lower numbers preempt higher numbers. | 
**progress** | **str** | A text representation of the job&#39;s progress. | [optional] 
**retries_remaining** | **int** | The number of retries remaining if the job fails. | 
**running_time** | **int** | The number of seconds the job has executed. | [optional] 
**start_time** | **int** | The time the job started, in seconds since the Epoch. | [optional] 
**state** | **str** | Current state of the job. | 
**total_phases** | **int** | The total number of phases of the job type. | 
**type** | **str** | The job type. | 
**waiting_on** | **int** | The ID of a job for which this job is waiting. | [optional] 
**waiting_reason** | **str** | The reason the job is waiting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


