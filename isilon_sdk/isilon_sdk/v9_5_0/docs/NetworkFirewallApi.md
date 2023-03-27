# isilon_sdk.v9_5_0.NetworkFirewallApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policies_policy_rule**](NetworkFirewallApi.md#create_policies_policy_rule) | **POST** /platform/16/network/firewall/policies/{Policy}/rules | 
[**delete_policies_policy_rule**](NetworkFirewallApi.md#delete_policies_policy_rule) | **DELETE** /platform/16/network/firewall/policies/{Policy}/rules/{PoliciesPolicyRuleId} | 
[**get_policies_policy_rule**](NetworkFirewallApi.md#get_policies_policy_rule) | **GET** /platform/16/network/firewall/policies/{Policy}/rules/{PoliciesPolicyRuleId} | 
[**list_policies_policy_rules**](NetworkFirewallApi.md#list_policies_policy_rules) | **GET** /platform/16/network/firewall/policies/{Policy}/rules | 
[**update_policies_policy_rule**](NetworkFirewallApi.md#update_policies_policy_rule) | **PUT** /platform/16/network/firewall/policies/{Policy}/rules/{PoliciesPolicyRuleId} | 


# **create_policies_policy_rule**
> CreateResponse create_policies_policy_rule(policies_policy_rule, policy, allow_renumbering=allow_renumbering, live=live)



Create a new network firewall rule.

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
api_instance = isilon_sdk.v9_5_0.NetworkFirewallApi(isilon_sdk.v9_5_0.ApiClient(configuration))
policies_policy_rule = isilon_sdk.v9_5_0.PoliciesPolicyRuleCreateParams() # PoliciesPolicyRuleCreateParams | 
policy = 'policy_example' # str | 
allow_renumbering = true # bool | Indicates whether to allow renumbering of other rules when an index already exists (optional)
live = true # bool | Live flag can only be used with active rules. Update will take effect immediately on all related network pools. (optional)

try:
    api_response = api_instance.create_policies_policy_rule(policies_policy_rule, policy, allow_renumbering=allow_renumbering, live=live)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkFirewallApi->create_policies_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policies_policy_rule** | [**PoliciesPolicyRuleCreateParams**](PoliciesPolicyRuleCreateParams.md)|  | 
 **policy** | **str**|  | 
 **allow_renumbering** | **bool**| Indicates whether to allow renumbering of other rules when an index already exists | [optional] 
 **live** | **bool**| Live flag can only be used with active rules. Update will take effect immediately on all related network pools. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policies_policy_rule**
> delete_policies_policy_rule(policies_policy_rule_id, policy, live=live)



Delete a network firewall rule.

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
api_instance = isilon_sdk.v9_5_0.NetworkFirewallApi(isilon_sdk.v9_5_0.ApiClient(configuration))
policies_policy_rule_id = 'policies_policy_rule_id_example' # str | Delete a network firewall rule.
policy = 'policy_example' # str | 
live = true # bool | Live flag can only be used with active rules. Update will take effect immediately on all related network pools. (optional)

try:
    api_instance.delete_policies_policy_rule(policies_policy_rule_id, policy, live=live)
except ApiException as e:
    print("Exception when calling NetworkFirewallApi->delete_policies_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policies_policy_rule_id** | **str**| Delete a network firewall rule. | 
 **policy** | **str**|  | 
 **live** | **bool**| Live flag can only be used with active rules. Update will take effect immediately on all related network pools. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policies_policy_rule**
> PoliciesPolicyRules get_policies_policy_rule(policies_policy_rule_id, policy)



View a network firewall rule.

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
api_instance = isilon_sdk.v9_5_0.NetworkFirewallApi(isilon_sdk.v9_5_0.ApiClient(configuration))
policies_policy_rule_id = 'policies_policy_rule_id_example' # str | View a network firewall rule.
policy = 'policy_example' # str | 

try:
    api_response = api_instance.get_policies_policy_rule(policies_policy_rule_id, policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkFirewallApi->get_policies_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policies_policy_rule_id** | **str**| View a network firewall rule. | 
 **policy** | **str**|  | 

### Return type

[**PoliciesPolicyRules**](PoliciesPolicyRules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policies_policy_rules**
> PoliciesPolicyRulesExtended list_policies_policy_rules(policy, dir=dir, limit=limit, resume=resume, sort=sort)



Get a list of network firewall rules.

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
api_instance = isilon_sdk.v9_5_0.NetworkFirewallApi(isilon_sdk.v9_5_0.ApiClient(configuration))
policy = 'policy_example' # str | 
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_policies_policy_rules(policy, dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkFirewallApi->list_policies_policy_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | **str**|  | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**PoliciesPolicyRulesExtended**](PoliciesPolicyRulesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policies_policy_rule**
> update_policies_policy_rule(policies_policy_rule, policies_policy_rule_id, policy, allow_renumbering=allow_renumbering, live=live)



Modify a network firewall rule.

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
api_instance = isilon_sdk.v9_5_0.NetworkFirewallApi(isilon_sdk.v9_5_0.ApiClient(configuration))
policies_policy_rule = isilon_sdk.v9_5_0.PoliciesPolicyRule() # PoliciesPolicyRule | 
policies_policy_rule_id = 'policies_policy_rule_id_example' # str | Modify a network firewall rule.
policy = 'policy_example' # str | 
allow_renumbering = true # bool | Indicates whether to allow renumbering of other rules when an index already exists (optional)
live = true # bool | Live flag can only be used with active rules. Update will take effect immediately on all related network pools. (optional)

try:
    api_instance.update_policies_policy_rule(policies_policy_rule, policies_policy_rule_id, policy, allow_renumbering=allow_renumbering, live=live)
except ApiException as e:
    print("Exception when calling NetworkFirewallApi->update_policies_policy_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policies_policy_rule** | [**PoliciesPolicyRule**](PoliciesPolicyRule.md)|  | 
 **policies_policy_rule_id** | **str**| Modify a network firewall rule. | 
 **policy** | **str**|  | 
 **allow_renumbering** | **bool**| Indicates whether to allow renumbering of other rules when an index already exists | [optional] 
 **live** | **bool**| Live flag can only be used with active rules. Update will take effect immediately on all related network pools. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

