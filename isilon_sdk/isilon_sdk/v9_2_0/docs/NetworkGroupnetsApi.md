# isilon_sdk.v9_2_0.NetworkGroupnetsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_groupnet_subnet**](NetworkGroupnetsApi.md#create_groupnet_subnet) | **POST** /platform/12/network/groupnets/{Groupnet}/subnets | 
[**create_subnets_subnet_pool**](NetworkGroupnetsApi.md#create_subnets_subnet_pool) | **POST** /platform/12/network/groupnets/{Groupnet}/subnets/{Subnet}/pools | 
[**delete_groupnet_subnet**](NetworkGroupnetsApi.md#delete_groupnet_subnet) | **DELETE** /platform/12/network/groupnets/{Groupnet}/subnets/{GroupnetSubnetId} | 
[**delete_subnets_subnet_pool**](NetworkGroupnetsApi.md#delete_subnets_subnet_pool) | **DELETE** /platform/12/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{SubnetsSubnetPoolId} | 
[**get_groupnet_subnet**](NetworkGroupnetsApi.md#get_groupnet_subnet) | **GET** /platform/12/network/groupnets/{Groupnet}/subnets/{GroupnetSubnetId} | 
[**get_subnets_subnet_pool**](NetworkGroupnetsApi.md#get_subnets_subnet_pool) | **GET** /platform/12/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{SubnetsSubnetPoolId} | 
[**list_groupnet_subnets**](NetworkGroupnetsApi.md#list_groupnet_subnets) | **GET** /platform/12/network/groupnets/{Groupnet}/subnets | 
[**list_subnets_subnet_pools**](NetworkGroupnetsApi.md#list_subnets_subnet_pools) | **GET** /platform/12/network/groupnets/{Groupnet}/subnets/{Subnet}/pools | 
[**update_groupnet_subnet**](NetworkGroupnetsApi.md#update_groupnet_subnet) | **PUT** /platform/12/network/groupnets/{Groupnet}/subnets/{GroupnetSubnetId} | 
[**update_subnets_subnet_pool**](NetworkGroupnetsApi.md#update_subnets_subnet_pool) | **PUT** /platform/12/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{SubnetsSubnetPoolId} | 


# **create_groupnet_subnet**
> CreateResponse create_groupnet_subnet(groupnet_subnet, groupnet)



Create a new subnet.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
groupnet_subnet = isilon_sdk.v9_2_0.GroupnetSubnetCreateParams() # GroupnetSubnetCreateParams | 
groupnet = 'groupnet_example' # str | 

try:
    api_response = api_instance.create_groupnet_subnet(groupnet_subnet, groupnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->create_groupnet_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet_subnet** | [**GroupnetSubnetCreateParams**](GroupnetSubnetCreateParams.md)|  | 
 **groupnet** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subnets_subnet_pool**
> CreateResponse create_subnets_subnet_pool(subnets_subnet_pool, groupnet, subnet, force=force)



Create a new pool.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
subnets_subnet_pool = isilon_sdk.v9_2_0.SubnetsSubnetPoolCreateParams() # SubnetsSubnetPoolCreateParams | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
force = true # bool | Force creating this pool even if it causes an MTU conflict. (optional)

try:
    api_response = api_instance.create_subnets_subnet_pool(subnets_subnet_pool, groupnet, subnet, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->create_subnets_subnet_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnets_subnet_pool** | [**SubnetsSubnetPoolCreateParams**](SubnetsSubnetPoolCreateParams.md)|  | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **force** | **bool**| Force creating this pool even if it causes an MTU conflict. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groupnet_subnet**
> delete_groupnet_subnet(groupnet_subnet_id, groupnet, force=force)



Delete a network subnet.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
groupnet_subnet_id = 'groupnet_subnet_id_example' # str | Delete a network subnet.
groupnet = 'groupnet_example' # str | 
force = true # bool | Force deleting this subnet even if pools in other subnets rely on this subnet's SC VIP. (optional)

try:
    api_instance.delete_groupnet_subnet(groupnet_subnet_id, groupnet, force=force)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->delete_groupnet_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet_subnet_id** | **str**| Delete a network subnet. | 
 **groupnet** | **str**|  | 
 **force** | **bool**| Force deleting this subnet even if pools in other subnets rely on this subnet&#39;s SC VIP. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subnets_subnet_pool**
> delete_subnets_subnet_pool(subnets_subnet_pool_id, groupnet, subnet)



Delete a network pool.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
subnets_subnet_pool_id = 'subnets_subnet_pool_id_example' # str | Delete a network pool.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 

try:
    api_instance.delete_subnets_subnet_pool(subnets_subnet_pool_id, groupnet, subnet)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->delete_subnets_subnet_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnets_subnet_pool_id** | **str**| Delete a network pool. | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groupnet_subnet**
> GroupnetSubnets get_groupnet_subnet(groupnet_subnet_id, groupnet)



View a network subnet.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
groupnet_subnet_id = 'groupnet_subnet_id_example' # str | View a network subnet.
groupnet = 'groupnet_example' # str | 

try:
    api_response = api_instance.get_groupnet_subnet(groupnet_subnet_id, groupnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->get_groupnet_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet_subnet_id** | **str**| View a network subnet. | 
 **groupnet** | **str**|  | 

### Return type

[**GroupnetSubnets**](GroupnetSubnets.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnets_subnet_pool**
> SubnetsSubnetPools get_subnets_subnet_pool(subnets_subnet_pool_id, groupnet, subnet)



View a single network pool.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
subnets_subnet_pool_id = 'subnets_subnet_pool_id_example' # str | View a single network pool.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 

try:
    api_response = api_instance.get_subnets_subnet_pool(subnets_subnet_pool_id, groupnet, subnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->get_subnets_subnet_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnets_subnet_pool_id** | **str**| View a single network pool. | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 

### Return type

[**SubnetsSubnetPools**](SubnetsSubnetPools.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groupnet_subnets**
> GroupnetSubnetsExtended list_groupnet_subnets(groupnet, dir=dir, limit=limit, resume=resume, sort=sort)



Get a list of subnets.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
groupnet = 'groupnet_example' # str | 
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_groupnet_subnets(groupnet, dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->list_groupnet_subnets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **dir** | **str**| The direction of the sort. | [optional] 
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

# **list_subnets_subnet_pools**
> SubnetsSubnetPoolsExtended list_subnets_subnet_pools(groupnet, subnet, access_zone=access_zone, alloc_method=alloc_method, dir=dir, limit=limit, resume=resume, sort=sort)



Get a list of network pools.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
access_zone = 'access_zone_example' # str | If specified, only pools with this zone name will be returned. (optional)
alloc_method = 'alloc_method_example' # str | If specified, only pools with this allocation type will be returned. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_subnets_subnet_pools(groupnet, subnet, access_zone=access_zone, alloc_method=alloc_method, dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->list_subnets_subnet_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **access_zone** | **str**| If specified, only pools with this zone name will be returned. | [optional] 
 **alloc_method** | **str**| If specified, only pools with this allocation type will be returned. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**SubnetsSubnetPoolsExtended**](SubnetsSubnetPoolsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_groupnet_subnet**
> update_groupnet_subnet(groupnet_subnet, groupnet_subnet_id, groupnet, force=force)



Modify a network subnet.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
groupnet_subnet = isilon_sdk.v9_2_0.GroupnetSubnet() # GroupnetSubnet | 
groupnet_subnet_id = 'groupnet_subnet_id_example' # str | Modify a network subnet.
groupnet = 'groupnet_example' # str | 
force = true # bool | Force modifying this subnet even if it causes an MTU conflict. (optional)

try:
    api_instance.update_groupnet_subnet(groupnet_subnet, groupnet_subnet_id, groupnet, force=force)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->update_groupnet_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet_subnet** | [**GroupnetSubnet**](GroupnetSubnet.md)|  | 
 **groupnet_subnet_id** | **str**| Modify a network subnet. | 
 **groupnet** | **str**|  | 
 **force** | **bool**| Force modifying this subnet even if it causes an MTU conflict. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subnets_subnet_pool**
> update_subnets_subnet_pool(subnets_subnet_pool, subnets_subnet_pool_id, groupnet, subnet, force=force)



Modify a network pool.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.NetworkGroupnetsApi(isilon_sdk.v9_2_0.ApiClient(configuration))
subnets_subnet_pool = isilon_sdk.v9_2_0.SubnetsSubnetPool() # SubnetsSubnetPool | 
subnets_subnet_pool_id = 'subnets_subnet_pool_id_example' # str | Modify a network pool.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
force = true # bool | Force creating this pool even if it causes an MTU conflict. (optional)

try:
    api_instance.update_subnets_subnet_pool(subnets_subnet_pool, subnets_subnet_pool_id, groupnet, subnet, force=force)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsApi->update_subnets_subnet_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnets_subnet_pool** | [**SubnetsSubnetPool**](SubnetsSubnetPool.md)|  | 
 **subnets_subnet_pool_id** | **str**| Modify a network pool. | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **force** | **bool**| Force creating this pool even if it causes an MTU conflict. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

