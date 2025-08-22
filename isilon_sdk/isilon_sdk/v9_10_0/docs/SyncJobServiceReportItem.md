# SyncJobServiceReportItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component** | **str** | The component that was processed. | [optional] 
**directory** | **str** | The directory of the service export. | [optional] 
**end_time** | **int** | The time the job ended this component. | [optional] 
**error_msg** | **list[str]** | A list of error messages generated while exporting components. | [optional] 
**filter** | **list[str]** | A list of path-based filters for exporting components. | [optional] 
**handlers_failed** | **int** | The number of handlers failed during export. | [optional] 
**handlers_skipped** | **int** | The number of handlers skipped during export. | [optional] 
**handlers_transferred** | **int** | The number of handlers exported. | [optional] 
**records_failed** | **int** | The number of records failed during export. | [optional] 
**records_skipped** | **int** | The number of records skipped during export. | [optional] 
**records_transferred** | **int** | The number of records exported. | [optional] 
**start_time** | **int** | The time the job began this component. | [optional] 
**status** | **str** | The current status of export for this component. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


