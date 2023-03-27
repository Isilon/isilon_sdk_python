# isilon_sdk.v9_3_0.EventApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_alert_condition**](EventApi.md#create_event_alert_condition) | **POST** /platform/4/event/alert-conditions | 
[**create_event_channel**](EventApi.md#create_event_channel) | **POST** /platform/12/event/channels | 
[**create_event_channel_0**](EventApi.md#create_event_channel_0) | **POST** /platform/12/event/channels/{EventChannelId} | 
[**create_event_event**](EventApi.md#create_event_event) | **POST** /platform/3/event/events | 
[**delete_event_alert_condition**](EventApi.md#delete_event_alert_condition) | **DELETE** /platform/4/event/alert-conditions/{EventAlertConditionId} | 
[**delete_event_alert_conditions**](EventApi.md#delete_event_alert_conditions) | **DELETE** /platform/4/event/alert-conditions | 
[**delete_event_channel**](EventApi.md#delete_event_channel) | **DELETE** /platform/12/event/channels/{EventChannelId} | 
[**get_event_alert_condition**](EventApi.md#get_event_alert_condition) | **GET** /platform/4/event/alert-conditions/{EventAlertConditionId} | 
[**get_event_categories**](EventApi.md#get_event_categories) | **GET** /platform/3/event/categories | 
[**get_event_category**](EventApi.md#get_event_category) | **GET** /platform/3/event/categories/{EventCategoryId} | 
[**get_event_channel**](EventApi.md#get_event_channel) | **GET** /platform/12/event/channels/{EventChannelId} | 
[**get_event_eventgroup_definition**](EventApi.md#get_event_eventgroup_definition) | **GET** /platform/12/event/eventgroup-definitions/{EventEventgroupDefinitionId} | 
[**get_event_eventgroup_definitions**](EventApi.md#get_event_eventgroup_definitions) | **GET** /platform/12/event/eventgroup-definitions | 
[**get_event_eventgroup_occurrence**](EventApi.md#get_event_eventgroup_occurrence) | **GET** /platform/12/event/eventgroup-occurrences/{EventEventgroupOccurrenceId} | 
[**get_event_eventgroup_occurrences**](EventApi.md#get_event_eventgroup_occurrences) | **GET** /platform/12/event/eventgroup-occurrences | 
[**get_event_eventlist**](EventApi.md#get_event_eventlist) | **GET** /platform/7/event/eventlists/{EventEventlistId} | 
[**get_event_eventlists**](EventApi.md#get_event_eventlists) | **GET** /platform/7/event/eventlists | 
[**get_event_maintenance**](EventApi.md#get_event_maintenance) | **GET** /platform/12/event/maintenance | 
[**get_event_settings**](EventApi.md#get_event_settings) | **GET** /platform/14/event/settings | 
[**get_event_suppress**](EventApi.md#get_event_suppress) | **GET** /platform/12/event/suppress | 
[**get_event_suppress_by_id**](EventApi.md#get_event_suppress_by_id) | **GET** /platform/12/event/suppress/{EventSuppressId} | 
[**get_event_threshold**](EventApi.md#get_event_threshold) | **GET** /platform/11/event/thresholds/{EventThresholdId} | 
[**get_event_thresholds**](EventApi.md#get_event_thresholds) | **GET** /platform/11/event/thresholds | 
[**list_event_alert_conditions**](EventApi.md#list_event_alert_conditions) | **GET** /platform/4/event/alert-conditions | 
[**list_event_channels**](EventApi.md#list_event_channels) | **GET** /platform/12/event/channels | 
[**update_event_alert_condition**](EventApi.md#update_event_alert_condition) | **PUT** /platform/4/event/alert-conditions/{EventAlertConditionId} | 
[**update_event_channel**](EventApi.md#update_event_channel) | **PUT** /platform/12/event/channels/{EventChannelId} | 
[**update_event_eventgroup_occurrence**](EventApi.md#update_event_eventgroup_occurrence) | **PUT** /platform/12/event/eventgroup-occurrences/{EventEventgroupOccurrenceId} | 
[**update_event_eventgroup_occurrences**](EventApi.md#update_event_eventgroup_occurrences) | **PUT** /platform/12/event/eventgroup-occurrences | 
[**update_event_maintenance**](EventApi.md#update_event_maintenance) | **PUT** /platform/12/event/maintenance | 
[**update_event_settings**](EventApi.md#update_event_settings) | **PUT** /platform/14/event/settings | 
[**update_event_suppress_by_id**](EventApi.md#update_event_suppress_by_id) | **PUT** /platform/12/event/suppress/{EventSuppressId} | 
[**update_event_threshold**](EventApi.md#update_event_threshold) | **PUT** /platform/11/event/thresholds/{EventThresholdId} | 


# **create_event_alert_condition**
> CreateResponse create_event_alert_condition(event_alert_condition)



Create a new alert condition.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_alert_condition = isilon_sdk.v9_3_0.EventAlertConditionCreateParams() # EventAlertConditionCreateParams | 

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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_channel = isilon_sdk.v9_3_0.EventChannelCreateParams() # EventChannelCreateParams | 

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

# **create_event_channel_0**
> create_event_channel_0(event_channel, event_channel_id)



Send a test message to the channel.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_channel = isilon_sdk.v9_3_0.Empty() # Empty | 
event_channel_id = 'event_channel_id_example' # str | Send a test message to the channel.

try:
    api_instance.create_event_channel_0(event_channel, event_channel_id)
except ApiException as e:
    print("Exception when calling EventApi->create_event_channel_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_channel** | [**Empty**](Empty.md)|  | 
 **event_channel_id** | **str**| Send a test message to the channel. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event_event**
> CreateQuotaReportResponse create_event_event(event_event)



Create a test event.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_event = isilon_sdk.v9_3_0.EventEvent() # EventEvent | 

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

[**CreateQuotaReportResponse**](CreateQuotaReportResponse.md)

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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
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



Delete the channel.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_channel_id = 'event_channel_id_example' # str | Delete the channel.

try:
    api_instance.delete_event_channel(event_channel_id)
except ApiException as e:
    print("Exception when calling EventApi->delete_event_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_channel_id** | **str**| Delete the channel. | 

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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
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



Retrieve the channel.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_channel_id = 'event_channel_id_example' # str | Retrieve the channel.

try:
    api_response = api_instance.get_event_channel(event_channel_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_channel_id** | **str**| Retrieve the channel. | 

### Return type

[**EventChannels**](EventChannels.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventgroup_definition**
> EventEventgroupDefinitions get_event_eventgroup_definition(event_eventgroup_definition_id, alert_info=alert_info)



Retrieve the eventgroup definition.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_eventgroup_definition_id = 'event_eventgroup_definition_id_example' # str | Retrieve the eventgroup definition.
alert_info = true # bool | Include alert rules and channels in output. (optional)

try:
    api_response = api_instance.get_event_eventgroup_definition(event_eventgroup_definition_id, alert_info=alert_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventgroup_definition: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_eventgroup_definition_id** | **str**| Retrieve the eventgroup definition. | 
 **alert_info** | **bool**| Include alert rules and channels in output. | [optional] 

### Return type

[**EventEventgroupDefinitions**](EventEventgroupDefinitions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventgroup_definitions**
> EventEventgroupDefinitionsExtended get_event_eventgroup_definitions(alert_info=alert_info, category=category, limit=limit, resume=resume)



List all eventgroup definitions.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
alert_info = true # bool | Include alert rules and channels in output. (optional)
category = 56 # int | Return eventgroups in the specified category. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_event_eventgroup_definitions(alert_info=alert_info, category=category, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventgroup_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_info** | **bool**| Include alert rules and channels in output. | [optional] 
 **category** | **int**| Return eventgroups in the specified category. | [optional] 
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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
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
> EventEventgroupOccurrencesExtended get_event_eventgroup_occurrences(begin=begin, cause=cause, devid=devid, dir=dir, end=end, event_count=event_count, ignore=ignore, last_event_begin=last_event_begin, last_event_end=last_event_end, limit=limit, maintenance=maintenance, partial_cause_long=partial_cause_long, partial_event_type=partial_event_type, partial_eventgroup_id=partial_eventgroup_id, resolved=resolved, resolver=resolver, resume=resume, severity=severity, sort=sort)



List all eventgroup occurrences.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
begin = 56 # int | Events that are in progress after this time. (optional)
cause = 'cause_example' # str | Filter by cause. (optional)
devid = [56] # list[int] | Filter by devid. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
end = 56 # int | Events that were in progress before this time. (optional)
event_count = 56 # int | Events for which event_count > this. (optional)
ignore = true # bool | Filter by ignored eventgroups. (optional)
last_event_begin = 56 # int | Filter eventgroups by those that have last_event after this time. (optional)
last_event_end = 56 # int | Filter eventgroups by those that have last_event before this time. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
maintenance = true # bool | Filter by eventgroups created during maintenance mode. (optional)
partial_cause_long = 'partial_cause_long_example' # str | Filter by partial long-cause description. (optional)
partial_event_type = 'partial_event_type_example' # str | Filter eventgroups by there associated event's event-type number. (optional)
partial_eventgroup_id = 'partial_eventgroup_id_example' # str | Filter by partial eventgroup id. (optional)
resolved = true # bool | Filter by resolved eventgroups. (optional)
resolver = 'resolver_example' # str | Filter by eventgroup resolver. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
severity = ['severity_example'] # list[str] | Filter by severity. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_event_eventgroup_occurrences(begin=begin, cause=cause, devid=devid, dir=dir, end=end, event_count=event_count, ignore=ignore, last_event_begin=last_event_begin, last_event_end=last_event_end, limit=limit, maintenance=maintenance, partial_cause_long=partial_cause_long, partial_event_type=partial_event_type, partial_eventgroup_id=partial_eventgroup_id, resolved=resolved, resolver=resolver, resume=resume, severity=severity, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventgroup_occurrences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Events that are in progress after this time. | [optional] 
 **cause** | **str**| Filter by cause. | [optional] 
 **devid** | [**list[int]**](int.md)| Filter by devid. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **end** | **int**| Events that were in progress before this time. | [optional] 
 **event_count** | **int**| Events for which event_count &gt; this. | [optional] 
 **ignore** | **bool**| Filter by ignored eventgroups. | [optional] 
 **last_event_begin** | **int**| Filter eventgroups by those that have last_event after this time. | [optional] 
 **last_event_end** | **int**| Filter eventgroups by those that have last_event before this time. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **maintenance** | **bool**| Filter by eventgroups created during maintenance mode. | [optional] 
 **partial_cause_long** | **str**| Filter by partial long-cause description. | [optional] 
 **partial_event_type** | **str**| Filter eventgroups by there associated event&#39;s event-type number. | [optional] 
 **partial_eventgroup_id** | **str**| Filter by partial eventgroup id. | [optional] 
 **resolved** | **bool**| Filter by resolved eventgroups. | [optional] 
 **resolver** | **str**| Filter by eventgroup resolver. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **severity** | [**list[str]**](str.md)| Filter by severity. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

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



Retrieve the list of events for an eventgroup occurrence.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_eventlist_id = 'event_eventlist_id_example' # str | Retrieve the list of events for an eventgroup occurrence.

try:
    api_response = api_instance.get_event_eventlist(event_eventlist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_eventlist_id** | **str**| Retrieve the list of events for an eventgroup occurrence. | 

### Return type

[**EventEventlists**](EventEventlists.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_eventlists**
> EventEventlistsExtended get_event_eventlists(event_instance=event_instance, eventgroup_id=eventgroup_id, limit=limit, resume=resume)



List all event occurrences grouped by eventgroup occurrence.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_instance = 'event_instance_example' # str | Return only this event occurrence (optional)
eventgroup_id = [56] # list[int] | Filter by eventgroup id. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_event_eventlists(event_instance=event_instance, eventgroup_id=eventgroup_id, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_eventlists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_instance** | **str**| Return only this event occurrence | [optional] 
 **eventgroup_id** | [**list[int]**](int.md)| Filter by eventgroup id. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventEventlistsExtended**](EventEventlistsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_maintenance**
> EventMaintenance get_event_maintenance(history=history, limit=limit, resume=resume)



List maintenance mode history.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
history = true # bool | True to list history. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_event_maintenance(history=history, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **history** | **bool**| True to list history. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventMaintenance**](EventMaintenance.md)

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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))

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

# **get_event_suppress**
> EventSuppress get_event_suppress()



List all event type IDs which are suppressed.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))

try:
    api_response = api_instance.get_event_suppress()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_suppress: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventSuppress**](EventSuppress.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_suppress_by_id**
> EventSuppressIdParams get_event_suppress_by_id(event_suppress_id)



Indicate whether this event type ID is suppressed.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_suppress_id = 'event_suppress_id_example' # str | Indicate whether this event type ID is suppressed.

try:
    api_response = api_instance.get_event_suppress_by_id(event_suppress_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_suppress_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_suppress_id** | **str**| Indicate whether this event type ID is suppressed. | 

### Return type

[**EventSuppressIdParams**](EventSuppressIdParams.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_threshold**
> EventThresholds get_event_threshold(event_threshold_id, event_id=event_id, limit=limit, resume=resume)



List all configurable event thresholds

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_threshold_id = 'event_threshold_id_example' # str | List all configurable event thresholds
event_id = 56 # int | Return thresholds for the specified event id (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_event_threshold(event_threshold_id, event_id=event_id, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_threshold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_threshold_id** | **str**| List all configurable event thresholds | 
 **event_id** | **int**| Return thresholds for the specified event id | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventThresholds**](EventThresholds.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_thresholds**
> EventThresholds get_event_thresholds(event_id=event_id, limit=limit, resume=resume)



List all configurable event thresholds

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_id = 56 # int | Return thresholds for the specified event id (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_event_thresholds(event_id=event_id, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->get_event_thresholds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**| Return thresholds for the specified event id | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**EventThresholds**](EventThresholds.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_alert_conditions**
> EventAlertConditionsExtended list_event_alert_conditions(channels=channels, dir=dir, limit=limit, resume=resume, sort=sort)



List all alert conditions.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
channels = 'channels_example' # str | Return only conditions for the specified channel: (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_event_alert_conditions(channels=channels, dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->list_event_alert_conditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channels** | **str**| Return only conditions for the specified channel: | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**EventAlertConditionsExtended**](EventAlertConditionsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_channels**
> EventChannelsExtended list_event_channels(dir=dir, limit=limit, resume=resume, sort=sort)



List all channels.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_event_channels(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventApi->list_event_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

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
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_alert_condition = isilon_sdk.v9_3_0.EventAlertCondition() # EventAlertCondition | 
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



Modify the channel.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_channel = isilon_sdk.v9_3_0.EventChannel() # EventChannel | 
event_channel_id = 'event_channel_id_example' # str | Modify the channel.

try:
    api_instance.update_event_channel(event_channel, event_channel_id)
except ApiException as e:
    print("Exception when calling EventApi->update_event_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_channel** | [**EventChannel**](EventChannel.md)|  | 
 **event_channel_id** | **str**| Modify the channel. | 

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



Modify eventgroup occurrence.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_eventgroup_occurrence = isilon_sdk.v9_3_0.EventEventgroupOccurrence() # EventEventgroupOccurrence | 
event_eventgroup_occurrence_id = 'event_eventgroup_occurrence_id_example' # str | Modify eventgroup occurrence.

try:
    api_instance.update_event_eventgroup_occurrence(event_eventgroup_occurrence, event_eventgroup_occurrence_id)
except ApiException as e:
    print("Exception when calling EventApi->update_event_eventgroup_occurrence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_eventgroup_occurrence** | [**EventEventgroupOccurrence**](EventEventgroupOccurrence.md)|  | 
 **event_eventgroup_occurrence_id** | **str**| Modify eventgroup occurrence. | 

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



Modify all eventgroup occurrences, resolve or ignore all.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_eventgroup_occurrences = isilon_sdk.v9_3_0.EventEventgroupOccurrence() # EventEventgroupOccurrence | 

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

# **update_event_maintenance**
> update_event_maintenance(event_maintenance)



Perform an action, enable/disable maintenance mode.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_maintenance = isilon_sdk.v9_3_0.EventMaintenanceExtended() # EventMaintenanceExtended | 

try:
    api_instance.update_event_maintenance(event_maintenance)
except ApiException as e:
    print("Exception when calling EventApi->update_event_maintenance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_maintenance** | [**EventMaintenanceExtended**](EventMaintenanceExtended.md)|  | 

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



Modify settings.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_settings = isilon_sdk.v9_3_0.EventSettingsSettings() # EventSettingsSettings | 

try:
    api_instance.update_event_settings(event_settings)
except ApiException as e:
    print("Exception when calling EventApi->update_event_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_settings** | [**EventSettingsSettings**](EventSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_suppress_by_id**
> update_event_suppress_by_id(event_suppress_id_params, event_suppress_id)



Suppress or un-suppress this event type ID.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_suppress_id_params = isilon_sdk.v9_3_0.EventSuppressIdParams() # EventSuppressIdParams | 
event_suppress_id = 'event_suppress_id_example' # str | Suppress or un-suppress this event type ID.

try:
    api_instance.update_event_suppress_by_id(event_suppress_id_params, event_suppress_id)
except ApiException as e:
    print("Exception when calling EventApi->update_event_suppress_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_suppress_id_params** | [**EventSuppressIdParams**](EventSuppressIdParams.md)|  | 
 **event_suppress_id** | **str**| Suppress or un-suppress this event type ID. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_threshold**
> update_event_threshold(event_threshold, event_threshold_id)



Modify event thresholds.

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
api_instance = isilon_sdk.v9_3_0.EventApi(isilon_sdk.v9_3_0.ApiClient(configuration))
event_threshold = isilon_sdk.v9_3_0.EventThreshold() # EventThreshold | 
event_threshold_id = 'event_threshold_id_example' # str | Modify event thresholds.

try:
    api_instance.update_event_threshold(event_threshold, event_threshold_id)
except ApiException as e:
    print("Exception when calling EventApi->update_event_threshold: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_threshold** | [**EventThreshold**](EventThreshold.md)|  | 
 **event_threshold_id** | **str**| Modify event thresholds. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

