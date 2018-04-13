# isi_sdk_8_1_0.IdResolutionApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_id_resolution_path**](IdResolutionApi.md#get_id_resolution_path) | **GET** /platform/4/id-resolution/paths/{IdResolutionPathId} | 
[**get_id_resolution_paths**](IdResolutionApi.md#get_id_resolution_paths) | **GET** /platform/4/id-resolution/paths | 


# **get_id_resolution_path**
> IdResolutionPaths get_id_resolution_path(id_resolution_path_id)



List lin to path mappings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.IdResolutionApi(isi_sdk_8_1_0.ApiClient(configuration))
id_resolution_path_id = 56 # int | List lin to path mappings.

try:
    api_response = api_instance.get_id_resolution_path(id_resolution_path_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionApi->get_id_resolution_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_resolution_path_id** | **int**| List lin to path mappings. | 

### Return type

[**IdResolutionPaths**](IdResolutionPaths.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id_resolution_paths**
> IdResolutionPathsExtended get_id_resolution_paths(sort=sort, lins=lins, limit=limit, dir=dir, resume=resume)



List lin to path mappings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.IdResolutionApi(isi_sdk_8_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
lins = 'lins_example' # str | A comma separated list specifying the lins that will be mapped with a path. Only the lins specified in this list will be mapped. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_id_resolution_paths(sort=sort, lins=lins, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionApi->get_id_resolution_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **lins** | **str**| A comma separated list specifying the lins that will be mapped with a path. Only the lins specified in this list will be mapped. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**IdResolutionPathsExtended**](IdResolutionPathsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

