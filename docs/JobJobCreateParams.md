# JobJobCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_dup** | **bool** | Whether or not to queue the job if one of the same type is already running or queued. | [optional] 
**avscan_params** | [**JobJobAvscanParams**](JobJobAvscanParams.md) |  | [optional] 
**changelistcreate_params** | [**JobJobChangelistcreateParams**](JobJobChangelistcreateParams.md) |  | [optional] 
**domainmark_params** | [**JobJobDomainmarkParams**](JobJobDomainmarkParams.md) |  | [optional] 
**paths** | **list[str]** | For jobs which take paths, the IFS paths to pass to the job. | 
**policy** | **str** | Impact policy of this job instance. | [optional] 
**prepair_params** | [**JobJobPrepairParams**](JobJobPrepairParams.md) |  | [optional] 
**priority** | **int** | Priority of this job instance; lower numbers preempt higher numbers. | [optional] 
**smartpoolstree_params** | [**JobJobSmartpoolstreeParams**](JobJobSmartpoolstreeParams.md) |  | [optional] 
**snaprevert_params** | [**JobJobSnaprevertParams**](JobJobSnaprevertParams.md) |  | [optional] 
**type** | **str** | Job type to queue. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


