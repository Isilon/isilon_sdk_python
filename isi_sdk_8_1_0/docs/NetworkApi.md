# isi_sdk_8_1_0.NetworkApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dnscache_flush_item**](NetworkApi.md#create_dnscache_flush_item) | **POST** /platform/3/network/dnscache/flush | 
[**create_network_groupnet**](NetworkApi.md#create_network_groupnet) | **POST** /platform/3/network/groupnets | 
[**create_network_sc_rebalance_all_item**](NetworkApi.md#create_network_sc_rebalance_all_item) | **POST** /platform/3/network/sc-rebalance-all | 
[**delete_network_groupnet**](NetworkApi.md#delete_network_groupnet) | **DELETE** /platform/3/network/groupnets/{NetworkGroupnetId} | 
[**get_network_dnscache**](NetworkApi.md#get_network_dnscache) | **GET** /platform/3/network/dnscache | 
[**get_network_external**](NetworkApi.md#get_network_external) | **GET** /platform/3/network/external | 
[**get_network_groupnet**](NetworkApi.md#get_network_groupnet) | **GET** /platform/3/network/groupnets/{NetworkGroupnetId} | 
[**get_network_interfaces**](NetworkApi.md#get_network_interfaces) | **GET** /platform/4/network/interfaces | 
[**get_network_pools**](NetworkApi.md#get_network_pools) | **GET** /platform/3/network/pools | 
[**get_network_rules**](NetworkApi.md#get_network_rules) | **GET** /platform/3/network/rules | 
[**get_network_subnets**](NetworkApi.md#get_network_subnets) | **GET** /platform/4/network/subnets | 
[**list_network_groupnets**](NetworkApi.md#list_network_groupnets) | **GET** /platform/3/network/groupnets | 
[**update_network_dnscache**](NetworkApi.md#update_network_dnscache) | **PUT** /platform/3/network/dnscache | 
[**update_network_external**](NetworkApi.md#update_network_external) | **PUT** /platform/3/network/external | 
[**update_network_groupnet**](NetworkApi.md#update_network_groupnet) | **PUT** /platform/3/network/groupnets/{NetworkGroupnetId} | 


# **create_dnscache_flush_item**
> Empty create_dnscache_flush_item(dnscache_flush_item)



Flush the DNSCache.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
dnscache_flush_item = isi_sdk_8_1_0.Empty() # Empty | 

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

# **create_network_groupnet**
> CreateResponse create_network_groupnet(network_groupnet)



Create a new groupnet.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
network_groupnet = isi_sdk_8_1_0.NetworkGroupnetCreateParams() # NetworkGroupnetCreateParams | 

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
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
network_sc_rebalance_all_item = isi_sdk_8_1_0.Empty() # Empty | 

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

# **delete_network_groupnet**
> delete_network_groupnet(network_groupnet_id)



Delete a network groupnet.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
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

# **get_network_dnscache**
> NetworkDnscache get_network_dnscache()



View network dns cache settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))

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
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))

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
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
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
> PoolsPoolInterfaces get_network_interfaces(sort=sort, network=network, resume=resume, lnns=lnns, alloc_method=alloc_method, limit=limit, dir=dir)



Get a list of interfaces.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
network = 'network_example' # str | Show interfaces associated with external and/or internal networks. Default is 'external' (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
lnns = 'lnns_example' # str | Get a list of interfaces for the specified lnn. (optional)
alloc_method = 'alloc_method_example' # str | Filter addresses and owners by pool address allocation method. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_network_interfaces(sort=sort, network=network, resume=resume, lnns=lnns, alloc_method=alloc_method, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **network** | **str**| Show interfaces associated with external and/or internal networks. Default is &#39;external&#39; | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **lnns** | **str**| Get a list of interfaces for the specified lnn. | [optional] 
 **alloc_method** | **str**| Filter addresses and owners by pool address allocation method. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**PoolsPoolInterfaces**](PoolsPoolInterfaces.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_pools**
> NetworkPools get_network_pools(sort=sort, subnet=subnet, resume=resume, access_zone=access_zone, alloc_method=alloc_method, limit=limit, groupnet=groupnet, dir=dir)



Get a list of flexnet pools.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
subnet = 'subnet_example' # str | If specified, only pools for this subnet will be returned. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
access_zone = 'access_zone_example' # str | If specified, only pools with this zone name will be returned. (optional)
alloc_method = 'alloc_method_example' # str | If specified, only pools with this allocation type will be returned. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
groupnet = 'groupnet_example' # str | If specified, only pools for this groupnet will be returned. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_network_pools(sort=sort, subnet=subnet, resume=resume, access_zone=access_zone, alloc_method=alloc_method, limit=limit, groupnet=groupnet, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **subnet** | **str**| If specified, only pools for this subnet will be returned. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **access_zone** | **str**| If specified, only pools with this zone name will be returned. | [optional] 
 **alloc_method** | **str**| If specified, only pools with this allocation type will be returned. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **groupnet** | **str**| If specified, only pools for this groupnet will be returned. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**NetworkPools**](NetworkPools.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_rules**
> PoolsPoolRulesExtended get_network_rules(sort=sort, subnet=subnet, resume=resume, limit=limit, dir=dir, groupnet=groupnet, pool=pool)



Get a list of network rules.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
subnet = 'subnet_example' # str | Name of the subnet to list rules from. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
groupnet = 'groupnet_example' # str | Name of the groupnet to list rules from. (optional)
pool = 'pool_example' # str | Name of the pool to list rules from. (optional)

try:
    api_response = api_instance.get_network_rules(sort=sort, subnet=subnet, resume=resume, limit=limit, dir=dir, groupnet=groupnet, pool=pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **subnet** | **str**| Name of the subnet to list rules from. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **groupnet** | **str**| Name of the groupnet to list rules from. | [optional] 
 **pool** | **str**| Name of the pool to list rules from. | [optional] 

### Return type

[**PoolsPoolRulesExtended**](PoolsPoolRulesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_subnets**
> GroupnetSubnetsExtended get_network_subnets(sort=sort, groupnet=groupnet, limit=limit, dir=dir, resume=resume)



Get a list of subnets.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
groupnet = 'groupnet_example' # str | If specified, only subnets for this groupnet will be returned. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_network_subnets(sort=sort, groupnet=groupnet, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->get_network_subnets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **groupnet** | **str**| If specified, only subnets for this groupnet will be returned. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**GroupnetSubnetsExtended**](GroupnetSubnetsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_groupnets**
> NetworkGroupnetsExtended list_network_groupnets(sort=sort, limit=limit, dir=dir, resume=resume)



Get a list of groupnets.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_network_groupnets(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkApi->list_network_groupnets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NetworkGroupnetsExtended**](NetworkGroupnetsExtended.md)

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
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
network_dnscache = isi_sdk_8_1_0.NetworkDnscacheExtended() # NetworkDnscacheExtended | 

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
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
network_external = isi_sdk_8_1_0.NetworkExternalExtended() # NetworkExternalExtended | 

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
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.NetworkApi(isi_sdk_8_1_0.ApiClient(configuration))
network_groupnet = isi_sdk_8_1_0.NetworkGroupnet() # NetworkGroupnet | 
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

