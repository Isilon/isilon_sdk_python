# isilon_sdk.v9_5_0.AuditApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_audit_topic**](AuditApi.md#create_audit_topic) | **POST** /platform/1/audit/topics | 
[**create_certificates_syslog_item**](AuditApi.md#create_certificates_syslog_item) | **POST** /platform/16/audit/certificates/syslog | 
[**delete_audit_logs**](AuditApi.md#delete_audit_logs) | **DELETE** /platform/11/audit/logs | 
[**delete_audit_topic**](AuditApi.md#delete_audit_topic) | **DELETE** /platform/1/audit/topics/{AuditTopicId} | 
[**delete_certificates_syslog_by_id**](AuditApi.md#delete_certificates_syslog_by_id) | **DELETE** /platform/16/audit/certificates/syslog/{CertificatesSyslogId} | 
[**get_audit_logs**](AuditApi.md#get_audit_logs) | **GET** /platform/11/audit/logs | 
[**get_audit_progress**](AuditApi.md#get_audit_progress) | **GET** /platform/4/audit/progress | 
[**get_audit_settings**](AuditApi.md#get_audit_settings) | **GET** /platform/16/audit/settings | 
[**get_audit_topic**](AuditApi.md#get_audit_topic) | **GET** /platform/1/audit/topics/{AuditTopicId} | 
[**get_certificates_syslog_by_id**](AuditApi.md#get_certificates_syslog_by_id) | **GET** /platform/16/audit/certificates/syslog/{CertificatesSyslogId} | 
[**get_progress_global**](AuditApi.md#get_progress_global) | **GET** /platform/4/audit/progress/global | 
[**get_settings_global**](AuditApi.md#get_settings_global) | **GET** /platform/16/audit/settings/global | 
[**list_audit_topics**](AuditApi.md#list_audit_topics) | **GET** /platform/1/audit/topics | 
[**list_certificates_syslog**](AuditApi.md#list_certificates_syslog) | **GET** /platform/16/audit/certificates/syslog | 
[**update_audit_settings**](AuditApi.md#update_audit_settings) | **PUT** /platform/16/audit/settings | 
[**update_audit_topic**](AuditApi.md#update_audit_topic) | **PUT** /platform/1/audit/topics/{AuditTopicId} | 
[**update_certificates_syslog_by_id**](AuditApi.md#update_certificates_syslog_by_id) | **PUT** /platform/16/audit/certificates/syslog/{CertificatesSyslogId} | 
[**update_settings_global**](AuditApi.md#update_settings_global) | **PUT** /platform/16/audit/settings/global | 


# **create_audit_topic**
> CreateResponse create_audit_topic(audit_topic)



Create a new audit topic.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
audit_topic = isilon_sdk.v9_5_0.AuditTopicCreateParams() # AuditTopicCreateParams | 

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

# **create_certificates_syslog_item**
> CreateResponse create_certificates_syslog_item(certificates_syslog_item)



Import a syslog TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
certificates_syslog_item = isilon_sdk.v9_5_0.CertificatesSyslogItem() # CertificatesSyslogItem | 

try:
    api_response = api_instance.create_certificates_syslog_item(certificates_syslog_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->create_certificates_syslog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_syslog_item** | [**CertificatesSyslogItem**](CertificatesSyslogItem.md)|  | 

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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
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

# **delete_certificates_syslog_by_id**
> delete_certificates_syslog_by_id(certificates_syslog_id)



Delete a syslog TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
certificates_syslog_id = 'certificates_syslog_id_example' # str | Delete a syslog TLS server certificate.

try:
    api_instance.delete_certificates_syslog_by_id(certificates_syslog_id)
except ApiException as e:
    print("Exception when calling AuditApi->delete_certificates_syslog_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_syslog_id** | **str**| Delete a syslog TLS server certificate. | 

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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))

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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
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

# **get_certificates_syslog_by_id**
> CertificatesCa get_certificates_syslog_by_id(certificates_syslog_id)



Retrieve a syslog TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
certificates_syslog_id = 'certificates_syslog_id_example' # str | Retrieve a syslog TLS server certificate.

try:
    api_response = api_instance.get_certificates_syslog_by_id(certificates_syslog_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_certificates_syslog_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_syslog_id** | **str**| Retrieve a syslog TLS server certificate. | 

### Return type

[**CertificatesCa**](CertificatesCa.md)

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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))

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
> SettingsGlobal get_settings_global()



View global audit settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_settings_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsGlobal**](SettingsGlobal.md)

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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))

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

# **list_certificates_syslog**
> CertificatesCaExtended list_certificates_syslog(dir=dir, limit=limit, resume=resume, sort=sort)



Retrieve a list of all syslog TLS server certificates.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_certificates_syslog(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->list_certificates_syslog: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CertificatesCaExtended**](CertificatesCaExtended.md)

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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
audit_settings = isilon_sdk.v9_5_0.AuditSettingsSettings() # AuditSettingsSettings | 
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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
audit_topic = isilon_sdk.v9_5_0.AuditTopic() # AuditTopic | 
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

# **update_certificates_syslog_by_id**
> update_certificates_syslog_by_id(certificates_syslog_id_params, certificates_syslog_id)



Modify a syslog TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
certificates_syslog_id_params = isilon_sdk.v9_5_0.CertificatesSyslogIdParams() # CertificatesSyslogIdParams | 
certificates_syslog_id = 'certificates_syslog_id_example' # str | Modify a syslog TLS server certificate.

try:
    api_instance.update_certificates_syslog_by_id(certificates_syslog_id_params, certificates_syslog_id)
except ApiException as e:
    print("Exception when calling AuditApi->update_certificates_syslog_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_syslog_id_params** | [**CertificatesSyslogIdParams**](CertificatesSyslogIdParams.md)|  | 
 **certificates_syslog_id** | **str**| Modify a syslog TLS server certificate. | 

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
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuditApi(isilon_sdk.v9_5_0.ApiClient(configuration))
settings_global = isilon_sdk.v9_5_0.SettingsGlobalSettings() # SettingsGlobalSettings | 
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

