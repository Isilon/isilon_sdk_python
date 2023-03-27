# isilon_sdk.v9_4_0.SyncServiceTargetApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policies_policy_cancel_item**](SyncServiceTargetApi.md#create_policies_policy_cancel_item) | **POST** /platform/7/sync/service/target/policies/{Policy}/cancel | 


# **create_policies_policy_cancel_item**
> CreateResponse create_policies_policy_cancel_item(policies_policy_cancel_item, policy)



Cancel the most recent SyncIQ job for this service replication policy from the target side.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.SyncServiceTargetApi(isilon_sdk.v9_4_0.ApiClient(configuration))
policies_policy_cancel_item = isilon_sdk.v9_4_0.Empty() # Empty | 
policy = 'policy_example' # str | 

try:
    api_response = api_instance.create_policies_policy_cancel_item(policies_policy_cancel_item, policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncServiceTargetApi->create_policies_policy_cancel_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policies_policy_cancel_item** | [**Empty**](Empty.md)|  | 
 **policy** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

