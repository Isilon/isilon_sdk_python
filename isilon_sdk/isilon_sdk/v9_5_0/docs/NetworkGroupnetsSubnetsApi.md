# isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pools_pool_rebalance_ip**](NetworkGroupnetsSubnetsApi.md#create_pools_pool_rebalance_ip) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rebalance-ips | 
[**create_pools_pool_rule**](NetworkGroupnetsSubnetsApi.md#create_pools_pool_rule) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules | 
[**create_pools_pool_sc_resume_node**](NetworkGroupnetsSubnetsApi.md#create_pools_pool_sc_resume_node) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/sc-resume-nodes | 
[**create_pools_pool_sc_suspend_node**](NetworkGroupnetsSubnetsApi.md#create_pools_pool_sc_suspend_node) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/sc-suspend-nodes | 
[**delete_pools_pool_rule**](NetworkGroupnetsSubnetsApi.md#delete_pools_pool_rule) | **DELETE** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules/{PoolsPoolRuleId} | 
[**get_pools_pool_interfaces**](NetworkGroupnetsSubnetsApi.md#get_pools_pool_interfaces) | **GET** /platform/7/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/interfaces | 
[**get_pools_pool_rule**](NetworkGroupnetsSubnetsApi.md#get_pools_pool_rule) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules/{PoolsPoolRuleId} | 
[**get_pools_pool_status**](NetworkGroupnetsSubnetsApi.md#get_pools_pool_status) | **GET** /platform/15/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/status | 
[**list_pools_pool_rules**](NetworkGroupnetsSubnetsApi.md#list_pools_pool_rules) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules | 
[**update_pools_pool_rule**](NetworkGroupnetsSubnetsApi.md#update_pools_pool_rule) | **PUT** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules/{PoolsPoolRuleId} | 


# **create_pools_pool_rebalance_ip**
> Empty create_pools_pool_rebalance_ip(pools_pool_rebalance_ip, groupnet, subnet, pool)



Rebalance IP addresses in specified pool.

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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
pools_pool_rebalance_ip = isilon_sdk.v9_5_0.Empty() # Empty | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try:
    api_response = api_instance.create_pools_pool_rebalance_ip(pools_pool_rebalance_ip, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->create_pools_pool_rebalance_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools_pool_rebalance_ip** | [**Empty**](Empty.md)|  | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pools_pool_rule**
> CreateResponse create_pools_pool_rule(pools_pool_rule, groupnet, subnet, pool)



Create a new rule.

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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
pools_pool_rule = isilon_sdk.v9_5_0.PoolsPoolRuleCreateParams() # PoolsPoolRuleCreateParams | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try:
    api_response = api_instance.create_pools_pool_rule(pools_pool_rule, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->create_pools_pool_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools_pool_rule** | [**PoolsPoolRuleCreateParams**](PoolsPoolRuleCreateParams.md)|  | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pools_pool_sc_resume_node**
> Empty create_pools_pool_sc_resume_node(pools_pool_sc_resume_node, groupnet, subnet, pool)



Resume suspended nodes.

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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
pools_pool_sc_resume_node = isilon_sdk.v9_5_0.PoolsPoolScResumeNode() # PoolsPoolScResumeNode | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try:
    api_response = api_instance.create_pools_pool_sc_resume_node(pools_pool_sc_resume_node, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->create_pools_pool_sc_resume_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools_pool_sc_resume_node** | [**PoolsPoolScResumeNode**](PoolsPoolScResumeNode.md)|  | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pools_pool_sc_suspend_node**
> Empty create_pools_pool_sc_suspend_node(pools_pool_sc_suspend_node, groupnet, subnet, pool)



Suspend nodes.

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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
pools_pool_sc_suspend_node = isilon_sdk.v9_5_0.PoolsPoolScResumeNode() # PoolsPoolScResumeNode | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try:
    api_response = api_instance.create_pools_pool_sc_suspend_node(pools_pool_sc_suspend_node, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->create_pools_pool_sc_suspend_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools_pool_sc_suspend_node** | [**PoolsPoolScResumeNode**](PoolsPoolScResumeNode.md)|  | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pools_pool_rule**
> delete_pools_pool_rule(pools_pool_rule_id, groupnet, subnet, pool)



Delete a network rule.

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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
pools_pool_rule_id = 'pools_pool_rule_id_example' # str | Delete a network rule.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try:
    api_instance.delete_pools_pool_rule(pools_pool_rule_id, groupnet, subnet, pool)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->delete_pools_pool_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools_pool_rule_id** | **str**| Delete a network rule. | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pools_pool_interfaces**
> PoolsPoolInterfaces get_pools_pool_interfaces(groupnet, subnet, pool, dir=dir, limit=limit, lnns=lnns, resume=resume, sort=sort)



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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
lnns = 'lnns_example' # str | Get a list of interfaces for the specified lnn. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_pools_pool_interfaces(groupnet, subnet, pool, dir=dir, limit=limit, lnns=lnns, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->get_pools_pool_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **lnns** | **str**| Get a list of interfaces for the specified lnn. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**PoolsPoolInterfaces**](PoolsPoolInterfaces.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pools_pool_rule**
> PoolsPoolRules get_pools_pool_rule(pools_pool_rule_id, groupnet, subnet, pool)



View a single network rule.

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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
pools_pool_rule_id = 'pools_pool_rule_id_example' # str | View a single network rule.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try:
    api_response = api_instance.get_pools_pool_rule(pools_pool_rule_id, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->get_pools_pool_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools_pool_rule_id** | **str**| View a single network rule. | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 

### Return type

[**PoolsPoolRules**](PoolsPoolRules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pools_pool_status**
> PoolsPoolStatus get_pools_pool_status(groupnet, subnet, pool, show_all=show_all)



View the status of a single network pool.

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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 
show_all = true # bool | Whether or not OneFS should return all nodes configured in the network pool, even if SmartConnect doesn't detect any problem with the nodes. Default: only return nodes that can't be resolved via DNS. (optional)

try:
    api_response = api_instance.get_pools_pool_status(groupnet, subnet, pool, show_all=show_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->get_pools_pool_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 
 **show_all** | **bool**| Whether or not OneFS should return all nodes configured in the network pool, even if SmartConnect doesn&#39;t detect any problem with the nodes. Default: only return nodes that can&#39;t be resolved via DNS. | [optional] 

### Return type

[**PoolsPoolStatus**](PoolsPoolStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pools_pool_rules**
> PoolsPoolRulesExtended list_pools_pool_rules(groupnet, subnet, pool, dir=dir, limit=limit, resume=resume, sort=sort)



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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_pools_pool_rules(groupnet, subnet, pool, dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->list_pools_pool_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**PoolsPoolRulesExtended**](PoolsPoolRulesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pools_pool_rule**
> update_pools_pool_rule(pools_pool_rule, pools_pool_rule_id, groupnet, subnet, pool)



Modify a network rule.

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
api_instance = isilon_sdk.v9_5_0.NetworkGroupnetsSubnetsApi(isilon_sdk.v9_5_0.ApiClient(configuration))
pools_pool_rule = isilon_sdk.v9_5_0.PoolsPoolRule() # PoolsPoolRule | 
pools_pool_rule_id = 'pools_pool_rule_id_example' # str | Modify a network rule.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try:
    api_instance.update_pools_pool_rule(pools_pool_rule, pools_pool_rule_id, groupnet, subnet, pool)
except ApiException as e:
    print("Exception when calling NetworkGroupnetsSubnetsApi->update_pools_pool_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pools_pool_rule** | [**PoolsPoolRule**](PoolsPoolRule.md)|  | 
 **pools_pool_rule_id** | **str**| Modify a network rule. | 
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

