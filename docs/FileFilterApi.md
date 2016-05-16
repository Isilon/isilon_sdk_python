# isi_sdk.FileFilterApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_file_filter_settings**](FileFilterApi.md#get_file_filter_settings) | **GET** /platform/3/file-filter/settings | 
[**update_file_filter_settings**](FileFilterApi.md#update_file_filter_settings) | **PUT** /platform/3/file-filter/settings | 


# **get_file_filter_settings**
> FileFilterSettings get_file_filter_settings()



View File Filtering settings of an access zone

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
api_instance = isi_sdk.FileFilterApi()

try: 
    api_response = api_instance.get_file_filter_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FileFilterApi->get_file_filter_settings: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FileFilterSettings**](FileFilterSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_file_filter_settings**
> update_file_filter_settings(file_filter_settings)



Modify one or more File Filtering settings for an access zone

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
api_instance = isi_sdk.FileFilterApi()
file_filter_settings = isi_sdk.FileFilterSettings() # FileFilterSettings | 

try: 
    api_instance.update_file_filter_settings(file_filter_settings)
except ApiException as e:
    print "Exception when calling FileFilterApi->update_file_filter_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_filter_settings** | [**FileFilterSettings**](FileFilterSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

