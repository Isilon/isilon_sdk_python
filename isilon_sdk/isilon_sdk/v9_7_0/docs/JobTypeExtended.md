# JobTypeExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the job type is enabled and able to run. | 
**policy** | **str** | Default impact policy of this job type. | 
**priority** | **int** | Default priority of this job type; lower numbers preempt higher numbers. | 
**schedule** | **str** | The schedule on which this job type is queued, if any. | [optional] 
**allow_multiple_instances** | **bool** | Whether multiple instances of this job type may run simultaneously. | 
**description** | **str** | Brief description of the job type. | 
**exclusion_set** | **str** | The set(s) of mutually-exclusive job types to which this job belongs.  No job in this set may run with any other job in this set.  Obsolete; this value will always be an empty string, as exclusion sets are no longer a job type property. | 
**hidden** | **bool** | Whether this job type is normally visible in the UI. | 
**id** | **str** | Job type ID. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


