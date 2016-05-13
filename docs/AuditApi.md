# isi_sdk.AuditApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_topic**](AuditApi.md#create_audit_topic) | **POST** /platform/1/audit/topics | 
[**delete_audit_topic**](AuditApi.md#delete_audit_topic) | **DELETE** /platform/1/audit/topics/{AuditTopicId} | 
[**get_audit_settings**](AuditApi.md#get_audit_settings) | **GET** /platform/3/audit/settings | 
[**get_audit_topic**](AuditApi.md#get_audit_topic) | **GET** /platform/1/audit/topics/{AuditTopicId} | 
[**get_settings_global**](AuditApi.md#get_settings_global) | **GET** /platform/3/audit/settings/global | 
[**list_audit_topics**](AuditApi.md#list_audit_topics) | **GET** /platform/1/audit/topics | 
[**update_audit_settings**](AuditApi.md#update_audit_settings) | **PUT** /platform/3/audit/settings | 
[**update_audit_topic**](AuditApi.md#update_audit_topic) | **PUT** /platform/1/audit/topics/{AuditTopicId} | 
[**update_settings_global**](AuditApi.md#update_settings_global) | **PUT** /platform/3/audit/settings/global | 


# **create_audit_topic**
> CreateResponse create_audit_topic(audit_topic)



Create a new audit topic.

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
api_instance = isi_sdk.AuditApi()
audit_topic = isi_sdk.AuditTopicCreateParams() # AuditTopicCreateParams | 

try: 
    api_response = api_instance.create_audit_topic(audit_topic)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditApi->create_audit_topic: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_topic** | [**AuditTopicCreateParams**](AuditTopicCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audit_topic**
> delete_audit_topic(audit_topic_id)



Delete the audit topic.

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
api_instance = isi_sdk.AuditApi()
audit_topic_id = 'audit_topic_id_example' # str | Delete the audit topic.

try: 
    api_instance.delete_audit_topic(audit_topic_id)
except ApiException as e:
    print "Exception when calling AuditApi->delete_audit_topic: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_topic_id** | **str**| Delete the audit topic. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_settings**
> AuditSettings get_audit_settings(zone=zone)



View per-Access Zone Audit settings.

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
api_instance = isi_sdk.AuditApi()
zone = 'zone_example' # str | Access zone which contains audit settings. (optional)

try: 
    api_response = api_instance.get_audit_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditApi->get_audit_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains audit settings. | [optional] 

### Return type

[**AuditSettings**](AuditSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_topic**
> AuditTopics get_audit_topic(audit_topic_id)



Retrieve the audit topic information.

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
api_instance = isi_sdk.AuditApi()
audit_topic_id = 'audit_topic_id_example' # str | Retrieve the audit topic information.

try: 
    api_response = api_instance.get_audit_topic(audit_topic_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditApi->get_audit_topic: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_topic_id** | **str**| Retrieve the audit topic information. | 

### Return type

[**AuditTopics**](AuditTopics.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_global**
> SettingsGlobalExtended get_settings_global()



View Global Audit settings.

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
api_instance = isi_sdk.AuditApi()

try: 
    api_response = api_instance.get_settings_global()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditApi->get_settings_global: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsGlobalExtended**](SettingsGlobalExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_topics**
> AuditTopicsExtended list_audit_topics()



Retrieve a list of audit topics.

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
api_instance = isi_sdk.AuditApi()

try: 
    api_response = api_instance.list_audit_topics()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuditApi->list_audit_topics: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditTopicsExtended**](AuditTopicsExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_settings**
> update_audit_settings(audit_settings, zone=zone)



Modify per-Access Zone Audit settings.

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
api_instance = isi_sdk.AuditApi()
audit_settings = isi_sdk.AuditSettingsSettings() # AuditSettingsSettings | 
zone = 'zone_example' # str | Access zone which contains audit settings. (optional)

try: 
    api_instance.update_audit_settings(audit_settings, zone=zone)
except ApiException as e:
    print "Exception when calling AuditApi->update_audit_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_settings** | [**AuditSettingsSettings**](AuditSettingsSettings.md)|  | 
 **zone** | **str**| Access zone which contains audit settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_topic**
> update_audit_topic(audit_topic, audit_topic_id)



Modify the audit topic.

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
api_instance = isi_sdk.AuditApi()
audit_topic = isi_sdk.AuditTopic() # AuditTopic | 
audit_topic_id = 'audit_topic_id_example' # str | Modify the audit topic.

try: 
    api_instance.update_audit_topic(audit_topic, audit_topic_id)
except ApiException as e:
    print "Exception when calling AuditApi->update_audit_topic: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_topic** | [**AuditTopic**](AuditTopic.md)|  | 
 **audit_topic_id** | **str**| Modify the audit topic. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_global**
> update_settings_global(settings_global)



Modify Global Audit settings.

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
api_instance = isi_sdk.AuditApi()
settings_global = isi_sdk.SettingsGlobalSettings() # SettingsGlobalSettings | 

try: 
    api_instance.update_settings_global(settings_global)
except ApiException as e:
    print "Exception when calling AuditApi->update_settings_global: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_global** | [**SettingsGlobalSettings**](SettingsGlobalSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

