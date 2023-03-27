# isilon_sdk.v9_1_0.FilesystemApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings_access_time**](FilesystemApi.md#get_settings_access_time) | **GET** /platform/1/filesystem/settings/access-time | 
[**get_settings_character_encodings**](FilesystemApi.md#get_settings_character_encodings) | **GET** /platform/7/filesystem/settings/character-encodings | 
[**get_settings_compression**](FilesystemApi.md#get_settings_compression) | **GET** /platform/6/filesystem/settings/compression | 
[**update_settings_access_time**](FilesystemApi.md#update_settings_access_time) | **PUT** /platform/1/filesystem/settings/access-time | 
[**update_settings_character_encodings**](FilesystemApi.md#update_settings_character_encodings) | **PUT** /platform/7/filesystem/settings/character-encodings | 
[**update_settings_compression**](FilesystemApi.md#update_settings_compression) | **PUT** /platform/6/filesystem/settings/compression | 


# **get_settings_access_time**
> SettingsAccessTime get_settings_access_time()



Retrieve settings for access time.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.FilesystemApi(isilon_sdk.v9_1_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_access_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemApi->get_settings_access_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsAccessTime**](SettingsAccessTime.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_character_encodings**
> SettingsCharacterEncodings get_settings_character_encodings()



Retrieve current cluster character encoding settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.FilesystemApi(isilon_sdk.v9_1_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_character_encodings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemApi->get_settings_character_encodings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsCharacterEncodings**](SettingsCharacterEncodings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_compression**
> SettingsCompression get_settings_compression()



Retrieve settings for filesystem compression.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.FilesystemApi(isilon_sdk.v9_1_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_compression()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilesystemApi->get_settings_compression: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsCompression**](SettingsCompression.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_access_time**
> update_settings_access_time(settings_access_time)



Set settings for access time.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.FilesystemApi(isilon_sdk.v9_1_0.ApiClient(configuration))
settings_access_time = isilon_sdk.v9_1_0.SettingsAccessTimeExtended() # SettingsAccessTimeExtended | 

try:
    api_instance.update_settings_access_time(settings_access_time)
except ApiException as e:
    print("Exception when calling FilesystemApi->update_settings_access_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_access_time** | [**SettingsAccessTimeExtended**](SettingsAccessTimeExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_character_encodings**
> update_settings_character_encodings(settings_character_encodings)



Set current character encoding.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.FilesystemApi(isilon_sdk.v9_1_0.ApiClient(configuration))
settings_character_encodings = isilon_sdk.v9_1_0.SettingsCharacterEncodingsExtended() # SettingsCharacterEncodingsExtended | 

try:
    api_instance.update_settings_character_encodings(settings_character_encodings)
except ApiException as e:
    print("Exception when calling FilesystemApi->update_settings_character_encodings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_character_encodings** | [**SettingsCharacterEncodingsExtended**](SettingsCharacterEncodingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_compression**
> update_settings_compression(settings_compression)



Set settings for filesystem compression.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.FilesystemApi(isilon_sdk.v9_1_0.ApiClient(configuration))
settings_compression = isilon_sdk.v9_1_0.SettingsCompressionExtended() # SettingsCompressionExtended | 

try:
    api_instance.update_settings_compression(settings_compression)
except ApiException as e:
    print("Exception when calling FilesystemApi->update_settings_compression: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_compression** | [**SettingsCompressionExtended**](SettingsCompressionExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

