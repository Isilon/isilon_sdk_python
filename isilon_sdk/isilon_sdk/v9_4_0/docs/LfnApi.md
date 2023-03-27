# isilon_sdk.v9_4_0.LfnApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lfn_item**](LfnApi.md#create_lfn_item) | **POST** /platform/12/lfn | 
[**delete_lfn**](LfnApi.md#delete_lfn) | **DELETE** /platform/12/lfn | 
[**delete_lfn_path**](LfnApi.md#delete_lfn_path) | **DELETE** /platform/12/lfn/{LfnPath} | 
[**get_lfn_path**](LfnApi.md#get_lfn_path) | **GET** /platform/12/lfn/{LfnPath} | 
[**list_lfn**](LfnApi.md#list_lfn) | **GET** /platform/12/lfn | 
[**update_lfn_path**](LfnApi.md#update_lfn_path) | **PUT** /platform/12/lfn/{LfnPath} | 


# **create_lfn_item**
> LfnDomain create_lfn_item(lfn_item)



Create a new file name length configuration domain.

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
api_instance = isilon_sdk.v9_4_0.LfnApi(isilon_sdk.v9_4_0.ApiClient(configuration))
lfn_item = isilon_sdk.v9_4_0.LfnItem() # LfnItem | 

try:
    api_response = api_instance.create_lfn_item(lfn_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LfnApi->create_lfn_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lfn_item** | [**LfnItem**](LfnItem.md)|  | 

### Return type

[**LfnDomain**](LfnDomain.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lfn**
> delete_lfn()



Delete all file name length configuration domains, returning to legacy limits.

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
api_instance = isilon_sdk.v9_4_0.LfnApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_instance.delete_lfn()
except ApiException as e:
    print("Exception when calling LfnApi->delete_lfn: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lfn_path**
> delete_lfn_path(lfn_path)



Delete the file name length configuration domain that originates at the specified path.

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
api_instance = isilon_sdk.v9_4_0.LfnApi(isilon_sdk.v9_4_0.ApiClient(configuration))
lfn_path = 'lfn_path_example' # str | Delete the file name length configuration domain that originates at the specified path.

try:
    api_instance.delete_lfn_path(lfn_path)
except ApiException as e:
    print("Exception when calling LfnApi->delete_lfn_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lfn_path** | **str**| Delete the file name length configuration domain that originates at the specified path. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lfn_path**
> Lfn get_lfn_path(lfn_path)



Retrieve file name length configuration information.

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
api_instance = isilon_sdk.v9_4_0.LfnApi(isilon_sdk.v9_4_0.ApiClient(configuration))
lfn_path = 'lfn_path_example' # str | Retrieve file name length configuration information.

try:
    api_response = api_instance.get_lfn_path(lfn_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LfnApi->get_lfn_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lfn_path** | **str**| Retrieve file name length configuration information. | 

### Return type

[**Lfn**](Lfn.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lfn**
> LfnExtended list_lfn(dir=dir, limit=limit, resume=resume, sort=sort)



List all file name length configuration domains.

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
api_instance = isilon_sdk.v9_4_0.LfnApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_lfn(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LfnApi->list_lfn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**LfnExtended**](LfnExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lfn_path**
> update_lfn_path(lfn_path_params, lfn_path)



Modify file name length settings if specified path is the root of the configuration. All input fields are optional, but one or more must be supplied.

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
api_instance = isilon_sdk.v9_4_0.LfnApi(isilon_sdk.v9_4_0.ApiClient(configuration))
lfn_path_params = isilon_sdk.v9_4_0.LfnPathParams() # LfnPathParams | 
lfn_path = 'lfn_path_example' # str | Modify file name length settings if specified path is the root of the configuration. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_lfn_path(lfn_path_params, lfn_path)
except ApiException as e:
    print("Exception when calling LfnApi->update_lfn_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lfn_path_params** | [**LfnPathParams**](LfnPathParams.md)|  | 
 **lfn_path** | **str**| Modify file name length settings if specified path is the root of the configuration. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

