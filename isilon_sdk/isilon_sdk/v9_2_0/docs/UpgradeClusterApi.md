# isilon_sdk.v9_2_0.UpgradeClusterApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nodes_node_patch_sync_item**](UpgradeClusterApi.md#create_nodes_node_patch_sync_item) | **POST** /platform/4/upgrade/cluster/nodes/{Lnn}/patch/sync | 
[**get_nodes_node_firmware_device**](UpgradeClusterApi.md#get_nodes_node_firmware_device) | **GET** /platform/10/upgrade/cluster/nodes/{Lnn}/firmware/device | 
[**get_nodes_node_firmware_status**](UpgradeClusterApi.md#get_nodes_node_firmware_status) | **GET** /platform/10/upgrade/cluster/nodes/{Lnn}/firmware/status | 


# **create_nodes_node_patch_sync_item**
> Empty create_nodes_node_patch_sync_item(nodes_node_patch_sync_item, lnn)



Retry any pending patch sync operations.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.UpgradeClusterApi(isilon_sdk.v9_2_0.ApiClient(configuration))
nodes_node_patch_sync_item = isilon_sdk.v9_2_0.Empty() # Empty | 
lnn = 56 # int | 

try:
    api_response = api_instance.create_nodes_node_patch_sync_item(nodes_node_patch_sync_item, lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeClusterApi->create_nodes_node_patch_sync_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nodes_node_patch_sync_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_node_firmware_device**
> NodesNodeFirmwareDevice get_nodes_node_firmware_device(lnn, devices=devices)



The firmware status for the node.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.UpgradeClusterApi(isilon_sdk.v9_2_0.ApiClient(configuration))
lnn = 56 # int | 
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)

try:
    api_response = api_instance.get_nodes_node_firmware_device(lnn, devices=devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeClusterApi->get_nodes_node_firmware_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 

### Return type

[**NodesNodeFirmwareDevice**](NodesNodeFirmwareDevice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_node_firmware_status**
> NodesNodeFirmwareDevice get_nodes_node_firmware_status(lnn, devices=devices)



The firmware status for the node.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.UpgradeClusterApi(isilon_sdk.v9_2_0.ApiClient(configuration))
lnn = 56 # int | 
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)

try:
    api_response = api_instance.get_nodes_node_firmware_status(lnn, devices=devices)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeClusterApi->get_nodes_node_firmware_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 

### Return type

[**NodesNodeFirmwareDevice**](NodesNodeFirmwareDevice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

