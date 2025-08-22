# isilon_sdk.v9_5_0.NetworkApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dnscache_flush_item**](NetworkApi.md#create_dnscache_flush_item) | **POST** /platform/3/network/dnscache/flush | 
[**create_firewall_policy**](NetworkApi.md#create_firewall_policy) | **POST** /platform/16/network/firewall/policies | 
[**create_firewall_reset_global_policy_item**](NetworkApi.md#create_firewall_reset_global_policy_item) | **POST** /platform/16/network/firewall/reset-global-policy | 
[**create_network_groupnet**](NetworkApi.md#create_network_groupnet) | **POST** /platform/10/network/groupnets | 
[**create_network_sc_rebalance_all_item**](NetworkApi.md#create_network_sc_rebalance_all_item) | **POST** /platform/3/network/sc-rebalance-all | 
[**delete_firewall_policy**](NetworkApi.md#delete_firewall_policy) | **DELETE** /platform/16/network/firewall/policies/{FirewallPolicyId} | 
[**delete_network_groupnet**](NetworkApi.md#delete_network_groupnet) | **DELETE** /platform/10/network/groupnets/{NetworkGroupnetId} | 
[**get_firewall_policy**](NetworkApi.md#get_firewall_policy) | **GET** /platform/16/network/firewall/policies/{FirewallPolicyId} | 
[**get_firewall_rules**](NetworkApi.md#get_firewall_rules) | **GET** /platform/16/network/firewall/rules | 
[**get_firewall_services**](NetworkApi.md#get_firewall_services) | **GET** /platform/16/network/firewall/services | 
[**get_firewall_settings**](NetworkApi.md#get_firewall_settings) | **GET** /platform/16/network/firewall/settings | 
[**get_network_dnscache**](NetworkApi.md#get_network_dnscache) | **GET** /platform/3/network/dnscache | 
[**get_network_external**](NetworkApi.md#get_network_external) | **GET** /platform/16/network/external | 
[**get_network_groupnet**](NetworkApi.md#get_network_groupnet) | **GET** /platform/10/network/groupnets/{NetworkGroupnetId} | 
[**get_network_interfaces**](NetworkApi.md#get_network_interfaces) | **GET** /platform/16/network/interfaces | 
[**get_network_pools**](NetworkApi.md#get_network_pools) | **GET** /platform/16/network/pools | 
[**get_network_rules**](NetworkApi.md#get_network_rules) | **GET** /platform/3/network/rules | 
[**get_network_subnets**](NetworkApi.md#get_network_subnets) | **GET** /platform/16/network/subnets | 
[**list_firewall_policies**](NetworkApi.md#list_firewall_policies) | **GET** /platform/16/network/firewall/policies | 
[**list_network_groupnets**](NetworkApi.md#list_network_groupnets) | **GET** /platform/10/network/groupnets | 
[**update_firewall_policy**](NetworkApi.md#update_firewall_policy) | **PUT** /platform/16/network/firewall/policies/{FirewallPolicyId} | 
[**update_firewall_settings**](NetworkApi.md#update_firewall_settings) | **PUT** /platform/16/network/firewall/settings | 
[**update_network_dnscache**](NetworkApi.md#update_network_dnscache) | **PUT** /platform/3/network/dnscache | 
[**update_network_external**](NetworkApi.md#update_network_external) | **PUT** /platform/16/network/external | 
[**update_network_groupnet**](NetworkApi.md#update_network_groupnet) | **PUT** /platform/10/network/groupnets/{NetworkGroupnetId} | 


# **create_dnscache_flush_item**
> Empty create_dnscache_flush_item(dnscache_flush_item)



Flush the DNSCache.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dnscache_flush_item = isilon_sdk.v9_5_0.Empty() # Empty | 

try:
    api_response = api_instance.create_dnscache_flush_item(dnscache_flush_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_dnscache_flush_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dnscache_flush_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_firewall_policy**
> CreateResponse create_firewall_policy(firewall_policy)



Create a new network policy with empty rules.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
firewall_policy = isilon_sdk.v9_5_0.FirewallPolicyCreateParams() # FirewallPolicyCreateParams | 

try:
    api_response = api_instance.create_firewall_policy(firewall_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_policy** | [**FirewallPolicyCreateParams**](FirewallPolicyCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_firewall_reset_global_policy_item**
> Empty create_firewall_reset_global_policy_item(firewall_reset_global_policy_item, live=live)



Reset global policies to default.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
firewall_reset_global_policy_item = isilon_sdk.v9_5_0.Empty() # Empty | 
live = true # bool | Live option must be used with global policies. Such reset will take effect immediately. (optional)

try:
    api_response = api_instance.create_firewall_reset_global_policy_item(firewall_reset_global_policy_item, live=live)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_firewall_reset_global_policy_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_reset_global_policy_item** | [**Empty**](Empty.md)|  | 
 **live** | **bool**| Live option must be used with global policies. Such reset will take effect immediately. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_groupnet**
> CreateResponse create_network_groupnet(network_groupnet)



Create a new groupnet.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
network_groupnet = isilon_sdk.v9_5_0.NetworkGroupnetCreateParams() # NetworkGroupnetCreateParams | 

try:
    api_response = api_instance.create_network_groupnet(network_groupnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_network_groupnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_groupnet** | [**NetworkGroupnetCreateParams**](NetworkGroupnetCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_sc_rebalance_all_item**
> Empty create_network_sc_rebalance_all_item(network_sc_rebalance_all_item)



Rebalance IP addresses in all pools.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
network_sc_rebalance_all_item = isilon_sdk.v9_5_0.Empty() # Empty | 

try:
    api_response = api_instance.create_network_sc_rebalance_all_item(network_sc_rebalance_all_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->create_network_sc_rebalance_all_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_sc_rebalance_all_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_firewall_policy**
> delete_firewall_policy(firewall_policy_id)



Delete a network firewall policy.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
firewall_policy_id = 'firewall_policy_id_example' # str | Delete a network firewall policy.

try:
    api_instance.delete_firewall_policy(firewall_policy_id)
except ApiException as e:
    print("Exception when calling NetworkApi->delete_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_policy_id** | **str**| Delete a network firewall policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_groupnet**
> delete_network_groupnet(network_groupnet_id)



Delete a network groupnet.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
network_groupnet_id = 'network_groupnet_id_example' # str | Delete a network groupnet.

try:
    api_instance.delete_network_groupnet(network_groupnet_id)
except ApiException as e:
    print("Exception when calling NetworkApi->delete_network_groupnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_groupnet_id** | **str**| Delete a network groupnet. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_policy**
> FirewallPolicies get_firewall_policy(firewall_policy_id)



View a network firewall policy.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
firewall_policy_id = 'firewall_policy_id_example' # str | View a network firewall policy.

try:
    api_response = api_instance.get_firewall_policy(firewall_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_policy_id** | **str**| View a network firewall policy. | 

### Return type

[**FirewallPolicies**](FirewallPolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_rules**
> FirewallRules get_firewall_rules(dir=dir, limit=limit, resume=resume, sort=sort)



Get a list of all firewall rules.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_firewall_rules(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_firewall_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**FirewallRules**](FirewallRules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_services**
> FirewallServices get_firewall_services(dir=dir, limit=limit, resume=resume, sort=sort)



View network firewall default services.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_firewall_services(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_firewall_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**FirewallServices**](FirewallServices.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firewall_settings**
> FirewallSettings get_firewall_settings()



View network firewall settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_firewall_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_firewall_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FirewallSettings**](FirewallSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_dnscache**
> NetworkDnscache get_network_dnscache()



View network dns cache settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_network_dnscache()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_dnscache: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkDnscache**](NetworkDnscache.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_external**
> NetworkExternal get_network_external()



View external network settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_network_external()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_external: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkExternal**](NetworkExternal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_groupnet**
> NetworkGroupnets get_network_groupnet(network_groupnet_id)



View a network groupnet.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
network_groupnet_id = 'network_groupnet_id_example' # str | View a network groupnet.

try:
    api_response = api_instance.get_network_groupnet(network_groupnet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_groupnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_groupnet_id** | **str**| View a network groupnet. | 

### Return type

[**NetworkGroupnets**](NetworkGroupnets.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_interfaces**
> NetworkInterfacesExtended get_network_interfaces(cache=cache, dir=dir, include_access_zones=include_access_zones, include_vlans=include_vlans, limit=limit, lnn=lnn, network=network, owner=owner, resume=resume, sort=sort, type=type, vlan_id=vlan_id)



Get a list of interfaces.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
cache = 'cache_example' # str | Control where interface data is source from. no-cache only returns live data from a running node, and if a node can't be reached, no results will be returned. cache-only only returns cached data, some fields are set as null/unknown if they can't be determined, and IPs listed are the IPs that should be configured. Finally, nodes-first will try to query live nodes, and fall back to the cache for any nodes that fail. Default: nodes-first (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
include_access_zones = true # bool | If include_access_zones is set to false, the \"access_zone\" field will be set to an empty string. (optional)
include_vlans = true # bool | If include_vlans is set to true, all vlans are returned unless further filtered by vlan_id. If include_vlans is set to false, no vlans are returned. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
lnn = [56] # list[int] | Get a list of interfaces for the specified lnns. (optional)
network = 'network_example' # str | Show interfaces associated with external and/or internal networks. Default is 'external' (optional)
owner = 'owner_example' # str | Filter results by owner id. Support partials matches too. Ex owner=groupnet0 or owner=groupnet0.subnet0.pool0. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
type = 'type_example' # str | Filter the returned IPs by IP type. (optional)
vlan_id = 56 # int | Only return IPs/interfaces configured in the specified VLAN ID (optional)

try:
    api_response = api_instance.get_network_interfaces(cache=cache, dir=dir, include_access_zones=include_access_zones, include_vlans=include_vlans, limit=limit, lnn=lnn, network=network, owner=owner, resume=resume, sort=sort, type=type, vlan_id=vlan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache** | **str**| Control where interface data is source from. no-cache only returns live data from a running node, and if a node can&#39;t be reached, no results will be returned. cache-only only returns cached data, some fields are set as null/unknown if they can&#39;t be determined, and IPs listed are the IPs that should be configured. Finally, nodes-first will try to query live nodes, and fall back to the cache for any nodes that fail. Default: nodes-first | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **include_access_zones** | **bool**| If include_access_zones is set to false, the \&quot;access_zone\&quot; field will be set to an empty string. | [optional] 
 **include_vlans** | **bool**| If include_vlans is set to true, all vlans are returned unless further filtered by vlan_id. If include_vlans is set to false, no vlans are returned. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **lnn** | [**list[int]**](int.md)| Get a list of interfaces for the specified lnns. | [optional] 
 **network** | **str**| Show interfaces associated with external and/or internal networks. Default is &#39;external&#39; | [optional] 
 **owner** | **str**| Filter results by owner id. Support partials matches too. Ex owner&#x3D;groupnet0 or owner&#x3D;groupnet0.subnet0.pool0. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **type** | **str**| Filter the returned IPs by IP type. | [optional] 
 **vlan_id** | **int**| Only return IPs/interfaces configured in the specified VLAN ID | [optional] 

### Return type

[**NetworkInterfacesExtended**](NetworkInterfacesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_pools**
> NetworkPools get_network_pools(access_zone=access_zone, alloc_method=alloc_method, dir=dir, groupnet=groupnet, limit=limit, resume=resume, sort=sort, subnet=subnet)



Get a list of network pools.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
access_zone = 'access_zone_example' # str | If specified, only pools with this zone name will be returned. (optional)
alloc_method = 'alloc_method_example' # str | If specified, only pools with this allocation type will be returned. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
groupnet = 'groupnet_example' # str | If specified, only pools for this groupnet will be returned. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
subnet = 'subnet_example' # str | If specified, only pools for this subnet will be returned. (optional)

try:
    api_response = api_instance.get_network_pools(access_zone=access_zone, alloc_method=alloc_method, dir=dir, groupnet=groupnet, limit=limit, resume=resume, sort=sort, subnet=subnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_zone** | **str**| If specified, only pools with this zone name will be returned. | [optional] 
 **alloc_method** | **str**| If specified, only pools with this allocation type will be returned. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **groupnet** | **str**| If specified, only pools for this groupnet will be returned. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **subnet** | **str**| If specified, only pools for this subnet will be returned. | [optional] 

### Return type

[**NetworkPools**](NetworkPools.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_rules**
> PoolsPoolRulesExtended get_network_rules(dir=dir, groupnet=groupnet, limit=limit, pool=pool, resume=resume, sort=sort, subnet=subnet)



Get a list of network rules.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
groupnet = 'groupnet_example' # str | Name of the groupnet to list rules from. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
pool = 'pool_example' # str | Name of the pool to list rules from. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
subnet = 'subnet_example' # str | Name of the subnet to list rules from. (optional)

try:
    api_response = api_instance.get_network_rules(dir=dir, groupnet=groupnet, limit=limit, pool=pool, resume=resume, sort=sort, subnet=subnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **groupnet** | **str**| Name of the groupnet to list rules from. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **pool** | **str**| Name of the pool to list rules from. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **subnet** | **str**| Name of the subnet to list rules from. | [optional] 

### Return type

[**PoolsPoolRulesExtended**](PoolsPoolRulesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_subnets**
> GroupnetSubnetsExtended get_network_subnets(dir=dir, groupnet=groupnet, limit=limit, resume=resume, sort=sort)



Get a list of subnets.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
groupnet = 'groupnet_example' # str | If specified, only subnets for this groupnet will be returned. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_network_subnets(dir=dir, groupnet=groupnet, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_subnets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **groupnet** | **str**| If specified, only subnets for this groupnet will be returned. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**GroupnetSubnetsExtended**](GroupnetSubnetsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_firewall_policies**
> FirewallPoliciesExtended list_firewall_policies(dir=dir, limit=limit, resume=resume, sort=sort)



Get a list of firewall policies.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_firewall_policies(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->list_firewall_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**FirewallPoliciesExtended**](FirewallPoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_groupnets**
> NetworkGroupnetsExtended list_network_groupnets(dir=dir, limit=limit, resume=resume, sort=sort)



Get a list of groupnets.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_network_groupnets(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->list_network_groupnets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**NetworkGroupnetsExtended**](NetworkGroupnetsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_policy**
> update_firewall_policy(firewall_policy, firewall_policy_id, clone=clone, live=live)



Modify a network firewall policy.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
firewall_policy = isilon_sdk.v9_5_0.FirewallPolicy() # FirewallPolicy | 
firewall_policy_id = 'firewall_policy_id_example' # str | Modify a network firewall policy.
clone = true # bool | Clone an existing policy to a new one. (optional)
live = true # bool | Live flag can only be used with active rules. Update will take effect immediately on all related network pools. (optional)

try:
    api_instance.update_firewall_policy(firewall_policy, firewall_policy_id, clone=clone, live=live)
except ApiException as e:
    print("Exception when calling NetworkApi->update_firewall_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_policy** | [**FirewallPolicy**](FirewallPolicy.md)|  | 
 **firewall_policy_id** | **str**| Modify a network firewall policy. | 
 **clone** | **bool**| Clone an existing policy to a new one. | [optional] 
 **live** | **bool**| Live flag can only be used with active rules. Update will take effect immediately on all related network pools. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_firewall_settings**
> update_firewall_settings(firewall_settings, force=force)



Modify network firewall settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
firewall_settings = isilon_sdk.v9_5_0.FirewallSettingsExtended() # FirewallSettingsExtended | 
force = true # bool | Force modify firewall settings, even if it leads to FTP service being blocked (optional)

try:
    api_instance.update_firewall_settings(firewall_settings, force=force)
except ApiException as e:
    print("Exception when calling NetworkApi->update_firewall_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_settings** | [**FirewallSettingsExtended**](FirewallSettingsExtended.md)|  | 
 **force** | **bool**| Force modify firewall settings, even if it leads to FTP service being blocked | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_dnscache**
> update_network_dnscache(network_dnscache)



Modify network dns cache settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
network_dnscache = isilon_sdk.v9_5_0.NetworkDnscacheExtended() # NetworkDnscacheExtended | 

try:
    api_instance.update_network_dnscache(network_dnscache)
except ApiException as e:
    print("Exception when calling NetworkApi->update_network_dnscache: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_dnscache** | [**NetworkDnscacheExtended**](NetworkDnscacheExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_external**
> update_network_external(network_external)



Modify external network settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
network_external = isilon_sdk.v9_5_0.NetworkExternalExtended() # NetworkExternalExtended | 

try:
    api_instance.update_network_external(network_external)
except ApiException as e:
    print("Exception when calling NetworkApi->update_network_external: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_external** | [**NetworkExternalExtended**](NetworkExternalExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_groupnet**
> update_network_groupnet(network_groupnet, network_groupnet_id)



Modify a network groupnet.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.NetworkApi(isilon_sdk.v9_5_0.ApiClient(configuration))
network_groupnet = isilon_sdk.v9_5_0.NetworkGroupnet() # NetworkGroupnet | 
network_groupnet_id = 'network_groupnet_id_example' # str | Modify a network groupnet.

try:
    api_instance.update_network_groupnet(network_groupnet, network_groupnet_id)
except ApiException as e:
    print("Exception when calling NetworkApi->update_network_groupnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_groupnet** | [**NetworkGroupnet**](NetworkGroupnet.md)|  | 
 **network_groupnet_id** | **str**| Modify a network groupnet. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

