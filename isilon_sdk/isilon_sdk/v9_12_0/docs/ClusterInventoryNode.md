# ClusterInventoryNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bmc** | [**ClusterInventoryNodeBmc**](ClusterInventoryNodeBmc.md) | The inventory of the node&#39;s BMC. | [optional] 
**drives** | [**list[ClusterInventoryNodeDrive]**](ClusterInventoryNodeDrive.md) | List of drives on the node | [optional] 
**host_ip_addresses** | **list[str]** | List of host IP addresses assigned to the node. | [optional] 
**lnn** | **int** | Logical node number of node | [optional] 
**model** | **str** | A string identifying a particular hardware model of the OneFS product. | [optional] 
**name** | **str** | The name of the node. | [optional] 
**network_interfaces** | [**list[ClusterInventoryNodeNetworkInterface]**](ClusterInventoryNodeNetworkInterface.md) | List of network interfaces on the node | [optional] 
**os_version** | **str** | OneFS build version running on the node | [optional] 
**serial** | **str** | Serial number of this node. | [optional] 
**status** | **list[str]** | The health status of the node. | [optional] 
**timestamp** | **str** | Timestamp for when the inventory was last updated. | [optional] 
**uptime** | **str** | The time the node has been online. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


