# isilon_sdk.v9_5_0.SupportassistApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_supportassist_data_item**](SupportassistApi.md#create_supportassist_data_item) | **POST** /platform/16/supportassist/data | 
[**create_supportassist_payload_item**](SupportassistApi.md#create_supportassist_payload_item) | **POST** /platform/16/supportassist/payload | 
[**create_supportassist_task_item**](SupportassistApi.md#create_supportassist_task_item) | **POST** /platform/16/supportassist/task | 
[**delete_supportassist_task_by_id**](SupportassistApi.md#delete_supportassist_task_by_id) | **DELETE** /platform/16/supportassist/task/{SupportassistTaskId} | 
[**get_supportassist_license**](SupportassistApi.md#get_supportassist_license) | **GET** /platform/16/supportassist/license | 
[**get_supportassist_settings**](SupportassistApi.md#get_supportassist_settings) | **GET** /platform/16/supportassist/settings | 
[**get_supportassist_status**](SupportassistApi.md#get_supportassist_status) | **GET** /platform/16/supportassist/status | 
[**get_supportassist_task_by_id**](SupportassistApi.md#get_supportassist_task_by_id) | **GET** /platform/16/supportassist/task/{SupportassistTaskId} | 
[**get_supportassist_terms**](SupportassistApi.md#get_supportassist_terms) | **GET** /platform/16/supportassist/terms | 
[**list_supportassist_task**](SupportassistApi.md#list_supportassist_task) | **GET** /platform/16/supportassist/task | 
[**update_supportassist_settings**](SupportassistApi.md#update_supportassist_settings) | **PUT** /platform/16/supportassist/settings | 
[**update_supportassist_status**](SupportassistApi.md#update_supportassist_status) | **PUT** /platform/16/supportassist/status | 
[**update_supportassist_terms**](SupportassistApi.md#update_supportassist_terms) | **PUT** /platform/16/supportassist/terms | 


# **create_supportassist_data_item**
> CreateResponse create_supportassist_data_item(supportassist_data_item)



SupportAssist task response from ESE to product

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))
supportassist_data_item = isilon_sdk.v9_5_0.SupportassistDataItem() # SupportassistDataItem | 

try:
    api_response = api_instance.create_supportassist_data_item(supportassist_data_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->create_supportassist_data_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportassist_data_item** | [**SupportassistDataItem**](SupportassistDataItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_supportassist_payload_item**
> CreateResponse create_supportassist_payload_item(supportassist_payload_item)



Start a payload request task.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))
supportassist_payload_item = isilon_sdk.v9_5_0.SupportassistPayloadItem() # SupportassistPayloadItem | 

try:
    api_response = api_instance.create_supportassist_payload_item(supportassist_payload_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->create_supportassist_payload_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportassist_payload_item** | [**SupportassistPayloadItem**](SupportassistPayloadItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_supportassist_task_item**
> CreateResponse create_supportassist_task_item(supportassist_task_item)



Create a SupportAssist task.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))
supportassist_task_item = isilon_sdk.v9_5_0.SupportassistTaskItem() # SupportassistTaskItem | 

try:
    api_response = api_instance.create_supportassist_task_item(supportassist_task_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->create_supportassist_task_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportassist_task_item** | [**SupportassistTaskItem**](SupportassistTaskItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_supportassist_task_by_id**
> delete_supportassist_task_by_id(supportassist_task_id)



Delete a SupportAssist task by ID.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))
supportassist_task_id = 'supportassist_task_id_example' # str | Delete a SupportAssist task by ID.

try:
    api_instance.delete_supportassist_task_by_id(supportassist_task_id)
except ApiException as e:
    print("Exception when calling SupportassistApi->delete_supportassist_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportassist_task_id** | **str**| Delete a SupportAssist task by ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supportassist_license**
> SupportassistLicense get_supportassist_license()



License activation status.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_supportassist_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->get_supportassist_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportassistLicense**](SupportassistLicense.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supportassist_settings**
> SupportassistSettings get_supportassist_settings()



List settings.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_supportassist_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->get_supportassist_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportassistSettings**](SupportassistSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supportassist_status**
> SupportassistStatus get_supportassist_status()



Get status arguments.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_supportassist_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->get_supportassist_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportassistStatus**](SupportassistStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supportassist_task_by_id**
> SupportassistTask get_supportassist_task_by_id(supportassist_task_id)



Get the status of a SupportAssist task by ID or all tasks from the specified source.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))
supportassist_task_id = 'supportassist_task_id_example' # str | Get the status of a SupportAssist task by ID or all tasks from the specified source.

try:
    api_response = api_instance.get_supportassist_task_by_id(supportassist_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->get_supportassist_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportassist_task_id** | **str**| Get the status of a SupportAssist task by ID or all tasks from the specified source. | 

### Return type

[**SupportassistTask**](SupportassistTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supportassist_terms**
> SupportassistTerms get_supportassist_terms()



The T&C text for SupportAssist.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_supportassist_terms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->get_supportassist_terms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportassistTerms**](SupportassistTerms.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supportassist_task**
> SupportassistTask list_supportassist_task()



Get all SupportAssist tasks.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.list_supportassist_task()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SupportassistApi->list_supportassist_task: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportassistTask**](SupportassistTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supportassist_settings**
> update_supportassist_settings(supportassist_settings)



Modify one or more settings.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))
supportassist_settings = isilon_sdk.v9_5_0.SupportassistSettingsExtended() # SupportassistSettingsExtended | 

try:
    api_instance.update_supportassist_settings(supportassist_settings)
except ApiException as e:
    print("Exception when calling SupportassistApi->update_supportassist_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportassist_settings** | [**SupportassistSettingsExtended**](SupportassistSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supportassist_status**
> update_supportassist_status(supportassist_status)



Modify status arguments.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))
supportassist_status = isilon_sdk.v9_5_0.SupportassistStatusExtended() # SupportassistStatusExtended | 

try:
    api_instance.update_supportassist_status(supportassist_status)
except ApiException as e:
    print("Exception when calling SupportassistApi->update_supportassist_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportassist_status** | [**SupportassistStatusExtended**](SupportassistStatusExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_supportassist_terms**
> update_supportassist_terms(supportassist_terms)



Setting T&C accepted/rejected status.

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
api_instance = isilon_sdk.v9_5_0.SupportassistApi(isilon_sdk.v9_5_0.ApiClient(configuration))
supportassist_terms = isilon_sdk.v9_5_0.SupportassistTermsExtended() # SupportassistTermsExtended | 

try:
    api_instance.update_supportassist_terms(supportassist_terms)
except ApiException as e:
    print("Exception when calling SupportassistApi->update_supportassist_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **supportassist_terms** | [**SupportassistTermsExtended**](SupportassistTermsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

