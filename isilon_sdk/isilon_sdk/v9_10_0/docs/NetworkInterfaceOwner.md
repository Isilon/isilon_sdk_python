# NetworkInterfaceOwner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_zone** | **str** | Name of configured Access Zone. | [optional] 
**groupnet** | **str** |  | [optional] 
**id** | **str** | The id of the owner. The concatenation of the groupnet, subnet, and pool fields as relevant. | [optional] 
**ip_addrs** | **list[str]** | List of IPs on this interface in the pool | [optional] 
**pool** | **str** |  | [optional] 
**prefixlen** | **int** | Prefix length of the subnet this owner belongs to. | [optional] 
**subnet** | **str** |  | [optional] 
**subtype** | **str** | Name of the system allocating the IPs for this Network Pool. | [optional] 
**type** | **str** | Specifies the type of network addresses that this interface owner contains. | [optional] 
**vlan_id** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


