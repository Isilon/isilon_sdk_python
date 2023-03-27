# isilon_sdk.v9_3_0.StoragepoolNodetypesApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nodetype_assess**](StoragepoolNodetypesApi.md#get_nodetype_assess) | **GET** /platform/12/storagepool/nodetypes/{Nid}/assess | 


# **get_nodetype_assess**
> NodetypeAssess get_nodetype_assess(nid)



Assess nodepools for modifying node type.

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
api_instance = isilon_sdk.v9_3_0.StoragepoolNodetypesApi(isilon_sdk.v9_3_0.ApiClient(configuration))
nid = 'nid_example' # str | 

try:
    api_response = api_instance.get_nodetype_assess(nid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolNodetypesApi->get_nodetype_assess: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nid** | **str**|  | 

### Return type

[**NodetypeAssess**](NodetypeAssess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

