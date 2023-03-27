# isilon_sdk.v9_2_1.LocalApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_time**](LocalApi.md#get_cluster_time) | **GET** /platform/3/local/cluster/time | 
[**get_network_interfaces**](LocalApi.md#get_network_interfaces) | **GET** /platform/12/local/network/interfaces | 
[**get_protocols_smb_sessions**](LocalApi.md#get_protocols_smb_sessions) | **GET** /platform/11/local/protocols/smb/sessions | 
[**get_upgrade_cluster_firmware_device**](LocalApi.md#get_upgrade_cluster_firmware_device) | **GET** /platform/10/local/upgrade/cluster/firmware/device | 
[**get_upgrade_cluster_firmware_status**](LocalApi.md#get_upgrade_cluster_firmware_status) | **GET** /platform/3/local/upgrade/cluster/firmware/status | 


# **get_cluster_time**
> ClusterTimeExtendedExtended get_cluster_time()



Get the current time on the local node.

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
api_instance = isilon_sdk.v9_2_1.LocalApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_cluster_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTimeExtendedExtended**](ClusterTimeExtendedExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_interfaces**
> NetworkInterfaces get_network_interfaces(cache=cache, dir=dir, include_vlans=include_vlans, limit=limit, lnn=lnn, network=network, owner=owner, resume=resume, sort=sort, type=type, vlan_id=vlan_id)



Get a list of interfaces.

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
api_instance = isilon_sdk.v9_2_1.LocalApi(isilon_sdk.v9_2_1.ApiClient(configuration))
cache = 'cache_example' # str | Control where interface data is source from. no-cache only returns live data from a running node, and if a node can't be reached, no results will be returned. cache-only only returns cached data, some fields are set as null/unknown if they can't be determined, and IPs listed are the IPs that should be configured. Finally, nodes-first will try to query live nodes, and fall back to the cache for any nodes that fail. Default: nodes-first (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
include_vlans = true # bool | If include_vlans is set to true, all vlans are returned unless further filtered by vlan_id. If include_vlans is set to false, no vlans are returned. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
lnn = [56] # list[int] | Get a list of interfaces for the specified lnns. (optional)
network = 'network_example' # str | Show interfaces associated with external and/or internal networks. Default is 'external' (optional)
owner = 'owner_example' # str | Filter results by owner id. Support partials matches too. Ex owner=groupnet0 or owner=groupnet0.subnet0.pool0. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
type = 'type_example' # str | Filter the returned IPs by IP type. (optional)
vlan_id = 56 # int | Only return IPs/interfaces configured in the specified VLAN ID (optional)

try:
    api_response = api_instance.get_network_interfaces(cache=cache, dir=dir, include_vlans=include_vlans, limit=limit, lnn=lnn, network=network, owner=owner, resume=resume, sort=sort, type=type, vlan_id=vlan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache** | **str**| Control where interface data is source from. no-cache only returns live data from a running node, and if a node can&#39;t be reached, no results will be returned. cache-only only returns cached data, some fields are set as null/unknown if they can&#39;t be determined, and IPs listed are the IPs that should be configured. Finally, nodes-first will try to query live nodes, and fall back to the cache for any nodes that fail. Default: nodes-first | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **include_vlans** | **bool**| If include_vlans is set to true, all vlans are returned unless further filtered by vlan_id. If include_vlans is set to false, no vlans are returned. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **lnn** | [**list[int]**](int.md)| Get a list of interfaces for the specified lnns. | [optional] 
 **network** | **str**| Show interfaces associated with external and/or internal networks. Default is &#39;external&#39; | [optional] 
 **owner** | **str**| Filter results by owner id. Support partials matches too. Ex owner&#x3D;groupnet0 or owner&#x3D;groupnet0.subnet0.pool0. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **type** | **str**| Filter the returned IPs by IP type. | [optional] 
 **vlan_id** | **int**| Only return IPs/interfaces configured in the specified VLAN ID | [optional] 

### Return type

[**NetworkInterfaces**](NetworkInterfaces.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protocols_smb_sessions**
> ProtocolsSmbSessions get_protocols_smb_sessions(limit=limit, lnn=lnn, lnn_skip=lnn_skip, resume=resume)



List open SMB sessions.

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
api_instance = isilon_sdk.v9_2_1.LocalApi(isilon_sdk.v9_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
lnn = 'lnn_example' # str | The node to fetch open sessions from. (optional)
lnn_skip = 'lnn_skip_example' # str | When parameter lnn=all, don't fetch open session info from this node. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_protocols_smb_sessions(limit=limit, lnn=lnn, lnn_skip=lnn_skip, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_protocols_smb_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **lnn** | **str**| The node to fetch open sessions from. | [optional] 
 **lnn_skip** | **str**| When parameter lnn&#x3D;all, don&#39;t fetch open session info from this node. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**ProtocolsSmbSessions**](ProtocolsSmbSessions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_cluster_firmware_device**
> UpgradeClusterFirmwareDevice get_upgrade_cluster_firmware_device(devices=devices, package=package, refresh=refresh)



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
api_instance = isilon_sdk.v9_2_1.LocalApi(isilon_sdk.v9_2_1.ApiClient(configuration))
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list. Default is false. (optional)
refresh = true # bool | Re-gather firmware status. Default is false. (optional)

try:
    api_response = api_instance.get_upgrade_cluster_firmware_device(devices=devices, package=package, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_upgrade_cluster_firmware_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **package** | **bool**| Show package. If false, this returns an empty list. Default is false. | [optional] 
 **refresh** | **bool**| Re-gather firmware status. Default is false. | [optional] 

### Return type

[**UpgradeClusterFirmwareDevice**](UpgradeClusterFirmwareDevice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_cluster_firmware_status**
> UpgradeClusterFirmwareDevice get_upgrade_cluster_firmware_status(devices=devices, package=package, refresh=refresh)



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
api_instance = isilon_sdk.v9_2_1.LocalApi(isilon_sdk.v9_2_1.ApiClient(configuration))
devices = true # bool | Show devices. If false, this returns an empty list. Default is false. (optional)
package = true # bool | Show package. If false, this returns an empty list. Default is false. (optional)
refresh = true # bool | Re-gather firmware status. Default is false. (optional)

try:
    api_response = api_instance.get_upgrade_cluster_firmware_status(devices=devices, package=package, refresh=refresh)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalApi->get_upgrade_cluster_firmware_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devices** | **bool**| Show devices. If false, this returns an empty list. Default is false. | [optional] 
 **package** | **bool**| Show package. If false, this returns an empty list. Default is false. | [optional] 
 **refresh** | **bool**| Re-gather firmware status. Default is false. | [optional] 

### Return type

[**UpgradeClusterFirmwareDevice**](UpgradeClusterFirmwareDevice.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

