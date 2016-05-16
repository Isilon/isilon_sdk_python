# isi_sdk.SnapshotChangelistsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_changelist_lin**](SnapshotChangelistsApi.md#get_changelist_lin) | **GET** /platform/1/snapshot/changelists/{Changelist}/lins/{ChangelistLinId} | 
[**get_changelist_lins**](SnapshotChangelistsApi.md#get_changelist_lins) | **GET** /platform/1/snapshot/changelists/{Changelist}/lins | 


# **get_changelist_lin**
> ChangelistLins get_changelist_lin(changelist_lin_id, changelist)



Get a single entry from the changelist.

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
api_instance = isi_sdk.SnapshotChangelistsApi()
changelist_lin_id = 56 # int | Get a single entry from the changelist.
changelist = 'changelist_example' # str | 

try: 
    api_response = api_instance.get_changelist_lin(changelist_lin_id, changelist)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotChangelistsApi->get_changelist_lin: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changelist_lin_id** | **int**| Get a single entry from the changelist. | 
 **changelist** | **str**|  | 

### Return type

[**ChangelistLins**](ChangelistLins.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changelist_lins**
> ChangelistLinsExtended get_changelist_lins(changelist)



Get entries from a changelist.

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
api_instance = isi_sdk.SnapshotChangelistsApi()
changelist = 'changelist_example' # str | 

try: 
    api_response = api_instance.get_changelist_lins(changelist)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotChangelistsApi->get_changelist_lins: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changelist** | **str**|  | 

### Return type

[**ChangelistLinsExtended**](ChangelistLinsExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

