# isilon_sdk.v9_5_0.OsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_os_security**](OsApi.md#get_os_security) | **GET** /platform/16/os/security | 


# **get_os_security**
> OsSecurity get_os_security()



Per Node OS Security settings status

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
api_instance = isilon_sdk.v9_5_0.OsApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_os_security()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OsApi->get_os_security: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OsSecurity**](OsSecurity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

