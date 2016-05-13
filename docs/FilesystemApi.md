# isi_sdk.FilesystemApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings_access_time**](FilesystemApi.md#get_settings_access_time) | **GET** /platform/1/filesystem/settings/access-time | 
[**update_settings_access_time**](FilesystemApi.md#update_settings_access_time) | **PUT** /platform/1/filesystem/settings/access-time | 


# **get_settings_access_time**
> SettingsAccessTime get_settings_access_time()



Retrieve settings for access time.

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
api_instance = isi_sdk.FilesystemApi()

try: 
    api_response = api_instance.get_settings_access_time()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilesystemApi->get_settings_access_time: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsAccessTime**](SettingsAccessTime.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_access_time**
> update_settings_access_time(settings_access_time)



Set settings for access time.

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
api_instance = isi_sdk.FilesystemApi()
settings_access_time = isi_sdk.SettingsAccessTimeExtended() # SettingsAccessTimeExtended | 

try: 
    api_instance.update_settings_access_time(settings_access_time)
except ApiException as e:
    print "Exception when calling FilesystemApi->update_settings_access_time: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_access_time** | [**SettingsAccessTimeExtended**](SettingsAccessTimeExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

