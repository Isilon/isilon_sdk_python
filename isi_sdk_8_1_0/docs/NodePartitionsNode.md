# NodePartitionsNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of how many partitions are included. | [optional] 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID of the node reporting this information. | [optional] 
**lnn** | **int** | Logical node number of the node reporting this information. | [optional] 
**partitions** | [**list[NodePartitionsNodePartition]**](NodePartitionsNodePartition.md) | Partition information. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


