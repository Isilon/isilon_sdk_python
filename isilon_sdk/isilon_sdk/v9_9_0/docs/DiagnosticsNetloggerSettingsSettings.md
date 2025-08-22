# DiagnosticsNetloggerSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients** | **str** | Limit packet collection to specified Client hostname/IP addresses. | [optional] 
**count** | **int** | The number of packet capture files to keep after they reach the duration limit.  Defaults to the latest 3 files.  0 is infinite. | [optional] 
**duration** | **int** | Duration in minutes of each capture file | [optional] 
**interfaces** | **str** | Limit packet collection to specified network interfaces. | [optional] 
**nodelist** | **str** | List of nodes specified by LNN on which to run the capture, or empty for all | [optional] 
**ports** | **str** | Limit packet collection to specified TCP or UDP ports | [optional] 
**protocols** | **str** | Limit packet collection to specified protocols | [optional] 
**snaplength** | **int** | The maximum amount of data for each packet that is captured.  Default is 320 bytes. Valid range is 64 to 9100 bytes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


