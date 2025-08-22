# isilon_sdk.v9_12_0.RepairApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repair_action**](RepairApi.md#create_repair_action) | **POST** /platform/23/repair/actions | 
[**create_repair_request**](RepairApi.md#create_repair_request) | **POST** /platform/23/repair/requests | 
[**delete_repair_action**](RepairApi.md#delete_repair_action) | **DELETE** /platform/23/repair/actions/{RepairActionId} | 
[**get_repair_action**](RepairApi.md#get_repair_action) | **GET** /platform/23/repair/actions/{RepairActionId} | 
[**get_repair_request**](RepairApi.md#get_repair_request) | **GET** /platform/23/repair/requests/{RepairRequestId} | 
[**get_repair_settings**](RepairApi.md#get_repair_settings) | **GET** /platform/23/repair/settings | 
[**list_repair_actions**](RepairApi.md#list_repair_actions) | **GET** /platform/23/repair/actions | 
[**list_repair_requests**](RepairApi.md#list_repair_requests) | **GET** /platform/23/repair/requests | 
[**update_repair_settings**](RepairApi.md#update_repair_settings) | **PUT** /platform/23/repair/settings | 


# **create_repair_action**
> CreateResponse create_repair_action(repair_action, skip_conflict_check=skip_conflict_check, skip_dependency_check=skip_dependency_check, skip_restricted_check=skip_restricted_check, skip_version_check=skip_version_check)



Install a repair action package.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))
repair_action = isilon_sdk.v9_12_0.RepairActionCreateParams() # RepairActionCreateParams | 
skip_conflict_check = true # bool | Bypass conflict checks. Defaults to false. (optional)
skip_dependency_check = true # bool | Bypass dependency checks. Defaults to false. (optional)
skip_restricted_check = true # bool | Bypass restricted checks. Defaults to false. (optional)
skip_version_check = true # bool | Bypass version checks. Defaults to false. (optional)

try:
    api_response = api_instance.create_repair_action(repair_action, skip_conflict_check=skip_conflict_check, skip_dependency_check=skip_dependency_check, skip_restricted_check=skip_restricted_check, skip_version_check=skip_version_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepairApi->create_repair_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repair_action** | [**RepairActionCreateParams**](RepairActionCreateParams.md)|  | 
 **skip_conflict_check** | **bool**| Bypass conflict checks. Defaults to false. | [optional] 
 **skip_dependency_check** | **bool**| Bypass dependency checks. Defaults to false. | [optional] 
 **skip_restricted_check** | **bool**| Bypass restricted checks. Defaults to false. | [optional] 
 **skip_version_check** | **bool**| Bypass version checks. Defaults to false. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repair_request**
> CreateRepairRequestResponse create_repair_request(repair_request)



Request a repair.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))
repair_request = isilon_sdk.v9_12_0.RepairRequest() # RepairRequest | 

try:
    api_response = api_instance.create_repair_request(repair_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepairApi->create_repair_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repair_request** | [**RepairRequest**](RepairRequest.md)|  | 

### Return type

[**CreateRepairRequestResponse**](CreateRepairRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repair_action**
> delete_repair_action(repair_action_id, process_type=process_type, skip_conflict_check=skip_conflict_check, skip_dependency_check=skip_dependency_check, skip_restricted_check=skip_restricted_check, skip_version_check=skip_version_check)



Uninstall a repair-action.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))
repair_action_id = 'repair_action_id_example' # str | Uninstall a repair-action.
process_type = 'process_type_example' # str | Process type can be 'simultaneous', 'rolling', or 'parallel' (optional)
skip_conflict_check = true # bool | Bypass conflict checks. Defaults to false. (optional)
skip_dependency_check = true # bool | Bypass dependency checks. Defaults to false. (optional)
skip_restricted_check = true # bool | Bypass restricted checks. Defaults to false. (optional)
skip_version_check = true # bool | Bypass version checks. Defaults to false. (optional)

try:
    api_instance.delete_repair_action(repair_action_id, process_type=process_type, skip_conflict_check=skip_conflict_check, skip_dependency_check=skip_dependency_check, skip_restricted_check=skip_restricted_check, skip_version_check=skip_version_check)
except ApiException as e:
    print("Exception when calling RepairApi->delete_repair_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repair_action_id** | **str**| Uninstall a repair-action. | 
 **process_type** | **str**| Process type can be &#39;simultaneous&#39;, &#39;rolling&#39;, or &#39;parallel&#39; | [optional] 
 **skip_conflict_check** | **bool**| Bypass conflict checks. Defaults to false. | [optional] 
 **skip_dependency_check** | **bool**| Bypass dependency checks. Defaults to false. | [optional] 
 **skip_restricted_check** | **bool**| Bypass restricted checks. Defaults to false. | [optional] 
 **skip_version_check** | **bool**| Bypass version checks. Defaults to false. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repair_action**
> RepairActions get_repair_action(repair_action_id, local=local, location=location)



View a single repair-action.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))
repair_action_id = 'repair_action_id_example' # str | View a single repair-action.
local = true # bool | View repair-action information on local node only. (optional)
location = 'location_example' # str | Path location of repair-action file. (optional)

try:
    api_response = api_instance.get_repair_action(repair_action_id, local=local, location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepairApi->get_repair_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repair_action_id** | **str**| View a single repair-action. | 
 **local** | **bool**| View repair-action information on local node only. | [optional] 
 **location** | **str**| Path location of repair-action file. | [optional] 

### Return type

[**RepairActions**](RepairActions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repair_request**
> RepairRequests get_repair_request(repair_request_id)



Retrieve the repair.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))
repair_request_id = 'repair_request_id_example' # str | Retrieve the repair.

try:
    api_response = api_instance.get_repair_request(repair_request_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepairApi->get_repair_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repair_request_id** | **str**| Retrieve the repair. | 

### Return type

[**RepairRequests**](RepairRequests.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repair_settings**
> RepairSettings get_repair_settings()



List the repair settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))

try:
    api_response = api_instance.get_repair_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepairApi->get_repair_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RepairSettings**](RepairSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repair_actions**
> RepairActionsExtended list_repair_actions(dir=dir, limit=limit, local=local, resume=resume, sort=sort)



List all repair actions.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
local = true # bool | View repair actions on the local node only. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_repair_actions(dir=dir, limit=limit, local=local, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepairApi->list_repair_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **local** | **bool**| View repair actions on the local node only. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**RepairActionsExtended**](RepairActionsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repair_requests**
> RepairRequestsExtended list_repair_requests(dir=dir, latest=latest, limit=limit, resume=resume, sort=sort)



Get repair results.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
latest = true # bool | Returns only the latest repair. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_repair_requests(dir=dir, latest=latest, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RepairApi->list_repair_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **latest** | **bool**| Returns only the latest repair. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**RepairRequestsExtended**](RepairRequestsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repair_settings**
> update_repair_settings(repair_settings)



Update one or more repair settings

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.RepairApi(isilon_sdk.v9_12_0.ApiClient(configuration))
repair_settings = isilon_sdk.v9_12_0.RepairSettings() # RepairSettings | 

try:
    api_instance.update_repair_settings(repair_settings)
except ApiException as e:
    print("Exception when calling RepairApi->update_repair_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repair_settings** | [**RepairSettings**](RepairSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

