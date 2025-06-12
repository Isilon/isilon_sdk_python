# isilon_sdk.v9_10_0.ConnectivityApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connectivity_data_item**](ConnectivityApi.md#create_connectivity_data_item) | **POST** /platform/21/connectivity/data | 
[**create_connectivity_payload_item**](ConnectivityApi.md#create_connectivity_payload_item) | **POST** /platform/21/connectivity/payload | 
[**create_connectivity_task_item**](ConnectivityApi.md#create_connectivity_task_item) | **POST** /platform/21/connectivity/task | 
[**delete_connectivity_task_by_id**](ConnectivityApi.md#delete_connectivity_task_by_id) | **DELETE** /platform/21/connectivity/task/{ConnectivityTaskId} | 
[**get_connectivity_license**](ConnectivityApi.md#get_connectivity_license) | **GET** /platform/21/connectivity/license | 
[**get_connectivity_settings**](ConnectivityApi.md#get_connectivity_settings) | **GET** /platform/21/connectivity/settings | 
[**get_connectivity_status**](ConnectivityApi.md#get_connectivity_status) | **GET** /platform/21/connectivity/status | 
[**get_connectivity_task_by_id**](ConnectivityApi.md#get_connectivity_task_by_id) | **GET** /platform/21/connectivity/task/{ConnectivityTaskId} | 
[**get_connectivity_terms**](ConnectivityApi.md#get_connectivity_terms) | **GET** /platform/21/connectivity/terms | 
[**list_connectivity_task**](ConnectivityApi.md#list_connectivity_task) | **GET** /platform/21/connectivity/task | 
[**update_connectivity_settings**](ConnectivityApi.md#update_connectivity_settings) | **PUT** /platform/21/connectivity/settings | 
[**update_connectivity_status**](ConnectivityApi.md#update_connectivity_status) | **PUT** /platform/21/connectivity/status | 
[**update_connectivity_terms**](ConnectivityApi.md#update_connectivity_terms) | **PUT** /platform/21/connectivity/terms | 


# **create_connectivity_data_item**
> CreateResponse create_connectivity_data_item(connectivity_data_item)



Connectivity task response from Dell Technologies connectivity services

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))
connectivity_data_item = isilon_sdk.v9_10_0.SupportassistDataItem() # SupportassistDataItem | 

try:
    api_response = api_instance.create_connectivity_data_item(connectivity_data_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->create_connectivity_data_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_data_item** | [**SupportassistDataItem**](SupportassistDataItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connectivity_payload_item**
> CreateResponse create_connectivity_payload_item(connectivity_payload_item)



Start a payload request task.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))
connectivity_payload_item = isilon_sdk.v9_10_0.SupportassistPayloadItem() # SupportassistPayloadItem | 

try:
    api_response = api_instance.create_connectivity_payload_item(connectivity_payload_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->create_connectivity_payload_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_payload_item** | [**SupportassistPayloadItem**](SupportassistPayloadItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connectivity_task_item**
> CreateResponse create_connectivity_task_item(connectivity_task_item)



Create a Connectivity task.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))
connectivity_task_item = isilon_sdk.v9_10_0.SupportassistTaskItem() # SupportassistTaskItem | 

try:
    api_response = api_instance.create_connectivity_task_item(connectivity_task_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->create_connectivity_task_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_task_item** | [**SupportassistTaskItem**](SupportassistTaskItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connectivity_task_by_id**
> delete_connectivity_task_by_id(connectivity_task_id)



Delete a Connectivity task by ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))
connectivity_task_id = 'connectivity_task_id_example' # str | Delete a Connectivity task by ID.

try:
    api_instance.delete_connectivity_task_by_id(connectivity_task_id)
except ApiException as e:
    print("Exception when calling ConnectivityApi->delete_connectivity_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_task_id** | **str**| Delete a Connectivity task by ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectivity_license**
> SupportassistLicense get_connectivity_license()



License activation status.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))

try:
    api_response = api_instance.get_connectivity_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->get_connectivity_license: %s\n" % e)
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

# **get_connectivity_settings**
> ConnectivitySettings get_connectivity_settings()



List settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))

try:
    api_response = api_instance.get_connectivity_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->get_connectivity_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectivitySettings**](ConnectivitySettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectivity_status**
> ConnectivityStatus get_connectivity_status()



Get status arguments.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))

try:
    api_response = api_instance.get_connectivity_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->get_connectivity_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectivityStatus**](ConnectivityStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectivity_task_by_id**
> SupportassistTask get_connectivity_task_by_id(connectivity_task_id)



Get the status of a Connectivity task by ID or all tasks from the specified source.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))
connectivity_task_id = 'connectivity_task_id_example' # str | Get the status of a Connectivity task by ID or all tasks from the specified source.

try:
    api_response = api_instance.get_connectivity_task_by_id(connectivity_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->get_connectivity_task_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_task_id** | **str**| Get the status of a Connectivity task by ID or all tasks from the specified source. | 

### Return type

[**SupportassistTask**](SupportassistTask.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectivity_terms**
> SupportassistTerms get_connectivity_terms()



The Telemetry Notice text for Dell Technologies connectivity services.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))

try:
    api_response = api_instance.get_connectivity_terms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->get_connectivity_terms: %s\n" % e)
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

# **list_connectivity_task**
> SupportassistTask list_connectivity_task()



Get all Connectivity tasks.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))

try:
    api_response = api_instance.list_connectivity_task()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectivityApi->list_connectivity_task: %s\n" % e)
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

# **update_connectivity_settings**
> update_connectivity_settings(connectivity_settings)



Modify one or more settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))
connectivity_settings = isilon_sdk.v9_10_0.SupportassistSettingsExtended() # SupportassistSettingsExtended | 

try:
    api_instance.update_connectivity_settings(connectivity_settings)
except ApiException as e:
    print("Exception when calling ConnectivityApi->update_connectivity_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_settings** | [**SupportassistSettingsExtended**](SupportassistSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connectivity_status**
> update_connectivity_status(connectivity_status)



Modify status arguments.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))
connectivity_status = isilon_sdk.v9_10_0.ConnectivityStatusExtended() # ConnectivityStatusExtended | 

try:
    api_instance.update_connectivity_status(connectivity_status)
except ApiException as e:
    print("Exception when calling ConnectivityApi->update_connectivity_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_status** | [**ConnectivityStatusExtended**](ConnectivityStatusExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connectivity_terms**
> update_connectivity_terms(connectivity_terms)



Setting Telemetry Notice accepted or rejected.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.ConnectivityApi(isilon_sdk.v9_10_0.ApiClient(configuration))
connectivity_terms = isilon_sdk.v9_10_0.SupportassistTermsExtended() # SupportassistTermsExtended | 

try:
    api_instance.update_connectivity_terms(connectivity_terms)
except ApiException as e:
    print("Exception when calling ConnectivityApi->update_connectivity_terms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectivity_terms** | [**SupportassistTermsExtended**](SupportassistTermsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

