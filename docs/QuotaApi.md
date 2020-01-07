# isi_sdk_8_2_1.QuotaApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quota_quota**](QuotaApi.md#create_quota_quota) | **POST** /platform/8/quota/quotas | 
[**create_quota_report**](QuotaApi.md#create_quota_report) | **POST** /platform/1/quota/reports | 
[**create_settings_mapping**](QuotaApi.md#create_settings_mapping) | **POST** /platform/1/quota/settings/mappings | 
[**create_settings_notification**](QuotaApi.md#create_settings_notification) | **POST** /platform/7/quota/settings/notifications | 
[**delete_quota_quota**](QuotaApi.md#delete_quota_quota) | **DELETE** /platform/8/quota/quotas/{QuotaQuotaId} | 
[**delete_quota_quotas**](QuotaApi.md#delete_quota_quotas) | **DELETE** /platform/8/quota/quotas | 
[**delete_quota_report**](QuotaApi.md#delete_quota_report) | **DELETE** /platform/1/quota/reports/{QuotaReportId} | 
[**delete_settings_mapping**](QuotaApi.md#delete_settings_mapping) | **DELETE** /platform/1/quota/settings/mappings/{SettingsMappingId} | 
[**delete_settings_mappings**](QuotaApi.md#delete_settings_mappings) | **DELETE** /platform/1/quota/settings/mappings | 
[**delete_settings_notification**](QuotaApi.md#delete_settings_notification) | **DELETE** /platform/7/quota/settings/notifications/{SettingsNotificationId} | 
[**delete_settings_notifications**](QuotaApi.md#delete_settings_notifications) | **DELETE** /platform/7/quota/settings/notifications | 
[**get_quota_license**](QuotaApi.md#get_quota_license) | **GET** /platform/5/quota/license | 
[**get_quota_quota**](QuotaApi.md#get_quota_quota) | **GET** /platform/8/quota/quotas/{QuotaQuotaId} | 
[**get_quota_quotas_summary**](QuotaApi.md#get_quota_quotas_summary) | **GET** /platform/1/quota/quotas-summary | 
[**get_quota_report**](QuotaApi.md#get_quota_report) | **GET** /platform/1/quota/reports/{QuotaReportId} | 
[**get_settings_mapping**](QuotaApi.md#get_settings_mapping) | **GET** /platform/1/quota/settings/mappings/{SettingsMappingId} | 
[**get_settings_notification**](QuotaApi.md#get_settings_notification) | **GET** /platform/7/quota/settings/notifications/{SettingsNotificationId} | 
[**get_settings_reports**](QuotaApi.md#get_settings_reports) | **GET** /platform/1/quota/settings/reports | 
[**list_quota_quotas**](QuotaApi.md#list_quota_quotas) | **GET** /platform/8/quota/quotas | 
[**list_quota_reports**](QuotaApi.md#list_quota_reports) | **GET** /platform/1/quota/reports | 
[**list_settings_mappings**](QuotaApi.md#list_settings_mappings) | **GET** /platform/1/quota/settings/mappings | 
[**list_settings_notifications**](QuotaApi.md#list_settings_notifications) | **GET** /platform/7/quota/settings/notifications | 
[**update_quota_quota**](QuotaApi.md#update_quota_quota) | **PUT** /platform/8/quota/quotas/{QuotaQuotaId} | 
[**update_settings_mapping**](QuotaApi.md#update_settings_mapping) | **PUT** /platform/1/quota/settings/mappings/{SettingsMappingId} | 
[**update_settings_notification**](QuotaApi.md#update_settings_notification) | **PUT** /platform/7/quota/settings/notifications/{SettingsNotificationId} | 
[**update_settings_reports**](QuotaApi.md#update_settings_reports) | **PUT** /platform/1/quota/settings/reports | 


# **create_quota_quota**
> CreateResponse create_quota_quota(quota_quota, zone=zone)



Create a new quota.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
quota_quota = isi_sdk_8_2_1.QuotaQuotaCreateParams() # QuotaQuotaCreateParams | 
zone = 'zone_example' # str | Optional named zone to use for user and group resolution. (optional)

try:
    api_response = api_instance.create_quota_quota(quota_quota, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->create_quota_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_quota** | [**QuotaQuotaCreateParams**](QuotaQuotaCreateParams.md)|  | 
 **zone** | **str**| Optional named zone to use for user and group resolution. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quota_report**
> CreateQuotaReportResponse create_quota_report(quota_report)



Create a new report. The type of this report is 'manual'; it is also sometimes called 'live' or 'ad-hoc'.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
quota_report = isi_sdk_8_2_1.Empty() # Empty | 

try:
    api_response = api_instance.create_quota_report(quota_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->create_quota_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_report** | [**Empty**](Empty.md)|  | 

### Return type

[**CreateQuotaReportResponse**](CreateQuotaReportResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_mapping**
> CreateResponse create_settings_mapping(settings_mapping)



Create a new rule. The new rule must not conflict with an existing rule (e.g. match both the type and domain fields).

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_mapping = isi_sdk_8_2_1.SettingsMappingCreateParams() # SettingsMappingCreateParams | 

try:
    api_response = api_instance.create_settings_mapping(settings_mapping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->create_settings_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_mapping** | [**SettingsMappingCreateParams**](SettingsMappingCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_notification**
> CreateResponse create_settings_notification(settings_notification)



Create a new global notification rule.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_notification = isi_sdk_8_2_1.QuotaNotificationCreateParams() # QuotaNotificationCreateParams | 

try:
    api_response = api_instance.create_settings_notification(settings_notification)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->create_settings_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_notification** | [**QuotaNotificationCreateParams**](QuotaNotificationCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quota_quota**
> delete_quota_quota(quota_quota_id)



Delete the quota.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
quota_quota_id = 'quota_quota_id_example' # str | Delete the quota.

try:
    api_instance.delete_quota_quota(quota_quota_id)
except ApiException as e:
    print("Exception when calling QuotaApi->delete_quota_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_quota_id** | **str**| Delete the quota. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quota_quotas**
> delete_quota_quotas(enforced=enforced, include_snapshots=include_snapshots, zone=zone, recurse_path_children=recurse_path_children, recurse_path_parents=recurse_path_parents, persona=persona, path=path, type=type)



Delete all or matching quotas.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
enforced = true # bool | Only delete quotas with this enforcement (non-accounting). (optional)
include_snapshots = true # bool | Only delete quotas with this setting for include_snapshots. (optional)
zone = 'zone_example' # str | Optional named zone to use for user and group resolution. (optional)
recurse_path_children = true # bool | If used with the path argument, delete all quotas at that path or any descendent sub-directory. (optional)
recurse_path_parents = true # bool | If used with the path argument, delete all quotas at that path or any parent directory. (optional)
persona = 'persona_example' # str | Only delete user or group quotas matching this persona (must be used with the corresponding type argument).  Format is <PERSONA_TYPE>:<string/integer>, where PERSONA_TYPE is one of USER, GROUP, SID, ID, or GID. (optional)
path = 'path_example' # str | Only delete quotas matching this path (see also recurse_path_*). (optional)
type = 'type_example' # str | Only delete quotas matching this type. (optional)

try:
    api_instance.delete_quota_quotas(enforced=enforced, include_snapshots=include_snapshots, zone=zone, recurse_path_children=recurse_path_children, recurse_path_parents=recurse_path_parents, persona=persona, path=path, type=type)
except ApiException as e:
    print("Exception when calling QuotaApi->delete_quota_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enforced** | **bool**| Only delete quotas with this enforcement (non-accounting). | [optional] 
 **include_snapshots** | **bool**| Only delete quotas with this setting for include_snapshots. | [optional] 
 **zone** | **str**| Optional named zone to use for user and group resolution. | [optional] 
 **recurse_path_children** | **bool**| If used with the path argument, delete all quotas at that path or any descendent sub-directory. | [optional] 
 **recurse_path_parents** | **bool**| If used with the path argument, delete all quotas at that path or any parent directory. | [optional] 
 **persona** | **str**| Only delete user or group quotas matching this persona (must be used with the corresponding type argument).  Format is &lt;PERSONA_TYPE&gt;:&lt;string/integer&gt;, where PERSONA_TYPE is one of USER, GROUP, SID, ID, or GID. | [optional] 
 **path** | **str**| Only delete quotas matching this path (see also recurse_path_*). | [optional] 
 **type** | **str**| Only delete quotas matching this type. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quota_report**
> delete_quota_report(quota_report_id)



Delete the report.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
quota_report_id = 'quota_report_id_example' # str | Delete the report.

try:
    api_instance.delete_quota_report(quota_report_id)
except ApiException as e:
    print("Exception when calling QuotaApi->delete_quota_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_report_id** | **str**| Delete the report. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_settings_mapping**
> delete_settings_mapping(settings_mapping_id)



Delete the mapping.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_mapping_id = 'settings_mapping_id_example' # str | Delete the mapping.

try:
    api_instance.delete_settings_mapping(settings_mapping_id)
except ApiException as e:
    print("Exception when calling QuotaApi->delete_settings_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_mapping_id** | **str**| Delete the mapping. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_settings_mappings**
> delete_settings_mappings()



Delete all rules.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))

try:
    api_instance.delete_settings_mappings()
except ApiException as e:
    print("Exception when calling QuotaApi->delete_settings_mappings: %s\n" % e)
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

# **delete_settings_notification**
> delete_settings_notification(settings_notification_id)



Delete the notification rule.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_notification_id = 'settings_notification_id_example' # str | Delete the notification rule.

try:
    api_instance.delete_settings_notification(settings_notification_id)
except ApiException as e:
    print("Exception when calling QuotaApi->delete_settings_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_notification_id** | **str**| Delete the notification rule. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_settings_notifications**
> delete_settings_notifications()



Delete all rules.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))

try:
    api_instance.delete_settings_notifications()
except ApiException as e:
    print("Exception when calling QuotaApi->delete_settings_notifications: %s\n" % e)
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

# **get_quota_license**
> LicenseLicense get_quota_license()



Retrieve license information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_quota_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_quota_license: %s\n" % e)
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

# **get_quota_quota**
> QuotaQuotas get_quota_quota(quota_quota_id, resolve_names=resolve_names, zone=zone)



Retrieve quota information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
quota_quota_id = 'quota_quota_id_example' # str | Retrieve quota information.
resolve_names = true # bool | If true, resolve group and user names in personas. (optional)
zone = 'zone_example' # str | Optional named zone to use for user and group resolution. (optional)

try:
    api_response = api_instance.get_quota_quota(quota_quota_id, resolve_names=resolve_names, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_quota_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_quota_id** | **str**| Retrieve quota information. | 
 **resolve_names** | **bool**| If true, resolve group and user names in personas. | [optional] 
 **zone** | **str**| Optional named zone to use for user and group resolution. | [optional] 

### Return type

[**QuotaQuotas**](QuotaQuotas.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota_quotas_summary**
> QuotaQuotasSummary get_quota_quotas_summary()



Return summary information about quotas.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_quota_quotas_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_quota_quotas_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuotaQuotasSummary**](QuotaQuotasSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota_report**
> ReportAbout get_quota_report(quota_report_id, contents=contents)



Retrieve report data (XML) or contents (meta-data).

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
quota_report_id = 'quota_report_id_example' # str | Retrieve report data (XML) or contents (meta-data).
contents = true # bool | Display JSON meta-data contents instead of report data. (optional)

try:
    api_response = api_instance.get_quota_report(quota_report_id, contents=contents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_quota_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_report_id** | **str**| Retrieve report data (XML) or contents (meta-data). | 
 **contents** | **bool**| Display JSON meta-data contents instead of report data. | [optional] 

### Return type

[**ReportAbout**](ReportAbout.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_mapping**
> SettingsMappings get_settings_mapping(settings_mapping_id)



Retrieve the mapping information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_mapping_id = 'settings_mapping_id_example' # str | Retrieve the mapping information.

try:
    api_response = api_instance.get_settings_mapping(settings_mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_settings_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_mapping_id** | **str**| Retrieve the mapping information. | 

### Return type

[**SettingsMappings**](SettingsMappings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_notification**
> QuotaNotifications get_settings_notification(settings_notification_id)



Retrieve notification rule information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_notification_id = 'settings_notification_id_example' # str | Retrieve notification rule information.

try:
    api_response = api_instance.get_settings_notification(settings_notification_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_settings_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_notification_id** | **str**| Retrieve notification rule information. | 

### Return type

[**QuotaNotifications**](QuotaNotifications.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_reports**
> SettingsReports get_settings_reports(scope=scope)



List all settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_settings_reports(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->get_settings_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**SettingsReports**](SettingsReports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quota_quotas**
> QuotaQuotasExtended list_quota_quotas(enforced=enforced, include_snapshots=include_snapshots, zone=zone, resume=resume, recurse_path_children=recurse_path_children, resolve_names=resolve_names, recurse_path_parents=recurse_path_parents, persona=persona, limit=limit, exceeded=exceeded, path=path, type=type, report_id=report_id)



List all or matching quotas. Can also be used to retrieve quota state from existing reports. For any query argument not supplied, the default behavior is return all.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
enforced = true # bool | Only list quotas with this enforcement (non-accounting). (optional)
include_snapshots = true # bool | Only list quotas with this setting for include_snapshots. (optional)
zone = 'zone_example' # str | Optional named zone to use for user and group resolution. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
recurse_path_children = true # bool | If used with the path argument, match all quotas at that path or any descendent sub-directory. (optional)
resolve_names = true # bool | If true, resolve group and user names in personas. (optional)
recurse_path_parents = true # bool | If used with the path argument, match all quotas at that path or any parent directory. (optional)
persona = 'persona_example' # str | Only list user or group quotas matching this persona (must be used with the corresponding type argument).  Format is <PERSONA_TYPE>:<string/integer>, where PERSONA_TYPE is one of USER, GROUP, SID, ID, or GID. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
exceeded = true # bool | Set to true to only list quotas which have exceeded one or more of their thresholds. (optional)
path = 'path_example' # str | Only list quotas matching this path (see also recurse_path_*). (optional)
type = 'type_example' # str | Only list quotas matching this type. (optional)
report_id = 'report_id_example' # str | Use the named report as a source rather than the live quotas. See the /q/quota/reports resource for a list of valid reports. (optional)

try:
    api_response = api_instance.list_quota_quotas(enforced=enforced, include_snapshots=include_snapshots, zone=zone, resume=resume, recurse_path_children=recurse_path_children, resolve_names=resolve_names, recurse_path_parents=recurse_path_parents, persona=persona, limit=limit, exceeded=exceeded, path=path, type=type, report_id=report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->list_quota_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enforced** | **bool**| Only list quotas with this enforcement (non-accounting). | [optional] 
 **include_snapshots** | **bool**| Only list quotas with this setting for include_snapshots. | [optional] 
 **zone** | **str**| Optional named zone to use for user and group resolution. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **recurse_path_children** | **bool**| If used with the path argument, match all quotas at that path or any descendent sub-directory. | [optional] 
 **resolve_names** | **bool**| If true, resolve group and user names in personas. | [optional] 
 **recurse_path_parents** | **bool**| If used with the path argument, match all quotas at that path or any parent directory. | [optional] 
 **persona** | **str**| Only list user or group quotas matching this persona (must be used with the corresponding type argument).  Format is &lt;PERSONA_TYPE&gt;:&lt;string/integer&gt;, where PERSONA_TYPE is one of USER, GROUP, SID, ID, or GID. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **exceeded** | **bool**| Set to true to only list quotas which have exceeded one or more of their thresholds. | [optional] 
 **path** | **str**| Only list quotas matching this path (see also recurse_path_*). | [optional] 
 **type** | **str**| Only list quotas matching this type. | [optional] 
 **report_id** | **str**| Use the named report as a source rather than the live quotas. See the /q/quota/reports resource for a list of valid reports. | [optional] 

### Return type

[**QuotaQuotasExtended**](QuotaQuotasExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quota_reports**
> QuotaReports list_quota_reports(sort=sort, resume=resume, generated=generated, limit=limit, type=type, dir=dir)



List all or matching reports.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
sort = 'sort_example' # str | Order results by this field. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
generated = 'generated_example' # str | Only list reports matching this source. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
type = 'type_example' # str | Only list reports matching this type. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_quota_reports(sort=sort, resume=resume, generated=generated, limit=limit, type=type, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->list_quota_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Order results by this field. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **generated** | **str**| Only list reports matching this source. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **type** | **str**| Only list reports matching this type. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**QuotaReports**](QuotaReports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings_mappings**
> SettingsMappings list_settings_mappings()



List all rules.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))

try:
    api_response = api_instance.list_settings_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->list_settings_mappings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsMappings**](SettingsMappings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings_notifications**
> QuotaNotificationsExtended list_settings_notifications()



List all rules.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))

try:
    api_response = api_instance.list_settings_notifications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaApi->list_settings_notifications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuotaNotificationsExtended**](QuotaNotificationsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quota_quota**
> update_quota_quota(quota_quota, quota_quota_id)



Modify quota. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
quota_quota = isi_sdk_8_2_1.QuotaQuota() # QuotaQuota | 
quota_quota_id = 'quota_quota_id_example' # str | Modify quota. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_quota_quota(quota_quota, quota_quota_id)
except ApiException as e:
    print("Exception when calling QuotaApi->update_quota_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_quota** | [**QuotaQuota**](QuotaQuota.md)|  | 
 **quota_quota_id** | **str**| Modify quota. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_mapping**
> update_settings_mapping(settings_mapping, settings_mapping_id)



Modify the mapping.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_mapping = isi_sdk_8_2_1.SettingsMappingExtended() # SettingsMappingExtended | 
settings_mapping_id = 'settings_mapping_id_example' # str | Modify the mapping.

try:
    api_instance.update_settings_mapping(settings_mapping, settings_mapping_id)
except ApiException as e:
    print("Exception when calling QuotaApi->update_settings_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_mapping** | [**SettingsMappingExtended**](SettingsMappingExtended.md)|  | 
 **settings_mapping_id** | **str**| Modify the mapping. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_notification**
> update_settings_notification(settings_notification, settings_notification_id)



Modify notification rule. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_notification = isi_sdk_8_2_1.QuotaNotification() # QuotaNotification | 
settings_notification_id = 'settings_notification_id_example' # str | Modify notification rule. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_settings_notification(settings_notification, settings_notification_id)
except ApiException as e:
    print("Exception when calling QuotaApi->update_settings_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_notification** | [**QuotaNotification**](QuotaNotification.md)|  | 
 **settings_notification_id** | **str**| Modify notification rule. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_reports**
> update_settings_reports(settings_reports)



Modify one or more settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.QuotaApi(isi_sdk_8_2_1.ApiClient(configuration))
settings_reports = isi_sdk_8_2_1.SettingsReportsExtended() # SettingsReportsExtended | 

try:
    api_instance.update_settings_reports(settings_reports)
except ApiException as e:
    print("Exception when calling QuotaApi->update_settings_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_reports** | [**SettingsReportsExtended**](SettingsReportsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

