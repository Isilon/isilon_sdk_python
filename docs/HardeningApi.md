# isi_sdk_8_1_1.HardeningApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hardening_apply_item**](HardeningApi.md#create_hardening_apply_item) | **POST** /platform/3/hardening/apply | 
[**create_hardening_resolve_item**](HardeningApi.md#create_hardening_resolve_item) | **POST** /platform/3/hardening/resolve | 
[**create_hardening_revert_item**](HardeningApi.md#create_hardening_revert_item) | **POST** /platform/3/hardening/revert | 
[**get_hardening_state**](HardeningApi.md#get_hardening_state) | **GET** /platform/3/hardening/state | 
[**get_hardening_status**](HardeningApi.md#get_hardening_status) | **GET** /platform/3/hardening/status | 


# **create_hardening_apply_item**
> CreateHardeningApplyItemResponse create_hardening_apply_item(hardening_apply_item)



Apply hardening on the cluster.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.HardeningApi(isi_sdk_8_1_1.ApiClient(configuration))
hardening_apply_item = isi_sdk_8_1_1.HardeningApplyItem() # HardeningApplyItem | 

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

# **create_hardening_resolve_item**
> CreateHardeningResolveItemResponse create_hardening_resolve_item(hardening_resolve_item, accept=accept)



Resolve issues related to hardening, found in current cluster configuration.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.HardeningApi(isi_sdk_8_1_1.ApiClient(configuration))
hardening_resolve_item = isi_sdk_8_1_1.HardeningResolveItem() # HardeningResolveItem | 
accept = true # bool | If true, execution proceeds to resolve all issues. If false, executrion aborts. This is a required argument. (optional)

try:
    api_response = api_instance.create_hardening_resolve_item(hardening_resolve_item, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->create_hardening_resolve_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardening_resolve_item** | [**HardeningResolveItem**](HardeningResolveItem.md)|  | 
 **accept** | **bool**| If true, execution proceeds to resolve all issues. If false, executrion aborts. This is a required argument. | [optional] 

### Return type

[**CreateHardeningResolveItemResponse**](CreateHardeningResolveItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hardening_revert_item**
> CreateHardeningRevertItemResponse create_hardening_revert_item(hardening_revert_item, force=force)



Revert hardening on the cluster.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.HardeningApi(isi_sdk_8_1_1.ApiClient(configuration))
hardening_revert_item = isi_sdk_8_1_1.Empty() # Empty | 
force = true # bool | If specified, revert operation continues even in case of a failure. Default is false in which case revert stops at the first failure. (optional)

try:
    api_response = api_instance.create_hardening_revert_item(hardening_revert_item, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->create_hardening_revert_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardening_revert_item** | [**Empty**](Empty.md)|  | 
 **force** | **bool**| If specified, revert operation continues even in case of a failure. Default is false in which case revert stops at the first failure. | [optional] 

### Return type

[**CreateHardeningRevertItemResponse**](CreateHardeningRevertItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardening_state**
> HardeningState get_hardening_state()



Get the state of the current hardening operation, if one is happening.  Note that this is different from the /status resource, which returns the overall hardening status of the cluster.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.HardeningApi(isi_sdk_8_1_1.ApiClient(configuration))

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

# **get_hardening_status**
> HardeningStatus get_hardening_status()



Get a message indicating whether or not the cluster is hardened. Note that this is different from the /state resource, which returns the state of a specific hardening operation (apply or revert).

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.HardeningApi(isi_sdk_8_1_1.ApiClient(configuration))

try:
    api_response = api_instance.get_hardening_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardeningApi->get_hardening_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HardeningStatus**](HardeningStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

