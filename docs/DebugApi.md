# isi_sdk.DebugApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_debug_stats**](DebugApi.md#delete_debug_stats) | **DELETE** /platform/1/debug/stats | 
[**get_debug_stats**](DebugApi.md#get_debug_stats) | **GET** /platform/1/debug/stats | 


# **delete_debug_stats**
> delete_debug_stats()



Clear per-resource statistics counters.

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
api_instance = isi_sdk.DebugApi()

try: 
    api_instance.delete_debug_stats()
except ApiException as e:
    print "Exception when calling DebugApi->delete_debug_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debug_stats**
> DebugStats get_debug_stats()



List cumulative call statistics for each resource.

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
api_instance = isi_sdk.DebugApi()

try: 
    api_response = api_instance.get_debug_stats()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DebugApi->get_debug_stats: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DebugStats**](DebugStats.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

