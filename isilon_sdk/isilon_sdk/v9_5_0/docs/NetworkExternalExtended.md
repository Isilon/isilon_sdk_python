# NetworkExternalExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv6_accept_redirects** | **bool** | If disabled, OneFS will stop processing ICMPv6 Redirect messages. | [optional] 
**ipv6_auto_config_enabled** | **bool** | True if rtsold daemon is enabled.  When set to false, the rtsold service is disabled, and IPv6 auto configuration is disabled | [optional] 
**ipv6_dad_enabled** | **bool** | Indicates if OneFS will perform Duplicate Address Detection on designated Network Pools and, optionally, SmartConnect Service IPs. | [optional] 
**ipv6_dad_timeout** | **int** | Denotes the number of seconds it takes for IPv6 Duplicate Address Detection to occur. During this time, the IP Addresses will not be usable. | [optional] 
**ipv6_enabled** | **bool** | Indicates if Front End interfaces are configured to support IPv6. | [optional] 
**ipv6_generate_link_local** | **bool** | Configure if OneFS should generate IPv6 Link Local IPs on the Front End Network. | [optional] 
**ipv6_ssip_perform_dad** | **bool** | Enable Duplicate Address Detection on SmartConnect Service IPs. | [optional] 
**sbr** | **bool** | Enable or disable Source Based Routing (Defaults to false) | [optional] 
**sc_rebalance_delay** | **int** | Delay in seconds for IP rebalance. | [optional] 
**sc_server_ttl** | **int** | Sets the TTL on NS and SOA records | [optional] 
**tcp_ports** | **list[int]** | List of client TCP ports. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


