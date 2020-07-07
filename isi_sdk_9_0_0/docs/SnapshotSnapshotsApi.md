# isi_sdk_9_0_0.SnapshotSnapshotsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot_lock**](SnapshotSnapshotsApi.md#create_snapshot_lock) | **POST** /platform/1/snapshot/snapshots/{Sid}/locks | 
[**delete_snapshot_lock**](SnapshotSnapshotsApi.md#delete_snapshot_lock) | **DELETE** /platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId} | 
[**delete_snapshot_locks**](SnapshotSnapshotsApi.md#delete_snapshot_locks) | **DELETE** /platform/1/snapshot/snapshots/{Sid}/locks | 
[**get_snapshot_lock**](SnapshotSnapshotsApi.md#get_snapshot_lock) | **GET** /platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId} | 
[**list_snapshot_locks**](SnapshotSnapshotsApi.md#list_snapshot_locks) | **GET** /platform/1/snapshot/snapshots/{Sid}/locks | 
[**update_snapshot_lock**](SnapshotSnapshotsApi.md#update_snapshot_lock) | **PUT** /platform/1/snapshot/snapshots/{Sid}/locks/{SnapshotLockId} | 


# **create_snapshot_lock**
> CreateSnapshotLockResponse create_snapshot_lock(snapshot_lock, sid)



Create a new lock on this snapshot.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SnapshotSnapshotsApi(isi_sdk_9_0_0.ApiClient(configuration))
snapshot_lock = isi_sdk_9_0_0.SnapshotLockCreateParams() # SnapshotLockCreateParams | 
sid = 'sid_example' # str | 

try:
    api_response = api_instance.create_snapshot_lock(snapshot_lock, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotSnapshotsApi->create_snapshot_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_lock** | [**SnapshotLockCreateParams**](SnapshotLockCreateParams.md)|  | 
 **sid** | **str**|  | 

### Return type

[**CreateSnapshotLockResponse**](CreateSnapshotLockResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_lock**
> delete_snapshot_lock(snapshot_lock_id, sid)



Delete the snapshot lock.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SnapshotSnapshotsApi(isi_sdk_9_0_0.ApiClient(configuration))
snapshot_lock_id = 'snapshot_lock_id_example' # str | Delete the snapshot lock.
sid = 'sid_example' # str | 

try:
    api_instance.delete_snapshot_lock(snapshot_lock_id, sid)
except ApiException as e:
    print("Exception when calling SnapshotSnapshotsApi->delete_snapshot_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_lock_id** | **str**| Delete the snapshot lock. | 
 **sid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_locks**
> delete_snapshot_locks(sid)



Delete all locks. Will try to drain count of recursively held locks so that the snapshot can be deleted.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SnapshotSnapshotsApi(isi_sdk_9_0_0.ApiClient(configuration))
sid = 'sid_example' # str | 

try:
    api_instance.delete_snapshot_locks(sid)
except ApiException as e:
    print("Exception when calling SnapshotSnapshotsApi->delete_snapshot_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_lock**
> SnapshotLocks get_snapshot_lock(snapshot_lock_id, sid)



Retrieve lock information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SnapshotSnapshotsApi(isi_sdk_9_0_0.ApiClient(configuration))
snapshot_lock_id = 'snapshot_lock_id_example' # str | Retrieve lock information.
sid = 'sid_example' # str | 

try:
    api_response = api_instance.get_snapshot_lock(snapshot_lock_id, sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotSnapshotsApi->get_snapshot_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_lock_id** | **str**| Retrieve lock information. | 
 **sid** | **str**|  | 

### Return type

[**SnapshotLocks**](SnapshotLocks.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_locks**
> SnapshotLocksExtended list_snapshot_locks(sid, sort=sort, limit=limit, dir=dir, resume=resume)



List all locks.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SnapshotSnapshotsApi(isi_sdk_9_0_0.ApiClient(configuration))
sid = 'sid_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting.  Choices are id, expires, and comment.  Default is id. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_snapshot_locks(sid, sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotSnapshotsApi->list_snapshot_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting.  Choices are id, expires, and comment.  Default is id. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SnapshotLocksExtended**](SnapshotLocksExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_lock**
> update_snapshot_lock(snapshot_lock, snapshot_lock_id, sid)



Modify lock. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SnapshotSnapshotsApi(isi_sdk_9_0_0.ApiClient(configuration))
snapshot_lock = isi_sdk_9_0_0.SnapshotLock() # SnapshotLock | 
snapshot_lock_id = 'snapshot_lock_id_example' # str | Modify lock. All input fields are optional, but one or more must be supplied.
sid = 'sid_example' # str | 

try:
    api_instance.update_snapshot_lock(snapshot_lock, snapshot_lock_id, sid)
except ApiException as e:
    print("Exception when calling SnapshotSnapshotsApi->update_snapshot_lock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_lock** | [**SnapshotLock**](SnapshotLock.md)|  | 
 **snapshot_lock_id** | **str**| Modify lock. All input fields are optional, but one or more must be supplied. | 
 **sid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

