# isi_sdk_9_1_0.FileFilterApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_filter_settings**](FileFilterApi.md#get_file_filter_settings) | **GET** /platform/3/file-filter/settings | 
[**update_file_filter_settings**](FileFilterApi.md#update_file_filter_settings) | **PUT** /platform/3/file-filter/settings | 


# **get_file_filter_settings**
> FileFilterSettings get_file_filter_settings(zone=zone)



View File Filtering settings of an access zone

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.FileFilterApi(isi_sdk_9_1_0.ApiClient(configuration))
zone = 'zone_example' # str | Specifies the access zones in which these settings apply. (optional)

try:
    api_response = api_instance.get_file_filter_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileFilterApi->get_file_filter_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Specifies the access zones in which these settings apply. | [optional] 

### Return type

[**FileFilterSettings**](FileFilterSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_filter_settings**
> update_file_filter_settings(file_filter_settings, zone=zone)



Modify one or more File Filtering settings for an access zone

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.FileFilterApi(isi_sdk_9_1_0.ApiClient(configuration))
file_filter_settings = isi_sdk_9_1_0.FileFilterSettingsExtended() # FileFilterSettingsExtended | 
zone = 'zone_example' # str | Specifies the access zones in which these settings apply. (optional)

try:
    api_instance.update_file_filter_settings(file_filter_settings, zone=zone)
except ApiException as e:
    print("Exception when calling FileFilterApi->update_file_filter_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_filter_settings** | [**FileFilterSettingsExtended**](FileFilterSettingsExtended.md)|  | 
 **zone** | **str**| Specifies the access zones in which these settings apply. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

