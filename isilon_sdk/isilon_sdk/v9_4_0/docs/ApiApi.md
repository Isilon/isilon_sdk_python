# isilon_sdk.v9_4_0.ApiApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sessions_invalidation**](ApiApi.md#create_sessions_invalidation) | **POST** /platform/14/api/sessions/invalidations | 
[**create_sessions_rekey_item**](ApiApi.md#create_sessions_rekey_item) | **POST** /platform/14/api/sessions/rekey | 
[**delete_sessions_invalidation**](ApiApi.md#delete_sessions_invalidation) | **DELETE** /platform/14/api/sessions/invalidations/{SessionsInvalidationId} | 
[**get_sessions_invalidation**](ApiApi.md#get_sessions_invalidation) | **GET** /platform/14/api/sessions/invalidations/{SessionsInvalidationId} | 
[**get_settings_sessions**](ApiApi.md#get_settings_sessions) | **GET** /platform/14/api/settings/sessions | 
[**list_sessions_invalidations**](ApiApi.md#list_sessions_invalidations) | **GET** /platform/14/api/sessions/invalidations | 
[**update_sessions_invalidation**](ApiApi.md#update_sessions_invalidation) | **PUT** /platform/14/api/sessions/invalidations/{SessionsInvalidationId} | 
[**update_settings_sessions**](ApiApi.md#update_settings_sessions) | **PUT** /platform/14/api/settings/sessions | 


# **create_sessions_invalidation**
> CreateResponse create_sessions_invalidation(sessions_invalidation, zone=zone)



Create a new Platform API session invalidation.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.ApiApi(isilon_sdk.v9_4_0.ApiClient(configuration))
sessions_invalidation = isilon_sdk.v9_4_0.SessionsInvalidationCreateParams() # SessionsInvalidationCreateParams | 
zone = 'zone_example' # str | The zone to create the invalidation in. (optional)

try:
    api_response = api_instance.create_sessions_invalidation(sessions_invalidation, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_sessions_invalidation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessions_invalidation** | [**SessionsInvalidationCreateParams**](SessionsInvalidationCreateParams.md)|  | 
 **zone** | **str**| The zone to create the invalidation in. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sessions_rekey_item**
> Empty create_sessions_rekey_item(sessions_rekey_item)



Delete all existing session API signing keys and create a new signing key.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.ApiApi(isilon_sdk.v9_4_0.ApiClient(configuration))
sessions_rekey_item = isilon_sdk.v9_4_0.Empty() # Empty | 

try:
    api_response = api_instance.create_sessions_rekey_item(sessions_rekey_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_sessions_rekey_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessions_rekey_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sessions_invalidation**
> delete_sessions_invalidation(sessions_invalidation_id, zone=zone)



Delete a user's Platform API session invalidation.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.ApiApi(isilon_sdk.v9_4_0.ApiClient(configuration))
sessions_invalidation_id = 'sessions_invalidation_id_example' # str | Delete a user's Platform API session invalidation.
zone = 'zone_example' # str | The zone to delete an invalidation from. (optional)

try:
    api_instance.delete_sessions_invalidation(sessions_invalidation_id, zone=zone)
except ApiException as e:
    print("Exception when calling ApiApi->delete_sessions_invalidation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessions_invalidation_id** | **str**| Delete a user&#39;s Platform API session invalidation. | 
 **zone** | **str**| The zone to delete an invalidation from. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sessions_invalidation**
> SessionsInvalidations get_sessions_invalidation(sessions_invalidation_id, zone=zone)



Get user Platform API session invalidation information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.ApiApi(isilon_sdk.v9_4_0.ApiClient(configuration))
sessions_invalidation_id = 'sessions_invalidation_id_example' # str | Get user Platform API session invalidation information.
zone = 'zone_example' # str | The zone to get the invalidation from. (optional)

try:
    api_response = api_instance.get_sessions_invalidation(sessions_invalidation_id, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_sessions_invalidation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessions_invalidation_id** | **str**| Get user Platform API session invalidation information. | 
 **zone** | **str**| The zone to get the invalidation from. | [optional] 

### Return type

[**SessionsInvalidations**](SessionsInvalidations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_sessions**
> SettingsSessions get_settings_sessions()



Retrieve the HTTP API session settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.ApiApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_sessions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_settings_sessions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsSessions**](SettingsSessions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sessions_invalidations**
> SessionsInvalidations list_sessions_invalidations(zone=zone)



Get Platform API session invalidations.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.ApiApi(isilon_sdk.v9_4_0.ApiClient(configuration))
zone = 'zone_example' # str | The zone to get invalidations from. (optional)

try:
    api_response = api_instance.list_sessions_invalidations(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->list_sessions_invalidations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The zone to get invalidations from. | [optional] 

### Return type

[**SessionsInvalidations**](SessionsInvalidations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sessions_invalidation**
> update_sessions_invalidation(sessions_invalidation, sessions_invalidation_id, zone=zone)



Modify a user's Platform API session invalidation.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.ApiApi(isilon_sdk.v9_4_0.ApiClient(configuration))
sessions_invalidation = isilon_sdk.v9_4_0.SessionsInvalidation() # SessionsInvalidation | 
sessions_invalidation_id = 'sessions_invalidation_id_example' # str | Modify a user's Platform API session invalidation.
zone = 'zone_example' # str | The zone to modify an invalidation in. (optional)

try:
    api_instance.update_sessions_invalidation(sessions_invalidation, sessions_invalidation_id, zone=zone)
except ApiException as e:
    print("Exception when calling ApiApi->update_sessions_invalidation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sessions_invalidation** | [**SessionsInvalidation**](SessionsInvalidation.md)|  | 
 **sessions_invalidation_id** | **str**| Modify a user&#39;s Platform API session invalidation. | 
 **zone** | **str**| The zone to modify an invalidation in. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_sessions**
> update_settings_sessions(settings_sessions)



Modify the HTTP API session settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.ApiApi(isilon_sdk.v9_4_0.ApiClient(configuration))
settings_sessions = isilon_sdk.v9_4_0.SettingsSessionsSettings() # SettingsSessionsSettings | 

try:
    api_instance.update_settings_sessions(settings_sessions)
except ApiException as e:
    print("Exception when calling ApiApi->update_settings_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_sessions** | [**SettingsSessionsSettings**](SettingsSessionsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

