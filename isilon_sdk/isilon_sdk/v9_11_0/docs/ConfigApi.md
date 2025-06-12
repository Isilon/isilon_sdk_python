# isilon_sdk.v9_11_0.ConfigApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_config_export**](ConfigApi.md#create_config_export) | **POST** /platform/20/config/exports | 
[**create_config_import**](ConfigApi.md#create_config_import) | **POST** /platform/20/config/imports | 
[**get_config_config_lock**](ConfigApi.md#get_config_config_lock) | **GET** /platform/18/config/config-lock | 
[**get_config_export**](ConfigApi.md#get_config_export) | **GET** /platform/20/config/exports/{ConfigExportId} | 
[**get_config_import**](ConfigApi.md#get_config_import) | **GET** /platform/20/config/imports/{ConfigImportId} | 
[**list_config_exports**](ConfigApi.md#list_config_exports) | **GET** /platform/20/config/exports | 
[**list_config_imports**](ConfigApi.md#list_config_imports) | **GET** /platform/20/config/imports | 
[**update_config_config_lock**](ConfigApi.md#update_config_config_lock) | **PUT** /platform/18/config/config-lock | 


# **create_config_export**
> CreateConfigExportResponse create_config_export(config_export)



Create a new config export task.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigApi(isilon_sdk.v9_11_0.ApiClient(configuration))
config_export = isilon_sdk.v9_11_0.ConfigExportCreateParams() # ConfigExportCreateParams | 

try:
    api_response = api_instance.create_config_export(config_export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->create_config_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_export** | [**ConfigExportCreateParams**](ConfigExportCreateParams.md)|  | 

### Return type

[**CreateConfigExportResponse**](CreateConfigExportResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_config_import**
> CreateConfigImportResponse create_config_import(config_import)



Create a new config import task.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigApi(isilon_sdk.v9_11_0.ApiClient(configuration))
config_import = isilon_sdk.v9_11_0.ConfigImportCreateParams() # ConfigImportCreateParams | 

try:
    api_response = api_instance.create_config_import(config_import)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->create_config_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_import** | [**ConfigImportCreateParams**](ConfigImportCreateParams.md)|  | 

### Return type

[**CreateConfigImportResponse**](CreateConfigImportResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_config_lock**
> ConfigConfigLock get_config_config_lock()



Get configuration lock status.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigApi(isilon_sdk.v9_11_0.ApiClient(configuration))

try:
    api_response = api_instance.get_config_config_lock()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config_config_lock: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigConfigLock**](ConfigConfigLock.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_export**
> ConfigExports get_config_export(config_export_id)



Retrieve export task information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigApi(isilon_sdk.v9_11_0.ApiClient(configuration))
config_export_id = 'config_export_id_example' # str | Retrieve export task information.

try:
    api_response = api_instance.get_config_export(config_export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_export_id** | **str**| Retrieve export task information. | 

### Return type

[**ConfigExports**](ConfigExports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_import**
> ConfigImports get_config_import(config_import_id)



Retrieve import task information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigApi(isilon_sdk.v9_11_0.ApiClient(configuration))
config_import_id = 'config_import_id_example' # str | Retrieve import task information.

try:
    api_response = api_instance.get_config_import(config_import_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->get_config_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_import_id** | **str**| Retrieve import task information. | 

### Return type

[**ConfigImports**](ConfigImports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_exports**
> ConfigExports list_config_exports(dir=dir, sort=sort)



List all config export tasks.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigApi(isilon_sdk.v9_11_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_config_exports(dir=dir, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_config_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**ConfigExports**](ConfigExports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_imports**
> ConfigImports list_config_imports(dir=dir, sort=sort)



List all config import tasks.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigApi(isilon_sdk.v9_11_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_config_imports(dir=dir, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigApi->list_config_imports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**ConfigImports**](ConfigImports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_config_lock**
> update_config_config_lock(action, config_config_lock)



Enable/Disable configuration lock.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigApi(isilon_sdk.v9_11_0.ApiClient(configuration))
action = 'action_example' # str | Enable/disable configuration lock
config_config_lock = isilon_sdk.v9_11_0.Empty() # Empty | 

try:
    api_instance.update_config_config_lock(action, config_config_lock)
except ApiException as e:
    print("Exception when calling ConfigApi->update_config_config_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Enable/disable configuration lock | 
 **config_config_lock** | [**Empty**](Empty.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

