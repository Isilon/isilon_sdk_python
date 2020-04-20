# ClusterInternalNetworks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_ip_addresses** | [**list[ClusterInternalNetworksFailoverIpAddresse]**](ClusterInternalNetworksFailoverIpAddresse.md) | Array of IP address ranges to be used to configure the internal failover network of the OneFS cluster. | [optional] 
**failover_status** | **str** | Status of failover network. | [optional] 
**int_a_fabric** | **str** | Network fabric used for the primary network int-a. | [optional] 
**int_a_ip_addresses** | [**list[ClusterInternalNetworksFailoverIpAddresse]**](ClusterInternalNetworksFailoverIpAddresse.md) | Array of IP address ranges to be used to configure the internal int-a network of the OneFS cluster. | [optional] 
**int_a_mtu** | **int** | Maximum Transfer Unit (MTU) of the primary network int-a. | [optional] 
**int_a_prefix_length** | **int** | Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask. | [optional] 
**int_a_status** | **str** | Status of the primary network int-a. | [optional] 
**int_b_fabric** | **str** | Network fabric used for the failover network. | [optional] 
**int_b_ip_addresses** | [**list[ClusterInternalNetworksFailoverIpAddresse]**](ClusterInternalNetworksFailoverIpAddresse.md) | Array of IP address ranges to be used to configure the internal int-b network of the OneFS cluster. | [optional] 
**int_b_mtu** | **int** | Maximum Transfer Unit (MTU) of the failover network int-b. | [optional] 
**int_b_prefix_length** | **int** | Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


