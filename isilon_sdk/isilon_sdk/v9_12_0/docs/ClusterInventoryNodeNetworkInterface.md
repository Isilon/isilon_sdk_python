# ClusterInventoryNodeNetworkInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firmware** | **str** | Firmware version of the network interface. | [optional] 
**ip_addrs** | **list[str]** | List of IP addresses assigned to the interface. | [optional] 
**ipv4_gateway** | **str** |  | [optional] 
**ipv6_gateway** | **str** |  | [optional] 
**mac_address** | **str** | MAC address | [optional] 
**name** | **str** | Name of the network interface. | [optional] 
**port** | **str** | The port of the interface, e.g., 1:200gige-1, 3:int-a, | [optional] 
**role** | **str** | Indicates if the interface is associated with an external or internal network. | [optional] 
**speed** | **int** | The negotiated speed of the interface, in Mbps. | [optional] 
**status** | **str** | The status of the interface. | [optional] 
**switch_connection** | [**ClusterInventoryNodeNetworkInterfaceSwitchConnection**](ClusterInventoryNodeNetworkInterfaceSwitchConnection.md) | Information related to switch connection. | [optional] 
**vendor** | **str** | Vendor of the network interface. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


