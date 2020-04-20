# isi_sdk_8_1_0.SyncPoliciesApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_reset_item**](SyncPoliciesApi.md#create_policy_reset_item) | **POST** /platform/1/sync/policies/{Policy}/reset | 


# **create_policy_reset_item**
> CreateResponse create_policy_reset_item(policy_reset_item, policy)



Reset a SyncIQ policy incremental state and force a full sync/copy.

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
api_instance = isi_sdk_8_1_0.SyncPoliciesApi(isi_sdk_8_1_0.ApiClient(configuration))
policy_reset_item = isi_sdk_8_1_0.Empty() # Empty | 
policy = 'policy_example' # str | 

try:
    api_response = api_instance.create_policy_reset_item(policy_reset_item, policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncPoliciesApi->create_policy_reset_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_reset_item** | [**Empty**](Empty.md)|  | 
 **policy** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

