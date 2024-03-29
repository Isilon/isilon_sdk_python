# isilon_sdk.v9_4_0.SnapshotApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot_alias**](SnapshotApi.md#create_snapshot_alias) | **POST** /platform/1/snapshot/aliases | 
[**create_snapshot_schedule**](SnapshotApi.md#create_snapshot_schedule) | **POST** /platform/3/snapshot/schedules | 
[**create_snapshot_snapshot**](SnapshotApi.md#create_snapshot_snapshot) | **POST** /platform/1/snapshot/snapshots | 
[**create_snapshot_writable_item**](SnapshotApi.md#create_snapshot_writable_item) | **POST** /platform/14/snapshot/writable | 
[**delete_snapshot_alias**](SnapshotApi.md#delete_snapshot_alias) | **DELETE** /platform/1/snapshot/aliases/{SnapshotAliasId} | 
[**delete_snapshot_aliases**](SnapshotApi.md#delete_snapshot_aliases) | **DELETE** /platform/1/snapshot/aliases | 
[**delete_snapshot_changelist**](SnapshotApi.md#delete_snapshot_changelist) | **DELETE** /platform/1/snapshot/changelists/{SnapshotChangelistId} | 
[**delete_snapshot_repstate**](SnapshotApi.md#delete_snapshot_repstate) | **DELETE** /platform/1/snapshot/repstates/{SnapshotRepstateId} | 
[**delete_snapshot_schedule**](SnapshotApi.md#delete_snapshot_schedule) | **DELETE** /platform/3/snapshot/schedules/{SnapshotScheduleId} | 
[**delete_snapshot_schedules**](SnapshotApi.md#delete_snapshot_schedules) | **DELETE** /platform/3/snapshot/schedules | 
[**delete_snapshot_snapshot**](SnapshotApi.md#delete_snapshot_snapshot) | **DELETE** /platform/1/snapshot/snapshots/{SnapshotSnapshotId} | 
[**delete_snapshot_snapshots**](SnapshotApi.md#delete_snapshot_snapshots) | **DELETE** /platform/1/snapshot/snapshots | 
[**delete_snapshot_writable**](SnapshotApi.md#delete_snapshot_writable) | **DELETE** /platform/14/snapshot/writable | 
[**delete_snapshot_writable_wspath**](SnapshotApi.md#delete_snapshot_writable_wspath) | **DELETE** /platform/14/snapshot/writable/{SnapshotWritableWspath} | 
[**get_changelists_changelist_diff_region**](SnapshotApi.md#get_changelists_changelist_diff_region) | **GET** /platform/10/snapshot/changelists/{Changelist}/diff-regions/{ChangelistsChangelistDiffRegionId} | 
[**get_snapshot_alias**](SnapshotApi.md#get_snapshot_alias) | **GET** /platform/1/snapshot/aliases/{SnapshotAliasId} | 
[**get_snapshot_changelist**](SnapshotApi.md#get_snapshot_changelist) | **GET** /platform/1/snapshot/changelists/{SnapshotChangelistId} | 
[**get_snapshot_changelists**](SnapshotApi.md#get_snapshot_changelists) | **GET** /platform/1/snapshot/changelists | 
[**get_snapshot_license**](SnapshotApi.md#get_snapshot_license) | **GET** /platform/5/snapshot/license | 
[**get_snapshot_pending**](SnapshotApi.md#get_snapshot_pending) | **GET** /platform/1/snapshot/pending | 
[**get_snapshot_repstate**](SnapshotApi.md#get_snapshot_repstate) | **GET** /platform/1/snapshot/repstates/{SnapshotRepstateId} | 
[**get_snapshot_repstates**](SnapshotApi.md#get_snapshot_repstates) | **GET** /platform/1/snapshot/repstates | 
[**get_snapshot_schedule**](SnapshotApi.md#get_snapshot_schedule) | **GET** /platform/3/snapshot/schedules/{SnapshotScheduleId} | 
[**get_snapshot_settings**](SnapshotApi.md#get_snapshot_settings) | **GET** /platform/1/snapshot/settings | 
[**get_snapshot_snapshot**](SnapshotApi.md#get_snapshot_snapshot) | **GET** /platform/1/snapshot/snapshots/{SnapshotSnapshotId} | 
[**get_snapshot_snapshots_summary**](SnapshotApi.md#get_snapshot_snapshots_summary) | **GET** /platform/1/snapshot/snapshots-summary | 
[**get_snapshot_writable_snapshot_summary**](SnapshotApi.md#get_snapshot_writable_snapshot_summary) | **GET** /platform/14/snapshot/writable-snapshot-summary | 
[**get_snapshot_writable_wspath**](SnapshotApi.md#get_snapshot_writable_wspath) | **GET** /platform/14/snapshot/writable/{SnapshotWritableWspath} | 
[**list_snapshot_aliases**](SnapshotApi.md#list_snapshot_aliases) | **GET** /platform/1/snapshot/aliases | 
[**list_snapshot_schedules**](SnapshotApi.md#list_snapshot_schedules) | **GET** /platform/3/snapshot/schedules | 
[**list_snapshot_snapshots**](SnapshotApi.md#list_snapshot_snapshots) | **GET** /platform/1/snapshot/snapshots | 
[**list_snapshot_writable**](SnapshotApi.md#list_snapshot_writable) | **GET** /platform/14/snapshot/writable | 
[**update_snapshot_alias**](SnapshotApi.md#update_snapshot_alias) | **PUT** /platform/1/snapshot/aliases/{SnapshotAliasId} | 
[**update_snapshot_schedule**](SnapshotApi.md#update_snapshot_schedule) | **PUT** /platform/3/snapshot/schedules/{SnapshotScheduleId} | 
[**update_snapshot_settings**](SnapshotApi.md#update_snapshot_settings) | **PUT** /platform/1/snapshot/settings | 
[**update_snapshot_snapshot**](SnapshotApi.md#update_snapshot_snapshot) | **PUT** /platform/1/snapshot/snapshots/{SnapshotSnapshotId} | 


# **create_snapshot_alias**
> CreateSnapshotAliasResponse create_snapshot_alias(snapshot_alias)



Create a new snapshot alias.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_alias = isilon_sdk.v9_4_0.SnapshotAliasCreateParams() # SnapshotAliasCreateParams | 

try:
    api_response = api_instance.create_snapshot_alias(snapshot_alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->create_snapshot_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_alias** | [**SnapshotAliasCreateParams**](SnapshotAliasCreateParams.md)|  | 

### Return type

[**CreateSnapshotAliasResponse**](CreateSnapshotAliasResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_schedule**
> CreateSnapshotScheduleResponse create_snapshot_schedule(snapshot_schedule)



Create a new schedule.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_schedule = isilon_sdk.v9_4_0.SnapshotScheduleCreateParams() # SnapshotScheduleCreateParams | 

try:
    api_response = api_instance.create_snapshot_schedule(snapshot_schedule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->create_snapshot_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_schedule** | [**SnapshotScheduleCreateParams**](SnapshotScheduleCreateParams.md)|  | 

### Return type

[**CreateSnapshotScheduleResponse**](CreateSnapshotScheduleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_snapshot**
> SnapshotSnapshotExtended create_snapshot_snapshot(snapshot_snapshot)



Create a new snapshot.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_snapshot = isilon_sdk.v9_4_0.SnapshotSnapshotCreateParams() # SnapshotSnapshotCreateParams | 

try:
    api_response = api_instance.create_snapshot_snapshot(snapshot_snapshot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->create_snapshot_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_snapshot** | [**SnapshotSnapshotCreateParams**](SnapshotSnapshotCreateParams.md)|  | 

### Return type

[**SnapshotSnapshotExtended**](SnapshotSnapshotExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_writable_item**
> SnapshotWritableWritableItem create_snapshot_writable_item(snapshot_writable_item)



Create a new writable snapshot.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_writable_item = isilon_sdk.v9_4_0.SnapshotWritableItem() # SnapshotWritableItem | 

try:
    api_response = api_instance.create_snapshot_writable_item(snapshot_writable_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->create_snapshot_writable_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_writable_item** | [**SnapshotWritableItem**](SnapshotWritableItem.md)|  | 

### Return type

[**SnapshotWritableWritableItem**](SnapshotWritableWritableItem.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_alias**
> delete_snapshot_alias(snapshot_alias_id)



Delete the snapshot alias

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_alias_id = 'snapshot_alias_id_example' # str | Delete the snapshot alias

try:
    api_instance.delete_snapshot_alias(snapshot_alias_id)
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_alias_id** | **str**| Delete the snapshot alias | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_aliases**
> delete_snapshot_aliases()



Delete all or matching snapshot aliases.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_instance.delete_snapshot_aliases()
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_aliases: %s\n" % e)
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

# **delete_snapshot_changelist**
> delete_snapshot_changelist(snapshot_changelist_id)



Delete the specified changelist.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_changelist_id = 'snapshot_changelist_id_example' # str | Delete the specified changelist.

try:
    api_instance.delete_snapshot_changelist(snapshot_changelist_id)
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_changelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_changelist_id** | **str**| Delete the specified changelist. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_repstate**
> delete_snapshot_repstate(snapshot_repstate_id)



Delete the specified repstate.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_repstate_id = 'snapshot_repstate_id_example' # str | Delete the specified repstate.

try:
    api_instance.delete_snapshot_repstate(snapshot_repstate_id)
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_repstate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_repstate_id** | **str**| Delete the specified repstate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_schedule**
> delete_snapshot_schedule(snapshot_schedule_id)



Delete the schedule. This does not affect already created snapshots.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_schedule_id = 'snapshot_schedule_id_example' # str | Delete the schedule. This does not affect already created snapshots.

try:
    api_instance.delete_snapshot_schedule(snapshot_schedule_id)
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_schedule_id** | **str**| Delete the schedule. This does not affect already created snapshots. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_schedules**
> delete_snapshot_schedules()



Delete all snapshot schedules.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_instance.delete_snapshot_schedules()
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_schedules: %s\n" % e)
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

# **delete_snapshot_snapshot**
> delete_snapshot_snapshot(snapshot_snapshot_id)



Delete the snapshot. Deleted snapshots will be placed into a deleting state until the system can reclaim the space used by the snapshot.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_snapshot_id = 'snapshot_snapshot_id_example' # str | Delete the snapshot. Deleted snapshots will be placed into a deleting state until the system can reclaim the space used by the snapshot.

try:
    api_instance.delete_snapshot_snapshot(snapshot_snapshot_id)
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_snapshot_id** | **str**| Delete the snapshot. Deleted snapshots will be placed into a deleting state until the system can reclaim the space used by the snapshot. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_snapshots**
> delete_snapshot_snapshots(schedule=schedule, type=type)



Delete all or matching snapshots.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
schedule = 'schedule_example' # str | Only list snapshots created by this schedule. (optional)
type = 'type_example' # str | Only list snapshots matching this type. (optional)

try:
    api_instance.delete_snapshot_snapshots(schedule=schedule, type=type)
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule** | **str**| Only list snapshots created by this schedule. | [optional] 
 **type** | **str**| Only list snapshots matching this type. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_writable**
> delete_snapshot_writable()



Delete all or matching writable snapshots.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_instance.delete_snapshot_writable()
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_writable: %s\n" % e)
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

# **delete_snapshot_writable_wspath**
> delete_snapshot_writable_wspath(snapshot_writable_wspath)



Delete the writable snapshot. Deleted writable snapshots    will be placed into a deleting state until the system can reclaim the    space used by the writable snapshot.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_writable_wspath = 'snapshot_writable_wspath_example' # str | Delete the writable snapshot. Deleted writable snapshots    will be placed into a deleting state until the system can reclaim the    space used by the writable snapshot.

try:
    api_instance.delete_snapshot_writable_wspath(snapshot_writable_wspath)
except ApiException as e:
    print("Exception when calling SnapshotApi->delete_snapshot_writable_wspath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_writable_wspath** | **str**| Delete the writable snapshot. Deleted writable snapshots    will be placed into a deleting state until the system can reclaim the    space used by the writable snapshot. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_changelists_changelist_diff_region**
> ChangelistsChangelistDiffRegions get_changelists_changelist_diff_region(changelists_changelist_diff_region_id, changelist, limit=limit, offset=offset, resume=resume)



Get snap diff regions of a file.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
changelists_changelist_diff_region_id = 56 # int | Get snap diff regions of a file.
changelist = 'changelist_example' # str | 
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
offset = 56 # int |  (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_changelists_changelist_diff_region(changelists_changelist_diff_region_id, changelist, limit=limit, offset=offset, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_changelists_changelist_diff_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **changelists_changelist_diff_region_id** | **int**| Get snap diff regions of a file. | 
 **changelist** | **str**|  | 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **offset** | **int**|  | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**ChangelistsChangelistDiffRegions**](ChangelistsChangelistDiffRegions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_alias**
> SnapshotAliases get_snapshot_alias(snapshot_alias_id)



Retrieve snapshot alias information.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_alias_id = 'snapshot_alias_id_example' # str | Retrieve snapshot alias information.

try:
    api_response = api_instance.get_snapshot_alias(snapshot_alias_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_alias_id** | **str**| Retrieve snapshot alias information. | 

### Return type

[**SnapshotAliases**](SnapshotAliases.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_changelist**
> SnapshotChangelists get_snapshot_changelist(snapshot_changelist_id, limit=limit, resume=resume)



Retrieve basic information on a changelist.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_changelist_id = 'snapshot_changelist_id_example' # str | Retrieve basic information on a changelist.
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_snapshot_changelist(snapshot_changelist_id, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_changelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_changelist_id** | **str**| Retrieve basic information on a changelist. | 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SnapshotChangelists**](SnapshotChangelists.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_changelists**
> SnapshotChangelistsExtended get_snapshot_changelists(limit=limit, resume=resume)



List all changelists.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_snapshot_changelists(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_changelists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SnapshotChangelistsExtended**](SnapshotChangelistsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_license**
> LicenseLicense get_snapshot_license()



Retrieve license information.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_snapshot_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseLicense**](LicenseLicense.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_pending**
> SnapshotPending get_snapshot_pending(begin=begin, end=end, limit=limit, resume=resume, schedule=schedule)



Return list of snapshots to be taken.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
begin = 56 # int | Unix Epoch time to start generating matches. Default is now. (optional)
end = 56 # int | Unix Epoch time to end generating matches. Default is forever. (optional)
limit = 56 # int | Return no more than this many result at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
schedule = 'schedule_example' # str | Limit output only to the named schedule. (optional)

try:
    api_response = api_instance.get_snapshot_pending(begin=begin, end=end, limit=limit, resume=resume, schedule=schedule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Unix Epoch time to start generating matches. Default is now. | [optional] 
 **end** | **int**| Unix Epoch time to end generating matches. Default is forever. | [optional] 
 **limit** | **int**| Return no more than this many result at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **schedule** | **str**| Limit output only to the named schedule. | [optional] 

### Return type

[**SnapshotPending**](SnapshotPending.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_repstate**
> SnapshotRepstates get_snapshot_repstate(snapshot_repstate_id, limit=limit, resume=resume)



Retrieve basic information on a repstate.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_repstate_id = 'snapshot_repstate_id_example' # str | Retrieve basic information on a repstate.
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_snapshot_repstate(snapshot_repstate_id, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_repstate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_repstate_id** | **str**| Retrieve basic information on a repstate. | 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SnapshotRepstates**](SnapshotRepstates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_repstates**
> SnapshotRepstatesExtended get_snapshot_repstates(limit=limit, resume=resume)



List all repstates.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_snapshot_repstates(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_repstates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SnapshotRepstatesExtended**](SnapshotRepstatesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_schedule**
> SnapshotSchedules get_snapshot_schedule(snapshot_schedule_id)



Retrieve the schedule.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_schedule_id = 'snapshot_schedule_id_example' # str | Retrieve the schedule.

try:
    api_response = api_instance.get_snapshot_schedule(snapshot_schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_schedule_id** | **str**| Retrieve the schedule. | 

### Return type

[**SnapshotSchedules**](SnapshotSchedules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_settings**
> SnapshotSettings get_snapshot_settings()



List all settings

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_snapshot_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotSettings**](SnapshotSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_snapshot**
> SnapshotSnapshots get_snapshot_snapshot(snapshot_snapshot_id)



Retrieve snapshot information.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_snapshot_id = 'snapshot_snapshot_id_example' # str | Retrieve snapshot information.

try:
    api_response = api_instance.get_snapshot_snapshot(snapshot_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_snapshot_id** | **str**| Retrieve snapshot information. | 

### Return type

[**SnapshotSnapshots**](SnapshotSnapshots.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_snapshots_summary**
> SnapshotSnapshotsSummary get_snapshot_snapshots_summary()



Return summary information about snapshots.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_snapshot_snapshots_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_snapshots_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotSnapshotsSummary**](SnapshotSnapshotsSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_writable_snapshot_summary**
> SnapshotWritableSnapshotSummary get_snapshot_writable_snapshot_summary()



Return summary information about writable snapshots.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_snapshot_writable_snapshot_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_writable_snapshot_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotWritableSnapshotSummary**](SnapshotWritableSnapshotSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_writable_wspath**
> SnapshotWritable get_snapshot_writable_wspath(snapshot_writable_wspath)



Retrieve writable snapshot information.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_writable_wspath = 'snapshot_writable_wspath_example' # str | Retrieve writable snapshot information.

try:
    api_response = api_instance.get_snapshot_writable_wspath(snapshot_writable_wspath)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->get_snapshot_writable_wspath: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_writable_wspath** | **str**| Retrieve writable snapshot information. | 

### Return type

[**SnapshotWritable**](SnapshotWritable.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_aliases**
> SnapshotAliasesExtended list_snapshot_aliases(dir=dir, limit=limit, resume=resume, sort=sort)



List all or matching snapshot aliases.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting.  Choices are id, name, snapshot, and created.  Default is id. (optional)

try:
    api_response = api_instance.list_snapshot_aliases(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->list_snapshot_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting.  Choices are id, name, snapshot, and created.  Default is id. | [optional] 

### Return type

[**SnapshotAliasesExtended**](SnapshotAliasesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_schedules**
> SnapshotSchedulesExtended list_snapshot_schedules(dir=dir, limit=limit, resume=resume, sort=sort)



List all or matching schedules.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting.  Choices are id, name, path, pattern, schedule, duration, alias, next_run, and next_snapshot.  Default is id. (optional)

try:
    api_response = api_instance.list_snapshot_schedules(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->list_snapshot_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting.  Choices are id, name, path, pattern, schedule, duration, alias, next_run, and next_snapshot.  Default is id. | [optional] 

### Return type

[**SnapshotSchedulesExtended**](SnapshotSchedulesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_snapshots**
> SnapshotSnapshotsExtended list_snapshot_snapshots(dir=dir, limit=limit, resume=resume, schedule=schedule, sort=sort, state=state, type=type)



List all or matching snapshots.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
schedule = 'schedule_example' # str | Only list snapshots created by this schedule. (optional)
sort = 'sort_example' # str | The field that will be used for sorting.  Choices are id, name, path, created, expires, size, has_locks, schedule, alias_target, alias_target_name, pct_filesystem, pct_reserve, and state.  Default is id. (optional)
state = 'state_example' # str | Only list snapshots matching this state. (optional)
type = 'type_example' # str | Only list snapshots matching this type. (optional)

try:
    api_response = api_instance.list_snapshot_snapshots(dir=dir, limit=limit, resume=resume, schedule=schedule, sort=sort, state=state, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->list_snapshot_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **schedule** | **str**| Only list snapshots created by this schedule. | [optional] 
 **sort** | **str**| The field that will be used for sorting.  Choices are id, name, path, created, expires, size, has_locks, schedule, alias_target, alias_target_name, pct_filesystem, pct_reserve, and state.  Default is id. | [optional] 
 **state** | **str**| Only list snapshots matching this state. | [optional] 
 **type** | **str**| Only list snapshots matching this type. | [optional] 

### Return type

[**SnapshotSnapshotsExtended**](SnapshotSnapshotsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_writable**
> SnapshotWritableExtended list_snapshot_writable(dir=dir, limit=limit, resume=resume, sort=sort, state=state)



List all or matching writable snapshots.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting.  Choices are path, src name, src path, created, size and state. Default is created. (optional)
state = 'state_example' # str | Only list writable snapshots matching this state. (optional)

try:
    api_response = api_instance.list_snapshot_writable(dir=dir, limit=limit, resume=resume, sort=sort, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SnapshotApi->list_snapshot_writable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting.  Choices are path, src name, src path, created, size and state. Default is created. | [optional] 
 **state** | **str**| Only list writable snapshots matching this state. | [optional] 

### Return type

[**SnapshotWritableExtended**](SnapshotWritableExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_alias**
> update_snapshot_alias(snapshot_alias, snapshot_alias_id)



Modify snapshot alias. All input fields are optional, but one or more must be supplied.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_alias = isilon_sdk.v9_4_0.SnapshotAlias() # SnapshotAlias | 
snapshot_alias_id = 'snapshot_alias_id_example' # str | Modify snapshot alias. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_snapshot_alias(snapshot_alias, snapshot_alias_id)
except ApiException as e:
    print("Exception when calling SnapshotApi->update_snapshot_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_alias** | [**SnapshotAlias**](SnapshotAlias.md)|  | 
 **snapshot_alias_id** | **str**| Modify snapshot alias. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_schedule**
> update_snapshot_schedule(snapshot_schedule, snapshot_schedule_id)



Modify the schedule. All input fields are optional, but one or more must be supplied.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_schedule = isilon_sdk.v9_4_0.SnapshotSchedule() # SnapshotSchedule | 
snapshot_schedule_id = 'snapshot_schedule_id_example' # str | Modify the schedule. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_snapshot_schedule(snapshot_schedule, snapshot_schedule_id)
except ApiException as e:
    print("Exception when calling SnapshotApi->update_snapshot_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_schedule** | [**SnapshotSchedule**](SnapshotSchedule.md)|  | 
 **snapshot_schedule_id** | **str**| Modify the schedule. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_settings**
> update_snapshot_settings(snapshot_settings)



Modify one or more settings.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_settings = isilon_sdk.v9_4_0.SnapshotSettingsExtended() # SnapshotSettingsExtended | 

try:
    api_instance.update_snapshot_settings(snapshot_settings)
except ApiException as e:
    print("Exception when calling SnapshotApi->update_snapshot_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_settings** | [**SnapshotSettingsExtended**](SnapshotSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_snapshot**
> update_snapshot_snapshot(snapshot_snapshot, snapshot_snapshot_id)



Modify snapshot. All input fields are optional, but one or more must be supplied.

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
api_instance = isilon_sdk.v9_4_0.SnapshotApi(isilon_sdk.v9_4_0.ApiClient(configuration))
snapshot_snapshot = isilon_sdk.v9_4_0.SnapshotSnapshot() # SnapshotSnapshot | 
snapshot_snapshot_id = 'snapshot_snapshot_id_example' # str | Modify snapshot. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_snapshot_snapshot(snapshot_snapshot, snapshot_snapshot_id)
except ApiException as e:
    print("Exception when calling SnapshotApi->update_snapshot_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_snapshot** | [**SnapshotSnapshot**](SnapshotSnapshot.md)|  | 
 **snapshot_snapshot_id** | **str**| Modify snapshot. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

