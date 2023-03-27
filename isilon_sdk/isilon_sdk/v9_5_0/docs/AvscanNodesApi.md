# isilon_sdk.v9_5_0.AvscanNodesApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_status**](AvscanNodesApi.md#get_node_status) | **GET** /platform/11/avscan/nodes/{Lnn}/status | 


# **get_node_status**
> NodeStatus get_node_status(lnn)



View CAVA Antivirus status.

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
api_instance = isilon_sdk.v9_5_0.AvscanNodesApi(isilon_sdk.v9_5_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_status(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanNodesApi->get_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStatus**](NodeStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

