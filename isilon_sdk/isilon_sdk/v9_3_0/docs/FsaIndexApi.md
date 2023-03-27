# isilon_sdk.v9_3_0.FsaIndexApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_name_lin**](FsaIndexApi.md#get_name_lin) | **GET** /platform/8/fsa/index/{Name}/lins/{NameLinId} | 
[**get_name_lins**](FsaIndexApi.md#get_name_lins) | **GET** /platform/8/fsa/index/{Name}/lins | 


# **get_name_lin**
> NameLins get_name_lin(name_lin_id, name, path=path)



Get a single index entry from the index table.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.FsaIndexApi(isilon_sdk.v9_3_0.ApiClient(configuration))
name_lin_id = 56 # int | Get a single index entry from the index table.
name = 'name_example' # str | 
path = true # bool | Resolve the path for an index entry. This query argument is invalid if an initial index job is in progress or incomplete or if an incremental index job is in progress or incomplete. (optional)

try:
    api_response = api_instance.get_name_lin(name_lin_id, name, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaIndexApi->get_name_lin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name_lin_id** | **int**| Get a single index entry from the index table. | 
 **name** | **str**|  | 
 **path** | **bool**| Resolve the path for an index entry. This query argument is invalid if an initial index job is in progress or incomplete or if an incremental index job is in progress or incomplete. | [optional] 

### Return type

[**NameLins**](NameLins.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_name_lins**
> NameLinsExtended get_name_lins(name, limit=limit, lin=lin, path=path, resume=resume)



Get index entries from the given index table.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.FsaIndexApi(isilon_sdk.v9_3_0.ApiClient(configuration))
name = 'name_example' # str | 
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
lin = [56] # list[int] | LIN of file or directory to lookup. Accepts multiple query arguments. (optional)
path = true # bool | Resolve the path for an index entry. This query argument is invalid if an initial index job is in progress or incomplete or if an incremental index job is in progress or incomplete. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_name_lins(name, limit=limit, lin=lin, path=path, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaIndexApi->get_name_lins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **lin** | [**list[int]**](int.md)| LIN of file or directory to lookup. Accepts multiple query arguments. | [optional] 
 **path** | **bool**| Resolve the path for an index entry. This query argument is invalid if an initial index job is in progress or incomplete or if an incremental index job is in progress or incomplete. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NameLinsExtended**](NameLinsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

