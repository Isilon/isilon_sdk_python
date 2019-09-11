# ClusterTimeNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 
**time** | **int** | The current time on the cluster as a UNIX epoch (seconds since 1/1/1970), as reported by this node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


