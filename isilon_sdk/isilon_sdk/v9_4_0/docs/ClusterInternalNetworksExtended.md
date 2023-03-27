# ClusterInternalNetworksExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_ip_addresses** | [**list[ClusterInternalNetworksFailoverIpAddresseExtended]**](ClusterInternalNetworksFailoverIpAddresseExtended.md) | Array of IP address ranges to be used to configure the internal failover network of the OneFS cluster. | [optional] 
**failover_status** | **str** | Status of failover network. | [optional] 
**int_a_ip_addresses** | [**list[ClusterInternalNetworksIntAIpAddresseExtended]**](ClusterInternalNetworksIntAIpAddresseExtended.md) | Array of IP address ranges to be used to configure the internal int-a network of the OneFS cluster. | [optional] 
**int_a_prefix_length** | **int** | Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask. | [optional] 
**int_b_ip_addresses** | [**list[ClusterInternalNetworksIntBIpAddresseExtended]**](ClusterInternalNetworksIntBIpAddresseExtended.md) | Array of IP address ranges to be used to configure the internal int-b network of the OneFS cluster. | [optional] 
**int_b_prefix_length** | **int** | Prefixlen specifies the length of network bits used in an IP address. This field is the right-hand part of the CIDR notation representing the subnet mask. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


