# NdmpLogsNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **str** | The page on this node&#39;s NDMP log file being returned. | [optional] 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**logs** | **str** | The log file entries from the current page on this node. | [optional] 
**max_page** | **int** | The highest page number in this node&#39;s NDMP log file. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


