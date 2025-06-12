# NodeStateNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**readonly** | [**NodeStateNodeReadonly**](NodeStateNodeReadonly.md) | Node readonly state. | [optional] 
**servicelight** | [**NodeStateNodeServicelight**](NodeStateNodeServicelight.md) | Node service light state. | [optional] 
**smartfail** | [**NodeStateNodeSmartfail**](NodeStateNodeSmartfail.md) | Node smartfail state. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


