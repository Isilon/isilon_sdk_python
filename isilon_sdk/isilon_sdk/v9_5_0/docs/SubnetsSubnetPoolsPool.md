# SubnetsSubnetPoolsPool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_zone** | **str** | Name of a valid access zone to map IP address pool to the zone. | 
**addr_family** | **str** | IP address format. | 
**aggregation_mode** | **str** | OneFS supports the following NIC aggregation modes. | 
**alloc_method** | **str** | Specifies how IP address allocation is done among pool members. | 
**description** | **str** | A description of the pool. | 
**firewall_policy** | **str** | Name of the Firewall Policy associated with this Network Pool. | 
**groupnet** | **str** | Name of the groupnet this pool belongs to. | 
**id** | **str** | Unique Pool ID. | 
**ifaces** | [**list[SubnetsSubnetPoolIface]**](SubnetsSubnetPoolIface.md) | List of interface members in this pool. | 
**ipv6_perform_dad** | **bool** | Indicates if the Network Pool should perform IPv6 Duplicate Address         Detection when configuring the IPs. Only applies to IPv6 Network Pools. | 
**name** | **str** | The name of the pool. It must be unique throughout the given subnet.It&#39;s a required field with POST method. | 
**nfsv3_rroce_only** | **bool** | Indicates that pool contains only RDMA RRoCE capable interfaces. | 
**ranges** | [**list[SubnetsSubnetPoolRange]**](SubnetsSubnetPoolRange.md) | List of IP address ranges in this pool. | 
**rebalance_policy** | **str** | Rebalance policy.. | 
**rules** | **list[str]** | Names of the rules in this pool. | 
**sc_auto_unsuspend_delay** | **int** | Time delay in seconds before a node which has been                 automatically unsuspended becomes usable in SmartConnect                responses for pool zones. | 
**sc_connect_policy** | **str** | SmartConnect client connection balancing policy. | 
**sc_dns_zone** | **str** | SmartConnect zone name for the pool. | 
**sc_dns_zone_aliases** | **list[str]** | List of SmartConnect zone aliases (DNS names) to the pool. | 
**sc_failover_policy** | **str** | SmartConnect IP failover policy. | 
**sc_subnet** | **str** | Name of SmartConnect service subnet for this pool. | 
**sc_suspended_nodes** | **list[int]** | List of LNNs showing currently suspended nodes in SmartConnect. | 
**sc_ttl** | **int** | Time to live value for SmartConnect DNS query responses in seconds. | 
**static_routes** | [**list[SubnetsSubnetPoolStaticRoute]**](SubnetsSubnetPoolStaticRoute.md) | List of interface members in this pool. | 
**subnet** | **str** | The name of the subnet. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


