# isi_sdk_9_0_0.LocalApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_time**](LocalApi.md#get_cluster_time) | **GET** /platform/3/local/cluster/time | 
[**get_upgrade_cluster_firmware_device**](LocalApi.md#get_upgrade_cluster_firmware_device) | **GET** /platform/10/local/upgrade/cluster/firmware/device | 
[**get_upgrade_cluster_firmware_status**](LocalApi.md#get_upgrade_cluster_firmware_status) | **GET** /platform/3/local/upgrade/cluster/firmware/status | 


# **get_cluster_time**
> ClusterTimeExtendedExtended get_cluster_time()



Get the current time on the local node.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.LocalApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_cluster_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTimeExtendedExtended**](ClusterTimeExtendedExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_cluster_firmware_device**
> UpgradeClusterFirmwareDevice get_upgrade_cluster_firmware_device(refresh=refresh, devices=devices, package=package)



The firmware status for the cluster.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.LocalApi(isi_sdk_9_0_0.ApiClient(configuration))
refresh = true # bool | Re-gather firmware status. Default is false. (optional)
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list. Default is false. (optional)

try:
    api_response = api_instance.get_upgrade_cluster_firmware_device(refresh=refresh, devices=devices, package=package)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_upgrade_cluster_firmware_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Re-gather firmware status. Default is false. | [optional] 
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **package** | **bool**| Show package. If false, this returns an empty list. Default is false. | [optional] 

### Return type

[**UpgradeClusterFirmwareDevice**](UpgradeClusterFirmwareDevice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_cluster_firmware_status**
> UpgradeClusterFirmwareDevice get_upgrade_cluster_firmware_status(refresh=refresh, devices=devices, package=package)



The firmware status for the cluster.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.LocalApi(isi_sdk_9_0_0.ApiClient(configuration))
refresh = true # bool | Re-gather firmware status. Default is false. (optional)
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list. Default is false. (optional)

try:
    api_response = api_instance.get_upgrade_cluster_firmware_status(refresh=refresh, devices=devices, package=package)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_upgrade_cluster_firmware_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Re-gather firmware status. Default is false. | [optional] 
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **package** | **bool**| Show package. If false, this returns an empty list. Default is false. | [optional] 

### Return type

[**UpgradeClusterFirmwareDevice**](UpgradeClusterFirmwareDevice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

