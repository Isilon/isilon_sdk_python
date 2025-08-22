# isilon_sdk.v9_5_0.HardeningApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hardening_apply_item**](HardeningApi.md#create_hardening_apply_item) | **POST** /platform/16/hardening/apply | 
[**create_hardening_disable_item**](HardeningApi.md#create_hardening_disable_item) | **POST** /platform/16/hardening/disable | 
[**create_hardening_report**](HardeningApi.md#create_hardening_report) | **POST** /platform/16/hardening/reports | 
[**get_hardening_list**](HardeningApi.md#get_hardening_list) | **GET** /platform/16/hardening/list | 
[**get_hardening_state**](HardeningApi.md#get_hardening_state) | **GET** /platform/16/hardening/state | 
[**list_hardening_reports**](HardeningApi.md#list_hardening_reports) | **GET** /platform/16/hardening/reports | 


# **create_hardening_apply_item**
> CreateHardeningApplyItemResponse create_hardening_apply_item(hardening_apply_item)



Applies the rules in a hardening profile.

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
api_instance = isilon_sdk.v9_5_0.HardeningApi(isilon_sdk.v9_5_0.ApiClient(configuration))
hardening_apply_item = isilon_sdk.v9_5_0.HardeningApplyItem() # HardeningApplyItem | 

try:
    api_response = api_instance.create_hardening_apply_item(hardening_apply_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->create_hardening_apply_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardening_apply_item** | [**HardeningApplyItem**](HardeningApplyItem.md)|  | 

### Return type

[**CreateHardeningApplyItemResponse**](CreateHardeningApplyItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hardening_disable_item**
> CreateHardeningApplyItemResponse create_hardening_disable_item(hardening_disable_item)



Reset a hardening profile to its default configuration.

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
api_instance = isilon_sdk.v9_5_0.HardeningApi(isilon_sdk.v9_5_0.ApiClient(configuration))
hardening_disable_item = isilon_sdk.v9_5_0.HardeningApplyItem() # HardeningApplyItem | 

try:
    api_response = api_instance.create_hardening_disable_item(hardening_disable_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->create_hardening_disable_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardening_disable_item** | [**HardeningApplyItem**](HardeningApplyItem.md)|  | 

### Return type

[**CreateHardeningApplyItemResponse**](CreateHardeningApplyItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hardening_report**
> CreateHardeningApplyItemResponse create_hardening_report(hardening_report)



Creates a report for all the hardening rules.

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
api_instance = isilon_sdk.v9_5_0.HardeningApi(isilon_sdk.v9_5_0.ApiClient(configuration))
hardening_report = isilon_sdk.v9_5_0.Empty() # Empty | 

try:
    api_response = api_instance.create_hardening_report(hardening_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->create_hardening_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardening_report** | [**Empty**](Empty.md)|  | 

### Return type

[**CreateHardeningApplyItemResponse**](CreateHardeningApplyItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardening_list**
> HardeningList get_hardening_list()



Get the list of available hardening profile names, descriptions, and applied status.

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
api_instance = isilon_sdk.v9_5_0.HardeningApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_hardening_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->get_hardening_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HardeningList**](HardeningList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardening_state**
> HardeningState get_hardening_state()



Get the state of the hardening service, Running or Available.  Note that this is different from the status resource, which returns the status of hardening profiles.

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
api_instance = isilon_sdk.v9_5_0.HardeningApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_hardening_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->get_hardening_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HardeningState**](HardeningState.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hardening_reports**
> HardeningReports list_hardening_reports()



View the report for all the hardening rules.

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
api_instance = isilon_sdk.v9_5_0.HardeningApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.list_hardening_reports()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->list_hardening_reports: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HardeningReports**](HardeningReports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

