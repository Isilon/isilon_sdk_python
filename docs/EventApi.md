# isi_sdk_7_2.EventApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_event**](EventApi.md#get_event_event) | **GET** /platform/2/event/events/{EventEventId} | 
[**get_event_events**](EventApi.md#get_event_events) | **GET** /platform/2/event/events | 


# **get_event_event**
> EventEvents get_event_event(event_event_id)



Retrieve event information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.EventApi(isi_sdk_7_2.ApiClient(configuration))
event_event_id = 'event_event_id_example' # str | Retrieve event information.

try:
    api_response = api_instance.get_event_event(event_event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_event_id** | **str**| Retrieve event information. | 

### Return type

[**EventEvents**](EventEvents.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_events**
> EventEventsExtended get_event_events(count=count, sort=sort, begin=begin, end=end, event_type=event_type, coalesced=coalesced, resume=resume, devid=devid, acknowledged=acknowledged, ended=ended, limit=limit, dir=dir, coalescing=coalescing, severity=severity)



Retrieve event information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.EventApi(isi_sdk_7_2.ApiClient(configuration))
count = true # bool | If true, return a count of events. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
begin = 56 # int | Specifies the earliest time to query events from. (optional)
end = 56 # int | Specifies the latest time to query events from. (optional)
event_type = [56] # list[int] | Specifies the event_id of events to query for. (optional)
coalesced = true # bool | If true, only return events that have been coalesced. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
devid = ['devid_example'] # list[str] | Specifies the devid of events to query for. (optional)
acknowledged = true # bool | If true, only return events that have been acknowledged. (optional)
ended = true # bool | If true, only return events that have ended. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
coalescing = true # bool | If true, only return coalescing events. (optional)
severity = ['severity_example'] # list[str] | Specifies the severity of events to query for. (optional)

try:
    api_response = api_instance.get_event_events(count=count, sort=sort, begin=begin, end=end, event_type=event_type, coalesced=coalesced, resume=resume, devid=devid, acknowledged=acknowledged, ended=ended, limit=limit, dir=dir, coalescing=coalescing, severity=severity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **bool**| If true, return a count of events. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **begin** | **int**| Specifies the earliest time to query events from. | [optional] 
 **end** | **int**| Specifies the latest time to query events from. | [optional] 
 **event_type** | [**list[int]**](int.md)| Specifies the event_id of events to query for. | [optional] 
 **coalesced** | **bool**| If true, only return events that have been coalesced. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **devid** | [**list[str]**](str.md)| Specifies the devid of events to query for. | [optional] 
 **acknowledged** | **bool**| If true, only return events that have been acknowledged. | [optional] 
 **ended** | **bool**| If true, only return events that have ended. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **coalescing** | **bool**| If true, only return coalescing events. | [optional] 
 **severity** | [**list[str]**](str.md)| Specifies the severity of events to query for. | [optional] 

### Return type

[**EventEventsExtended**](EventEventsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

