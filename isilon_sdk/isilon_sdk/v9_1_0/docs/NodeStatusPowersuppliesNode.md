# NodeStatusPowersuppliesNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Count of how many power supplies are supported. | [optional] 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**failures** | **int** | Count of how many power supplies have failed. | [optional] 
**has_cff** | **bool** | Does this node have a CFF power supply. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**status** | **str** | A descriptive status string for this node&#39;s power supplies. | [optional] 
**supplies** | [**list[NodeStatusPowersuppliesNodeSupply]**](NodeStatusPowersuppliesNodeSupply.md) | List of this node&#39;s power supplies. | [optional] 
**supports_cff** | **bool** | Does this node support CFF power supplies. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


