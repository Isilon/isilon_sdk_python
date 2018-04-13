# NodeStateReadonlyNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed** | **bool** | The current read-only mode allowed status for the node. | [optional] 
**enabled** | **bool** | The current read-only user mode status for the node. NOTE: If read-only mode is currently disallowed for this node, it will remain read/write until read-only mode is allowed again. This value only sets or clears any user-specified requests for read-only mode. If the node has been placed into read-only mode by the system, it will remain in read-only mode until the system conditions which triggered read-only mode have cleared. | [optional] 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID of the node reporting this information. | [optional] 
**lnn** | **int** | Logical node number of the node reporting this information. | [optional] 
**mode** | **bool** | The current read-only mode status for the node. | [optional] 
**status** | **str** | The current read-only mode status description for the node. | [optional] 
**valid** | **bool** | The read-only state values are valid (False &#x3D; Error). | [optional] 
**value** | **int** | The current read-only value (enumerated bitfield) for the node. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


