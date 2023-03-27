# ClusterFirmwareStatusNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**list[UpgradeClusterFirmwareDeviceNodeDevice]**](UpgradeClusterFirmwareDeviceNodeDevice.md) | List of the firmware status for hardware components on the node. | [optional] 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**node_unavailable** | **bool** | Node is unavailable. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


