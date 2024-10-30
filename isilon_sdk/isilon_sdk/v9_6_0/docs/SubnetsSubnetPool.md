# SubnetsSubnetPool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_zone** | **str** | Name of a valid access zone to map IP address pool to the zone. | [optional] 
**aggregation_mode** | **str** | OneFS supports the following NIC aggregation modes. | [optional] 
**alloc_method** | **str** | Specifies how IP address allocation is done among pool members. | [optional] 
**description** | **str** | A description of the pool. | [optional] 
**ifaces** | [**list[SubnetsSubnetPoolIface]**](SubnetsSubnetPoolIface.md) | List of interface members in this pool. | [optional] 
**ipv6_perform_dad** | **bool** | Indicates if the Network Pool should perform IPv6 Duplicate Address         Detection when configuring the IPs. Only applies to IPv6 Network Pools. | [optional] 
**name** | **str** | The name of the pool. It must be unique throughout the given subnet.It&#39;s a required field with POST method. | [optional] 
**nfsv3_rroce_only** | **bool** | Indicates that pool contains only RDMA RRoCE capable interfaces. | [optional] 
**ranges** | [**list[SubnetsSubnetPoolRange]**](SubnetsSubnetPoolRange.md) | List of IP address ranges in this pool. | [optional] 
**rebalance_policy** | **str** | Rebalance policy.. | [optional] 
**sc_auto_unsuspend_delay** | **int** | Time delay in seconds before a node which has been                 automatically unsuspended becomes usable in SmartConnect                responses for pool zones. | [optional] 
**sc_connect_policy** | **str** | SmartConnect client connection balancing policy. | [optional] 
**sc_dns_zone** | **str** | SmartConnect zone name for the pool. | [optional] 
**sc_dns_zone_aliases** | **list[str]** | List of SmartConnect zone aliases (DNS names) to the pool. | [optional] 
**sc_failover_policy** | **str** | SmartConnect IP failover policy. | [optional] 
**sc_subnet** | **str** | Name of SmartConnect service subnet for this pool. | [optional] 
**sc_ttl** | **int** | Time to live value for SmartConnect DNS query responses in seconds. | [optional] 
**static_routes** | [**list[SubnetsSubnetPoolStaticRoute]**](SubnetsSubnetPoolStaticRoute.md) | List of interface members in this pool. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


