# HdfsInotifySettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enable or disable the collection of edits over HDFS and access to the edits via HDFS INotify stream. | [optional] 
**maximum_delay** | **int** | The maximum duration in seconds until an edit event is reported in INotify. The default is 60, which amounts to a minute. | [optional] 
**retention** | **int** | The minimum amount of time in seconds the edits will be retained. The default is 172800, which amounts to 48hr. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


