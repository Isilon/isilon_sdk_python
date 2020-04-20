# isi_sdk_8_0.QuotaQuotasApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quota_notification**](QuotaQuotasApi.md#create_quota_notification) | **POST** /platform/1/quota/quotas/{Qid}/notifications | 
[**delete_quota_notification**](QuotaQuotasApi.md#delete_quota_notification) | **DELETE** /platform/1/quota/quotas/{Qid}/notifications/{QuotaNotificationId} | 
[**delete_quota_notifications**](QuotaQuotasApi.md#delete_quota_notifications) | **DELETE** /platform/1/quota/quotas/{Qid}/notifications | 
[**get_quota_notification**](QuotaQuotasApi.md#get_quota_notification) | **GET** /platform/1/quota/quotas/{Qid}/notifications/{QuotaNotificationId} | 
[**list_quota_notifications**](QuotaQuotasApi.md#list_quota_notifications) | **GET** /platform/1/quota/quotas/{Qid}/notifications | 
[**update_quota_notification**](QuotaQuotasApi.md#update_quota_notification) | **PUT** /platform/1/quota/quotas/{Qid}/notifications/{QuotaNotificationId} | 
[**update_quota_notifications**](QuotaQuotasApi.md#update_quota_notifications) | **PUT** /platform/1/quota/quotas/{Qid}/notifications | 


# **create_quota_notification**
> CreateResponse create_quota_notification(quota_notification, qid)



Create a new notification rule specific to this quota.

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
api_instance = isi_sdk_8_0.QuotaQuotasApi(isi_sdk_8_0.ApiClient(configuration))
quota_notification = isi_sdk_8_0.QuotaNotificationCreateParams() # QuotaNotificationCreateParams | 
qid = 'qid_example' # str | 

try:
    api_response = api_instance.create_quota_notification(quota_notification, qid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaQuotasApi->create_quota_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_notification** | [**QuotaNotificationCreateParams**](QuotaNotificationCreateParams.md)|  | 
 **qid** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quota_notification**
> delete_quota_notification(quota_notification_id, qid)



Delete the notification rule.

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
api_instance = isi_sdk_8_0.QuotaQuotasApi(isi_sdk_8_0.ApiClient(configuration))
quota_notification_id = 'quota_notification_id_example' # str | Delete the notification rule.
qid = 'qid_example' # str | 

try:
    api_instance.delete_quota_notification(quota_notification_id, qid)
except ApiException as e:
    print("Exception when calling QuotaQuotasApi->delete_quota_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_notification_id** | **str**| Delete the notification rule. | 
 **qid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quota_notifications**
> delete_quota_notifications(qid)



Delete all quota specific rules. The quota will then use the global rules.

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
api_instance = isi_sdk_8_0.QuotaQuotasApi(isi_sdk_8_0.ApiClient(configuration))
qid = 'qid_example' # str | 

try:
    api_instance.delete_quota_notifications(qid)
except ApiException as e:
    print("Exception when calling QuotaQuotasApi->delete_quota_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota_notification**
> QuotaNotifications get_quota_notification(quota_notification_id, qid)



Retrieve notification rule information.

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
api_instance = isi_sdk_8_0.QuotaQuotasApi(isi_sdk_8_0.ApiClient(configuration))
quota_notification_id = 'quota_notification_id_example' # str | Retrieve notification rule information.
qid = 'qid_example' # str | 

try:
    api_response = api_instance.get_quota_notification(quota_notification_id, qid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaQuotasApi->get_quota_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_notification_id** | **str**| Retrieve notification rule information. | 
 **qid** | **str**|  | 

### Return type

[**QuotaNotifications**](QuotaNotifications.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quota_notifications**
> QuotaNotificationsExtended list_quota_notifications(qid)



List all rules.

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
api_instance = isi_sdk_8_0.QuotaQuotasApi(isi_sdk_8_0.ApiClient(configuration))
qid = 'qid_example' # str | 

try:
    api_response = api_instance.list_quota_notifications(qid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaQuotasApi->list_quota_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **qid** | **str**|  | 

### Return type

[**QuotaNotificationsExtended**](QuotaNotificationsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quota_notification**
> update_quota_notification(quota_notification, quota_notification_id, qid)



Modify notification rule. All input fields are optional, but one or must be supplied.

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
api_instance = isi_sdk_8_0.QuotaQuotasApi(isi_sdk_8_0.ApiClient(configuration))
quota_notification = isi_sdk_8_0.QuotaNotification() # QuotaNotification | 
quota_notification_id = 'quota_notification_id_example' # str | Modify notification rule. All input fields are optional, but one or must be supplied.
qid = 'qid_example' # str | 

try:
    api_instance.update_quota_notification(quota_notification, quota_notification_id, qid)
except ApiException as e:
    print("Exception when calling QuotaQuotasApi->update_quota_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_notification** | [**QuotaNotification**](QuotaNotification.md)|  | 
 **quota_notification_id** | **str**| Modify notification rule. All input fields are optional, but one or must be supplied. | 
 **qid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_quota_notifications**
> update_quota_notifications(quota_notifications, qid)



This method creates an empty set of rules so that the global rules are not used. The input must be an empty JSON object.

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
api_instance = isi_sdk_8_0.QuotaQuotasApi(isi_sdk_8_0.ApiClient(configuration))
quota_notifications = isi_sdk_8_0.Empty() # Empty | 
qid = 'qid_example' # str | 

try:
    api_instance.update_quota_notifications(quota_notifications, qid)
except ApiException as e:
    print("Exception when calling QuotaQuotasApi->update_quota_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_notifications** | [**Empty**](Empty.md)|  | 
 **qid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

