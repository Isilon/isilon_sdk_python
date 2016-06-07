# isi_sdk.NetworkGroupnetsSubnetsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pools_pool_rebalance_ip**](NetworkGroupnetsSubnetsApi.md#create_pools_pool_rebalance_ip) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rebalance-ips | 
[**create_pools_pool_rule**](NetworkGroupnetsSubnetsApi.md#create_pools_pool_rule) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules | 
[**create_pools_pool_sc_resume_node**](NetworkGroupnetsSubnetsApi.md#create_pools_pool_sc_resume_node) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/sc-resume-nodes | 
[**create_pools_pool_sc_suspend_node**](NetworkGroupnetsSubnetsApi.md#create_pools_pool_sc_suspend_node) | **POST** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/sc-suspend-nodes | 
[**delete_pools_pool_rule**](NetworkGroupnetsSubnetsApi.md#delete_pools_pool_rule) | **DELETE** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules/{PoolsPoolRuleId} | 
[**get_pools_pool_interfaces**](NetworkGroupnetsSubnetsApi.md#get_pools_pool_interfaces) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/interfaces | 
[**get_pools_pool_rule**](NetworkGroupnetsSubnetsApi.md#get_pools_pool_rule) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules/{PoolsPoolRuleId} | 
[**list_pools_pool_rules**](NetworkGroupnetsSubnetsApi.md#list_pools_pool_rules) | **GET** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules | 
[**update_pools_pool_rule**](NetworkGroupnetsSubnetsApi.md#update_pools_pool_rule) | **PUT** /platform/3/network/groupnets/{Groupnet}/subnets/{Subnet}/pools/{Pool}/rules/{PoolsPoolRuleId} | 


# **create_pools_pool_rebalance_ip**
> Empty create_pools_pool_rebalance_ip(pools_pool_rebalance_ip, groupnet, subnet, pool)



Rebalance IP addresses in specified pool.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
pools_pool_rebalance_ip = isi_sdk.Empty() # Empty | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try: 
    api_response = api_instance.create_pools_pool_rebalance_ip(pools_pool_rebalance_ip, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->create_pools_pool_rebalance_ip: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pools_pool_rule**
> CreateResponse create_pools_pool_rule(pools_pool_rule, groupnet, subnet, pool)



Create a new rule.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
pools_pool_rule = isi_sdk.PoolsPoolRuleCreateParams() # PoolsPoolRuleCreateParams | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try: 
    api_response = api_instance.create_pools_pool_rule(pools_pool_rule, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->create_pools_pool_rule: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pools_pool_sc_resume_node**
> Empty create_pools_pool_sc_resume_node(pools_pool_sc_resume_node, groupnet, subnet, pool)



Resume suspended nodes.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
pools_pool_sc_resume_node = isi_sdk.PoolsPoolScResumeNode() # PoolsPoolScResumeNode | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try: 
    api_response = api_instance.create_pools_pool_sc_resume_node(pools_pool_sc_resume_node, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->create_pools_pool_sc_resume_node: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pools_pool_sc_suspend_node**
> Empty create_pools_pool_sc_suspend_node(pools_pool_sc_suspend_node, groupnet, subnet, pool)



Suspend nodes.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
pools_pool_sc_suspend_node = isi_sdk.PoolsPoolScResumeNode() # PoolsPoolScResumeNode | 
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try: 
    api_response = api_instance.create_pools_pool_sc_suspend_node(pools_pool_sc_suspend_node, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->create_pools_pool_sc_suspend_node: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pools_pool_rule**
> delete_pools_pool_rule(pools_pool_rule_id, groupnet, subnet, pool)



Delete a network rule.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
pools_pool_rule_id = 'pools_pool_rule_id_example' # str | Delete a network rule.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try: 
    api_instance.delete_pools_pool_rule(pools_pool_rule_id, groupnet, subnet, pool)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->delete_pools_pool_rule: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pools_pool_interfaces**
> PoolsPoolInterfaces get_pools_pool_interfaces(groupnet, subnet, pool, sort=sort, resume=resume, limit=limit, dir=dir, lnns=lnns)



Get a list of interfaces.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
lnns = 'lnns_example' # str | Get a list of interfaces for the specified lnn. (optional)

try: 
    api_response = api_instance.get_pools_pool_interfaces(groupnet, subnet, pool, sort=sort, resume=resume, limit=limit, dir=dir, lnns=lnns)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->get_pools_pool_interfaces: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **lnns** | **str**| Get a list of interfaces for the specified lnn. | [optional] 

### Return type

[**PoolsPoolInterfaces**](PoolsPoolInterfaces.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pools_pool_rule**
> PoolsPoolRules get_pools_pool_rule(pools_pool_rule_id, groupnet, subnet, pool)



View a single network rule.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
pools_pool_rule_id = 'pools_pool_rule_id_example' # str | View a single network rule.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try: 
    api_response = api_instance.get_pools_pool_rule(pools_pool_rule_id, groupnet, subnet, pool)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->get_pools_pool_rule: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pools_pool_rules**
> PoolsPoolRulesExtended list_pools_pool_rules(groupnet, subnet, pool, sort=sort, limit=limit, dir=dir, resume=resume)



Get a list of network rules.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try: 
    api_response = api_instance.list_pools_pool_rules(groupnet, subnet, pool, sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->list_pools_pool_rules: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groupnet** | **str**|  | 
 **subnet** | **str**|  | 
 **pool** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**PoolsPoolRulesExtended**](PoolsPoolRulesExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pools_pool_rule**
> update_pools_pool_rule(pools_pool_rule, pools_pool_rule_id, groupnet, subnet, pool)



Modify a network rule.

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
api_instance = isi_sdk.NetworkGroupnetsSubnetsApi()
pools_pool_rule = isi_sdk.PoolsPoolRule() # PoolsPoolRule | 
pools_pool_rule_id = 'pools_pool_rule_id_example' # str | Modify a network rule.
groupnet = 'groupnet_example' # str | 
subnet = 'subnet_example' # str | 
pool = 'pool_example' # str | 

try: 
    api_instance.update_pools_pool_rule(pools_pool_rule, pools_pool_rule_id, groupnet, subnet, pool)
except ApiException as e:
    print "Exception when calling NetworkGroupnetsSubnetsApi->update_pools_pool_rule: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

