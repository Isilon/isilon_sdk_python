# isilon_sdk.v9_5_0.ClusterModeApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_mode_settings**](ClusterModeApi.md#get_cluster_mode_settings) | **GET** /platform/14/cluster-mode/settings | 
[**update_cluster_mode_settings**](ClusterModeApi.md#update_cluster_mode_settings) | **PUT** /platform/14/cluster-mode/settings | 


# **get_cluster_mode_settings**
> ClusterModeSettings get_cluster_mode_settings()



Get cluster mode services settings

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
api_instance = isilon_sdk.v9_5_0.ClusterModeApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_mode_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterModeApi->get_cluster_mode_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterModeSettings**](ClusterModeSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_mode_settings**
> update_cluster_mode_settings(cluster_mode_settings)



Modify cluster mode services settings

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
api_instance = isilon_sdk.v9_5_0.ClusterModeApi(isilon_sdk.v9_5_0.ApiClient(configuration))
cluster_mode_settings = isilon_sdk.v9_5_0.ClusterModeSettingsExtended() # ClusterModeSettingsExtended | 

try:
    api_instance.update_cluster_mode_settings(cluster_mode_settings)
except ApiException as e:
    print("Exception when calling ClusterModeApi->update_cluster_mode_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_mode_settings** | [**ClusterModeSettingsExtended**](ClusterModeSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

