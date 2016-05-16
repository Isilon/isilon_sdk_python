# NetworkDnscacheSetting

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_entry_limit** | **int** | DNS cache entry limit | 
**cluster_timeout** | **int** | Timeout value for calls made to other nodes in the cluster | 
**dns_timeout** | **int** | Timeout value for calls made to the dns resolvers | 
**eager_refresh** | **int** | Lead time to refresh cache entries nearing expiration | 
**testping_delta** | **int** | Deltas for checking cbind cluster health | 
**ttl_max_noerror** | **int** | Upper bound on ttl for cache hits | 
**ttl_max_nxdomain** | **int** | Upper bound on ttl for nxdomain | 
**ttl_max_other** | **int** | Upper bound on ttl for non-nxdomain failures | 
**ttl_max_servfail** | **int** | Upper bound on ttl for server failures | 
**ttl_min_noerror** | **int** | Lower bound on ttl for cache hits | 
**ttl_min_nxdomain** | **int** | Lower bound on ttl for nxdomain | 
**ttl_min_other** | **int** | Lower bound on ttl for non-nxdomain failures | 
**ttl_min_servfail** | **int** | Lower bound on ttl for server failures | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


