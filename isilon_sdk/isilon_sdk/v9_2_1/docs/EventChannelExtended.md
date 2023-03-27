# EventChannelExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_nodes** | **list[int]** | Nodes (LNNs) that can be masters for this channel. | [optional] 
**enabled** | **bool** | Channel is to be used or not. | [optional] 
**excluded_nodes** | **list[int]** | Nodes (LNNs) that can NOT be the masters for this channel. | [optional] 
**parameters** | [**EventChannelParameters**](EventChannelParameters.md) | Parameters to be used for an smtp channel. | [optional] 
**system** | **bool** | Channel is a pre-defined system channel. | [optional] 
**type** | **str** | The mechanism used by the channel. | [optional] 
**id** | **int** | Unique identifier. | [optional] 
**name** | **str** | Channel name, may not contain /. | [optional] 
**rules** | **list[str]** | Alert rules involving this eventgroup type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


