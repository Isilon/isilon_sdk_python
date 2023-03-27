# isilon_sdk.v9_3_0.DebugApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_debug_stats**](DebugApi.md#delete_debug_stats) | **DELETE** /platform/1/debug/stats | 
[**get_debug_stats**](DebugApi.md#get_debug_stats) | **GET** /platform/1/debug/stats | 


# **delete_debug_stats**
> delete_debug_stats()



Clear per-resource statistics counters.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.DebugApi(isilon_sdk.v9_3_0.ApiClient(configuration))

try:
    api_instance.delete_debug_stats()
except ApiException as e:
    print("Exception when calling DebugApi->delete_debug_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_stats**
> DebugStats get_debug_stats()



List cumulative call statistics for each resource.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.DebugApi(isilon_sdk.v9_3_0.ApiClient(configuration))

try:
    api_response = api_instance.get_debug_stats()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DebugApi->get_debug_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DebugStats**](DebugStats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

