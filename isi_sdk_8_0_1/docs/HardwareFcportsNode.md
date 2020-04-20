# HardwareFcportsNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**fcports** | [**list[HardwareFcportsNodeFcport]**](HardwareFcportsNodeFcport.md) | A list of the FC ports on this node. | [optional] 
**id** | **int** | Node ID of the node reporting this information. | [optional] 
**lnn** | **int** | Logical node number of the node reporting this information. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


