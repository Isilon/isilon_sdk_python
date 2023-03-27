# isilon_sdk.v9_2_1.UpgradeApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_add_remaining_node**](UpgradeApi.md#create_cluster_add_remaining_node) | **POST** /platform/3/upgrade/cluster/add_remaining_nodes | 
[**create_cluster_archive_item**](UpgradeApi.md#create_cluster_archive_item) | **POST** /platform/3/upgrade/cluster/archive | 
[**create_cluster_assess_item**](UpgradeApi.md#create_cluster_assess_item) | **POST** /platform/5/upgrade/cluster/assess | 
[**create_cluster_commit_item**](UpgradeApi.md#create_cluster_commit_item) | **POST** /platform/3/upgrade/cluster/commit | 
[**create_cluster_firmware_assess_item**](UpgradeApi.md#create_cluster_firmware_assess_item) | **POST** /platform/10/upgrade/cluster/firmware/assess | 
[**create_cluster_firmware_upgrade_item**](UpgradeApi.md#create_cluster_firmware_upgrade_item) | **POST** /platform/12/upgrade/cluster/firmware/upgrade | 
[**create_cluster_patch_abort_item**](UpgradeApi.md#create_cluster_patch_abort_item) | **POST** /platform/3/upgrade/cluster/patch/abort | 
[**create_cluster_patch_patch**](UpgradeApi.md#create_cluster_patch_patch) | **POST** /platform/11/upgrade/cluster/patch/patches | 
[**create_cluster_pause_item**](UpgradeApi.md#create_cluster_pause_item) | **POST** /platform/7/upgrade/cluster/pause | 
[**create_cluster_resume_item**](UpgradeApi.md#create_cluster_resume_item) | **POST** /platform/7/upgrade/cluster/resume | 
[**create_cluster_retry_last_action_item**](UpgradeApi.md#create_cluster_retry_last_action_item) | **POST** /platform/3/upgrade/cluster/retry_last_action | 
[**create_cluster_rollback_item**](UpgradeApi.md#create_cluster_rollback_item) | **POST** /platform/3/upgrade/cluster/rollback | 
[**create_cluster_upgrade_item**](UpgradeApi.md#create_cluster_upgrade_item) | **POST** /platform/12/upgrade/cluster/upgrade | 
[**delete_cluster_patch_patch**](UpgradeApi.md#delete_cluster_patch_patch) | **DELETE** /platform/11/upgrade/cluster/patch/patches/{ClusterPatchPatchId} | 
[**get_cluster_drain_list**](UpgradeApi.md#get_cluster_drain_list) | **GET** /platform/12/upgrade/cluster/drain/list | 
[**get_cluster_drain_timeout**](UpgradeApi.md#get_cluster_drain_timeout) | **GET** /platform/12/upgrade/cluster/drain/timeout | 
[**get_cluster_firmware_device**](UpgradeApi.md#get_cluster_firmware_device) | **GET** /platform/10/upgrade/cluster/firmware/device | 
[**get_cluster_firmware_progress**](UpgradeApi.md#get_cluster_firmware_progress) | **GET** /platform/3/upgrade/cluster/firmware/progress | 
[**get_cluster_firmware_status**](UpgradeApi.md#get_cluster_firmware_status) | **GET** /platform/10/upgrade/cluster/firmware/status | 
[**get_cluster_node**](UpgradeApi.md#get_cluster_node) | **GET** /platform/12/upgrade/cluster/nodes/{ClusterNodeId} | 
[**get_cluster_nodes**](UpgradeApi.md#get_cluster_nodes) | **GET** /platform/12/upgrade/cluster/nodes | 
[**get_cluster_patch_patch**](UpgradeApi.md#get_cluster_patch_patch) | **GET** /platform/11/upgrade/cluster/patch/patches/{ClusterPatchPatchId} | 
[**get_upgrade_cluster**](UpgradeApi.md#get_upgrade_cluster) | **GET** /platform/7/upgrade/cluster | 
[**list_cluster_patch_patches**](UpgradeApi.md#list_cluster_patch_patches) | **GET** /platform/11/upgrade/cluster/patch/patches | 
[**update_cluster_drain**](UpgradeApi.md#update_cluster_drain) | **PUT** /platform/12/upgrade/cluster/drain | 
[**update_cluster_drain_timeout**](UpgradeApi.md#update_cluster_drain_timeout) | **PUT** /platform/12/upgrade/cluster/drain/timeout | 
[**update_cluster_unblock**](UpgradeApi.md#update_cluster_unblock) | **PUT** /platform/9/upgrade/cluster/unblock | 
[**update_cluster_upgrade**](UpgradeApi.md#update_cluster_upgrade) | **PUT** /platform/12/upgrade/cluster/upgrade | 


# **create_cluster_add_remaining_node**
> Empty create_cluster_add_remaining_node(cluster_add_remaining_node)



Let system absorb any remaining or new nodes inside the existing upgrade.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_add_remaining_node = isilon_sdk.v9_2_1.Empty() # Empty | 

try:
    api_response = api_instance.create_cluster_add_remaining_node(cluster_add_remaining_node)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_add_remaining_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_add_remaining_node** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_archive_item**
> Empty create_cluster_archive_item(cluster_archive_item)



Start an archive of an upgrade.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_archive_item = isilon_sdk.v9_2_1.ClusterArchiveItem() # ClusterArchiveItem | 

try:
    api_response = api_instance.create_cluster_archive_item(cluster_archive_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_archive_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_archive_item** | [**ClusterArchiveItem**](ClusterArchiveItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_assess_item**
> Empty create_cluster_assess_item(cluster_assess_item)



Start upgrade assessment on cluster.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_assess_item = isilon_sdk.v9_2_1.ClusterAssessItem() # ClusterAssessItem | 

try:
    api_response = api_instance.create_cluster_assess_item(cluster_assess_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_assess_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_assess_item** | [**ClusterAssessItem**](ClusterAssessItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_commit_item**
> Empty create_cluster_commit_item(cluster_commit_item)



Commit the upgrade of a cluster.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_commit_item = isilon_sdk.v9_2_1.Empty() # Empty | 

try:
    api_response = api_instance.create_cluster_commit_item(cluster_commit_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_commit_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_commit_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_firmware_assess_item**
> Empty create_cluster_firmware_assess_item(cluster_firmware_assess_item)



Start firmware upgrade assessment on cluster.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_firmware_assess_item = isilon_sdk.v9_2_1.ClusterFirmwareAssessItem() # ClusterFirmwareAssessItem | 

try:
    api_response = api_instance.create_cluster_firmware_assess_item(cluster_firmware_assess_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_firmware_assess_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_firmware_assess_item** | [**ClusterFirmwareAssessItem**](ClusterFirmwareAssessItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_firmware_upgrade_item**
> Empty create_cluster_firmware_upgrade_item(cluster_firmware_upgrade_item)



The settings necessary to start a firmware upgrade.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_firmware_upgrade_item = isilon_sdk.v9_2_1.ClusterFirmwareUpgradeItem() # ClusterFirmwareUpgradeItem | 

try:
    api_response = api_instance.create_cluster_firmware_upgrade_item(cluster_firmware_upgrade_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_firmware_upgrade_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_firmware_upgrade_item** | [**ClusterFirmwareUpgradeItem**](ClusterFirmwareUpgradeItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_patch_abort_item**
> Empty create_cluster_patch_abort_item(cluster_patch_abort_item)



Abort the previous action performed by the patch system.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_patch_abort_item = isilon_sdk.v9_2_1.Empty() # Empty | 

try:
    api_response = api_instance.create_cluster_patch_abort_item(cluster_patch_abort_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_patch_abort_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_patch_abort_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_patch_patch**
> CreateResponse create_cluster_patch_patch(cluster_patch_patch, process_type=process_type, skip_conflict_check=skip_conflict_check, skip_dependency_check=skip_dependency_check, skip_restricted_check=skip_restricted_check, skip_version_check=skip_version_check)



Install a patch.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_patch_patch = isilon_sdk.v9_2_1.ClusterPatchPatch() # ClusterPatchPatch | 
process_type = 'process_type_example' # str | Process type can be 'simultaneous', 'rolling', or 'parallel'. (optional)
skip_conflict_check = true # bool | Bypass conflict checks. Defaults to false. (optional)
skip_dependency_check = true # bool | Bypass dependency checks. Defaults to false. (optional)
skip_restricted_check = true # bool | Bypass restricted checks. Defaults to false. (optional)
skip_version_check = true # bool | Bypass version checks. Defaults to false. (optional)

try:
    api_response = api_instance.create_cluster_patch_patch(cluster_patch_patch, process_type=process_type, skip_conflict_check=skip_conflict_check, skip_dependency_check=skip_dependency_check, skip_restricted_check=skip_restricted_check, skip_version_check=skip_version_check)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_patch_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_patch_patch** | [**ClusterPatchPatch**](ClusterPatchPatch.md)|  | 
 **process_type** | **str**| Process type can be &#39;simultaneous&#39;, &#39;rolling&#39;, or &#39;parallel&#39;. | [optional] 
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

# **create_cluster_pause_item**
> Empty create_cluster_pause_item(cluster_pause_item)



Pause a running upgrade process.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_pause_item = isilon_sdk.v9_2_1.Empty() # Empty | 

try:
    api_response = api_instance.create_cluster_pause_item(cluster_pause_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_pause_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_pause_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_resume_item**
> Empty create_cluster_resume_item(cluster_resume_item)



Resume a paused upgrade process.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_resume_item = isilon_sdk.v9_2_1.Empty() # Empty | 

try:
    api_response = api_instance.create_cluster_resume_item(cluster_resume_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_resume_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_resume_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_retry_last_action_item**
> Empty create_cluster_retry_last_action_item(cluster_retry_last_action_item)



Retry the last upgrade action, in-case the previous attempt failed.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_retry_last_action_item = isilon_sdk.v9_2_1.ClusterRetryLastActionItem() # ClusterRetryLastActionItem | 

try:
    api_response = api_instance.create_cluster_retry_last_action_item(cluster_retry_last_action_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_retry_last_action_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_retry_last_action_item** | [**ClusterRetryLastActionItem**](ClusterRetryLastActionItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_rollback_item**
> Empty create_cluster_rollback_item(cluster_rollback_item)



Rollback the upgrade of a cluster.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_rollback_item = isilon_sdk.v9_2_1.Empty() # Empty | 

try:
    api_response = api_instance.create_cluster_rollback_item(cluster_rollback_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_rollback_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_rollback_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_upgrade_item**
> Empty create_cluster_upgrade_item(cluster_upgrade_item)



The settings necessary to start an upgrade.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_upgrade_item = isilon_sdk.v9_2_1.ClusterUpgradeItem() # ClusterUpgradeItem | 

try:
    api_response = api_instance.create_cluster_upgrade_item(cluster_upgrade_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_upgrade_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_upgrade_item** | [**ClusterUpgradeItem**](ClusterUpgradeItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_patch_patch**
> delete_cluster_patch_patch(cluster_patch_patch_id, process_type=process_type, skip_conflict_check=skip_conflict_check, skip_dependency_check=skip_dependency_check, skip_restricted_check=skip_restricted_check, skip_version_check=skip_version_check)



Uninstall a patch.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_patch_patch_id = 'cluster_patch_patch_id_example' # str | Uninstall a patch.
process_type = 'process_type_example' # str | Process type can be 'simultaneous', 'rolling', or 'parallel' (optional)
skip_conflict_check = true # bool | Bypass conflict checks. Defaults to false. (optional)
skip_dependency_check = true # bool | Bypass dependency checks. Defaults to false. (optional)
skip_restricted_check = true # bool | Bypass restricted checks. Defaults to false. (optional)
skip_version_check = true # bool | Bypass version checks. Defaults to false. (optional)

try:
    api_instance.delete_cluster_patch_patch(cluster_patch_patch_id, process_type=process_type, skip_conflict_check=skip_conflict_check, skip_dependency_check=skip_dependency_check, skip_restricted_check=skip_restricted_check, skip_version_check=skip_version_check)
except ApiException as e:
    print("Exception when calling UpgradeApi->delete_cluster_patch_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_patch_patch_id** | **str**| Uninstall a patch. | 
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

# **get_cluster_drain_list**
> ClusterDrainList get_cluster_drain_list(drain_list)



View Drain delay/skip lists.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
drain_list = 'drain_list_example' # str | Delay or Skip list.

try:
    api_response = api_instance.get_cluster_drain_list(drain_list)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_drain_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drain_list** | **str**| Delay or Skip list. | 

### Return type

[**ClusterDrainList**](ClusterDrainList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_drain_timeout**
> ClusterDrainTimeout get_cluster_drain_timeout()



View or modify drain timeouts.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_drain_timeout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_drain_timeout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterDrainTimeout**](ClusterDrainTimeout.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_firmware_device**
> ClusterFirmwareDevice get_cluster_firmware_device(devices=devices, package=package, refresh=refresh)



The firmware status for the cluster.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list. Default is false. (optional)
refresh = true # bool | Re-gather firmware status. Default is false. (optional)

try:
    api_response = api_instance.get_cluster_firmware_device(devices=devices, package=package, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_firmware_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **package** | **bool**| Show package. If false, this returns an empty list. Default is false. | [optional] 
 **refresh** | **bool**| Re-gather firmware status. Default is false. | [optional] 

### Return type

[**ClusterFirmwareDevice**](ClusterFirmwareDevice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_firmware_progress**
> ClusterFirmwareProgress get_cluster_firmware_progress()



Cluster wide firmware upgrade status info.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_firmware_progress()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_firmware_progress: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterFirmwareProgress**](ClusterFirmwareProgress.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_firmware_status**
> ClusterFirmwareStatus get_cluster_firmware_status(devices=devices, refresh=refresh)



The firmware status for the cluster.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
refresh = true # bool | Re-gather firmware status. Default is false. (optional)

try:
    api_response = api_instance.get_cluster_firmware_status(devices=devices, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_firmware_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **refresh** | **bool**| Re-gather firmware status. Default is false. | [optional] 

### Return type

[**ClusterFirmwareStatus**](ClusterFirmwareStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node**
> ClusterNodesExtendedExtended get_cluster_node(cluster_node_id)



The node details useful during an upgrade or assessment.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_node_id = 56 # int | The node details useful during an upgrade or assessment.

try:
    api_response = api_instance.get_cluster_node(cluster_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_node_id** | **int**| The node details useful during an upgrade or assessment. | 

### Return type

[**ClusterNodesExtendedExtended**](ClusterNodesExtendedExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes**
> ClusterNodesExtendedExtendedExtended get_cluster_nodes(by_domain=by_domain)



View information about nodes during an upgrade, rollback, or pre-upgrade assessment.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
by_domain = false # bool | If true, tag nodes that are assigned to like-failure domains (optional) (default to false)

try:
    api_response = api_instance.get_cluster_nodes(by_domain=by_domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by_domain** | **bool**| If true, tag nodes that are assigned to like-failure domains | [optional] [default to false]

### Return type

[**ClusterNodesExtendedExtendedExtended**](ClusterNodesExtendedExtendedExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_patch_patch**
> ClusterPatchPatches get_cluster_patch_patch(cluster_patch_patch_id, local=local, location=location)



View a single patch.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_patch_patch_id = 'cluster_patch_patch_id_example' # str | View a single patch.
local = true # bool | View patch information on local node only. (optional)
location = 'location_example' # str | Path location of patch file. (optional)

try:
    api_response = api_instance.get_cluster_patch_patch(cluster_patch_patch_id, local=local, location=location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_patch_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_patch_patch_id** | **str**| View a single patch. | 
 **local** | **bool**| View patch information on local node only. | [optional] 
 **location** | **str**| Path location of patch file. | [optional] 

### Return type

[**ClusterPatchPatches**](ClusterPatchPatches.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_cluster**
> UpgradeCluster get_upgrade_cluster()



Cluster wide upgrade status info.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_upgrade_cluster()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_upgrade_cluster: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeCluster**](UpgradeCluster.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cluster_patch_patches**
> ClusterPatchPatchesExtended list_cluster_patch_patches(dir=dir, limit=limit, local=local, location=location, resume=resume, sort=sort)



List all patches.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
local = true # bool | View patches on the local node only. (optional)
location = 'location_example' # str | Path location of patch file. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_cluster_patch_patches(dir=dir, limit=limit, local=local, location=location, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->list_cluster_patch_patches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **local** | **bool**| View patches on the local node only. | [optional] 
 **location** | **str**| Path location of patch file. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**ClusterPatchPatchesExtended**](ClusterPatchPatchesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_drain**
> update_cluster_drain(cluster_drain)



Alter drain action.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_drain = isilon_sdk.v9_2_1.ClusterDrain() # ClusterDrain | 

try:
    api_instance.update_cluster_drain(cluster_drain)
except ApiException as e:
    print("Exception when calling UpgradeApi->update_cluster_drain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_drain** | [**ClusterDrain**](ClusterDrain.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_drain_timeout**
> update_cluster_drain_timeout(cluster_drain_timeout)



View or modify drain timeouts.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_drain_timeout = isilon_sdk.v9_2_1.ClusterDrainTimeout() # ClusterDrainTimeout | 

try:
    api_instance.update_cluster_drain_timeout(cluster_drain_timeout)
except ApiException as e:
    print("Exception when calling UpgradeApi->update_cluster_drain_timeout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_drain_timeout** | [**ClusterDrainTimeout**](ClusterDrainTimeout.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_unblock**
> update_cluster_unblock(cluster_unblock)



Unblock parallel upgrade.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_unblock = isilon_sdk.v9_2_1.ClusterUnblock() # ClusterUnblock | 

try:
    api_instance.update_cluster_unblock(cluster_unblock)
except ApiException as e:
    print("Exception when calling UpgradeApi->update_cluster_unblock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_unblock** | [**ClusterUnblock**](ClusterUnblock.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_upgrade**
> update_cluster_upgrade(cluster_upgrade)



Add nodes to a running upgrade.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.UpgradeApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cluster_upgrade = isilon_sdk.v9_2_1.ClusterUpgrade() # ClusterUpgrade | 

try:
    api_instance.update_cluster_upgrade(cluster_upgrade)
except ApiException as e:
    print("Exception when calling UpgradeApi->update_cluster_upgrade: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_upgrade** | [**ClusterUpgrade**](ClusterUpgrade.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

