# isi_sdk_8_1_1.UpgradeApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_add_remaining_node**](UpgradeApi.md#create_cluster_add_remaining_node) | **POST** /platform/3/upgrade/cluster/add_remaining_nodes | 
[**create_cluster_archive_item**](UpgradeApi.md#create_cluster_archive_item) | **POST** /platform/3/upgrade/cluster/archive | 
[**create_cluster_assess_item**](UpgradeApi.md#create_cluster_assess_item) | **POST** /platform/5/upgrade/cluster/assess | 
[**create_cluster_commit_item**](UpgradeApi.md#create_cluster_commit_item) | **POST** /platform/3/upgrade/cluster/commit | 
[**create_cluster_firmware_assess_item**](UpgradeApi.md#create_cluster_firmware_assess_item) | **POST** /platform/3/upgrade/cluster/firmware/assess | 
[**create_cluster_firmware_upgrade_item**](UpgradeApi.md#create_cluster_firmware_upgrade_item) | **POST** /platform/3/upgrade/cluster/firmware/upgrade | 
[**create_cluster_patch_abort_item**](UpgradeApi.md#create_cluster_patch_abort_item) | **POST** /platform/3/upgrade/cluster/patch/abort | 
[**create_cluster_patch_patch**](UpgradeApi.md#create_cluster_patch_patch) | **POST** /platform/3/upgrade/cluster/patch/patches | 
[**create_cluster_retry_last_action_item**](UpgradeApi.md#create_cluster_retry_last_action_item) | **POST** /platform/3/upgrade/cluster/retry_last_action | 
[**create_cluster_rollback_item**](UpgradeApi.md#create_cluster_rollback_item) | **POST** /platform/3/upgrade/cluster/rollback | 
[**create_cluster_upgrade_item**](UpgradeApi.md#create_cluster_upgrade_item) | **POST** /platform/5/upgrade/cluster/upgrade | 
[**create_hardware_start_item**](UpgradeApi.md#create_hardware_start_item) | **POST** /platform/5/upgrade/hardware/start | 
[**create_hardware_stop_item**](UpgradeApi.md#create_hardware_stop_item) | **POST** /platform/5/upgrade/hardware/stop | 
[**delete_cluster_patch_patch**](UpgradeApi.md#delete_cluster_patch_patch) | **DELETE** /platform/3/upgrade/cluster/patch/patches/{ClusterPatchPatchId} | 
[**get_cluster_firmware_progress**](UpgradeApi.md#get_cluster_firmware_progress) | **GET** /platform/3/upgrade/cluster/firmware/progress | 
[**get_cluster_firmware_status**](UpgradeApi.md#get_cluster_firmware_status) | **GET** /platform/3/upgrade/cluster/firmware/status | 
[**get_cluster_node**](UpgradeApi.md#get_cluster_node) | **GET** /platform/3/upgrade/cluster/nodes/{ClusterNodeId} | 
[**get_cluster_nodes**](UpgradeApi.md#get_cluster_nodes) | **GET** /platform/3/upgrade/cluster/nodes | 
[**get_cluster_patch_patch**](UpgradeApi.md#get_cluster_patch_patch) | **GET** /platform/3/upgrade/cluster/patch/patches/{ClusterPatchPatchId} | 
[**get_hardware_status**](UpgradeApi.md#get_hardware_status) | **GET** /platform/5/upgrade/hardware/status | 
[**get_upgrade_cluster**](UpgradeApi.md#get_upgrade_cluster) | **GET** /platform/4/upgrade/cluster | 
[**list_cluster_patch_patches**](UpgradeApi.md#list_cluster_patch_patches) | **GET** /platform/3/upgrade/cluster/patch/patches | 
[**update_cluster_upgrade**](UpgradeApi.md#update_cluster_upgrade) | **PUT** /platform/5/upgrade/cluster/upgrade | 


# **create_cluster_add_remaining_node**
> Empty create_cluster_add_remaining_node(cluster_add_remaining_node)



Let system absorb any remaining or new nodes inside the existing upgrade.

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_add_remaining_node = isi_sdk_8_1_1.Empty() # Empty | 

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_archive_item = isi_sdk_8_1_1.ClusterArchiveItem() # ClusterArchiveItem | 

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_assess_item = isi_sdk_8_1_1.ClusterAssessItem() # ClusterAssessItem | 

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_commit_item = isi_sdk_8_1_1.Empty() # Empty | 

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_firmware_assess_item = isi_sdk_8_1_1.Empty() # Empty | 

try:
    api_response = api_instance.create_cluster_firmware_assess_item(cluster_firmware_assess_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_firmware_assess_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_firmware_assess_item** | [**Empty**](Empty.md)|  | 

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_firmware_upgrade_item = isi_sdk_8_1_1.ClusterFirmwareUpgradeItem() # ClusterFirmwareUpgradeItem | 

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_patch_abort_item = isi_sdk_8_1_1.Empty() # Empty | 

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
> CreateResponse create_cluster_patch_patch(cluster_patch_patch, override=override, rolling=rolling)



Install a patch.

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_patch_patch = isi_sdk_8_1_1.ClusterPatchPatch() # ClusterPatchPatch | 
override = true # bool | Whether to ignore patch system validation and force the installation. (optional)
rolling = true # bool | Whether to install the patch on one node at a time. Defaults to true. (optional)

try:
    api_response = api_instance.create_cluster_patch_patch(cluster_patch_patch, override=override, rolling=rolling)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_cluster_patch_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_patch_patch** | [**ClusterPatchPatch**](ClusterPatchPatch.md)|  | 
 **override** | **bool**| Whether to ignore patch system validation and force the installation. | [optional] 
 **rolling** | **bool**| Whether to install the patch on one node at a time. Defaults to true. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_retry_last_action_item = isi_sdk_8_1_1.ClusterRetryLastActionItem() # ClusterRetryLastActionItem | 

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_rollback_item = isi_sdk_8_1_1.Empty() # Empty | 

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_upgrade_item = isi_sdk_8_1_1.ClusterUpgradeItem() # ClusterUpgradeItem | 

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

# **create_hardware_start_item**
> create_hardware_start_item(hardware_start_item)



Start a hardware upgrade

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
hardware_start_item = isi_sdk_8_1_1.HardwareStartItem() # HardwareStartItem | 

try:
    api_instance.create_hardware_start_item(hardware_start_item)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_hardware_start_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_start_item** | [**HardwareStartItem**](HardwareStartItem.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hardware_stop_item**
> create_hardware_stop_item(hardware_stop_item)



Stop an in-progess hardware upgrade process

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
hardware_stop_item = isi_sdk_8_1_1.HardwareStopItem() # HardwareStopItem | 

try:
    api_instance.create_hardware_stop_item(hardware_stop_item)
except ApiException as e:
    print("Exception when calling UpgradeApi->create_hardware_stop_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_stop_item** | [**HardwareStopItem**](HardwareStopItem.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_patch_patch**
> delete_cluster_patch_patch(cluster_patch_patch_id, override=override, rolling=rolling)



Uninstall a patch.

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_patch_patch_id = 'cluster_patch_patch_id_example' # str | Uninstall a patch.
override = true # bool | Whether to ignore patch system validation and force the uninstallation. (optional)
rolling = true # bool | Whether to uninstall the patch on one node at a time. Defaults to true. (optional)

try:
    api_instance.delete_cluster_patch_patch(cluster_patch_patch_id, override=override, rolling=rolling)
except ApiException as e:
    print("Exception when calling UpgradeApi->delete_cluster_patch_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_patch_patch_id** | **str**| Uninstall a patch. | 
 **override** | **bool**| Whether to ignore patch system validation and force the uninstallation. | [optional] 
 **rolling** | **bool**| Whether to uninstall the patch on one node at a time. Defaults to true. | [optional] 

### Return type

void (empty response body)

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))

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
> ClusterFirmwareStatus get_cluster_firmware_status(devices=devices, package=package)



The firmware status for the cluster.

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list.Default is false. (optional)

try:
    api_response = api_instance.get_cluster_firmware_status(devices=devices, package=package)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_firmware_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **package** | **bool**| Show package. If false, this returns an empty list.Default is false. | [optional] 

### Return type

[**ClusterFirmwareStatus**](ClusterFirmwareStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node**
> ClusterNodes get_cluster_node(cluster_node_id)



The node details useful during an upgrade or assessment.

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
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

[**ClusterNodes**](ClusterNodes.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes**
> ClusterNodesExtended get_cluster_nodes()



View information about nodes during an upgrade, rollback, or pre-upgrade assessment.

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_cluster_nodes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterNodesExtended**](ClusterNodesExtended.md)

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_patch_patch_id = 'cluster_patch_patch_id_example' # str | View a single patch.
local = true # bool | Only view patch information on the local node. (optional)
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
 **local** | **bool**| Only view patch information on the local node. | [optional] 
 **location** | **str**| Path location of patch file. | [optional] 

### Return type

[**ClusterPatchPatches**](ClusterPatchPatches.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_status**
> HardwareStatus get_hardware_status()



View the status of hardware upgrades in progress

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))

try:
    api_response = api_instance.get_hardware_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->get_hardware_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HardwareStatus**](HardwareStatus.md)

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))

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
> ClusterPatchPatchesExtended list_cluster_patch_patches(sort=sort, resume=resume, limit=limit, location=location, local=local, dir=dir)



List all patches.

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
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
location = 'location_example' # str | Path location of patch file. (optional)
local = true # bool | Whether to view patches on the local node only. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_cluster_patch_patches(sort=sort, resume=resume, limit=limit, location=location, local=local, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UpgradeApi->list_cluster_patch_patches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **location** | **str**| Path location of patch file. | [optional] 
 **local** | **bool**| Whether to view patches on the local node only. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**ClusterPatchPatchesExtended**](ClusterPatchPatchesExtended.md)

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
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.UpgradeApi(isi_sdk_8_1_1.ApiClient(configuration))
cluster_upgrade = isi_sdk_8_1_1.ClusterUpgrade() # ClusterUpgrade | 

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

