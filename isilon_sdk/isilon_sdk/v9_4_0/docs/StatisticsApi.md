# isilon_sdk.v9_4_0.StatisticsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics_current**](StatisticsApi.md#get_statistics_current) | **GET** /platform/1/statistics/current | 
[**get_statistics_history**](StatisticsApi.md#get_statistics_history) | **GET** /platform/1/statistics/history | 
[**get_statistics_key**](StatisticsApi.md#get_statistics_key) | **GET** /platform/1/statistics/keys/{StatisticsKeyId} | 
[**get_statistics_keys**](StatisticsApi.md#get_statistics_keys) | **GET** /platform/1/statistics/keys | 
[**get_statistics_operations**](StatisticsApi.md#get_statistics_operations) | **GET** /platform/3/statistics/operations | 
[**get_statistics_protocols**](StatisticsApi.md#get_statistics_protocols) | **GET** /platform/1/statistics/protocols | 
[**get_summary_client**](StatisticsApi.md#get_summary_client) | **GET** /platform/3/statistics/summary/client | 
[**get_summary_cloud**](StatisticsApi.md#get_summary_cloud) | **GET** /platform/14/statistics/summary/cloud | 
[**get_summary_drive**](StatisticsApi.md#get_summary_drive) | **GET** /platform/3/statistics/summary/drive | 
[**get_summary_heat**](StatisticsApi.md#get_summary_heat) | **GET** /platform/3/statistics/summary/heat | 
[**get_summary_protocol**](StatisticsApi.md#get_summary_protocol) | **GET** /platform/3/statistics/summary/protocol | 
[**get_summary_protocol_stats**](StatisticsApi.md#get_summary_protocol_stats) | **GET** /platform/3/statistics/summary/protocol-stats | 
[**get_summary_system**](StatisticsApi.md#get_summary_system) | **GET** /platform/3/statistics/summary/system | 
[**get_summary_workload**](StatisticsApi.md#get_summary_workload) | **GET** /platform/10/statistics/summary/workload | 


# **get_statistics_current**
> StatisticsCurrent get_statistics_current(degraded=degraded, desc_info=desc_info, devid=devid, key=key, keys=keys, nodes=nodes, raw=raw, show_nodes=show_nodes, stale=stale, substr=substr, timeout=timeout, type_info=type_info)



Retrieve stats.

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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
degraded = true # bool | If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. (optional)
desc_info = true # bool | Shows the description for the specified key(s). (optional)
devid = ['devid_example'] # list[str] | Node devid to query. Either an <integer> or \"all\". Can be used more than one time to query multiple nodes. \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used. (optional)
key = ['key_example'] # list[str] | One key name. Can be used more than one time to query multiple keys. Also works with 'keys' arguments. (optional)
keys = ['keys_example'] # list[str] | Multiple key names. Can be a comma separated list, or can be used more than one time to make queries for multiple keys. May be used in conjunction with 'substr'. Also works with 'key' arguments. (optional)
nodes = ['nodes_example'] # list[str] | Specify node(s) for which statistics should be reported. One or more comma separated <integer(s)> specifying which node(s) to query, or \"all\". Specifying more than one node may have unspecified results for keys that begin with \"cluster\". (optional)
raw = true # bool | Causes the output to be in hex format. For internal use only, please do not use this. (optional)
show_nodes = true # bool | Shows the logical node number or LNN in addition to the devid. (optional)
stale = true # bool | For internal use only, please do not use this. (optional)
substr = true # bool | Used in conjunction with the 'keys' argument, alters the behavior of keys. Makes the 'keys' arg perform a partial match. Defaults to false. (optional)
timeout = 56 # int | Time in seconds to wait for results from remote nodes. (optional)
type_info = true # bool | The type ID is used by internal services. For internal use only, please do not use this. (optional)

try:
    api_response = api_instance.get_statistics_current(degraded=degraded, desc_info=desc_info, devid=devid, key=key, keys=keys, nodes=nodes, raw=raw, show_nodes=show_nodes, stale=stale, substr=substr, timeout=timeout, type_info=type_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **degraded** | **bool**| If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. | [optional] 
 **desc_info** | **bool**| Shows the description for the specified key(s). | [optional] 
 **devid** | [**list[str]**](str.md)| Node devid to query. Either an &lt;integer&gt; or \&quot;all\&quot;. Can be used more than one time to query multiple nodes. \&quot;all\&quot; queries all up nodes. 0 means query the local node. For \&quot;cluster\&quot; scoped keys, in any devid including 0 can be used. | [optional] 
 **key** | [**list[str]**](str.md)| One key name. Can be used more than one time to query multiple keys. Also works with &#39;keys&#39; arguments. | [optional] 
 **keys** | [**list[str]**](str.md)| Multiple key names. Can be a comma separated list, or can be used more than one time to make queries for multiple keys. May be used in conjunction with &#39;substr&#39;. Also works with &#39;key&#39; arguments. | [optional] 
 **nodes** | [**list[str]**](str.md)| Specify node(s) for which statistics should be reported. One or more comma separated &lt;integer(s)&gt; specifying which node(s) to query, or \&quot;all\&quot;. Specifying more than one node may have unspecified results for keys that begin with \&quot;cluster\&quot;. | [optional] 
 **raw** | **bool**| Causes the output to be in hex format. For internal use only, please do not use this. | [optional] 
 **show_nodes** | **bool**| Shows the logical node number or LNN in addition to the devid. | [optional] 
 **stale** | **bool**| For internal use only, please do not use this. | [optional] 
 **substr** | **bool**| Used in conjunction with the &#39;keys&#39; argument, alters the behavior of keys. Makes the &#39;keys&#39; arg perform a partial match. Defaults to false. | [optional] 
 **timeout** | **int**| Time in seconds to wait for results from remote nodes. | [optional] 
 **type_info** | **bool**| The type ID is used by internal services. For internal use only, please do not use this. | [optional] 

### Return type

[**StatisticsCurrent**](StatisticsCurrent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_history**
> StatisticsHistory get_statistics_history(begin=begin, degraded=degraded, desc_info=desc_info, devid=devid, end=end, interval=interval, key=key, keys=keys, memory_only=memory_only, nodes=nodes, raw=raw, resolution=resolution, show_nodes=show_nodes, stale=stale, substr=substr, timeout=timeout, type_info=type_info)



Retrieve stats.

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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
begin = 56 # int | Earliest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. (optional)
degraded = true # bool | If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. (optional)
desc_info = true # bool | Shows the description for the specified key(s). (optional)
devid = ['devid_example'] # list[str] | Node devid to query. Either an <integer> or \"all\". Can be used more than one time to query multiple nodes. \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used. (optional)
end = 56 # int | Latest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. If not supplied, use now as the end time. (optional)
interval = 56 # int | Minimum sampling interval time in seconds. If native statistics are higher resolution, data will be down-sampled. (optional)
key = ['key_example'] # list[str] | One key name. Can be used more than one time to query multiple keys. Also works with 'keys' arguments. (optional)
keys = ['keys_example'] # list[str] | Multiple key names. Can be a comma separated list, or can be used more than one time to make queries for multiple keys. May be used in conjunction with 'substr'. Also works with 'key' arguments. (optional)
memory_only = true # bool | Only use statistics sources that reside in memory (faster, but with less retention). (optional)
nodes = ['nodes_example'] # list[str] | Specify node(s) for which statistics should be reported. One or more comma separated <integer(s)> specifying which node(s) to query, or \"all\". Specifying more than one node may have unspecified results for keys that begin with \"cluster\". (optional)
raw = true # bool | Causes the output to be in hex format. For internal use only, please do not use this. (optional)
resolution = 56 # int | Synonymous with 'interval', if supplied supersedes interval. (optional)
show_nodes = true # bool | Shows the logical node number or LNN in addition to the devid. (optional)
stale = true # bool | For internal use only, please do not use this. (optional)
substr = true # bool | Used in conjunction with the 'keys' argument, alters the behavior of keys. Makes the 'keys' arg perform a partial match. Defaults to false. (optional)
timeout = 56 # int | Time in seconds to wait for results from remote nodes. (optional)
type_info = true # bool | The type ID is used by internal services. For internal use only, please do not use this. (optional)

try:
    api_response = api_instance.get_statistics_history(begin=begin, degraded=degraded, desc_info=desc_info, devid=devid, end=end, interval=interval, key=key, keys=keys, memory_only=memory_only, nodes=nodes, raw=raw, resolution=resolution, show_nodes=show_nodes, stale=stale, substr=substr, timeout=timeout, type_info=type_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Earliest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. | [optional] 
 **degraded** | **bool**| If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. | [optional] 
 **desc_info** | **bool**| Shows the description for the specified key(s). | [optional] 
 **devid** | [**list[str]**](str.md)| Node devid to query. Either an &lt;integer&gt; or \&quot;all\&quot;. Can be used more than one time to query multiple nodes. \&quot;all\&quot; queries all up nodes. 0 means query the local node. For \&quot;cluster\&quot; scoped keys, in any devid including 0 can be used. | [optional] 
 **end** | **int**| Latest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. If not supplied, use now as the end time. | [optional] 
 **interval** | **int**| Minimum sampling interval time in seconds. If native statistics are higher resolution, data will be down-sampled. | [optional] 
 **key** | [**list[str]**](str.md)| One key name. Can be used more than one time to query multiple keys. Also works with &#39;keys&#39; arguments. | [optional] 
 **keys** | [**list[str]**](str.md)| Multiple key names. Can be a comma separated list, or can be used more than one time to make queries for multiple keys. May be used in conjunction with &#39;substr&#39;. Also works with &#39;key&#39; arguments. | [optional] 
 **memory_only** | **bool**| Only use statistics sources that reside in memory (faster, but with less retention). | [optional] 
 **nodes** | [**list[str]**](str.md)| Specify node(s) for which statistics should be reported. One or more comma separated &lt;integer(s)&gt; specifying which node(s) to query, or \&quot;all\&quot;. Specifying more than one node may have unspecified results for keys that begin with \&quot;cluster\&quot;. | [optional] 
 **raw** | **bool**| Causes the output to be in hex format. For internal use only, please do not use this. | [optional] 
 **resolution** | **int**| Synonymous with &#39;interval&#39;, if supplied supersedes interval. | [optional] 
 **show_nodes** | **bool**| Shows the logical node number or LNN in addition to the devid. | [optional] 
 **stale** | **bool**| For internal use only, please do not use this. | [optional] 
 **substr** | **bool**| Used in conjunction with the &#39;keys&#39; argument, alters the behavior of keys. Makes the &#39;keys&#39; arg perform a partial match. Defaults to false. | [optional] 
 **timeout** | **int**| Time in seconds to wait for results from remote nodes. | [optional] 
 **type_info** | **bool**| The type ID is used by internal services. For internal use only, please do not use this. | [optional] 

### Return type

[**StatisticsHistory**](StatisticsHistory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_key**
> StatisticsKeys get_statistics_key(statistics_key_id)



List key meta-data.

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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
statistics_key_id = 'statistics_key_id_example' # str | List key meta-data.

try:
    api_response = api_instance.get_statistics_key(statistics_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statistics_key_id** | **str**| List key meta-data. | 

### Return type

[**StatisticsKeys**](StatisticsKeys.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_keys**
> StatisticsKeysExtended get_statistics_keys(count=count, limit=limit, queryable=queryable, resume=resume)



List meta-data for matching keys.

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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
count = true # bool | Only count matching keys, do not return meta-data. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
queryable = true # bool | Only list keys that can/cannot be queries. Default is true. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_statistics_keys(count=count, limit=limit, queryable=queryable, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **bool**| Only count matching keys, do not return meta-data. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **queryable** | **bool**| Only list keys that can/cannot be queries. Default is true. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**StatisticsKeysExtended**](StatisticsKeysExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_operations**
> StatisticsOperations get_statistics_operations(protocols=protocols)



Retrieve operations list.

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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
protocols = ['protocols_example'] # list[str] | A comma separated list. Only report operations for specified protocol(s). Default is all.  (optional)

try:
    api_response = api_instance.get_statistics_operations(protocols=protocols)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **protocols** | [**list[str]**](str.md)| A comma separated list. Only report operations for specified protocol(s). Default is all.  | [optional] 

### Return type

[**StatisticsOperations**](StatisticsOperations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_protocols**
> StatisticsProtocols get_statistics_protocols(type=type)



Retrieve protocol list.

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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
type = 'type_example' # str | Specifies whether internal, external, or all protocols should be returned. (optional)

try:
    api_response = api_instance.get_statistics_protocols(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_protocols: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Specifies whether internal, external, or all protocols should be returned. | [optional] 

### Return type

[**StatisticsProtocols**](StatisticsProtocols.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_client**
> SummaryClient get_summary_client(classes=classes, degraded=degraded, local_addresses=local_addresses, local_names=local_names, nodes=nodes, numeric=numeric, protocols=protocols, remote_addresses=remote_addresses, remote_names=remote_names, sort=sort, timeout=timeout, totalby=totalby, user_ids=user_ids, user_names=user_names)





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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
classes = 'classes_example' # str | A comma separated list. Default is all. (other | write | read | namespace_read | namespace_write) (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
local_addresses = 'local_addresses_example' # str | A comma separated list. Only report statistics for operations handled by the local hosts with dotted-quad IP addresses enumerated.  (optional)
local_names = 'local_names_example' # str | A comma separated list. Only report statistics for operations handled by the local hosts with resolved names enumerated.  (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
numeric = true # bool | Do not resolve hostnames and usernames to their human readable form(s). Default is false.  (optional)
protocols = 'protocols_example' # str | A comma separated list. Default is all. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | nfsrdma | papi | jobd | irp | lsass_in | lsass_out | hdfs | s3 | internal | external) (optional)
remote_addresses = 'remote_addresses_example' # str | A comma separated list. Only report statistics for operations requested by the remote clients with dotted-quad IP addresses enumerated.  (optional)
remote_names = 'remote_names_example' # str | A comma separated list. Only report statistics for operations requested by the remote clients with resolved names enumerated.  (optional)
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (num_operations | operation_rate | in_max | in_min | in | in_avg | out_max | out_min | out | out_avg | time_max | time_min | time_avg | node | protocol | class | user_id | user_name | local_addr | local_name | remote_addr | remote_name) Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
totalby = 'totalby_example' # str | A comma separated list specifying what should be unique. (node | protocol | class | local_addr | local_name | remote_addr | remote_name | user_id | user_name | devid). Aggregation is performed over all the fields not specified in the list. (optional)
user_ids = 'user_ids_example' # str | A comma separated list. Only report statistics for operations requested by users with numeric UIDs enumerated.  (optional)
user_names = 'user_names_example' # str | A comma separated list. Only report statistics for operations requested by users with resolved names enumerated.  (optional)

try:
    api_response = api_instance.get_summary_client(classes=classes, degraded=degraded, local_addresses=local_addresses, local_names=local_names, nodes=nodes, numeric=numeric, protocols=protocols, remote_addresses=remote_addresses, remote_names=remote_names, sort=sort, timeout=timeout, totalby=totalby, user_ids=user_ids, user_names=user_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classes** | **str**| A comma separated list. Default is all. (other | write | read | namespace_read | namespace_write) | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **local_addresses** | **str**| A comma separated list. Only report statistics for operations handled by the local hosts with dotted-quad IP addresses enumerated.  | [optional] 
 **local_names** | **str**| A comma separated list. Only report statistics for operations handled by the local hosts with resolved names enumerated.  | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **numeric** | **bool**| Do not resolve hostnames and usernames to their human readable form(s). Default is false.  | [optional] 
 **protocols** | **str**| A comma separated list. Default is all. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | nfsrdma | papi | jobd | irp | lsass_in | lsass_out | hdfs | s3 | internal | external) | [optional] 
 **remote_addresses** | **str**| A comma separated list. Only report statistics for operations requested by the remote clients with dotted-quad IP addresses enumerated.  | [optional] 
 **remote_names** | **str**| A comma separated list. Only report statistics for operations requested by the remote clients with resolved names enumerated.  | [optional] 
 **sort** | **str**| Sort data by the specified comma-separated field(s). (num_operations | operation_rate | in_max | in_min | in | in_avg | out_max | out_min | out | out_avg | time_max | time_min | time_avg | node | protocol | class | user_id | user_name | local_addr | local_name | remote_addr | remote_name) Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **totalby** | **str**| A comma separated list specifying what should be unique. (node | protocol | class | local_addr | local_name | remote_addr | remote_name | user_id | user_name | devid). Aggregation is performed over all the fields not specified in the list. | [optional] 
 **user_ids** | **str**| A comma separated list. Only report statistics for operations requested by users with numeric UIDs enumerated.  | [optional] 
 **user_names** | **str**| A comma separated list. Only report statistics for operations requested by users with resolved names enumerated.  | [optional] 

### Return type

[**SummaryClient**](SummaryClient.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_cloud**
> SummaryCloud get_summary_cloud(account=account, degraded=degraded, nodes=nodes, policy=policy, sort=sort, timeout=timeout)



List all Cloudpools statistics.

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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
account = 'account_example' # str | Specify an account for which statistics should be reported. (optional)
degraded = true # bool | Continue to report even if some nodes do not respond.Defaults to false. (optional)
nodes = 'nodes_example' # str | Specify node(s) for which statistics should be reported. Default is 'all'. Zero (0) should be passed in as the sole argument to indicate local. (optional)
policy = 'policy_example' # str | Specify a policy for which statistics should be reported. (optional)
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). ( account | policy | in | out | reads | writes | deletes | cloud | node). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds. Defaults to 5 seconds. (optional)

try:
    api_response = api_instance.get_summary_cloud(account=account, degraded=degraded, nodes=nodes, policy=policy, sort=sort, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_cloud: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | **str**| Specify an account for which statistics should be reported. | [optional] 
 **degraded** | **bool**| Continue to report even if some nodes do not respond.Defaults to false. | [optional] 
 **nodes** | **str**| Specify node(s) for which statistics should be reported. Default is &#39;all&#39;. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **policy** | **str**| Specify a policy for which statistics should be reported. | [optional] 
 **sort** | **str**| Sort data by the specified comma-separated field(s). ( account | policy | in | out | reads | writes | deletes | cloud | node). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds. Defaults to 5 seconds. | [optional] 

### Return type

[**SummaryCloud**](SummaryCloud.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_drive**
> SummaryDrive get_summary_drive(degraded=degraded, nodes=nodes, sort=sort, timeout=timeout, type=type)





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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (drive_id | type | xfers_in | bytes_in | xfer_size_in | xfers_out | bytes_out | xfer_size_out | access_latency | access_slow | iosched_latency | iosched_queue | busy | used_bytes_percent | used_inodes). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
type = 'type_example' # str | Specify drive type(s) for which statistics should be reported. (optional)

try:
    api_response = api_instance.get_summary_drive(degraded=degraded, nodes=nodes, sort=sort, timeout=timeout, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_drive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **sort** | **str**| Sort data by the specified comma-separated field(s). (drive_id | type | xfers_in | bytes_in | xfer_size_in | xfers_out | bytes_out | xfer_size_out | access_latency | access_slow | iosched_latency | iosched_queue | busy | used_bytes_percent | used_inodes). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **type** | **str**| Specify drive type(s) for which statistics should be reported. | [optional] 

### Return type

[**SummaryDrive**](SummaryDrive.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_heat**
> SummaryHeat get_summary_heat(classes=classes, convertlin=convertlin, degraded=degraded, events=events, maxpath=maxpath, nodes=nodes, numeric=numeric, pathdepth=pathdepth, sort=sort, timeout=timeout, totalby=totalby)



File heat map, i.e. rate of file operations, and the type of operation listed by path/lin(s).

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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
classes = 'classes_example' # str | A comma separated list. Default is all. (other | write | read | namespace_read | namespace_write). (optional)
convertlin = true # bool | Convert lin to hex. Default is true.  (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
events = 'events_example' # str | A comma separated list. Default is all. Only report specified event types(s). (blocked | contended | deadlocked | getattr | link | lock | lookup | read | rename | setattr | unlink | write). (optional)
maxpath = 56 # int | Maximum bytes allocated for looking up a path. An ASCII character is 1 byte (it may be more for other types of encoding). The default is 4096 bytes. Zero (0) means unlimited (subject to the system limits). (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
numeric = true # bool | Do not resolve LINs into filenames. Default is false.  (optional)
pathdepth = 56 # int | Squash paths to this directory depth. Defaults to none, i.e. the paths are not limited (subject to the system limits). (optional)
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (operation_rate | node | event_name | class_name | lin | path). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
totalby = 'totalby_example' # str | A comma separated list specifying what should be unique. (node | event_name | event_class | operation_rate | path | lin). Aggregation is performed over all the fields not specified in the list. (optional)

try:
    api_response = api_instance.get_summary_heat(classes=classes, convertlin=convertlin, degraded=degraded, events=events, maxpath=maxpath, nodes=nodes, numeric=numeric, pathdepth=pathdepth, sort=sort, timeout=timeout, totalby=totalby)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_heat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classes** | **str**| A comma separated list. Default is all. (other | write | read | namespace_read | namespace_write). | [optional] 
 **convertlin** | **bool**| Convert lin to hex. Default is true.  | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **events** | **str**| A comma separated list. Default is all. Only report specified event types(s). (blocked | contended | deadlocked | getattr | link | lock | lookup | read | rename | setattr | unlink | write). | [optional] 
 **maxpath** | **int**| Maximum bytes allocated for looking up a path. An ASCII character is 1 byte (it may be more for other types of encoding). The default is 4096 bytes. Zero (0) means unlimited (subject to the system limits). | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **numeric** | **bool**| Do not resolve LINs into filenames. Default is false.  | [optional] 
 **pathdepth** | **int**| Squash paths to this directory depth. Defaults to none, i.e. the paths are not limited (subject to the system limits). | [optional] 
 **sort** | **str**| Sort data by the specified comma-separated field(s). (operation_rate | node | event_name | class_name | lin | path). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **totalby** | **str**| A comma separated list specifying what should be unique. (node | event_name | event_class | operation_rate | path | lin). Aggregation is performed over all the fields not specified in the list. | [optional] 

### Return type

[**SummaryHeat**](SummaryHeat.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_protocol**
> SummaryProtocol get_summary_protocol(classes=classes, degraded=degraded, nodes=nodes, operations=operations, protocols=protocols, sort=sort, timeout=timeout, totalby=totalby, zero=zero)





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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
classes = 'classes_example' # str | A comma separated list. Default is all. (other | write | read | create | delete | namespace_read | namespace_write | file_state | session_state). (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
operations = 'operations_example' # str | Specify operation(s) for which statistics should be reported (See the cli command: 'isi statistics list operations', for a total list). Default is all.  (optional)
protocols = 'protocols_example' # str | A comma separated list. Default is all external protocols. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | nfsrdma | papi | jobd | irp | lsass_in | lsass_out | hdfs | s3 | all | internal | external) (optional)
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (time | operation_count | operation_rate | in_max | in_min | in | in_avg | in_standard_dev | out_max | out_min | out | out_avg | out_standard_dev | time_max | time_min | time_avg | time_standard_dev | node | protocol | class | operation). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
totalby = 'totalby_example' # str | A comma separated list specifying what should be unique. (node | protocol | class | operation). Aggregation is performed over all the fields not specified in the list. (optional)
zero = true # bool | Show table entries with no values. (optional)

try:
    api_response = api_instance.get_summary_protocol(classes=classes, degraded=degraded, nodes=nodes, operations=operations, protocols=protocols, sort=sort, timeout=timeout, totalby=totalby, zero=zero)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_protocol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classes** | **str**| A comma separated list. Default is all. (other | write | read | create | delete | namespace_read | namespace_write | file_state | session_state). | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **operations** | **str**| Specify operation(s) for which statistics should be reported (See the cli command: &#39;isi statistics list operations&#39;, for a total list). Default is all.  | [optional] 
 **protocols** | **str**| A comma separated list. Default is all external protocols. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | nfsrdma | papi | jobd | irp | lsass_in | lsass_out | hdfs | s3 | all | internal | external) | [optional] 
 **sort** | **str**| Sort data by the specified comma-separated field(s). (time | operation_count | operation_rate | in_max | in_min | in | in_avg | in_standard_dev | out_max | out_min | out | out_avg | out_standard_dev | time_max | time_min | time_avg | time_standard_dev | node | protocol | class | operation). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **totalby** | **str**| A comma separated list specifying what should be unique. (node | protocol | class | operation). Aggregation is performed over all the fields not specified in the list. | [optional] 
 **zero** | **bool**| Show table entries with no values. | [optional] 

### Return type

[**SummaryProtocol**](SummaryProtocol.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_protocol_stats**
> SummaryProtocolStats get_summary_protocol_stats(degraded=degraded, nodes=nodes, protocol=protocol, timeout=timeout)





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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
protocol = 'protocol_example' # str | A single protocol. Default is nfs3. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | nfsrdma | papi | jobd | irp | lsass_in | lsass_out | hdfs | s3) (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)

try:
    api_response = api_instance.get_summary_protocol_stats(degraded=degraded, nodes=nodes, protocol=protocol, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_protocol_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **protocol** | **str**| A single protocol. Default is nfs3. (nfs3 | smb1 | nlm | ftp | http | siq | smb2 | nfs4 | nfsrdma | papi | jobd | irp | lsass_in | lsass_out | hdfs | s3) | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 

### Return type

[**SummaryProtocolStats**](SummaryProtocolStats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_system**
> SummarySystem get_summary_system(degraded=degraded, nodes=nodes, oprates=oprates, sort=sort, timeout=timeout)





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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
oprates = true # bool | Display protocol operation rate statistics rather than the default throughput statistics. (optional)
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). (time | node | cpu | smb | ftp | http | nfs | hdfs | s3 | total | net_in | net_out | disk_in). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)

try:
    api_response = api_instance.get_summary_system(degraded=degraded, nodes=nodes, oprates=oprates, sort=sort, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **oprates** | **bool**| Display protocol operation rate statistics rather than the default throughput statistics. | [optional] 
 **sort** | **str**| Sort data by the specified comma-separated field(s). (time | node | cpu | smb | ftp | http | nfs | hdfs | s3 | total | net_in | net_out | disk_in). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 

### Return type

[**SummarySystem**](SummarySystem.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_summary_workload**
> SummaryWorkload get_summary_workload(dataset=dataset, degraded=degraded, domain_ids=domain_ids, export_ids=export_ids, group_ids=group_ids, group_sids=group_sids, groupnames=groupnames, job_types=job_types, local_addresses=local_addresses, local_names=local_names, nodes=nodes, numeric=numeric, paths=paths, protocols=protocols, remote_addresses=remote_addresses, remote_names=remote_names, share_names=share_names, sort=sort, system_names=system_names, timeout=timeout, totalby=totalby, user_ids=user_ids, user_sids=user_sids, usernames=usernames, zone_ids=zone_ids, zone_names=zone_names)





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
api_instance = isilon_sdk.v9_4_0.StatisticsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dataset = 'dataset_example' # str | Report workload performance metrics for specified dataset. Default is 'System'. (optional)
degraded = true # bool | Continue to report if some nodes do not respond. (optional)
domain_ids = 'domain_ids_example' # str | A comma separated list. Only report statistics for domains specified by id, if configured.  (optional)
export_ids = 'export_ids_example' # str | A comma separated list. Only report statistics for exports specified by id, if configured.  (optional)
group_ids = 'group_ids_example' # str | A comma separated list. Only report statistics for groups specified by numeric GIDs, if configured.  (optional)
group_sids = 'group_sids_example' # str | A comma separated list. Only report statistics for groups specified by Group Security IDs, if configured.  (optional)
groupnames = 'groupnames_example' # str | A comma separated list. Only report statistics for groups specified by resolved names, if configured.  (optional)
job_types = ['job_types_example'] # list[str] | A comma separated list. Only report statistics for job(s) specified by type, if configured.  (optional)
local_addresses = 'local_addresses_example' # str | A comma separated list. Only report statistics for local hosts specified by IP addresses, if configured.  (optional)
local_names = 'local_names_example' # str | A comma separated list. Only report statistics for local hosts specified by resolved names, if configured.  (optional)
nodes = 'nodes_example' # str | A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. (optional)
numeric = true # bool | Do not resolve addresses and usernames to their human readable form(s). Default is false.  (optional)
paths = 'paths_example' # str | A comma separated list. Only report statistics for paths specified by name, if configured.  (optional)
protocols = 'protocols_example' # str | A comma separated list. Default is all. (smb1, smb2, nfs3, nfs4 and s3 only at this time.) (optional)
remote_addresses = 'remote_addresses_example' # str | A comma separated list. Only report statistics for remote clients specified by IP addresses, if configured.  (optional)
remote_names = 'remote_names_example' # str | A comma separated list. Only report statistics for remote clients specified by resolved names, if configured.  (optional)
share_names = 'share_names_example' # str | A comma separated list. Only report statistics for shares specified by name, if configured.  (optional)
sort = 'sort_example' # str | Sort data by the specified comma-separated field(s). ( node | workload_id | system_name | user_id | user_sid | username | group_id | group_sid | groupname | domain_id | path | zone_id | zone_name | export_id | local_addr | local_name | remote_addr | remote_name | protocol | share_name | job_type | cpu | bytes_in | bytes_out | ops | reads | writes | l2 | l3 | latency_read | latency_write | latency_other | error). Prepend 'asc:' or 'desc:' to a field to change the sort direction.  (optional)
system_names = 'system_names_example' # str | A comma separated list. Only report statistics for systems specified by resolved names, if configured.  (optional)
timeout = 56 # int | Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. (optional)
totalby = 'totalby_example' # str | A comma separated list specifying what should be unique. (node | system_name | user_id | user_sid | username | zone_id | zone_name | local_addr | local_name | remote_addr | remote_name | group_id | group_sid | groupname | domain_id | path | export_id | protocol | share_name | job_type). Aggregation is performed over all the fields not specified in the list. (optional)
user_ids = 'user_ids_example' # str | A comma separated list. Only report statistics for users specified by numeric UIDs, if configured.  (optional)
user_sids = 'user_sids_example' # str | A comma separated list. Only report statistics for users specified by Security IDs, if configured.  (optional)
usernames = 'usernames_example' # str | A comma separated list. Only report statistics for users specified by resolved names, if configured.  (optional)
zone_ids = 'zone_ids_example' # str | A comma separated list. Only report statistics for users in zone specified by id, if configured.  (optional)
zone_names = 'zone_names_example' # str | A comma separated list. Only report statistics for users in zone specified by name, if configured.  (optional)

try:
    api_response = api_instance.get_summary_workload(dataset=dataset, degraded=degraded, domain_ids=domain_ids, export_ids=export_ids, group_ids=group_ids, group_sids=group_sids, groupnames=groupnames, job_types=job_types, local_addresses=local_addresses, local_names=local_names, nodes=nodes, numeric=numeric, paths=paths, protocols=protocols, remote_addresses=remote_addresses, remote_names=remote_names, share_names=share_names, sort=sort, system_names=system_names, timeout=timeout, totalby=totalby, user_ids=user_ids, user_sids=user_sids, usernames=usernames, zone_ids=zone_ids, zone_names=zone_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_summary_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**| Report workload performance metrics for specified dataset. Default is &#39;System&#39;. | [optional] 
 **degraded** | **bool**| Continue to report if some nodes do not respond. | [optional] 
 **domain_ids** | **str**| A comma separated list. Only report statistics for domains specified by id, if configured.  | [optional] 
 **export_ids** | **str**| A comma separated list. Only report statistics for exports specified by id, if configured.  | [optional] 
 **group_ids** | **str**| A comma separated list. Only report statistics for groups specified by numeric GIDs, if configured.  | [optional] 
 **group_sids** | **str**| A comma separated list. Only report statistics for groups specified by Group Security IDs, if configured.  | [optional] 
 **groupnames** | **str**| A comma separated list. Only report statistics for groups specified by resolved names, if configured.  | [optional] 
 **job_types** | [**list[str]**](str.md)| A comma separated list. Only report statistics for job(s) specified by type, if configured.  | [optional] 
 **local_addresses** | **str**| A comma separated list. Only report statistics for local hosts specified by IP addresses, if configured.  | [optional] 
 **local_names** | **str**| A comma separated list. Only report statistics for local hosts specified by resolved names, if configured.  | [optional] 
 **nodes** | **str**| A comma separated list. Specify node(s) for which statistics should be reported. Default is all. Zero (0) should be passed in as the sole argument to indicate local. | [optional] 
 **numeric** | **bool**| Do not resolve addresses and usernames to their human readable form(s). Default is false.  | [optional] 
 **paths** | **str**| A comma separated list. Only report statistics for paths specified by name, if configured.  | [optional] 
 **protocols** | **str**| A comma separated list. Default is all. (smb1, smb2, nfs3, nfs4 and s3 only at this time.) | [optional] 
 **remote_addresses** | **str**| A comma separated list. Only report statistics for remote clients specified by IP addresses, if configured.  | [optional] 
 **remote_names** | **str**| A comma separated list. Only report statistics for remote clients specified by resolved names, if configured.  | [optional] 
 **share_names** | **str**| A comma separated list. Only report statistics for shares specified by name, if configured.  | [optional] 
 **sort** | **str**| Sort data by the specified comma-separated field(s). ( node | workload_id | system_name | user_id | user_sid | username | group_id | group_sid | groupname | domain_id | path | zone_id | zone_name | export_id | local_addr | local_name | remote_addr | remote_name | protocol | share_name | job_type | cpu | bytes_in | bytes_out | ops | reads | writes | l2 | l3 | latency_read | latency_write | latency_other | error). Prepend &#39;asc:&#39; or &#39;desc:&#39; to a field to change the sort direction.  | [optional] 
 **system_names** | **str**| A comma separated list. Only report statistics for systems specified by resolved names, if configured.  | [optional] 
 **timeout** | **int**| Timeout remote commands after NUM seconds, where NUM is the integer passed to the argument. | [optional] 
 **totalby** | **str**| A comma separated list specifying what should be unique. (node | system_name | user_id | user_sid | username | zone_id | zone_name | local_addr | local_name | remote_addr | remote_name | group_id | group_sid | groupname | domain_id | path | export_id | protocol | share_name | job_type). Aggregation is performed over all the fields not specified in the list. | [optional] 
 **user_ids** | **str**| A comma separated list. Only report statistics for users specified by numeric UIDs, if configured.  | [optional] 
 **user_sids** | **str**| A comma separated list. Only report statistics for users specified by Security IDs, if configured.  | [optional] 
 **usernames** | **str**| A comma separated list. Only report statistics for users specified by resolved names, if configured.  | [optional] 
 **zone_ids** | **str**| A comma separated list. Only report statistics for users in zone specified by id, if configured.  | [optional] 
 **zone_names** | **str**| A comma separated list. Only report statistics for users in zone specified by name, if configured.  | [optional] 

### Return type

[**SummaryWorkload**](SummaryWorkload.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

