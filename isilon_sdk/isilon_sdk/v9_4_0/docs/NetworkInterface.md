# NetworkInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flags** | **list[str]** | List of interface flags | 
**id** | **str** | Id is a concatenation of lnn and name in the format &#39;lnn:name&#39; e.g. 3:ext-2. | 
**ip_addrs** | **list[str]** | List of IP addresses | 
**ipv4_gateway** | **str** |  | [optional] 
**ipv6_gateway** | **str** |  | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | 
**mtu** | **int** | The mtu the interface. | [optional] 
**name** | **str** | The name of the interface. | 
**nic_name** | **str** | NIC name | 
**owners** | [**list[NetworkInterfaceOwner]**](NetworkInterfaceOwner.md) | List of owners (membership) | 
**speed** | **int** | The negotiated speed of the interface, in Mbps. | [optional] 
**status** | **str** | Status of the interface | 
**type** | **str** | The type of network interface | 
**vlans** | [**list[NetworkInterfaceVlan]**](NetworkInterfaceVlan.md) | List of VLANs | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


