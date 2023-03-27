# isilon_sdk.v9_4_0.SecurityApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_security_check_item**](SecurityApi.md#create_security_check_item) | **POST** /platform/15/security/check | 
[**get_check_report**](SecurityApi.md#get_check_report) | **GET** /platform/15/security/check/report | 
[**get_check_settings**](SecurityApi.md#get_check_settings) | **GET** /platform/15/security/check/settings | 
[**get_security_settings**](SecurityApi.md#get_security_settings) | **GET** /platform/15/security/settings | 
[**list_security_check**](SecurityApi.md#list_security_check) | **GET** /platform/15/security/check | 
[**update_check_settings**](SecurityApi.md#update_check_settings) | **PUT** /platform/15/security/check/settings | 
[**update_security_settings**](SecurityApi.md#update_security_settings) | **PUT** /platform/15/security/settings | 


# **create_security_check_item**
> create_security_check_item(security_check_item)



Start the security check.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.SecurityApi(isilon_sdk.v9_4_0.ApiClient(configuration))
security_check_item = isilon_sdk.v9_4_0.SecurityCheckItem() # SecurityCheckItem | 

try:
    api_instance.create_security_check_item(security_check_item)
except ApiException as e:
    print("Exception when calling SecurityApi->create_security_check_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_check_item** | [**SecurityCheckItem**](SecurityCheckItem.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_report**
> CheckReport get_check_report()



Retrieve security check report properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.SecurityApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_check_report()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_check_report: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CheckReport**](CheckReport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_check_settings**
> CheckSettings get_check_settings()



View the security check settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.SecurityApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_check_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_check_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CheckSettings**](CheckSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_settings**
> SecuritySettings get_security_settings()



Retrieve security properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.SecurityApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_security_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->get_security_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SecuritySettings**](SecuritySettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_security_check**
> SecurityCheck list_security_check()



Retrieve security check status properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.SecurityApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.list_security_check()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityApi->list_security_check: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SecurityCheck**](SecurityCheck.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_check_settings**
> update_check_settings(check_settings)



Modify the security check settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.SecurityApi(isilon_sdk.v9_4_0.ApiClient(configuration))
check_settings = isilon_sdk.v9_4_0.CheckSettingsExtended() # CheckSettingsExtended | 

try:
    api_instance.update_check_settings(check_settings)
except ApiException as e:
    print("Exception when calling SecurityApi->update_check_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_settings** | [**CheckSettingsExtended**](CheckSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_security_settings**
> update_security_settings(security_settings)



Modify security properties.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.SecurityApi(isilon_sdk.v9_4_0.ApiClient(configuration))
security_settings = isilon_sdk.v9_4_0.SecuritySettingsSettings() # SecuritySettingsSettings | 

try:
    api_instance.update_security_settings(security_settings)
except ApiException as e:
    print("Exception when calling SecurityApi->update_security_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_settings** | [**SecuritySettingsSettings**](SecuritySettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

