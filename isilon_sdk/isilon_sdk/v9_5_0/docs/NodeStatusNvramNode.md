# NodeStatusNvramNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batteries** | [**list[NodeStatusNvramNodeBattery]**](NodeStatusNvramNodeBattery.md) | This node&#39;s NVRAM battery status information. | [optional] 
**battery_count** | **int** | This node&#39;s NVRAM battery count. On failure: -1, otherwise 1 or 2. | [optional] 
**charge_status** | **str** | This node&#39;s NVRAM battery charge status, as a color. | [optional] 
**charge_status_number** | **int** | This node&#39;s NVRAM battery charge status, as a number. Error or not supported: -1. BR_BLACK: 0. BR_GREEN: 1. BR_YELLOW: 2. BR_RED: 3. | [optional] 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**present** | **bool** | This node has NVRAM. | [optional] 
**present_flash** | **bool** | This node has NVRAM with flash storage. | [optional] 
**present_size** | **int** | The size of the NVRAM, in bytes. | [optional] 
**present_type** | **str** | This node&#39;s NVRAM type. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 
**supported** | **bool** | This node supports NVRAM. | [optional] 
**supported_flash** | **bool** | This node supports NVRAM with flash storage. | [optional] 
**supported_type** | **str** | This node&#39;s supported NVRAM type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


