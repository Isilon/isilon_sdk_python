# ProtocolsSmbSessionsNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**resume** | **str** | Provide this token as the &#39;resume&#39; query argument to continue listing results. | [optional] 
**sessions** | [**list[ProtocolsSmbSessionsNodeSession]**](ProtocolsSmbSessionsNodeSession.md) | A list of open SMB sessions on node. | [optional] 
**total** | **int** | The number of sessions returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


