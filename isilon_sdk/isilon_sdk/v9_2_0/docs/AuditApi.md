# isilon_sdk.v9_2_0.AuditApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_topic**](AuditApi.md#create_audit_topic) | **POST** /platform/1/audit/topics | 
[**delete_audit_logs**](AuditApi.md#delete_audit_logs) | **DELETE** /platform/11/audit/logs | 
[**delete_audit_topic**](AuditApi.md#delete_audit_topic) | **DELETE** /platform/1/audit/topics/{AuditTopicId} | 
[**get_audit_logs**](AuditApi.md#get_audit_logs) | **GET** /platform/11/audit/logs | 
[**get_audit_progress**](AuditApi.md#get_audit_progress) | **GET** /platform/4/audit/progress | 
[**get_audit_settings**](AuditApi.md#get_audit_settings) | **GET** /platform/7/audit/settings | 
[**get_audit_topic**](AuditApi.md#get_audit_topic) | **GET** /platform/1/audit/topics/{AuditTopicId} | 
[**get_progress_global**](AuditApi.md#get_progress_global) | **GET** /platform/4/audit/progress/global | 
[**get_settings_global**](AuditApi.md#get_settings_global) | **GET** /platform/11/audit/settings/global | 
[**list_audit_topics**](AuditApi.md#list_audit_topics) | **GET** /platform/1/audit/topics | 
[**update_audit_settings**](AuditApi.md#update_audit_settings) | **PUT** /platform/7/audit/settings | 
[**update_audit_topic**](AuditApi.md#update_audit_topic) | **PUT** /platform/1/audit/topics/{AuditTopicId} | 
[**update_settings_global**](AuditApi.md#update_settings_global) | **PUT** /platform/11/audit/settings/global | 


# **create_audit_topic**
> CreateResponse create_audit_topic(audit_topic)



Create a new audit topic.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
audit_topic = isilon_sdk.v9_2_0.AuditTopicCreateParams() # AuditTopicCreateParams | 

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

# **delete_audit_logs**
> delete_audit_logs(before, force=force)



Manually delete audit log files.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
before = 56 # int | The timestamp before which logs will be deleted.
force = true # bool | Do not ask for confirmation. (optional)

try:
    api_instance.delete_audit_logs(before, force=force)
except ApiException as e:
    print("Exception when calling AuditApi->delete_audit_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **before** | **int**| The timestamp before which logs will be deleted. | 
 **force** | **bool**| Do not ask for confirmation. | [optional] 

### Return type

void (empty response body)

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
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
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

# **get_audit_logs**
> AuditLogs get_audit_logs()



Get the manual deletion status.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_audit_logs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_logs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditLogs**](AuditLogs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_progress**
> AuditProgress get_audit_progress(lnn=lnn)



View current audit log time.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
lnn = 56 # int | lnn of the node. (optional)

try:
    api_response = api_instance.get_audit_progress(lnn=lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**| lnn of the node. | [optional] 

### Return type

[**AuditProgress**](AuditProgress.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_settings**
> AuditSettings get_audit_settings(zone=zone)



View per-Access Zone Audit settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
zone = 'zone_example' # str | Access zone which contains audit settings. (optional)

try:
    api_response = api_instance.get_audit_settings(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone which contains audit settings. | [optional] 

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
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
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

# **get_progress_global**
> ProgressGlobal get_progress_global()



View the global audit log time.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_progress_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_progress_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProgressGlobal**](ProgressGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_global**
> SettingsGlobalExtended get_settings_global()



View global audit settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_settings_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsGlobalExtended**](SettingsGlobalExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_topics**
> AuditTopics list_audit_topics()



Retrieve a list of audit topics.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))

try:
    api_response = api_instance.list_audit_topics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->list_audit_topics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuditTopics**](AuditTopics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_settings**
> update_audit_settings(audit_settings, zone=zone)



Modify per-Access Zone Audit settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
audit_settings = isilon_sdk.v9_2_0.AuditSettingsSettings() # AuditSettingsSettings | 
zone = 'zone_example' # str | Access zone which contains audit settings. (optional)

try:
    api_instance.update_audit_settings(audit_settings, zone=zone)
except ApiException as e:
    print("Exception when calling AuditApi->update_audit_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_settings** | [**AuditSettingsSettings**](AuditSettingsSettings.md)|  | 
 **zone** | **str**| Access zone which contains audit settings. | [optional] 

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
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
audit_topic = isilon_sdk.v9_2_0.AuditTopic() # AuditTopic | 
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

# **update_settings_global**
> update_settings_global(settings_global, force=force)



Modify global audit settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_0
from isilon_sdk.v9_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_0.AuditApi(isilon_sdk.v9_2_0.ApiClient(configuration))
settings_global = isilon_sdk.v9_2_0.SettingsGlobalSettings() # SettingsGlobalSettings | 
force = true # bool | Do not ask for confirmation. (optional)

try:
    api_instance.update_settings_global(settings_global, force=force)
except ApiException as e:
    print("Exception when calling AuditApi->update_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_global** | [**SettingsGlobalSettings**](SettingsGlobalSettings.md)|  | 
 **force** | **bool**| Do not ask for confirmation. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

