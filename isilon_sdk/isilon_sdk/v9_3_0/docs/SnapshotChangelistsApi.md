# isilon_sdk.v9_3_0.SnapshotChangelistsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_changelist_entries**](SnapshotChangelistsApi.md#get_changelist_entries) | **GET** /platform/10/snapshot/changelists/{Changelist}/entries | 
[**get_changelist_entry**](SnapshotChangelistsApi.md#get_changelist_entry) | **GET** /platform/10/snapshot/changelists/{Changelist}/entries/{ChangelistEntryId} | 
[**get_changelist_lin**](SnapshotChangelistsApi.md#get_changelist_lin) | **GET** /platform/1/snapshot/changelists/{Changelist}/lins/{ChangelistLinId} | 
[**get_changelist_lins**](SnapshotChangelistsApi.md#get_changelist_lins) | **GET** /platform/1/snapshot/changelists/{Changelist}/lins | 


# **get_changelist_entries**
> ChangelistEntriesExtended get_changelist_entries(changelist, diff_regions=diff_regions, limit=limit, resume=resume)



Get entries from a changelist.

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
api_instance = isilon_sdk.v9_3_0.SnapshotChangelistsApi(isilon_sdk.v9_3_0.ApiClient(configuration))
changelist = 'changelist_example' # str | 
diff_regions = true # bool | Include snapshot diff regions in entry output. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_changelist_entries(changelist, diff_regions=diff_regions, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotChangelistsApi->get_changelist_entries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changelist** | **str**|  | 
 **diff_regions** | **bool**| Include snapshot diff regions in entry output. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**ChangelistEntriesExtended**](ChangelistEntriesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changelist_entry**
> ChangelistEntries get_changelist_entry(changelist_entry_id, changelist)



Get a single entry from the changelist.

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
api_instance = isilon_sdk.v9_3_0.SnapshotChangelistsApi(isilon_sdk.v9_3_0.ApiClient(configuration))
changelist_entry_id = 'changelist_entry_id_example' # str | Get a single entry from the changelist.
changelist = 'changelist_example' # str | 

try:
    api_response = api_instance.get_changelist_entry(changelist_entry_id, changelist)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotChangelistsApi->get_changelist_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changelist_entry_id** | **str**| Get a single entry from the changelist. | 
 **changelist** | **str**|  | 

### Return type

[**ChangelistEntries**](ChangelistEntries.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changelist_lin**
> ChangelistLins get_changelist_lin(changelist_lin_id, changelist, limit=limit, resume=resume)



Get a single entry from the changelist.

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
api_instance = isilon_sdk.v9_3_0.SnapshotChangelistsApi(isilon_sdk.v9_3_0.ApiClient(configuration))
changelist_lin_id = 56 # int | Get a single entry from the changelist.
changelist = 'changelist_example' # str | 
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_changelist_lin(changelist_lin_id, changelist, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotChangelistsApi->get_changelist_lin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changelist_lin_id** | **int**| Get a single entry from the changelist. | 
 **changelist** | **str**|  | 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**ChangelistLins**](ChangelistLins.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changelist_lins**
> ChangelistLinsExtended get_changelist_lins(changelist, limit=limit, resume=resume)



Get entries from a changelist.

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
api_instance = isilon_sdk.v9_3_0.SnapshotChangelistsApi(isilon_sdk.v9_3_0.ApiClient(configuration))
changelist = 'changelist_example' # str | 
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_changelist_lins(changelist, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotChangelistsApi->get_changelist_lins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changelist** | **str**|  | 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**ChangelistLinsExtended**](ChangelistLinsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

