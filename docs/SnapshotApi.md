# isi_sdk.SnapshotApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot_aliase**](SnapshotApi.md#create_snapshot_aliase) | **POST** /platform/1/snapshot/aliases | 
[**create_snapshot_changelist**](SnapshotApi.md#create_snapshot_changelist) | **POST** /platform/1/snapshot/changelists | 
[**create_snapshot_repstate**](SnapshotApi.md#create_snapshot_repstate) | **POST** /platform/1/snapshot/repstates | 
[**create_snapshot_schedule**](SnapshotApi.md#create_snapshot_schedule) | **POST** /platform/3/snapshot/schedules | 
[**create_snapshot_snapshot**](SnapshotApi.md#create_snapshot_snapshot) | **POST** /platform/1/snapshot/snapshots | 
[**delete_snapshot_aliase**](SnapshotApi.md#delete_snapshot_aliase) | **DELETE** /platform/1/snapshot/aliases/{SnapshotAliaseId} | 
[**delete_snapshot_aliases**](SnapshotApi.md#delete_snapshot_aliases) | **DELETE** /platform/1/snapshot/aliases | 
[**delete_snapshot_changelist**](SnapshotApi.md#delete_snapshot_changelist) | **DELETE** /platform/1/snapshot/changelists/{SnapshotChangelistId} | 
[**delete_snapshot_repstate**](SnapshotApi.md#delete_snapshot_repstate) | **DELETE** /platform/1/snapshot/repstates/{SnapshotRepstateId} | 
[**delete_snapshot_schedule**](SnapshotApi.md#delete_snapshot_schedule) | **DELETE** /platform/3/snapshot/schedules/{SnapshotScheduleId} | 
[**delete_snapshot_schedules**](SnapshotApi.md#delete_snapshot_schedules) | **DELETE** /platform/3/snapshot/schedules | 
[**delete_snapshot_snapshot**](SnapshotApi.md#delete_snapshot_snapshot) | **DELETE** /platform/1/snapshot/snapshots/{SnapshotSnapshotId} | 
[**delete_snapshot_snapshots**](SnapshotApi.md#delete_snapshot_snapshots) | **DELETE** /platform/1/snapshot/snapshots | 
[**get_snapshot_aliase**](SnapshotApi.md#get_snapshot_aliase) | **GET** /platform/1/snapshot/aliases/{SnapshotAliaseId} | 
[**get_snapshot_changelist**](SnapshotApi.md#get_snapshot_changelist) | **GET** /platform/1/snapshot/changelists/{SnapshotChangelistId} | 
[**get_snapshot_license**](SnapshotApi.md#get_snapshot_license) | **GET** /platform/1/snapshot/license | 
[**get_snapshot_pending**](SnapshotApi.md#get_snapshot_pending) | **GET** /platform/1/snapshot/pending | 
[**get_snapshot_repstate**](SnapshotApi.md#get_snapshot_repstate) | **GET** /platform/1/snapshot/repstates/{SnapshotRepstateId} | 
[**get_snapshot_schedule**](SnapshotApi.md#get_snapshot_schedule) | **GET** /platform/3/snapshot/schedules/{SnapshotScheduleId} | 
[**get_snapshot_settings**](SnapshotApi.md#get_snapshot_settings) | **GET** /platform/1/snapshot/settings | 
[**get_snapshot_snapshot**](SnapshotApi.md#get_snapshot_snapshot) | **GET** /platform/1/snapshot/snapshots/{SnapshotSnapshotId} | 
[**get_snapshot_snapshots_summary**](SnapshotApi.md#get_snapshot_snapshots_summary) | **GET** /platform/1/snapshot/snapshots-summary | 
[**list_snapshot_aliases**](SnapshotApi.md#list_snapshot_aliases) | **GET** /platform/1/snapshot/aliases | 
[**list_snapshot_changelists**](SnapshotApi.md#list_snapshot_changelists) | **GET** /platform/1/snapshot/changelists | 
[**list_snapshot_repstates**](SnapshotApi.md#list_snapshot_repstates) | **GET** /platform/1/snapshot/repstates | 
[**list_snapshot_schedules**](SnapshotApi.md#list_snapshot_schedules) | **GET** /platform/3/snapshot/schedules | 
[**list_snapshot_snapshots**](SnapshotApi.md#list_snapshot_snapshots) | **GET** /platform/1/snapshot/snapshots | 
[**update_snapshot_aliase**](SnapshotApi.md#update_snapshot_aliase) | **PUT** /platform/1/snapshot/aliases/{SnapshotAliaseId} | 
[**update_snapshot_schedule**](SnapshotApi.md#update_snapshot_schedule) | **PUT** /platform/3/snapshot/schedules/{SnapshotScheduleId} | 
[**update_snapshot_settings**](SnapshotApi.md#update_snapshot_settings) | **PUT** /platform/1/snapshot/settings | 
[**update_snapshot_snapshot**](SnapshotApi.md#update_snapshot_snapshot) | **PUT** /platform/1/snapshot/snapshots/{SnapshotSnapshotId} | 


# **create_snapshot_aliase**
> CreateSnapshotAliaseResponse create_snapshot_aliase(snapshot_aliase)



Create a new snapshot alias.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_aliase = isi_sdk.SnapshotAliaseCreateParams() # SnapshotAliaseCreateParams | 

try: 
    api_response = api_instance.create_snapshot_aliase(snapshot_aliase)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->create_snapshot_aliase: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_aliase** | [**SnapshotAliaseCreateParams**](SnapshotAliaseCreateParams.md)|  | 

### Return type

[**CreateSnapshotAliaseResponse**](CreateSnapshotAliaseResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_changelist**
> CreateSnapshotChangelistResponse create_snapshot_changelist(snapshot_changelist)



Create a new changelist.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_changelist = isi_sdk.SnapshotChangelists() # SnapshotChangelists | 

try: 
    api_response = api_instance.create_snapshot_changelist(snapshot_changelist)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->create_snapshot_changelist: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_changelist** | [**SnapshotChangelists**](SnapshotChangelists.md)|  | 

### Return type

[**CreateSnapshotChangelistResponse**](CreateSnapshotChangelistResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_repstate**
> CreateSnapshotRepstateResponse create_snapshot_repstate(snapshot_repstate)



Create a new repstates.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_repstate = isi_sdk.SnapshotRepstates() # SnapshotRepstates | 

try: 
    api_response = api_instance.create_snapshot_repstate(snapshot_repstate)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->create_snapshot_repstate: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_repstate** | [**SnapshotRepstates**](SnapshotRepstates.md)|  | 

### Return type

[**CreateSnapshotRepstateResponse**](CreateSnapshotRepstateResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_schedule**
> CreateSnapshotScheduleResponse create_snapshot_schedule(snapshot_schedule)



Create a new schedule.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_schedule = isi_sdk.SnapshotScheduleCreateParams() # SnapshotScheduleCreateParams | 

try: 
    api_response = api_instance.create_snapshot_schedule(snapshot_schedule)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->create_snapshot_schedule: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_schedule** | [**SnapshotScheduleCreateParams**](SnapshotScheduleCreateParams.md)|  | 

### Return type

[**CreateSnapshotScheduleResponse**](CreateSnapshotScheduleResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_snapshot_snapshot**
> SnapshotSnapshotExtended create_snapshot_snapshot(snapshot_snapshot)



Create a new snapshot.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_snapshot = isi_sdk.SnapshotSnapshotCreateParams() # SnapshotSnapshotCreateParams | 

try: 
    api_response = api_instance.create_snapshot_snapshot(snapshot_snapshot)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->create_snapshot_snapshot: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_snapshot** | [**SnapshotSnapshotCreateParams**](SnapshotSnapshotCreateParams.md)|  | 

### Return type

[**SnapshotSnapshotExtended**](SnapshotSnapshotExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_aliase**
> delete_snapshot_aliase(snapshot_aliase_id)



Delete the snapshot alias

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
api_instance = isi_sdk.SnapshotApi()
snapshot_aliase_id = 'snapshot_aliase_id_example' # str | Delete the snapshot alias

try: 
    api_instance.delete_snapshot_aliase(snapshot_aliase_id)
except ApiException as e:
    print "Exception when calling SnapshotApi->delete_snapshot_aliase: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_aliase_id** | **str**| Delete the snapshot alias | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_aliases**
> delete_snapshot_aliases()



Delete all or matching snapshot aliases.

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
api_instance = isi_sdk.SnapshotApi()

try: 
    api_instance.delete_snapshot_aliases()
except ApiException as e:
    print "Exception when calling SnapshotApi->delete_snapshot_aliases: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_changelist**
> delete_snapshot_changelist(snapshot_changelist_id)



Delete the specified changelist.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_changelist_id = 'snapshot_changelist_id_example' # str | Delete the specified changelist.

try: 
    api_instance.delete_snapshot_changelist(snapshot_changelist_id)
except ApiException as e:
    print "Exception when calling SnapshotApi->delete_snapshot_changelist: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_changelist_id** | **str**| Delete the specified changelist. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_repstate**
> delete_snapshot_repstate(snapshot_repstate_id)



Delete the specified repstate.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_repstate_id = 'snapshot_repstate_id_example' # str | Delete the specified repstate.

try: 
    api_instance.delete_snapshot_repstate(snapshot_repstate_id)
except ApiException as e:
    print "Exception when calling SnapshotApi->delete_snapshot_repstate: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_repstate_id** | **str**| Delete the specified repstate. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_schedule**
> delete_snapshot_schedule(snapshot_schedule_id)



Delete the schedule. This does not affect already created snapshots.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_schedule_id = 'snapshot_schedule_id_example' # str | Delete the schedule. This does not affect already created snapshots.

try: 
    api_instance.delete_snapshot_schedule(snapshot_schedule_id)
except ApiException as e:
    print "Exception when calling SnapshotApi->delete_snapshot_schedule: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_schedule_id** | **str**| Delete the schedule. This does not affect already created snapshots. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_schedules**
> delete_snapshot_schedules()



Delete all snapshot schedules.

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
api_instance = isi_sdk.SnapshotApi()

try: 
    api_instance.delete_snapshot_schedules()
except ApiException as e:
    print "Exception when calling SnapshotApi->delete_snapshot_schedules: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_snapshot**
> delete_snapshot_snapshot(snapshot_snapshot_id)



Delete the snapshot. Deleted snapshots will be placed into a deleting state until the system can reclaim the space used by the snapshot.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_snapshot_id = 'snapshot_snapshot_id_example' # str | Delete the snapshot. Deleted snapshots will be placed into a deleting state until the system can reclaim the space used by the snapshot.

try: 
    api_instance.delete_snapshot_snapshot(snapshot_snapshot_id)
except ApiException as e:
    print "Exception when calling SnapshotApi->delete_snapshot_snapshot: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_snapshot_id** | **str**| Delete the snapshot. Deleted snapshots will be placed into a deleting state until the system can reclaim the space used by the snapshot. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_snapshot_snapshots**
> delete_snapshot_snapshots(type=type, schedule=schedule)



Delete all or matching snapshots.

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
api_instance = isi_sdk.SnapshotApi()
type = 'type_example' # str | Only list snapshots matching this type. (optional)
schedule = 'schedule_example' # str | Only list snapshots created by this schedule. (optional)

try: 
    api_instance.delete_snapshot_snapshots(type=type, schedule=schedule)
except ApiException as e:
    print "Exception when calling SnapshotApi->delete_snapshot_snapshots: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Only list snapshots matching this type. | [optional] 
 **schedule** | **str**| Only list snapshots created by this schedule. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_aliase**
> SnapshotAliases get_snapshot_aliase(snapshot_aliase_id)



Retrieve snapshot alias information.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_aliase_id = 'snapshot_aliase_id_example' # str | Retrieve snapshot alias information.

try: 
    api_response = api_instance.get_snapshot_aliase(snapshot_aliase_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_aliase: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_aliase_id** | **str**| Retrieve snapshot alias information. | 

### Return type

[**SnapshotAliases**](SnapshotAliases.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_changelist**
> SnapshotChangelists get_snapshot_changelist(snapshot_changelist_id)



Retrieve basic information on a changelist.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_changelist_id = 'snapshot_changelist_id_example' # str | Retrieve basic information on a changelist.

try: 
    api_response = api_instance.get_snapshot_changelist(snapshot_changelist_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_changelist: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_changelist_id** | **str**| Retrieve basic information on a changelist. | 

### Return type

[**SnapshotChangelists**](SnapshotChangelists.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_license**
> LicenseLicense get_snapshot_license()



Retrieve license information.

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
api_instance = isi_sdk.SnapshotApi()

try: 
    api_response = api_instance.get_snapshot_license()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_license: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseLicense**](LicenseLicense.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_pending**
> SnapshotPending get_snapshot_pending(limit=limit, begin=begin, schedule=schedule, end=end, resume=resume)



Return list of snapshots to be taken.

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
api_instance = isi_sdk.SnapshotApi()
limit = 56 # int | Return no more than this many result at once (see resume). (optional)
begin = 56 # int | Unix Epoch time to start generating matches. Default is now. (optional)
schedule = 'schedule_example' # str | Limit output only to the named schedule. (optional)
end = 56 # int | Unix Epoch time to end generating matches. Default is forever. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try: 
    api_response = api_instance.get_snapshot_pending(limit=limit, begin=begin, schedule=schedule, end=end, resume=resume)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_pending: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many result at once (see resume). | [optional] 
 **begin** | **int**| Unix Epoch time to start generating matches. Default is now. | [optional] 
 **schedule** | **str**| Limit output only to the named schedule. | [optional] 
 **end** | **int**| Unix Epoch time to end generating matches. Default is forever. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SnapshotPending**](SnapshotPending.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_repstate**
> SnapshotRepstates get_snapshot_repstate(snapshot_repstate_id)



Retrieve basic information on a repstate.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_repstate_id = 'snapshot_repstate_id_example' # str | Retrieve basic information on a repstate.

try: 
    api_response = api_instance.get_snapshot_repstate(snapshot_repstate_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_repstate: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_repstate_id** | **str**| Retrieve basic information on a repstate. | 

### Return type

[**SnapshotRepstates**](SnapshotRepstates.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_schedule**
> SnapshotSchedules get_snapshot_schedule(snapshot_schedule_id)



Retrieve the schedule.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_schedule_id = 'snapshot_schedule_id_example' # str | Retrieve the schedule.

try: 
    api_response = api_instance.get_snapshot_schedule(snapshot_schedule_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_schedule: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_schedule_id** | **str**| Retrieve the schedule. | 

### Return type

[**SnapshotSchedules**](SnapshotSchedules.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_settings**
> SnapshotSettings get_snapshot_settings()



List all settings

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
api_instance = isi_sdk.SnapshotApi()

try: 
    api_response = api_instance.get_snapshot_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_settings: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotSettings**](SnapshotSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_snapshot**
> SnapshotSnapshots get_snapshot_snapshot(snapshot_snapshot_id)



Retrieve snapshot information.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_snapshot_id = 'snapshot_snapshot_id_example' # str | Retrieve snapshot information.

try: 
    api_response = api_instance.get_snapshot_snapshot(snapshot_snapshot_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_snapshot: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_snapshot_id** | **str**| Retrieve snapshot information. | 

### Return type

[**SnapshotSnapshots**](SnapshotSnapshots.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_snapshots_summary**
> SnapshotSnapshotsSummary get_snapshot_snapshots_summary()



Return summary information about snapshots.

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
api_instance = isi_sdk.SnapshotApi()

try: 
    api_response = api_instance.get_snapshot_snapshots_summary()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->get_snapshot_snapshots_summary: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotSnapshotsSummary**](SnapshotSnapshotsSummary.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_aliases**
> SnapshotAliasesExtended list_snapshot_aliases(sort=sort, limit=limit, dir=dir, resume=resume)



List all or matching snapshot aliases.

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
api_instance = isi_sdk.SnapshotApi()
sort = 'sort_example' # str | The field that will be used for sorting.  Choices are id, name, snapshot, and created.  Default is id. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try: 
    api_response = api_instance.list_snapshot_aliases(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->list_snapshot_aliases: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting.  Choices are id, name, snapshot, and created.  Default is id. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SnapshotAliasesExtended**](SnapshotAliasesExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_changelists**
> SnapshotChangelistsExtended list_snapshot_changelists()



List all changelists.

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
api_instance = isi_sdk.SnapshotApi()

try: 
    api_response = api_instance.list_snapshot_changelists()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->list_snapshot_changelists: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotChangelistsExtended**](SnapshotChangelistsExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_repstates**
> SnapshotRepstatesExtended list_snapshot_repstates()



List all repstates.

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
api_instance = isi_sdk.SnapshotApi()

try: 
    api_response = api_instance.list_snapshot_repstates()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->list_snapshot_repstates: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapshotRepstatesExtended**](SnapshotRepstatesExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_schedules**
> SnapshotSchedulesExtended list_snapshot_schedules(sort=sort, limit=limit, dir=dir, resume=resume)



List all or matching schedules.

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
api_instance = isi_sdk.SnapshotApi()
sort = 'sort_example' # str | The field that will be used for sorting.  Choices are id, name, path, pattern, schedule, duration, alias, next_run, and next_snapshot.  Default is id. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try: 
    api_response = api_instance.list_snapshot_schedules(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->list_snapshot_schedules: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting.  Choices are id, name, path, pattern, schedule, duration, alias, next_run, and next_snapshot.  Default is id. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SnapshotSchedulesExtended**](SnapshotSchedulesExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_snapshot_snapshots**
> SnapshotSnapshotsExtended list_snapshot_snapshots(sort=sort, schedule=schedule, resume=resume, state=state, limit=limit, type=type, dir=dir)



List all or matching snapshots.

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
api_instance = isi_sdk.SnapshotApi()
sort = 'sort_example' # str | The field that will be used for sorting.  Choices are id, name, path, created, expires, size, has_locks, schedule, alias_target, alias_target_name, pct_filesystem, pct_reserve, and state.  Default is id. (optional)
schedule = 'schedule_example' # str | Only list snapshots created by this schedule. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
state = 'state_example' # str | Only list snapshots matching this state. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
type = 'type_example' # str | Only list snapshots matching this type. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.list_snapshot_snapshots(sort=sort, schedule=schedule, resume=resume, state=state, limit=limit, type=type, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling SnapshotApi->list_snapshot_snapshots: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting.  Choices are id, name, path, created, expires, size, has_locks, schedule, alias_target, alias_target_name, pct_filesystem, pct_reserve, and state.  Default is id. | [optional] 
 **schedule** | **str**| Only list snapshots created by this schedule. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **state** | **str**| Only list snapshots matching this state. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **type** | **str**| Only list snapshots matching this type. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**SnapshotSnapshotsExtended**](SnapshotSnapshotsExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_aliase**
> update_snapshot_aliase(snapshot_aliase, snapshot_aliase_id)



Modify snapshot alias. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_aliase = isi_sdk.SnapshotAliase() # SnapshotAliase | 
snapshot_aliase_id = 'snapshot_aliase_id_example' # str | Modify snapshot alias. All input fields are optional, but one or more must be supplied.

try: 
    api_instance.update_snapshot_aliase(snapshot_aliase, snapshot_aliase_id)
except ApiException as e:
    print "Exception when calling SnapshotApi->update_snapshot_aliase: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_aliase** | [**SnapshotAliase**](SnapshotAliase.md)|  | 
 **snapshot_aliase_id** | **str**| Modify snapshot alias. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_schedule**
> update_snapshot_schedule(snapshot_schedule, snapshot_schedule_id)



Modify the schedule. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_schedule = isi_sdk.SnapshotSchedule() # SnapshotSchedule | 
snapshot_schedule_id = 'snapshot_schedule_id_example' # str | Modify the schedule. All input fields are optional, but one or more must be supplied.

try: 
    api_instance.update_snapshot_schedule(snapshot_schedule, snapshot_schedule_id)
except ApiException as e:
    print "Exception when calling SnapshotApi->update_snapshot_schedule: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_schedule** | [**SnapshotSchedule**](SnapshotSchedule.md)|  | 
 **snapshot_schedule_id** | **str**| Modify the schedule. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_settings**
> update_snapshot_settings(snapshot_settings)



Modify one or more settings.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_settings = isi_sdk.SnapshotSettingsExtended() # SnapshotSettingsExtended | 

try: 
    api_instance.update_snapshot_settings(snapshot_settings)
except ApiException as e:
    print "Exception when calling SnapshotApi->update_snapshot_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_settings** | [**SnapshotSettingsExtended**](SnapshotSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_snapshot_snapshot**
> update_snapshot_snapshot(snapshot_snapshot, snapshot_snapshot_id)



Modify snapshot. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.SnapshotApi()
snapshot_snapshot = isi_sdk.SnapshotSnapshot() # SnapshotSnapshot | 
snapshot_snapshot_id = 'snapshot_snapshot_id_example' # str | Modify snapshot. All input fields are optional, but one or more must be supplied.

try: 
    api_instance.update_snapshot_snapshot(snapshot_snapshot, snapshot_snapshot_id)
except ApiException as e:
    print "Exception when calling SnapshotApi->update_snapshot_snapshot: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_snapshot** | [**SnapshotSnapshot**](SnapshotSnapshot.md)|  | 
 **snapshot_snapshot_id** | **str**| Modify snapshot. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

