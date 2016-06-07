# isi_sdk.LocalApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_time**](LocalApi.md#get_cluster_time) | **GET** /platform/3/local/cluster/time | 


# **get_cluster_time**
> ClusterTimeExtendedExtended get_cluster_time()



Get the current time on the local node.

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
api_instance = isi_sdk.LocalApi()

try: 
    api_response = api_instance.get_cluster_time()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LocalApi->get_cluster_time: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTimeExtendedExtended**](ClusterTimeExtendedExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

