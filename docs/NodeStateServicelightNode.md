# NodeStateServicelightNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | The node service light state (True &#x3D; on). | 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**present** | **bool** | This node has a service light. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 
**supported** | **bool** | This node supports a service light. | [optional] 
**valid** | **bool** | The node service light state is valid (False &#x3D; Error). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


