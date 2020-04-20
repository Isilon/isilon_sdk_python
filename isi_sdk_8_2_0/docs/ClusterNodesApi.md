# isi_sdk_8_2_0.ClusterNodesApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_drives_drive_add_item**](ClusterNodesApi.md#create_drives_drive_add_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/add | 
[**create_drives_drive_firmware_update_item**](ClusterNodesApi.md#create_drives_drive_firmware_update_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/firmware/update | 
[**create_drives_drive_format_item**](ClusterNodesApi.md#create_drives_drive_format_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/format | 
[**create_drives_drive_purpose_item**](ClusterNodesApi.md#create_drives_drive_purpose_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/purpose | 
[**create_drives_drive_smartfail_item**](ClusterNodesApi.md#create_drives_drive_smartfail_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/smartfail | 
[**create_drives_drive_stopfail_item**](ClusterNodesApi.md#create_drives_drive_stopfail_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/stopfail | 
[**create_drives_drive_suspend_item**](ClusterNodesApi.md#create_drives_drive_suspend_item) | **POST** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/suspend | 
[**create_node_reboot_item**](ClusterNodesApi.md#create_node_reboot_item) | **POST** /platform/5/cluster/nodes/{Lnn}/reboot | 
[**create_node_shutdown_item**](ClusterNodesApi.md#create_node_shutdown_item) | **POST** /platform/5/cluster/nodes/{Lnn}/shutdown | 
[**get_drives_drive_firmware**](ClusterNodesApi.md#get_drives_drive_firmware) | **GET** /platform/7/cluster/nodes/{Lnn}/drives/{Driveid}/firmware | 
[**get_node_drive**](ClusterNodesApi.md#get_node_drive) | **GET** /platform/7/cluster/nodes/{Lnn}/drives/{NodeDriveId} | 
[**get_node_driveconfig**](ClusterNodesApi.md#get_node_driveconfig) | **GET** /platform/5/cluster/nodes/{Lnn}/driveconfig | 
[**get_node_drives**](ClusterNodesApi.md#get_node_drives) | **GET** /platform/7/cluster/nodes/{Lnn}/drives | 
[**get_node_drives_purposelist**](ClusterNodesApi.md#get_node_drives_purposelist) | **GET** /platform/3/cluster/nodes/{Lnn}/drives-purposelist | 
[**get_node_hardware**](ClusterNodesApi.md#get_node_hardware) | **GET** /platform/5/cluster/nodes/{Lnn}/hardware | 
[**get_node_hardware_fast**](ClusterNodesApi.md#get_node_hardware_fast) | **GET** /platform/3/cluster/nodes/{Lnn}/hardware-fast | 
[**get_node_internal_ip_address**](ClusterNodesApi.md#get_node_internal_ip_address) | **GET** /platform/7/cluster/nodes/{Lnn}/internal-ip-address | 
[**get_node_partitions**](ClusterNodesApi.md#get_node_partitions) | **GET** /platform/3/cluster/nodes/{Lnn}/partitions | 
[**get_node_sensors**](ClusterNodesApi.md#get_node_sensors) | **GET** /platform/3/cluster/nodes/{Lnn}/sensors | 
[**get_node_sled**](ClusterNodesApi.md#get_node_sled) | **GET** /platform/5/cluster/nodes/{Lnn}/sleds/{NodeSledId} | 
[**get_node_sleds**](ClusterNodesApi.md#get_node_sleds) | **GET** /platform/5/cluster/nodes/{Lnn}/sleds | 
[**get_node_state**](ClusterNodesApi.md#get_node_state) | **GET** /platform/3/cluster/nodes/{Lnn}/state | 
[**get_node_state_readonly**](ClusterNodesApi.md#get_node_state_readonly) | **GET** /platform/3/cluster/nodes/{Lnn}/state/readonly | 
[**get_node_state_servicelight**](ClusterNodesApi.md#get_node_state_servicelight) | **GET** /platform/3/cluster/nodes/{Lnn}/state/servicelight | 
[**get_node_state_smartfail**](ClusterNodesApi.md#get_node_state_smartfail) | **GET** /platform/3/cluster/nodes/{Lnn}/state/smartfail | 
[**get_node_status**](ClusterNodesApi.md#get_node_status) | **GET** /platform/3/cluster/nodes/{Lnn}/status | 
[**get_node_status_batterystatus**](ClusterNodesApi.md#get_node_status_batterystatus) | **GET** /platform/3/cluster/nodes/{Lnn}/status/batterystatus | 
[**list_drives_drive_firmware_update**](ClusterNodesApi.md#list_drives_drive_firmware_update) | **GET** /platform/3/cluster/nodes/{Lnn}/drives/{Driveid}/firmware/update | 
[**update_node_driveconfig**](ClusterNodesApi.md#update_node_driveconfig) | **PUT** /platform/5/cluster/nodes/{Lnn}/driveconfig | 
[**update_node_state_readonly**](ClusterNodesApi.md#update_node_state_readonly) | **PUT** /platform/3/cluster/nodes/{Lnn}/state/readonly | 
[**update_node_state_servicelight**](ClusterNodesApi.md#update_node_state_servicelight) | **PUT** /platform/3/cluster/nodes/{Lnn}/state/servicelight | 
[**update_node_state_smartfail**](ClusterNodesApi.md#update_node_state_smartfail) | **PUT** /platform/3/cluster/nodes/{Lnn}/state/smartfail | 


# **create_drives_drive_add_item**
> Empty create_drives_drive_add_item(drives_drive_add_item, lnn, driveid)



Add a drive to a node.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
drives_drive_add_item = isi_sdk_8_2_0.Empty() # Empty | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_add_item(drives_drive_add_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_add_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_add_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_firmware_update_item**
> Empty create_drives_drive_firmware_update_item(drives_drive_firmware_update_item, lnn, driveid)



Start a drive firmware update.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
drives_drive_firmware_update_item = isi_sdk_8_2_0.DrivesDriveFirmwareUpdateItem() # DrivesDriveFirmwareUpdateItem | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_firmware_update_item(drives_drive_firmware_update_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_firmware_update_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_firmware_update_item** | [**DrivesDriveFirmwareUpdateItem**](DrivesDriveFirmwareUpdateItem.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_format_item**
> Empty create_drives_drive_format_item(drives_drive_format_item, lnn, driveid)



Format a drive for use by OneFS.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
drives_drive_format_item = isi_sdk_8_2_0.DrivesDriveFormatItem() # DrivesDriveFormatItem | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_format_item(drives_drive_format_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_format_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_format_item** | [**DrivesDriveFormatItem**](DrivesDriveFormatItem.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_purpose_item**
> Empty create_drives_drive_purpose_item(drives_drive_purpose_item, lnn, driveid)



Assign a drive to a specific use case.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
drives_drive_purpose_item = isi_sdk_8_2_0.DrivesDrivePurposeItem() # DrivesDrivePurposeItem | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_purpose_item(drives_drive_purpose_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_purpose_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_purpose_item** | [**DrivesDrivePurposeItem**](DrivesDrivePurposeItem.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_smartfail_item**
> Empty create_drives_drive_smartfail_item(drives_drive_smartfail_item, lnn, driveid)



Remove a drive from use by OneFS.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
drives_drive_smartfail_item = isi_sdk_8_2_0.Empty() # Empty | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_smartfail_item(drives_drive_smartfail_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_smartfail_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_smartfail_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_stopfail_item**
> Empty create_drives_drive_stopfail_item(drives_drive_stopfail_item, lnn, driveid)



Stop restriping from a smartfailing drive.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
drives_drive_stopfail_item = isi_sdk_8_2_0.Empty() # Empty | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_stopfail_item(drives_drive_stopfail_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_stopfail_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_stopfail_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_drives_drive_suspend_item**
> Empty create_drives_drive_suspend_item(drives_drive_suspend_item, lnn, driveid)



Temporarily remove a drive from use by OneFS.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
drives_drive_suspend_item = isi_sdk_8_2_0.Empty() # Empty | 
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.create_drives_drive_suspend_item(drives_drive_suspend_item, lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_drives_drive_suspend_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drives_drive_suspend_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_reboot_item**
> Empty create_node_reboot_item(node_reboot_item, lnn, force=force)



Reboot the node specified by <LNN>.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
node_reboot_item = isi_sdk_8_2_0.Empty() # Empty | 
lnn = 56 # int | 
force = true # bool | Force reboot on Infinity platform even if a drive sled is not present. (optional)

try:
    api_response = api_instance.create_node_reboot_item(node_reboot_item, lnn, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_node_reboot_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_reboot_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **force** | **bool**| Force reboot on Infinity platform even if a drive sled is not present. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_node_shutdown_item**
> Empty create_node_shutdown_item(node_shutdown_item, lnn, force=force)



Shutdown the node specified by <LNN>.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
node_shutdown_item = isi_sdk_8_2_0.Empty() # Empty | 
lnn = 56 # int | 
force = true # bool | Force shutdown on Infinity platform even if a drive sled is not present. (optional)

try:
    api_response = api_instance.create_node_shutdown_item(node_shutdown_item, lnn, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->create_node_shutdown_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_shutdown_item** | [**Empty**](Empty.md)|  | 
 **lnn** | **int**|  | 
 **force** | **bool**| Force shutdown on Infinity platform even if a drive sled is not present. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drives_drive_firmware**
> DrivesDriveFirmware get_drives_drive_firmware(lnn, driveid)



Retrieve drive firmware information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.get_drives_drive_firmware(lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_drives_drive_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**DrivesDriveFirmware**](DrivesDriveFirmware.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_drive**
> NodeDrives get_node_drive(node_drive_id, lnn, timeout=timeout)



Retrieve drive information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
node_drive_id = 'node_drive_id_example' # str | Retrieve drive information.
lnn = 56 # int | 
timeout = 8.14 # float | Request timeout (optional)

try:
    api_response = api_instance.get_node_drive(node_drive_id, lnn, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_drive_id** | **str**| Retrieve drive information. | 
 **lnn** | **int**|  | 
 **timeout** | **float**| Request timeout | [optional] 

### Return type

[**NodeDrives**](NodeDrives.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_driveconfig**
> NodeDriveconfig get_node_driveconfig(lnn, timeout=timeout)



View a node's drive subsystem XML configuration file.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 
timeout = 8.14 # float | Request timeout (optional)

try:
    api_response = api_instance.get_node_driveconfig(lnn, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_driveconfig: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **timeout** | **float**| Request timeout | [optional] 

### Return type

[**NodeDriveconfig**](NodeDriveconfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_drives**
> NodeDrives get_node_drives(lnn, timeout=timeout)



List the drives on this node.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 
timeout = 8.14 # float | Request timeout (optional)

try:
    api_response = api_instance.get_node_drives(lnn, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_drives: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **timeout** | **float**| Request timeout | [optional] 

### Return type

[**NodeDrives**](NodeDrives.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_drives_purposelist**
> NodeDrivesPurposelist get_node_drives_purposelist(lnn)



Lists the available purposes for drives in this node.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_drives_purposelist(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_drives_purposelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeDrivesPurposelist**](NodeDrivesPurposelist.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_hardware**
> NodeHardware get_node_hardware(lnn, timeout=timeout)



Retrieve node hardware identity information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 
timeout = 8.14 # float | Request timeout (optional)

try:
    api_response = api_instance.get_node_hardware(lnn, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_hardware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **timeout** | **float**| Request timeout | [optional] 

### Return type

[**NodeHardware**](NodeHardware.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_hardware_fast**
> NodeHardwareFast get_node_hardware_fast(lnn)



Quickly retrieve a subset of node hardware identity information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_hardware_fast(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_hardware_fast: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeHardwareFast**](NodeHardwareFast.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_internal_ip_address**
> NodeInternalIpAddress get_node_internal_ip_address(lnn)



View internal ip address with respect to node.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_internal_ip_address(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_internal_ip_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeInternalIpAddress**](NodeInternalIpAddress.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_partitions**
> NodePartitions get_node_partitions(lnn)



Retrieve node partition information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_partitions(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_partitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodePartitions**](NodePartitions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_sensors**
> NodeSensors get_node_sensors(lnn)



Retrieve node sensor information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_sensors(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeSensors**](NodeSensors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_sled**
> NodeSleds get_node_sled(node_sled_id, lnn, timeout=timeout)



Get detailed information for the sled specified by <SLEDID>, or all sleds in the case where <SLEDID> is 'all', in the node specified by <LNN>.  Accepts <sledid> in either 'sled' or 'all' formats.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
node_sled_id = 'node_sled_id_example' # str | Get detailed information for the sled specified by <SLEDID>, or all sleds in the case where <SLEDID> is 'all', in the node specified by <LNN>.  Accepts <sledid> in either 'sled' or 'all' formats.
lnn = 56 # int | 
timeout = 8.14 # float | Request timeout (optional)

try:
    api_response = api_instance.get_node_sled(node_sled_id, lnn, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_sled: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_sled_id** | **str**| Get detailed information for the sled specified by &lt;SLEDID&gt;, or all sleds in the case where &lt;SLEDID&gt; is &#39;all&#39;, in the node specified by &lt;LNN&gt;.  Accepts &lt;sledid&gt; in either &#39;sled&#39; or &#39;all&#39; formats. | 
 **lnn** | **int**|  | 
 **timeout** | **float**| Request timeout | [optional] 

### Return type

[**NodeSleds**](NodeSleds.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_sleds**
> NodeSleds get_node_sleds(lnn, timeout=timeout)



Get detailed information for all sleds in this node. Equivalent to /5/cluster/nodes/<lnn>/sleds/all.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 
timeout = 8.14 # float | Request timeout (optional)

try:
    api_response = api_instance.get_node_sleds(lnn, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_sleds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **timeout** | **float**| Request timeout | [optional] 

### Return type

[**NodeSleds**](NodeSleds.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_state**
> NodeState get_node_state(lnn)



Retrieve node state information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_state(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeState**](NodeState.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_state_readonly**
> NodeStateReadonly get_node_state_readonly(lnn)



Retrieve node readonly state information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_state_readonly(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_state_readonly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStateReadonly**](NodeStateReadonly.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_state_servicelight**
> NodeStateServicelight get_node_state_servicelight(lnn)



Retrieve node service light state information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_state_servicelight(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_state_servicelight: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStateServicelight**](NodeStateServicelight.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_state_smartfail**
> NodeStateSmartfail get_node_state_smartfail(lnn)



Retrieve node smartfail state information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_state_smartfail(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_state_smartfail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStateSmartfail**](NodeStateSmartfail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_status**
> NodeStatus get_node_status(lnn)



Retrieve node status information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_status(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStatus**](NodeStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_status_batterystatus**
> NodeStatusBatterystatus get_node_status_batterystatus(lnn)



Retrieve node battery status information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 

try:
    api_response = api_instance.get_node_status_batterystatus(lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->get_node_status_batterystatus: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 

### Return type

[**NodeStatusBatterystatus**](NodeStatusBatterystatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_drives_drive_firmware_update**
> DrivesDriveFirmwareUpdate list_drives_drive_firmware_update(lnn, driveid)



Retrieve firmware update information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
lnn = 56 # int | 
driveid = 'driveid_example' # str | 

try:
    api_response = api_instance.list_drives_drive_firmware_update(lnn, driveid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->list_drives_drive_firmware_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lnn** | **int**|  | 
 **driveid** | **str**|  | 

### Return type

[**DrivesDriveFirmwareUpdate**](DrivesDriveFirmwareUpdate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_driveconfig**
> update_node_driveconfig(node_driveconfig, lnn)



Modify a node's drive subsystem XML configuration file.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
node_driveconfig = isi_sdk_8_2_0.NodeDriveconfigExtended() # NodeDriveconfigExtended | 
lnn = 56 # int | 

try:
    api_instance.update_node_driveconfig(node_driveconfig, lnn)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->update_node_driveconfig: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_driveconfig** | [**NodeDriveconfigExtended**](NodeDriveconfigExtended.md)|  | 
 **lnn** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_state_readonly**
> update_node_state_readonly(node_state_readonly, lnn)



Modify one or more node readonly state settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
node_state_readonly = isi_sdk_8_2_0.NodeStateReadonlyExtended() # NodeStateReadonlyExtended | 
lnn = 56 # int | 

try:
    api_instance.update_node_state_readonly(node_state_readonly, lnn)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->update_node_state_readonly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_state_readonly** | [**NodeStateReadonlyExtended**](NodeStateReadonlyExtended.md)|  | 
 **lnn** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_state_servicelight**
> update_node_state_servicelight(node_state_servicelight, lnn)



Modify one or more node service light state settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
node_state_servicelight = isi_sdk_8_2_0.NodeStateServicelightExtended() # NodeStateServicelightExtended | 
lnn = 56 # int | 

try:
    api_instance.update_node_state_servicelight(node_state_servicelight, lnn)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->update_node_state_servicelight: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_state_servicelight** | [**NodeStateServicelightExtended**](NodeStateServicelightExtended.md)|  | 
 **lnn** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_node_state_smartfail**
> update_node_state_smartfail(node_state_smartfail, lnn)



Modify smartfail state of the node.  Only the 'smartfailed' body member has any effect on node smartfail state.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.ClusterNodesApi(isi_sdk_8_2_0.ApiClient(configuration))
node_state_smartfail = isi_sdk_8_2_0.NodeStateSmartfailExtended() # NodeStateSmartfailExtended | 
lnn = 56 # int | 

try:
    api_instance.update_node_state_smartfail(node_state_smartfail, lnn)
except ApiException as e:
    print("Exception when calling ClusterNodesApi->update_node_state_smartfail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_state_smartfail** | [**NodeStateSmartfailExtended**](NodeStateSmartfailExtended.md)|  | 
 **lnn** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

