# GroupnetSubnetCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the subnet. | [optional] 
**dsr_addrs** | **list[str]** | List of Direct Server Return addresses. | [optional] 
**gateway** | **str** | Gateway IP address. | [optional] 
**gateway_priority** | **int** | Gateway priority. | [optional] 
**mtu** | **int** | MTU of the subnet. | [optional] 
**name** | **str** | The name of the subnet. | 
**prefixlen** | **int** | Subnet Prefix Length. | 
**sc_service_addr** | **str** | The address that SmartConnect listens for DNS requests. | [optional] 
**sc_service_name** | **str** | Domain Name corresponding to the SmartConnect Service Address. | [optional] 
**vlan_enabled** | **bool** | VLAN tagging enabled or disabled. | [optional] 
**vlan_id** | **int** | VLAN ID for all interfaces in the subnet. | [optional] 
**addr_family** | **str** | IP address format. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


