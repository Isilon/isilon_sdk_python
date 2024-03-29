# GroupnetSubnetExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the subnet. | [optional] 
**dsr_addrs** | **list[str]** | List of Direct Server Return addresses. | [optional] 
**gateway** | **str** | Gateway IP address. | [optional] 
**gateway_priority** | **int** | Gateway priority. | [optional] 
**mtu** | **int** | MTU of the subnet. | [optional] 
**name** | **str** | The name of the subnet. | [optional] 
**prefixlen** | **int** | Subnet Prefix Length. | [optional] 
**sc_service_addrs** | [**list[SubnetsSubnetPoolRange]**](SubnetsSubnetPoolRange.md) | List of IP addresses that SmartConnect listens for DNS requests. | [optional] 
**sc_service_name** | **str** | Domain Name corresponding to the SmartConnect Service Address. | [optional] 
**vlan_enabled** | **bool** | VLAN tagging enabled or disabled. | [optional] 
**vlan_id** | **int** | VLAN ID for all interfaces in the subnet. | [optional] 
**addr_family** | **str** | IP address format. | [optional] 
**base_addr** | **str** | The base IP address. | [optional] 
**firewall_policy** | **str** | Name of the Firewall Policy associated with this Network Subnet. | [optional] 
**groupnet** | **str** | Name of the groupnet this subnet belongs to. | [optional] 
**id** | **str** | Unique Subnet ID. | [optional] 
**pools** | **list[str]** | Name of the pools in the subnet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


