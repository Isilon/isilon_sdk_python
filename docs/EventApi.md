# isi_sdk_8_0.EventApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_alert_condition**](EventApi.md#create_event_alert_condition) | **POST** /platform/3/event/alert-conditions | 
[**create_event_channel**](EventApi.md#create_event_channel) | **POST** /platform/3/event/channels | 
[**create_event_event**](EventApi.md#create_event_event) | **POST** /platform/3/event/events | 
[**delete_event_alert_condition**](EventApi.md#delete_event_alert_condition) | **DELETE** /platform/3/event/alert-conditions/{EventAlertConditionId} | 
[**delete_event_alert_conditions**](EventApi.md#delete_event_alert_conditions) | **DELETE** /platform/3/event/alert-conditions | 
[**delete_event_channel**](EventApi.md#delete_event_channel) | **DELETE** /platform/3/event/channels/{EventChannelId} | 
[**get_event_alert_condition**](EventApi.md#get_event_alert_condition) | **GET** /platform/3/event/alert-conditions/{EventAlertConditionId} | 
[**get_event_categories**](EventApi.md#get_event_categories) | **GET** /platform/3/event/categories | 
[**get_event_category**](EventApi.md#get_event_category) | **GET** /platform/3/event/categories/{EventCategoryId} | 
[**get_event_channel**](EventApi.md#get_event_channel) | **GET** /platform/3/event/channels/{EventChannelId} | 
[**get_event_eventgroup_definition**](EventApi.md#get_event_eventgroup_definition) | **GET** /platform/3/event/eventgroup-definitions/{EventEventgroupDefinitionId} | 
[**get_event_eventgroup_definitions**](EventApi.md#get_event_eventgroup_definitions) | **GET** /platform/3/event/eventgroup-definitions | 
[**get_event_eventgroup_occurrence**](EventApi.md#get_event_eventgroup_occurrence) | **GET** /platform/3/event/eventgroup-occurrences/{EventEventgroupOccurrenceId} | 
[**get_event_eventgroup_occurrences**](EventApi.md#get_event_eventgroup_occurrences) | **GET** /platform/3/event/eventgroup-occurrences | 
[**get_event_eventlist**](EventApi.md#get_event_eventlist) | **GET** /platform/3/event/eventlists/{EventEventlistId} | 
[**get_event_eventlists**](EventApi.md#get_event_eventlists) | **GET** /platform/3/event/eventlists | 
[**get_event_settings**](EventApi.md#get_event_settings) | **GET** /platform/3/event/settings | 
[**list_event_alert_conditions**](EventApi.md#list_event_alert_conditions) | **GET** /platform/3/event/alert-conditions | 
[**list_event_channels**](EventApi.md#list_event_channels) | **GET** /platform/3/event/channels | 
[**update_event_alert_condition**](EventApi.md#update_event_alert_condition) | **PUT** /platform/3/event/alert-conditions/{EventAlertConditionId} | 
[**update_event_channel**](EventApi.md#update_event_channel) | **PUT** /platform/3/event/channels/{EventChannelId} | 
[**update_event_eventgroup_occurrence**](EventApi.md#update_event_eventgroup_occurrence) | **PUT** /platform/3/event/eventgroup-occurrences/{EventEventgroupOccurrenceId} | 
[**update_event_eventgroup_occurrences**](EventApi.md#update_event_eventgroup_occurrences) | **PUT** /platform/3/event/eventgroup-occurrences | 
[**update_event_settings**](EventApi.md#update_event_settings) | **PUT** /platform/3/event/settings | 


# **create_event_alert_condition**
> CreateResponse create_event_alert_condition(event_alert_condition)



Create a new alert condition.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_alert_condition = isi_sdk_8_0.EventAlertConditionCreateParams() # EventAlertConditionCreateParams | 

try:
    api_response = api_instance.create_event_alert_condition(event_alert_condition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->create_event_alert_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_alert_condition** | [**EventAlertConditionCreateParams**](EventAlertConditionCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_channel**
> CreateResponse create_event_channel(event_channel)



Create a new channel.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_channel = isi_sdk_8_0.EventChannelCreateParams() # EventChannelCreateParams | 

try:
    api_response = api_instance.create_event_channel(event_channel)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->create_event_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_channel** | [**EventChannelCreateParams**](EventChannelCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_event**
> CreateResponse create_event_event(event_event)



Create a test event.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_event = isi_sdk_8_0.EventEvent() # EventEvent | 

try:
    api_response = api_instance.create_event_event(event_event)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->create_event_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_event** | [**EventEvent**](EventEvent.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_alert_condition**
> delete_event_alert_condition(event_alert_condition_id)



Delete the alert-condition.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_alert_condition_id = 'event_alert_condition_id_example' # str | Delete the alert-condition.

try:
    api_instance.delete_event_alert_condition(event_alert_condition_id)
except ApiException as e:
    print("Exception when calling EventApi->delete_event_alert_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_alert_condition_id** | **str**| Delete the alert-condition. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_alert_conditions**
> delete_event_alert_conditions(channel=channel)



Bulk delete of alert conditions.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
channel = 'channel_example' # str | Delete only conditions for this channel (optional)

try:
    api_instance.delete_event_alert_conditions(channel=channel)
except ApiException as e:
    print("Exception when calling EventApi->delete_event_alert_conditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**| Delete only conditions for this channel | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_channel**
> delete_event_channel(event_channel_id)



Delete the alert-condition.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_channel_id = 'event_channel_id_example' # str | Delete the alert-condition.

try:
    api_instance.delete_event_channel(event_channel_id)
except ApiException as e:
    print("Exception when calling EventApi->delete_event_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_channel_id** | **str**| Delete the alert-condition. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_alert_condition**
> EventAlertConditions get_event_alert_condition(event_alert_condition_id)



Retrieve the alert-condition.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_alert_condition_id = 'event_alert_condition_id_example' # str | Retrieve the alert-condition.

try:
    api_response = api_instance.get_event_alert_condition(event_alert_condition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_alert_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_alert_condition_id** | **str**| Retrieve the alert-condition. | 

### Return type

[**EventAlertConditions**](EventAlertConditions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_categories**
> EventCategoriesExtended get_event_categories(limit=limit, resume=resume)



List all eventgroup categories.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_event_categories(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventCategoriesExtended**](EventCategoriesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_category**
> EventCategories get_event_category(event_category_id)



Retrieve the eventgroup category.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_category_id = 'event_category_id_example' # str | Retrieve the eventgroup category.

try:
    api_response = api_instance.get_event_category(event_category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_category_id** | **str**| Retrieve the eventgroup category. | 

### Return type

[**EventCategories**](EventCategories.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_channel**
> EventChannels get_event_channel(event_channel_id)



Retrieve the alert-condition.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_channel_id = 'event_channel_id_example' # str | Retrieve the alert-condition.

try:
    api_response = api_instance.get_event_channel(event_channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_channel_id** | **str**| Retrieve the alert-condition. | 

### Return type

[**EventChannels**](EventChannels.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventgroup_definition**
> EventEventgroupDefinitions get_event_eventgroup_definition(event_eventgroup_definition_id)



Retrieve the eventgroup definition.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_eventgroup_definition_id = 'event_eventgroup_definition_id_example' # str | Retrieve the eventgroup definition.

try:
    api_response = api_instance.get_event_eventgroup_definition(event_eventgroup_definition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventgroup_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_eventgroup_definition_id** | **str**| Retrieve the eventgroup definition. | 

### Return type

[**EventEventgroupDefinitions**](EventEventgroupDefinitions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventgroup_definitions**
> EventEventgroupDefinitionsExtended get_event_eventgroup_definitions(category=category, limit=limit, resume=resume)



List all eventgroup definitions.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
category = 56 # int | Return eventgroups in the specified category (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_event_eventgroup_definitions(category=category, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventgroup_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **int**| Return eventgroups in the specified category | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventEventgroupDefinitionsExtended**](EventEventgroupDefinitionsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventgroup_occurrence**
> EventEventgroupOccurrences get_event_eventgroup_occurrence(event_eventgroup_occurrence_id)



Retrieve individual eventgroup occurrence.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_eventgroup_occurrence_id = 'event_eventgroup_occurrence_id_example' # str | Retrieve individual eventgroup occurrence.

try:
    api_response = api_instance.get_event_eventgroup_occurrence(event_eventgroup_occurrence_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventgroup_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_eventgroup_occurrence_id** | **str**| Retrieve individual eventgroup occurrence. | 

### Return type

[**EventEventgroupOccurrences**](EventEventgroupOccurrences.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventgroup_occurrences**
> EventEventgroupOccurrencesExtended get_event_eventgroup_occurrences(resolved=resolved, sort=sort, begin=begin, end=end, event_count=event_count, resume=resume, fixer=fixer, ignore=ignore, limit=limit, cause=cause, dir=dir)



List all eventgroup occurrences.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
resolved = true # bool | Filter for resolved eventgroups (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
begin = 56 # int | events that are in progress after this time (optional)
end = 56 # int | events that were in progress before this time (optional)
event_count = 56 # int | events for which event_count > this (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
fixer = 'fixer_example' # str | Filter for eventgroup fixer (optional)
ignore = true # bool | Filter for ignored eventgroups (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
cause = 'cause_example' # str | Filter for cause (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_event_eventgroup_occurrences(resolved=resolved, sort=sort, begin=begin, end=end, event_count=event_count, resume=resume, fixer=fixer, ignore=ignore, limit=limit, cause=cause, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventgroup_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolved** | **bool**| Filter for resolved eventgroups | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **begin** | **int**| events that are in progress after this time | [optional] 
 **end** | **int**| events that were in progress before this time | [optional] 
 **event_count** | **int**| events for which event_count &gt; this | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **fixer** | **str**| Filter for eventgroup fixer | [optional] 
 **ignore** | **bool**| Filter for ignored eventgroups | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **cause** | **str**| Filter for cause | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**EventEventgroupOccurrencesExtended**](EventEventgroupOccurrencesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventlist**
> EventEventlists get_event_eventlist(event_eventlist_id)



Retrieve the list of events for a eventgroup occureence.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_eventlist_id = 'event_eventlist_id_example' # str | Retrieve the list of events for a eventgroup occureence.

try:
    api_response = api_instance.get_event_eventlist(event_eventlist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_eventlist_id** | **str**| Retrieve the list of events for a eventgroup occureence. | 

### Return type

[**EventEventlists**](EventEventlists.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventlists**
> EventEventlistsExtended get_event_eventlists(event_instance=event_instance, limit=limit, severity=severity, resume=resume)



List all event occurrences grouped by eventgroup occurrence.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_instance = 'event_instance_example' # str | Return only this event occurrence (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
severity = 'severity_example' # str | Minimum severity of returned events. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_event_eventlists(event_instance=event_instance, limit=limit, severity=severity, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_instance** | **str**| Return only this event occurrence | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **severity** | **str**| Minimum severity of returned events. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventEventlistsExtended**](EventEventlistsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_settings**
> EventSettings get_event_settings()



Retrieve the settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_event_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventSettings**](EventSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_alert_conditions**
> EventAlertConditionsExtended list_event_alert_conditions(sort=sort, channel_ids=channel_ids, limit=limit, dir=dir, resume=resume)



List all alert conditions.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
channel_ids = 'channel_ids_example' # str | Return only conditions for the specified channel: (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_event_alert_conditions(sort=sort, channel_ids=channel_ids, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->list_event_alert_conditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **channel_ids** | **str**| Return only conditions for the specified channel: | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventAlertConditionsExtended**](EventAlertConditionsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_channels**
> EventChannelsExtended list_event_channels(limit=limit, resume=resume)



List all channels.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_event_channels(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->list_event_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventChannelsExtended**](EventChannelsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_alert_condition**
> update_event_alert_condition(event_alert_condition, event_alert_condition_id)



Modify the alert-condition

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_alert_condition = isi_sdk_8_0.EventAlertCondition() # EventAlertCondition | 
event_alert_condition_id = 'event_alert_condition_id_example' # str | Modify the alert-condition

try:
    api_instance.update_event_alert_condition(event_alert_condition, event_alert_condition_id)
except ApiException as e:
    print("Exception when calling EventApi->update_event_alert_condition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_alert_condition** | [**EventAlertCondition**](EventAlertCondition.md)|  | 
 **event_alert_condition_id** | **str**| Modify the alert-condition | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_channel**
> update_event_channel(event_channel, event_channel_id)



Modify the alert-condition

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_channel = isi_sdk_8_0.EventChannel() # EventChannel | 
event_channel_id = 'event_channel_id_example' # str | Modify the alert-condition

try:
    api_instance.update_event_channel(event_channel, event_channel_id)
except ApiException as e:
    print("Exception when calling EventApi->update_event_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_channel** | [**EventChannel**](EventChannel.md)|  | 
 **event_channel_id** | **str**| Modify the alert-condition | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_eventgroup_occurrence**
> update_event_eventgroup_occurrence(event_eventgroup_occurrence, event_eventgroup_occurrence_id)



modify eventgroup occurrence.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_eventgroup_occurrence = isi_sdk_8_0.EventEventgroupOccurrence() # EventEventgroupOccurrence | 
event_eventgroup_occurrence_id = 'event_eventgroup_occurrence_id_example' # str | modify eventgroup occurrence.

try:
    api_instance.update_event_eventgroup_occurrence(event_eventgroup_occurrence, event_eventgroup_occurrence_id)
except ApiException as e:
    print("Exception when calling EventApi->update_event_eventgroup_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_eventgroup_occurrence** | [**EventEventgroupOccurrence**](EventEventgroupOccurrence.md)|  | 
 **event_eventgroup_occurrence_id** | **str**| modify eventgroup occurrence. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_eventgroup_occurrences**
> update_event_eventgroup_occurrences(event_eventgroup_occurrences)



Modify all eventgroup occurrences, resolve or ignore all

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_eventgroup_occurrences = isi_sdk_8_0.EventEventgroupOccurrence() # EventEventgroupOccurrence | 

try:
    api_instance.update_event_eventgroup_occurrences(event_eventgroup_occurrences)
except ApiException as e:
    print("Exception when calling EventApi->update_event_eventgroup_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_eventgroup_occurrences** | [**EventEventgroupOccurrence**](EventEventgroupOccurrence.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_settings**
> update_event_settings(event_settings)



Update settings

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.EventApi(isi_sdk_8_0.ApiClient(configuration))
event_settings = isi_sdk_8_0.EventSettings() # EventSettings | 

try:
    api_instance.update_event_settings(event_settings)
except ApiException as e:
    print("Exception when calling EventApi->update_event_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_settings** | [**EventSettings**](EventSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

