# isi_sdk_7_2.AuditApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_topic**](AuditApi.md#create_audit_topic) | **POST** /platform/1/audit/topics | 
[**delete_audit_topic**](AuditApi.md#delete_audit_topic) | **DELETE** /platform/1/audit/topics/{AuditTopicId} | 
[**get_audit_settings**](AuditApi.md#get_audit_settings) | **GET** /platform/1/audit/settings | 
[**get_audit_topic**](AuditApi.md#get_audit_topic) | **GET** /platform/1/audit/topics/{AuditTopicId} | 
[**list_audit_topics**](AuditApi.md#list_audit_topics) | **GET** /platform/1/audit/topics | 
[**update_audit_settings**](AuditApi.md#update_audit_settings) | **PUT** /platform/1/audit/settings | 
[**update_audit_topic**](AuditApi.md#update_audit_topic) | **PUT** /platform/1/audit/topics/{AuditTopicId} | 


# **create_audit_topic**
> CreateResponse create_audit_topic(audit_topic)



Create a new audit topic.

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
api_instance = isi_sdk_7_2.AuditApi(isi_sdk_7_2.ApiClient(configuration))
audit_topic = isi_sdk_7_2.AuditTopicCreateParams() # AuditTopicCreateParams | 

try:
    api_response = api_instance.create_audit_topic(audit_topic)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->create_audit_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_topic** | [**AuditTopicCreateParams**](AuditTopicCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audit_topic**
> delete_audit_topic(audit_topic_id)



Delete the audit topic.

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
api_instance = isi_sdk_7_2.AuditApi(isi_sdk_7_2.ApiClient(configuration))
audit_topic_id = 'audit_topic_id_example' # str | Delete the audit topic.

try:
    api_instance.delete_audit_topic(audit_topic_id)
except ApiException as e:
    print("Exception when calling AuditApi->delete_audit_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_topic_id** | **str**| Delete the audit topic. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_settings**
> AuditSettings get_audit_settings()



Retrieves the auditing global settings.

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
api_instance = isi_sdk_7_2.AuditApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_audit_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditSettings**](AuditSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_topic**
> AuditTopics get_audit_topic(audit_topic_id)



Retrieve the audit topic information.

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
api_instance = isi_sdk_7_2.AuditApi(isi_sdk_7_2.ApiClient(configuration))
audit_topic_id = 'audit_topic_id_example' # str | Retrieve the audit topic information.

try:
    api_response = api_instance.get_audit_topic(audit_topic_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_topic_id** | **str**| Retrieve the audit topic information. | 

### Return type

[**AuditTopics**](AuditTopics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_topics**
> AuditTopicsExtended list_audit_topics()



Retrieve a list of audit topics.

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
api_instance = isi_sdk_7_2.AuditApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.list_audit_topics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->list_audit_topics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditTopicsExtended**](AuditTopicsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_settings**
> update_audit_settings(audit_settings)



Modify the auditing global settings.  All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_7_2.AuditApi(isi_sdk_7_2.ApiClient(configuration))
audit_settings = isi_sdk_7_2.AuditSettingsSettings() # AuditSettingsSettings | 

try:
    api_instance.update_audit_settings(audit_settings)
except ApiException as e:
    print("Exception when calling AuditApi->update_audit_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_settings** | [**AuditSettingsSettings**](AuditSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_topic**
> update_audit_topic(audit_topic, audit_topic_id)



Modify the audit topic.

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
api_instance = isi_sdk_7_2.AuditApi(isi_sdk_7_2.ApiClient(configuration))
audit_topic = isi_sdk_7_2.AuditTopic() # AuditTopic | 
audit_topic_id = 'audit_topic_id_example' # str | Modify the audit topic.

try:
    api_instance.update_audit_topic(audit_topic, audit_topic_id)
except ApiException as e:
    print("Exception when calling AuditApi->update_audit_topic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_topic** | [**AuditTopic**](AuditTopic.md)|  | 
 **audit_topic_id** | **str**| Modify the audit topic. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

