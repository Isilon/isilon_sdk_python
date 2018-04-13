# isi_sdk_8_0.UpgradeClusterApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nodes_node_firmware_status**](UpgradeClusterApi.md#get_nodes_node_firmware_status) | **GET** /platform/3/upgrade/cluster/nodes/{Lnn}/firmware/status | 


# **get_nodes_node_firmware_status**
> NodesNodeFirmwareStatus get_nodes_node_firmware_status(lnn, devices=devices, package=package)



The firmware status for the node.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.UpgradeClusterApi(isi_sdk_8_0.ApiClient(configuration))
lnn = 56 # int | 
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list.Default is false. (optional)

try:
    api_response = api_instance.get_nodes_node_firmware_status(lnn, devices=devices, package=package)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeClusterApi->get_nodes_node_firmware_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **package** | **bool**| Show package. If false, this returns an empty list.Default is false. | [optional] 

### Return type

[**NodesNodeFirmwareStatus**](NodesNodeFirmwareStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

