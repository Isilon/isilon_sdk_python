# isi_sdk_8_2_2.LocalClusterApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nodes_node_internal_ip_address**](LocalClusterApi.md#get_nodes_node_internal_ip_address) | **GET** /platform/7/local/cluster/nodes/{Lnn}/internal-ip-address | 


# **get_nodes_node_internal_ip_address**
> NodesNodeInternalIpAddress get_nodes_node_internal_ip_address(lnn)



View internal ip address with respect to node.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_2
from isi_sdk_8_2_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_2.LocalClusterApi(isi_sdk_8_2_2.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_nodes_node_internal_ip_address(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalClusterApi->get_nodes_node_internal_ip_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodesNodeInternalIpAddress**](NodesNodeInternalIpAddress.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

