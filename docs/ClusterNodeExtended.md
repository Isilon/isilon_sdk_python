# ClusterNodeExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drive_d_config** | [**ClusterNodeDriveDConfig**](ClusterNodeDriveDConfig.md) | An object containing a node&#39;s drive subsystem XML configuration file. | [optional] 
**drives** | [**list[ClusterNodeDriveExtended]**](ClusterNodeDriveExtended.md) | List of the drives in this node. | [optional] 
**hardware** | [**ClusterNodeHardware**](ClusterNodeHardware.md) | Node hardware identifying information (static). | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**internal_ip_address** | **str** | IPv4 address in the format: xxx.xxx.xxx.xxx | 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**partitions** | [**ClusterNodePartitions**](ClusterNodePartitions.md) | Node partition information. | [optional] 
**sensors** | [**ClusterNodeSensors**](ClusterNodeSensors.md) | Node sensor information (hardware reported). | [optional] 
**sleds** | [**list[NodeSledsNodeSled]**](NodeSledsNodeSled.md) | List of the sleds in this node. | [optional] 
**state** | [**ClusterNodeStateExtended**](ClusterNodeStateExtended.md) | Node state information (reported and modifiable). | [optional] 
**status** | [**ClusterNodeStatus**](ClusterNodeStatus.md) | Node status information (hardware reported). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


