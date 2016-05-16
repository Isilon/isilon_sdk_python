# FsaResultExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pinned** | **bool** | True if the result is pinned to prevent automatic removal. | 
**begin_time** | **int** | Unix Epoch time of start of results collection job. | 
**content_path** | **str** | Path to results database. | 
**delete_link** | **str** | Resource to call with DELETE to remove results.. | 
**end_time** | **int** | Unix Epoch time of end of results collection job. | 
**fsa_state** | **str** | State of the result set. | 
**id** | **int** | The system generated result set ID. | 
**job_state** | **list[str]** | State information about the FSA Job. | 
**properties_link** | **str** | Resource to call to get result properties. | 
**size** | **int** | Size of the result set database in bytes. | 
**version** | **int** | FSA version used to create result set. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


