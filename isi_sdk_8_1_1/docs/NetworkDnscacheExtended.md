# NetworkDnscacheExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_entry_limit** | **int** | DNS cache entry limit | [optional] 
**cluster_timeout** | **int** | Timeout value for calls made to other nodes in the cluster | [optional] 
**dns_timeout** | **int** | Timeout value for calls made to the dns resolvers | [optional] 
**eager_refresh** | **int** | Lead time to refresh cache entries nearing expiration | [optional] 
**testping_delta** | **int** | Deltas for checking cbind cluster health | [optional] 
**ttl_max_noerror** | **int** | Upper bound on ttl for cache hits | [optional] 
**ttl_max_nxdomain** | **int** | Upper bound on ttl for nxdomain | [optional] 
**ttl_max_other** | **int** | Upper bound on ttl for non-nxdomain failures | [optional] 
**ttl_max_servfail** | **int** | Upper bound on ttl for server failures | [optional] 
**ttl_min_noerror** | **int** | Lower bound on ttl for cache hits | [optional] 
**ttl_min_nxdomain** | **int** | Lower bound on ttl for nxdomain | [optional] 
**ttl_min_other** | **int** | Lower bound on ttl for non-nxdomain failures | [optional] 
**ttl_min_servfail** | **int** | Lower bound on ttl for server failures | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


