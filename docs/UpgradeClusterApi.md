# isi_sdk.UpgradeClusterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nodes_node_firmware_status**](UpgradeClusterApi.md#get_nodes_node_firmware_status) | **GET** /platform/3/upgrade/cluster/nodes/{Lnn}/firmware/status | 


# **get_nodes_node_firmware_status**
> NodesNodeFirmwareStatus get_nodes_node_firmware_status(lnn, devices=devices, package=package)



The firmware status for the node.

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
api_instance = isi_sdk.UpgradeClusterApi()
lnn = 56 # int | 
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list.Default is false. (optional)

try: 
    api_response = api_instance.get_nodes_node_firmware_status(lnn, devices=devices, package=package)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeClusterApi->get_nodes_node_firmware_status: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

