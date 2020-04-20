# isi_sdk_8_2_0.ClusterApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster_add_node_item**](ClusterApi.md#create_cluster_add_node_item) | **POST** /platform/3/cluster/add-node | 
[**create_diagnostics_gather_start_item**](ClusterApi.md#create_diagnostics_gather_start_item) | **POST** /platform/3/cluster/diagnostics/gather/start | 
[**create_diagnostics_gather_stop_item**](ClusterApi.md#create_diagnostics_gather_stop_item) | **POST** /platform/3/cluster/diagnostics/gather/stop | 
[**create_diagnostics_netlogger_start_item**](ClusterApi.md#create_diagnostics_netlogger_start_item) | **POST** /platform/3/cluster/diagnostics/netlogger/start | 
[**create_diagnostics_netlogger_stop_item**](ClusterApi.md#create_diagnostics_netlogger_stop_item) | **POST** /platform/3/cluster/diagnostics/netlogger/stop | 
[**get_cluster_config**](ClusterApi.md#get_cluster_config) | **GET** /platform/3/cluster/config | 
[**get_cluster_email**](ClusterApi.md#get_cluster_email) | **GET** /platform/1/cluster/email | 
[**get_cluster_external_ips**](ClusterApi.md#get_cluster_external_ips) | **GET** /platform/2/cluster/external-ips | 
[**get_cluster_identity**](ClusterApi.md#get_cluster_identity) | **GET** /platform/5/cluster/identity | 
[**get_cluster_internal_networks**](ClusterApi.md#get_cluster_internal_networks) | **GET** /platform/7/cluster/internal-networks | 
[**get_cluster_node**](ClusterApi.md#get_cluster_node) | **GET** /platform/7/cluster/nodes/{ClusterNodeId} | 
[**get_cluster_nodes**](ClusterApi.md#get_cluster_nodes) | **GET** /platform/7/cluster/nodes | 
[**get_cluster_nodes_available**](ClusterApi.md#get_cluster_nodes_available) | **GET** /platform/3/cluster/nodes-available | 
[**get_cluster_owner**](ClusterApi.md#get_cluster_owner) | **GET** /platform/1/cluster/owner | 
[**get_cluster_statfs**](ClusterApi.md#get_cluster_statfs) | **GET** /platform/1/cluster/statfs | 
[**get_cluster_time**](ClusterApi.md#get_cluster_time) | **GET** /platform/3/cluster/time | 
[**get_cluster_timezone**](ClusterApi.md#get_cluster_timezone) | **GET** /platform/3/cluster/timezone | 
[**get_cluster_version**](ClusterApi.md#get_cluster_version) | **GET** /platform/3/cluster/version | 
[**get_diagnostics_gather**](ClusterApi.md#get_diagnostics_gather) | **GET** /platform/3/cluster/diagnostics/gather | 
[**get_diagnostics_gather_settings**](ClusterApi.md#get_diagnostics_gather_settings) | **GET** /platform/3/cluster/diagnostics/gather/settings | 
[**get_diagnostics_gather_status**](ClusterApi.md#get_diagnostics_gather_status) | **GET** /platform/3/cluster/diagnostics/gather/status | 
[**get_diagnostics_netlogger**](ClusterApi.md#get_diagnostics_netlogger) | **GET** /platform/3/cluster/diagnostics/netlogger | 
[**get_diagnostics_netlogger_settings**](ClusterApi.md#get_diagnostics_netlogger_settings) | **GET** /platform/3/cluster/diagnostics/netlogger/settings | 
[**get_diagnostics_netlogger_status**](ClusterApi.md#get_diagnostics_netlogger_status) | **GET** /platform/3/cluster/diagnostics/netlogger/status | 
[**get_timezone_region**](ClusterApi.md#get_timezone_region) | **GET** /platform/3/cluster/timezone/regions/{TimezoneRegionId} | 
[**get_timezone_settings**](ClusterApi.md#get_timezone_settings) | **GET** /platform/3/cluster/timezone/settings | 
[**update_cluster_email**](ClusterApi.md#update_cluster_email) | **PUT** /platform/1/cluster/email | 
[**update_cluster_identity**](ClusterApi.md#update_cluster_identity) | **PUT** /platform/5/cluster/identity | 
[**update_cluster_internal_networks**](ClusterApi.md#update_cluster_internal_networks) | **PUT** /platform/7/cluster/internal-networks | 
[**update_cluster_node**](ClusterApi.md#update_cluster_node) | **PUT** /platform/7/cluster/nodes/{ClusterNodeId} | 
[**update_cluster_owner**](ClusterApi.md#update_cluster_owner) | **PUT** /platform/1/cluster/owner | 
[**update_cluster_time**](ClusterApi.md#update_cluster_time) | **PUT** /platform/3/cluster/time | 
[**update_cluster_timezone**](ClusterApi.md#update_cluster_timezone) | **PUT** /platform/3/cluster/timezone | 
[**update_cluster_update_lnns**](ClusterApi.md#update_cluster_update_lnns) | **PUT** /platform/7/cluster/update-lnns | 
[**update_diagnostics_gather_settings**](ClusterApi.md#update_diagnostics_gather_settings) | **PUT** /platform/3/cluster/diagnostics/gather/settings | 
[**update_diagnostics_netlogger_settings**](ClusterApi.md#update_diagnostics_netlogger_settings) | **PUT** /platform/3/cluster/diagnostics/netlogger/settings | 
[**update_timezone_settings**](ClusterApi.md#update_timezone_settings) | **PUT** /platform/3/cluster/timezone/settings | 


# **create_cluster_add_node_item**
> Empty create_cluster_add_node_item(cluster_add_node_item)



Serial number and arguments of node to add.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_add_node_item = isi_sdk_8_2_0.ClusterAddNodeItem() # ClusterAddNodeItem | 

try:
    api_response = api_instance.create_cluster_add_node_item(cluster_add_node_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_cluster_add_node_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_add_node_item** | [**ClusterAddNodeItem**](ClusterAddNodeItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_diagnostics_gather_start_item**
> Empty create_diagnostics_gather_start_item(diagnostics_gather_start_item)



Start a new gather

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
diagnostics_gather_start_item = isi_sdk_8_2_0.DiagnosticsGatherSettingsExtended() # DiagnosticsGatherSettingsExtended | 

try:
    api_response = api_instance.create_diagnostics_gather_start_item(diagnostics_gather_start_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_diagnostics_gather_start_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostics_gather_start_item** | [**DiagnosticsGatherSettingsExtended**](DiagnosticsGatherSettingsExtended.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_diagnostics_gather_stop_item**
> Empty create_diagnostics_gather_stop_item(diagnostics_gather_stop_item)



Stop a running gather

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
diagnostics_gather_stop_item = isi_sdk_8_2_0.Empty() # Empty | 

try:
    api_response = api_instance.create_diagnostics_gather_stop_item(diagnostics_gather_stop_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_diagnostics_gather_stop_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostics_gather_stop_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_diagnostics_netlogger_start_item**
> Empty create_diagnostics_netlogger_start_item(diagnostics_netlogger_start_item)



Start a new packet capture

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
diagnostics_netlogger_start_item = isi_sdk_8_2_0.DiagnosticsNetloggerSettingsSettings() # DiagnosticsNetloggerSettingsSettings | 

try:
    api_response = api_instance.create_diagnostics_netlogger_start_item(diagnostics_netlogger_start_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_diagnostics_netlogger_start_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostics_netlogger_start_item** | [**DiagnosticsNetloggerSettingsSettings**](DiagnosticsNetloggerSettingsSettings.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_diagnostics_netlogger_stop_item**
> Empty create_diagnostics_netlogger_stop_item(diagnostics_netlogger_stop_item)



Stop a running packet capture

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
diagnostics_netlogger_stop_item = isi_sdk_8_2_0.Empty() # Empty | 

try:
    api_response = api_instance.create_diagnostics_netlogger_stop_item(diagnostics_netlogger_stop_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->create_diagnostics_netlogger_stop_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostics_netlogger_stop_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_config**
> ClusterConfig get_cluster_config()



Retrieve the cluster information.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterConfig**](ClusterConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_email**
> ClusterEmail get_cluster_email()



Get the cluster email notification settings.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_email()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_email: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterEmail**](ClusterEmail.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_external_ips**
> list[str] get_cluster_external_ips()



Retrieve the cluster IP addresses including IPV4 and IPV6.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_external_ips()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_external_ips: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_identity**
> ClusterIdentity get_cluster_identity()



Retrieve the login information.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_identity()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_identity: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterIdentity**](ClusterIdentity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_internal_networks**
> ClusterInternalNetworks get_cluster_internal_networks()



View internal networks settings.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_internal_networks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_internal_networks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterInternalNetworks**](ClusterInternalNetworks.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node**
> ClusterNodesExtendedExtended get_cluster_node(cluster_node_id, timeout=timeout)



Retrieve node information.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_node_id = 56 # int | Retrieve node information.
timeout = 8.14 # float | Request timeout (optional)

try:
    api_response = api_instance.get_cluster_node(cluster_node_id, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_node_id** | **int**| Retrieve node information. | 
 **timeout** | **float**| Request timeout | [optional] 

### Return type

[**ClusterNodesExtendedExtended**](ClusterNodesExtendedExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes**
> ClusterNodesExtendedExtended get_cluster_nodes(timeout=timeout)



List the nodes on this cluster.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
timeout = 8.14 # float | Request timeout (optional)

try:
    api_response = api_instance.get_cluster_nodes(timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **float**| Request timeout | [optional] 

### Return type

[**ClusterNodesExtendedExtended**](ClusterNodesExtendedExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes_available**
> ClusterNodesAvailable get_cluster_nodes_available()



List all nodes that are available to add to this cluster.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_nodes_available()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_nodes_available: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterNodesAvailable**](ClusterNodesAvailable.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_owner**
> ClusterOwner get_cluster_owner()



Get the cluster contact info settings

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_owner()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_owner: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterOwner**](ClusterOwner.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_statfs**
> ClusterStatfs get_cluster_statfs()



Retrieve the filesystem statistics.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_statfs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_statfs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStatfs**](ClusterStatfs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_time**
> ClusterTime get_cluster_time()



Retrieve the current time as reported by each node.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTime**](ClusterTime.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_timezone**
> ClusterTimezone get_cluster_timezone()



Get the cluster timezone.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_timezone()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_timezone: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTimezone**](ClusterTimezone.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_version**
> ClusterVersion get_cluster_version()



Retrieve the OneFS version as reported by each node.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterVersion**](ClusterVersion.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostics_gather**
> DiagnosticsGatherStatus get_diagnostics_gather()



Get the status of isi_gather_info.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_diagnostics_gather()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_diagnostics_gather: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiagnosticsGatherStatus**](DiagnosticsGatherStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostics_gather_settings**
> DiagnosticsGatherSettings get_diagnostics_gather_settings()



Get the default options for isi_gather_info.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_diagnostics_gather_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_diagnostics_gather_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiagnosticsGatherSettings**](DiagnosticsGatherSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostics_gather_status**
> DiagnosticsGatherStatus get_diagnostics_gather_status()



Get the status of isi_gather_info.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_diagnostics_gather_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_diagnostics_gather_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiagnosticsGatherStatus**](DiagnosticsGatherStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostics_netlogger**
> DiagnosticsNetloggerStatus get_diagnostics_netlogger()



Get the status of isi_netlogger.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_diagnostics_netlogger()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_diagnostics_netlogger: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiagnosticsNetloggerStatus**](DiagnosticsNetloggerStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostics_netlogger_settings**
> DiagnosticsNetloggerSettings get_diagnostics_netlogger_settings()



Get the default options for isi_netlogger.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_diagnostics_netlogger_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_diagnostics_netlogger_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiagnosticsNetloggerSettings**](DiagnosticsNetloggerSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_diagnostics_netlogger_status**
> DiagnosticsNetloggerStatus get_diagnostics_netlogger_status()



Get the status of isi_netlogger.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_diagnostics_netlogger_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_diagnostics_netlogger_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DiagnosticsNetloggerStatus**](DiagnosticsNetloggerStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezone_region**
> TimezoneRegions get_timezone_region(timezone_region_id, sort=sort, resume=resume, show_all=show_all, dst_reset=dst_reset, limit=limit, dir=dir)



List timezone regions.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
timezone_region_id = 'timezone_region_id_example' # str | List timezone regions.
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
show_all = true # bool | Show all timezones within the region specified in the URI. (optional)
dst_reset = true # bool | This query arg is not needed in normal use cases. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_timezone_region(timezone_region_id, sort=sort, resume=resume, show_all=show_all, dst_reset=dst_reset, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_timezone_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone_region_id** | **str**| List timezone regions. | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **show_all** | **bool**| Show all timezones within the region specified in the URI. | [optional] 
 **dst_reset** | **bool**| This query arg is not needed in normal use cases. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**TimezoneRegions**](TimezoneRegions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezone_settings**
> TimezoneSettings get_timezone_settings()



Retrieve the cluster timezone.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))

try:
    api_response = api_instance.get_timezone_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_timezone_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TimezoneSettings**](TimezoneSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_email**
> update_cluster_email(cluster_email)



Modify the cluster email notification settings.  All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_email = isi_sdk_8_2_0.ClusterEmailExtended() # ClusterEmailExtended | 

try:
    api_instance.update_cluster_email(cluster_email)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_email** | [**ClusterEmailExtended**](ClusterEmailExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_identity**
> update_cluster_identity(cluster_identity)



Modify the login information.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_identity = isi_sdk_8_2_0.ClusterIdentityExtended() # ClusterIdentityExtended | 

try:
    api_instance.update_cluster_identity(cluster_identity)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_identity** | [**ClusterIdentityExtended**](ClusterIdentityExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_internal_networks**
> update_cluster_internal_networks(cluster_internal_networks, reboot_confirmation_token=reboot_confirmation_token)



Modify IP address ranges to be used for internal network configuration.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_internal_networks = isi_sdk_8_2_0.ClusterInternalNetworksExtended() # ClusterInternalNetworksExtended | 
reboot_confirmation_token = 'reboot_confirmation_token_example' # str | Token returned by earlier PUT call with the same configuration. (optional)

try:
    api_instance.update_cluster_internal_networks(cluster_internal_networks, reboot_confirmation_token=reboot_confirmation_token)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster_internal_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_internal_networks** | [**ClusterInternalNetworksExtended**](ClusterInternalNetworksExtended.md)|  | 
 **reboot_confirmation_token** | **str**| Token returned by earlier PUT call with the same configuration. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_node**
> update_cluster_node(cluster_node, cluster_node_id)



Modify one or more node settings.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_node = isi_sdk_8_2_0.ClusterNode() # ClusterNode | 
cluster_node_id = 56 # int | Modify one or more node settings.

try:
    api_instance.update_cluster_node(cluster_node, cluster_node_id)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_node** | [**ClusterNode**](ClusterNode.md)|  | 
 **cluster_node_id** | **int**| Modify one or more node settings. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_owner**
> update_cluster_owner(cluster_owner)



Modify the cluster contact info settings.  All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_owner = isi_sdk_8_2_0.ClusterOwner() # ClusterOwner | 

try:
    api_instance.update_cluster_owner(cluster_owner)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster_owner: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_owner** | [**ClusterOwner**](ClusterOwner.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_time**
> update_cluster_time(cluster_time)



Set cluster time.  Time will mostly be synchronized across nodes, but there may be slight drift.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_time = isi_sdk_8_2_0.ClusterTimeExtended() # ClusterTimeExtended | 

try:
    api_instance.update_cluster_time(cluster_time)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster_time: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_time** | [**ClusterTimeExtended**](ClusterTimeExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_timezone**
> update_cluster_timezone(cluster_timezone)



Set a new timezone for the cluster.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_timezone = isi_sdk_8_2_0.ClusterTimezoneExtended() # ClusterTimezoneExtended | 

try:
    api_instance.update_cluster_timezone(cluster_timezone)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster_timezone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_timezone** | [**ClusterTimezoneExtended**](ClusterTimezoneExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster_update_lnns**
> update_cluster_update_lnns(cluster_update_lnns)



Modify the list of current lnn(s) with respective new lnn(s) to be used for configuration.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
cluster_update_lnns = isi_sdk_8_2_0.ClusterUpdateLnns() # ClusterUpdateLnns | 

try:
    api_instance.update_cluster_update_lnns(cluster_update_lnns)
except ApiException as e:
    print("Exception when calling ClusterApi->update_cluster_update_lnns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_update_lnns** | [**ClusterUpdateLnns**](ClusterUpdateLnns.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_diagnostics_gather_settings**
> update_diagnostics_gather_settings(diagnostics_gather_settings)



Set the default options for isi_gather_info.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
diagnostics_gather_settings = isi_sdk_8_2_0.DiagnosticsGatherSettingsExtended() # DiagnosticsGatherSettingsExtended | 

try:
    api_instance.update_diagnostics_gather_settings(diagnostics_gather_settings)
except ApiException as e:
    print("Exception when calling ClusterApi->update_diagnostics_gather_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostics_gather_settings** | [**DiagnosticsGatherSettingsExtended**](DiagnosticsGatherSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_diagnostics_netlogger_settings**
> update_diagnostics_netlogger_settings(diagnostics_netlogger_settings)



Set the default options for isi_netlogger.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
diagnostics_netlogger_settings = isi_sdk_8_2_0.DiagnosticsNetloggerSettingsSettings() # DiagnosticsNetloggerSettingsSettings | 

try:
    api_instance.update_diagnostics_netlogger_settings(diagnostics_netlogger_settings)
except ApiException as e:
    print("Exception when calling ClusterApi->update_diagnostics_netlogger_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostics_netlogger_settings** | [**DiagnosticsNetloggerSettingsSettings**](DiagnosticsNetloggerSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_timezone_settings**
> update_timezone_settings(timezone_settings)



Modify the cluster timezone.

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
api_instance = isi_sdk_8_2_0.ClusterApi(isi_sdk_8_2_0.ApiClient(configuration))
timezone_settings = isi_sdk_8_2_0.TimezoneRegionTimezone() # TimezoneRegionTimezone | 

try:
    api_instance.update_timezone_settings(timezone_settings)
except ApiException as e:
    print("Exception when calling ClusterApi->update_timezone_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timezone_settings** | [**TimezoneRegionTimezone**](TimezoneRegionTimezone.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

