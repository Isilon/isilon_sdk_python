# isi_sdk.UpgradeApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_add_remaining_node**](UpgradeApi.md#create_cluster_add_remaining_node) | **POST** /platform/3/upgrade/cluster/add_remaining_nodes | 
[**create_cluster_archive_item**](UpgradeApi.md#create_cluster_archive_item) | **POST** /platform/3/upgrade/cluster/archive | 
[**create_cluster_assess_item**](UpgradeApi.md#create_cluster_assess_item) | **POST** /platform/3/upgrade/cluster/assess | 
[**create_cluster_commit_item**](UpgradeApi.md#create_cluster_commit_item) | **POST** /platform/3/upgrade/cluster/commit | 
[**create_cluster_firmware_assess_item**](UpgradeApi.md#create_cluster_firmware_assess_item) | **POST** /platform/3/upgrade/cluster/firmware/assess | 
[**create_cluster_firmware_upgrade_item**](UpgradeApi.md#create_cluster_firmware_upgrade_item) | **POST** /platform/3/upgrade/cluster/firmware/upgrade | 
[**create_cluster_patch_abort_item**](UpgradeApi.md#create_cluster_patch_abort_item) | **POST** /platform/3/upgrade/cluster/patch/abort | 
[**create_cluster_retry_last_action_item**](UpgradeApi.md#create_cluster_retry_last_action_item) | **POST** /platform/3/upgrade/cluster/retry_last_action | 
[**create_cluster_rollback_item**](UpgradeApi.md#create_cluster_rollback_item) | **POST** /platform/3/upgrade/cluster/rollback | 
[**create_cluster_upgrade_item**](UpgradeApi.md#create_cluster_upgrade_item) | **POST** /platform/3/upgrade/cluster/upgrade | 
[**get_cluster_firmware_progress**](UpgradeApi.md#get_cluster_firmware_progress) | **GET** /platform/3/upgrade/cluster/firmware/progress | 
[**get_cluster_firmware_status**](UpgradeApi.md#get_cluster_firmware_status) | **GET** /platform/3/upgrade/cluster/firmware/status | 
[**get_cluster_node**](UpgradeApi.md#get_cluster_node) | **GET** /platform/3/upgrade/cluster/nodes/{ClusterNodeId} | 
[**get_cluster_nodes**](UpgradeApi.md#get_cluster_nodes) | **GET** /platform/3/upgrade/cluster/nodes | 
[**get_upgrade_cluster**](UpgradeApi.md#get_upgrade_cluster) | **GET** /platform/3/upgrade/cluster | 
[**update_cluster_upgrade**](UpgradeApi.md#update_cluster_upgrade) | **PUT** /platform/3/upgrade/cluster/upgrade | 


# **create_cluster_add_remaining_node**
> Empty create_cluster_add_remaining_node(cluster_add_remaining_node)



Let system absorb any remaining or new nodes inside the existing upgrade.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_add_remaining_node = isi_sdk.Empty() # Empty | 

try: 
    api_response = api_instance.create_cluster_add_remaining_node(cluster_add_remaining_node)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_add_remaining_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_add_remaining_node** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_archive_item**
> Empty create_cluster_archive_item(cluster_archive_item)



Start an archive of an upgrade.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_archive_item = isi_sdk.ClusterArchiveItem() # ClusterArchiveItem | 

try: 
    api_response = api_instance.create_cluster_archive_item(cluster_archive_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_archive_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_archive_item** | [**ClusterArchiveItem**](ClusterArchiveItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_assess_item**
> Empty create_cluster_assess_item(cluster_assess_item)



Start upgrade assessment on cluster.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_assess_item = isi_sdk.ClusterAssessItem() # ClusterAssessItem | 

try: 
    api_response = api_instance.create_cluster_assess_item(cluster_assess_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_assess_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_assess_item** | [**ClusterAssessItem**](ClusterAssessItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_commit_item**
> Empty create_cluster_commit_item(cluster_commit_item)



Commit the upgrade of a cluster.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_commit_item = isi_sdk.Empty() # Empty | 

try: 
    api_response = api_instance.create_cluster_commit_item(cluster_commit_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_commit_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_commit_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_firmware_assess_item**
> Empty create_cluster_firmware_assess_item(cluster_firmware_assess_item)



Start firmware upgrade assessment on cluster.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_firmware_assess_item = isi_sdk.Empty() # Empty | 

try: 
    api_response = api_instance.create_cluster_firmware_assess_item(cluster_firmware_assess_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_firmware_assess_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_firmware_assess_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_firmware_upgrade_item**
> Empty create_cluster_firmware_upgrade_item(cluster_firmware_upgrade_item)



The settings necessary to start a firmware upgrade.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_firmware_upgrade_item = isi_sdk.ClusterFirmwareUpgradeItem() # ClusterFirmwareUpgradeItem | 

try: 
    api_response = api_instance.create_cluster_firmware_upgrade_item(cluster_firmware_upgrade_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_firmware_upgrade_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_firmware_upgrade_item** | [**ClusterFirmwareUpgradeItem**](ClusterFirmwareUpgradeItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_patch_abort_item**
> Empty create_cluster_patch_abort_item(cluster_patch_abort_item)



Abort the previous action performed by the patch system.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_patch_abort_item = isi_sdk.Empty() # Empty | 

try: 
    api_response = api_instance.create_cluster_patch_abort_item(cluster_patch_abort_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_patch_abort_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_patch_abort_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_retry_last_action_item**
> Empty create_cluster_retry_last_action_item(cluster_retry_last_action_item)



Retry the last upgrade action, in-case the previous attempt failed.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_retry_last_action_item = isi_sdk.ClusterRetryLastActionItem() # ClusterRetryLastActionItem | 

try: 
    api_response = api_instance.create_cluster_retry_last_action_item(cluster_retry_last_action_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_retry_last_action_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_retry_last_action_item** | [**ClusterRetryLastActionItem**](ClusterRetryLastActionItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_rollback_item**
> Empty create_cluster_rollback_item(cluster_rollback_item)



Rollback the upgrade of a cluster.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_rollback_item = isi_sdk.Empty() # Empty | 

try: 
    api_response = api_instance.create_cluster_rollback_item(cluster_rollback_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_rollback_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_rollback_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_upgrade_item**
> Empty create_cluster_upgrade_item(cluster_upgrade_item)



The settings necessary to start an upgrade.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_upgrade_item = isi_sdk.ClusterUpgradeItem() # ClusterUpgradeItem | 

try: 
    api_response = api_instance.create_cluster_upgrade_item(cluster_upgrade_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->create_cluster_upgrade_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_upgrade_item** | [**ClusterUpgradeItem**](ClusterUpgradeItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_firmware_progress**
> ClusterFirmwareProgress get_cluster_firmware_progress()



Cluster wide firmware upgrade status info.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()

try: 
    api_response = api_instance.get_cluster_firmware_progress()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->get_cluster_firmware_progress: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterFirmwareProgress**](ClusterFirmwareProgress.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_firmware_status**
> ClusterFirmwareStatus get_cluster_firmware_status(devices=devices, package=package)



The firmware status for the cluster.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list.Default is false. (optional)

try: 
    api_response = api_instance.get_cluster_firmware_status(devices=devices, package=package)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->get_cluster_firmware_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **package** | **bool**| Show package. If false, this returns an empty list.Default is false. | [optional] 

### Return type

[**ClusterFirmwareStatus**](ClusterFirmwareStatus.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node**
> ClusterNodesExtended get_cluster_node(cluster_node_id)



The node details useful during an upgrade or assessment.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_node_id = 56 # int | The node details useful during an upgrade or assessment.

try: 
    api_response = api_instance.get_cluster_node(cluster_node_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->get_cluster_node: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_node_id** | **int**| The node details useful during an upgrade or assessment. | 

### Return type

[**ClusterNodesExtended**](ClusterNodesExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes**
> ClusterNodesExtended get_cluster_nodes()



View information about nodes during an upgrade, rollback, or pre-upgrade assessment.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()

try: 
    api_response = api_instance.get_cluster_nodes()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->get_cluster_nodes: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterNodesExtended**](ClusterNodesExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_cluster**
> UpgradeCluster get_upgrade_cluster()



Cluster wide upgrade status info.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()

try: 
    api_response = api_instance.get_upgrade_cluster()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UpgradeApi->get_upgrade_cluster: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UpgradeCluster**](UpgradeCluster.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_upgrade**
> update_cluster_upgrade(cluster_upgrade)



Add nodes to a running upgrade.

### Example 
```python
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.UpgradeApi()
cluster_upgrade = isi_sdk.ClusterUpgrade() # ClusterUpgrade | 

try: 
    api_instance.update_cluster_upgrade(cluster_upgrade)
except ApiException as e:
    print "Exception when calling UpgradeApi->update_cluster_upgrade: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_upgrade** | [**ClusterUpgrade**](ClusterUpgrade.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

