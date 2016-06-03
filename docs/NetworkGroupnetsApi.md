# isi_sdk.NetworkGroupnetsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_groupnet_subnet**](NetworkGroupnetsApi.md#create_groupnet_subnet) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets | 
[**create_subnets_subnet_pool**](NetworkGroupnetsApi.md#create_subnets_subnet_pool) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools | 
[**delete_groupnet_subnet**](NetworkGroupnetsApi.md#delete_groupnet_subnet) | **DELETE** /platform/3/network/groupnets/{Groupnet}/subnets/{GroupnetSubnetId} | 
[**delete_subnets_subnet_pool**](NetworkGroupnetsApi.md#delete_subnets_subnet_pool) | **DELETE** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{SubnetsSubnetPoolId} | 
[**get_groupnet_subnet**](NetworkGroupnetsApi.md#get_groupnet_subnet) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets/{GroupnetSubnetId} | 
[**get_subnets_subnet_pool**](NetworkGroupnetsApi.md#get_subnets_subnet_pool) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{SubnetsSubnetPoolId} | 
[**list_groupnet_subnets**](NetworkGroupnetsApi.md#list_groupnet_subnets) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets | 
[**list_subnets_subnet_pools**](NetworkGroupnetsApi.md#list_subnets_subnet_pools) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools | 
[**update_groupnet_subnet**](NetworkGroupnetsApi.md#update_groupnet_subnet) | **PUT** /platform/3/network/groupnets/{Groupnet}/subnets/{GroupnetSubnetId} | 
[**update_subnets_subnet_pool**](NetworkGroupnetsApi.md#update_subnets_subnet_pool) | **PUT** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{SubnetsSubnetPoolId} | 


# **create_groupnet_subnet**
> CreateResponse create_groupnet_subnet(groupnet_subnet, groupnet)



Create a new subnet.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
groupnet_subnet = isi_sdk.GroupnetSubnetCreateParams() # GroupnetSubnetCreateParams | 
groupnet = 'groupnet_example' # str | 

try: 
    api_response = api_instance.create_groupnet_subnet(groupnet_subnet, groupnet)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->create_groupnet_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet_subnet** | [**GroupnetSubnetCreateParams**](GroupnetSubnetCreateParams.md)|  | 
 **groupnet** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subnets_subnet_pool**
> CreateResponse create_subnets_subnet_pool(subnets_subnet_pool, groupnet, subnet, force=force)



Create a new pool.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
subnets_subnet_pool = isi_sdk.SubnetsSubnetPoolCreateParams() # SubnetsSubnetPoolCreateParams | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
force = true # bool | force creating this pool even if it causes an MTU conflict. (optional)

try: 
    api_response = api_instance.create_subnets_subnet_pool(subnets_subnet_pool, groupnet, subnet, force=force)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->create_subnets_subnet_pool: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnets_subnet_pool** | [**SubnetsSubnetPoolCreateParams**](SubnetsSubnetPoolCreateParams.md)|  | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **force** | **bool**| force creating this pool even if it causes an MTU conflict. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_groupnet_subnet**
> delete_groupnet_subnet(groupnet_subnet_id, groupnet, force=force)



Delete a network subnet..

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
groupnet_subnet_id = 'groupnet_subnet_id_example' # str | Delete a network subnet..
groupnet = 'groupnet_example' # str | 
force = true # bool | force deleting this subnet even if pools in other subnets rely on this subnet's SC VIP. (optional)

try: 
    api_instance.delete_groupnet_subnet(groupnet_subnet_id, groupnet, force=force)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->delete_groupnet_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet_subnet_id** | **str**| Delete a network subnet.. | 
 **groupnet** | **str**|  | 
 **force** | **bool**| force deleting this subnet even if pools in other subnets rely on this subnet&#39;s SC VIP. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subnets_subnet_pool**
> delete_subnets_subnet_pool(subnets_subnet_pool_id, groupnet, subnet)



Delete a network pool.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
subnets_subnet_pool_id = 'subnets_subnet_pool_id_example' # str | Delete a network pool.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 

try: 
    api_instance.delete_subnets_subnet_pool(subnets_subnet_pool_id, groupnet, subnet)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->delete_subnets_subnet_pool: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groupnet_subnet**
> GroupnetSubnets get_groupnet_subnet(groupnet_subnet_id, groupnet, force=force)



View a network subnet.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
groupnet_subnet_id = 'groupnet_subnet_id_example' # str | View a network subnet.
groupnet = 'groupnet_example' # str | 
force = true # bool | force modifying this subnet even if it causes an MTU conflict. (optional)

try: 
    api_response = api_instance.get_groupnet_subnet(groupnet_subnet_id, groupnet, force=force)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->get_groupnet_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet_subnet_id** | **str**| View a network subnet. | 
 **groupnet** | **str**|  | 
 **force** | **bool**| force modifying this subnet even if it causes an MTU conflict. | [optional] 

### Return type

[**GroupnetSubnets**](GroupnetSubnets.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subnets_subnet_pool**
> SubnetsSubnetPools get_subnets_subnet_pool(subnets_subnet_pool_id, groupnet, subnet)



View a single network pool.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
subnets_subnet_pool_id = 'subnets_subnet_pool_id_example' # str | View a single network pool.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 

try: 
    api_response = api_instance.get_subnets_subnet_pool(subnets_subnet_pool_id, groupnet, subnet)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->get_subnets_subnet_pool: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groupnet_subnets**
> GroupnetSubnetsExtended list_groupnet_subnets(groupnet, sort=sort, limit=limit, dir=dir, resume=resume)



Get a list of subnets.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
groupnet = 'groupnet_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try: 
    api_response = api_instance.list_groupnet_subnets(groupnet, sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->list_groupnet_subnets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**GroupnetSubnetsExtended**](GroupnetSubnetsExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subnets_subnet_pools**
> SubnetsSubnetPoolsExtended list_subnets_subnet_pools(groupnet, subnet, sort=sort, resume=resume, access_zone=access_zone, alloc_method=alloc_method, limit=limit, dir=dir)



Get a list of network pools.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
access_zone = 'access_zone_example' # str | If specified, only pools with this zone name will be returned. (optional)
alloc_method = 'alloc_method_example' # str | If specified, only pools with this allocation type will be returned. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.list_subnets_subnet_pools(groupnet, subnet, sort=sort, resume=resume, access_zone=access_zone, alloc_method=alloc_method, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->list_subnets_subnet_pools: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **access_zone** | **str**| If specified, only pools with this zone name will be returned. | [optional] 
 **alloc_method** | **str**| If specified, only pools with this allocation type will be returned. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**SubnetsSubnetPoolsExtended**](SubnetsSubnetPoolsExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_groupnet_subnet**
> update_groupnet_subnet(groupnet_subnet, groupnet_subnet_id, groupnet)



Modify a network subnet.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
groupnet_subnet = isi_sdk.GroupnetSubnet() # GroupnetSubnet | 
groupnet_subnet_id = 'groupnet_subnet_id_example' # str | Modify a network subnet.
groupnet = 'groupnet_example' # str | 

try: 
    api_instance.update_groupnet_subnet(groupnet_subnet, groupnet_subnet_id, groupnet)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->update_groupnet_subnet: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet_subnet** | [**GroupnetSubnet**](GroupnetSubnet.md)|  | 
 **groupnet_subnet_id** | **str**| Modify a network subnet. | 
 **groupnet** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subnets_subnet_pool**
> update_subnets_subnet_pool(subnets_subnet_pool, subnets_subnet_pool_id, groupnet, subnet, force=force)



Modify a network pool.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.NetworkGroupnetsApi()
subnets_subnet_pool = isi_sdk.SubnetsSubnetPool() # SubnetsSubnetPool | 
subnets_subnet_pool_id = 'subnets_subnet_pool_id_example' # str | Modify a network pool.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
force = true # bool | force creating this pool even if it causes an MTU conflict. (optional)

try: 
    api_instance.update_subnets_subnet_pool(subnets_subnet_pool, subnets_subnet_pool_id, groupnet, subnet, force=force)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsApi->update_subnets_subnet_pool: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subnets_subnet_pool** | [**SubnetsSubnetPool**](SubnetsSubnetPool.md)|  | 
 **subnets_subnet_pool_id** | **str**| Modify a network pool. | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **force** | **bool**| force creating this pool even if it causes an MTU conflict. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

