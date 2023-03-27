# isilon_sdk.v9_0_0.FsaResultsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_histogram_stat_by**](FsaResultsApi.md#get_histogram_stat_by) | **GET** /platform/3/fsa/results/{Id}/histogram/{Stat}/by | 
[**get_histogram_stat_by_breakout**](FsaResultsApi.md#get_histogram_stat_by_breakout) | **GET** /platform/3/fsa/results/{Id}/histogram/{Stat}/by/{HistogramStatByBreakout} | 
[**get_result_dir_pools_usage**](FsaResultsApi.md#get_result_dir_pools_usage) | **GET** /platform/9/fsa/results/{Id}/dir_pools_usage | 
[**get_result_dir_pools_usage_lin**](FsaResultsApi.md#get_result_dir_pools_usage_lin) | **GET** /platform/9/fsa/results/{Id}/dir_pools_usage/{ResultDirPoolsUsageLin} | 
[**get_result_directories**](FsaResultsApi.md#get_result_directories) | **GET** /platform/3/fsa/results/{Id}/directories | 
[**get_result_directory**](FsaResultsApi.md#get_result_directory) | **GET** /platform/3/fsa/results/{Id}/directories/{ResultDirectoryId} | 
[**get_result_histogram**](FsaResultsApi.md#get_result_histogram) | **GET** /platform/3/fsa/results/{Id}/histogram | 
[**get_result_histogram_stat**](FsaResultsApi.md#get_result_histogram_stat) | **GET** /platform/3/fsa/results/{Id}/histogram/{ResultHistogramStat} | 
[**get_result_top_dir**](FsaResultsApi.md#get_result_top_dir) | **GET** /platform/3/fsa/results/{Id}/top-dirs/{ResultTopDirId} | 
[**get_result_top_dirs**](FsaResultsApi.md#get_result_top_dirs) | **GET** /platform/3/fsa/results/{Id}/top-dirs | 
[**get_result_top_file**](FsaResultsApi.md#get_result_top_file) | **GET** /platform/3/fsa/results/{Id}/top-files/{ResultTopFileId} | 
[**get_result_top_files**](FsaResultsApi.md#get_result_top_files) | **GET** /platform/3/fsa/results/{Id}/top-files | 


# **get_histogram_stat_by**
> HistogramStatBy get_histogram_stat_by(id, stat)



This resource retrieves a histogram breakout for an individual FSA result set. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
id = 'id_example' # str | 
stat = 'stat_example' # str | 

try:
    api_response = api_instance.get_histogram_stat_by(id, stat)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_histogram_stat_by: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **stat** | **str**|  | 

### Return type

[**HistogramStatBy**](HistogramStatBy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_histogram_stat_by_breakout**
> HistogramStatBy get_histogram_stat_by_breakout(histogram_stat_by_breakout, id, stat, atime_filter=atime_filter, attribute_filter=attribute_filter, comp_report=comp_report, ctime_filter=ctime_filter, directory_filter=directory_filter, disk_pool_filter=disk_pool_filter, limit=limit, log_size_filter=log_size_filter, node_pool_filter=node_pool_filter, path_ext_filter=path_ext_filter, phys_size_filter=phys_size_filter, tier_filter=tier_filter)



This resource retrieves a histogram breakout for an individual FSA result set. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
histogram_stat_by_breakout = 'histogram_stat_by_breakout_example' # str | This resource retrieves a histogram breakout for an individual FSA result set. ID in the resource path is the result set ID.
id = 'id_example' # str | 
stat = 'stat_example' # str | 
atime_filter = 56 # int | Filter according to file accessed time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid atime filter values may be found by performing a histogram breakout by atime and viewing the resulting key values. (optional)
attribute_filter = 'attribute_filter_example' # str | Filter according to the name of a file user attribute. (optional)
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
ctime_filter = 56 # int | Filter according to file modified time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid ctime filter values may be found by performing a histogram breakout by ctime and viewing the resulting key values. (optional)
directory_filter = 'directory_filter_example' # str | Filter according to a specific directory, which includes all of its subdirectories. (optional)
disk_pool_filter = 'disk_pool_filter_example' # str | Filter according to the name of a disk pool, which is a set of drives that represent an independent failure domain. (optional)
limit = 56 # int | Limit the number of breakout results. (optional)
log_size_filter = 56 # int | Filter according to file logical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by logical size. The list of valid log_size filter values may be found by performing a histogram breakout by log_size and viewing the resulting key values. (optional)
node_pool_filter = 'node_pool_filter_example' # str | Filter according to the name of a node pool, which is a set of disk pools that belong to nodes of the same equivalence class. (optional)
path_ext_filter = 'path_ext_filter_example' # str | Filter according to the name of a single file extension. (optional)
phys_size_filter = 56 # int | Filter according to file physical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by physical size. The list of valid phys_size filter values may be found by performing a histogram breakout by phys_size and viewing the resulting key values. (optional)
tier_filter = 'tier_filter_example' # str | Filter according to the name of a storage tier, which is a user-created set of node pools. (optional)

try:
    api_response = api_instance.get_histogram_stat_by_breakout(histogram_stat_by_breakout, id, stat, atime_filter=atime_filter, attribute_filter=attribute_filter, comp_report=comp_report, ctime_filter=ctime_filter, directory_filter=directory_filter, disk_pool_filter=disk_pool_filter, limit=limit, log_size_filter=log_size_filter, node_pool_filter=node_pool_filter, path_ext_filter=path_ext_filter, phys_size_filter=phys_size_filter, tier_filter=tier_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_histogram_stat_by_breakout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **histogram_stat_by_breakout** | **str**| This resource retrieves a histogram breakout for an individual FSA result set. ID in the resource path is the result set ID. | 
 **id** | **str**|  | 
 **stat** | **str**|  | 
 **atime_filter** | **int**| Filter according to file accessed time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid atime filter values may be found by performing a histogram breakout by atime and viewing the resulting key values. | [optional] 
 **attribute_filter** | **str**| Filter according to the name of a file user attribute. | [optional] 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **ctime_filter** | **int**| Filter according to file modified time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid ctime filter values may be found by performing a histogram breakout by ctime and viewing the resulting key values. | [optional] 
 **directory_filter** | **str**| Filter according to a specific directory, which includes all of its subdirectories. | [optional] 
 **disk_pool_filter** | **str**| Filter according to the name of a disk pool, which is a set of drives that represent an independent failure domain. | [optional] 
 **limit** | **int**| Limit the number of breakout results. | [optional] 
 **log_size_filter** | **int**| Filter according to file logical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by logical size. The list of valid log_size filter values may be found by performing a histogram breakout by log_size and viewing the resulting key values. | [optional] 
 **node_pool_filter** | **str**| Filter according to the name of a node pool, which is a set of disk pools that belong to nodes of the same equivalence class. | [optional] 
 **path_ext_filter** | **str**| Filter according to the name of a single file extension. | [optional] 
 **phys_size_filter** | **int**| Filter according to file physical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by physical size. The list of valid phys_size filter values may be found by performing a histogram breakout by phys_size and viewing the resulting key values. | [optional] 
 **tier_filter** | **str**| Filter according to the name of a storage tier, which is a user-created set of node pools. | [optional] 

### Return type

[**HistogramStatBy**](HistogramStatBy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_dir_pools_usage**
> ResultDirPoolsUsage get_result_dir_pools_usage(id, comp_report=comp_report, path=path, storage_pool_type=storage_pool_type)



 View pool usage information of a directory, classified by storage pools in response \"usage_data\". The storage pool type can be specified by query parameter \"storage_pool_type\". The directory is \"path\" query parameter. The response \"dir_usage\" is total disk usage of directory, over all pools at a given storage pool level. When path cannot be found within result, status code 404 and error message will be returned.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
id = 'id_example' # str | 
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
path = 'path_example' # str |  Directory absolute path to report usage information. Path should be UTF8 percent encoded, should be within \"/ifs\". Defaults to \"/ifs\". (optional)
storage_pool_type = 'storage_pool_type_example' # str | The type of the storage pool. (optional)

try:
    api_response = api_instance.get_result_dir_pools_usage(id, comp_report=comp_report, path=path, storage_pool_type=storage_pool_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_dir_pools_usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **path** | **str**|  Directory absolute path to report usage information. Path should be UTF8 percent encoded, should be within \&quot;/ifs\&quot;. Defaults to \&quot;/ifs\&quot;. | [optional] 
 **storage_pool_type** | **str**| The type of the storage pool. | [optional] 

### Return type

[**ResultDirPoolsUsage**](ResultDirPoolsUsage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_dir_pools_usage_lin**
> ResultDirPoolsUsage get_result_dir_pools_usage_lin(result_dir_pools_usage_lin, id, comp_report=comp_report, storage_pool_type=storage_pool_type)



 View pool usage information of a directory, classified by storage pools in response \"usage_data\". The storage pool type can be specified by query parameter \"storage_pool_type\". The directory is LIN token of URI. The response \"dir_usage\" is total disk usage of directory, over all pools at a given storage pool level. When LIN cannot be found within result, status code 404 and error message will be returned.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
result_dir_pools_usage_lin = 56 # int |  View pool usage information of a directory, classified by storage pools in response \"usage_data\". The storage pool type can be specified by query parameter \"storage_pool_type\". The directory is LIN token of URI. The response \"dir_usage\" is total disk usage of directory, over all pools at a given storage pool level. When LIN cannot be found within result, status code 404 and error message will be returned.
id = 'id_example' # str | 
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
storage_pool_type = 'storage_pool_type_example' # str | The type of the storage pool. (optional)

try:
    api_response = api_instance.get_result_dir_pools_usage_lin(result_dir_pools_usage_lin, id, comp_report=comp_report, storage_pool_type=storage_pool_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_dir_pools_usage_lin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_dir_pools_usage_lin** | **int**|  View pool usage information of a directory, classified by storage pools in response \&quot;usage_data\&quot;. The storage pool type can be specified by query parameter \&quot;storage_pool_type\&quot;. The directory is LIN token of URI. The response \&quot;dir_usage\&quot; is total disk usage of directory, over all pools at a given storage pool level. When LIN cannot be found within result, status code 404 and error message will be returned. | 
 **id** | **str**|  | 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **storage_pool_type** | **str**| The type of the storage pool. | [optional] 

### Return type

[**ResultDirPoolsUsage**](ResultDirPoolsUsage.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_directories**
> ResultDirectoriesExtended get_result_directories(id, comp_report=comp_report, dir=dir, limit=limit, path=path, sort=sort)



This resource retrieves directory information. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
id = 'id_example' # str | 
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Limit the number of reported subdirectories. (optional)
path = 'path_example' # str | Primary directory path to report usage information, which may be specified instead of a LIN. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_result_directories(id, comp_report=comp_report, dir=dir, limit=limit, path=path, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_directories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Limit the number of reported subdirectories. | [optional] 
 **path** | **str**| Primary directory path to report usage information, which may be specified instead of a LIN. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**ResultDirectoriesExtended**](ResultDirectoriesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_directory**
> ResultDirectories get_result_directory(result_directory_id, id, comp_report=comp_report, dir=dir, limit=limit, sort=sort)



This resource retrieves directory information. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
result_directory_id = 56 # int | This resource retrieves directory information. ID in the resource path is the result set ID.
id = 'id_example' # str | 
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Limit the number of reported subdirectories. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_result_directory(result_directory_id, id, comp_report=comp_report, dir=dir, limit=limit, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_directory_id** | **int**| This resource retrieves directory information. ID in the resource path is the result set ID. | 
 **id** | **str**|  | 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Limit the number of reported subdirectories. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**ResultDirectories**](ResultDirectories.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_histogram**
> ResultHistogram get_result_histogram(id)



This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_result_histogram(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_histogram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResultHistogram**](ResultHistogram.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_histogram_stat**
> ResultHistogram get_result_histogram_stat(result_histogram_stat, id, atime_filter=atime_filter, attribute_filter=attribute_filter, comp_report=comp_report, ctime_filter=ctime_filter, directory_filter=directory_filter, disk_pool_filter=disk_pool_filter, log_size_filter=log_size_filter, node_pool_filter=node_pool_filter, path_ext_filter=path_ext_filter, phys_size_filter=phys_size_filter, tier_filter=tier_filter)



This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
result_histogram_stat = 'result_histogram_stat_example' # str | This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID.
id = 'id_example' # str | 
atime_filter = 56 # int | Filter according to file accessed time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid atime filter values may be found by performing a histogram breakout by atime and viewing the resulting key values. (optional)
attribute_filter = 'attribute_filter_example' # str | Filter according to the name of a file user attribute. (optional)
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
ctime_filter = 56 # int | Filter according to file modified time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid ctime filter values may be found by performing a histogram breakout by ctime and viewing the resulting key values. (optional)
directory_filter = 'directory_filter_example' # str | Filter according to a specific directory, which includes all of its subdirectories. (optional)
disk_pool_filter = 'disk_pool_filter_example' # str | Filter according to the name of a disk pool, which is a set of drives that represent an independent failure domain. (optional)
log_size_filter = 56 # int | Filter according to file logical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by logical size. The list of valid log_size filter values may be found by performing a histogram breakout by log_size and viewing the resulting key values. (optional)
node_pool_filter = 'node_pool_filter_example' # str | Filter according to the name of a node pool, which is a set of disk pools that belong to nodes of the same equivalence class. (optional)
path_ext_filter = 'path_ext_filter_example' # str | Filter according to the name of a single file extension. (optional)
phys_size_filter = 56 # int | Filter according to file physical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by physical size. The list of valid phys_size filter values may be found by performing a histogram breakout by phys_size and viewing the resulting key values. (optional)
tier_filter = 'tier_filter_example' # str | Filter according to the name of a storage tier, which is a user-created set of node pools. (optional)

try:
    api_response = api_instance.get_result_histogram_stat(result_histogram_stat, id, atime_filter=atime_filter, attribute_filter=attribute_filter, comp_report=comp_report, ctime_filter=ctime_filter, directory_filter=directory_filter, disk_pool_filter=disk_pool_filter, log_size_filter=log_size_filter, node_pool_filter=node_pool_filter, path_ext_filter=path_ext_filter, phys_size_filter=phys_size_filter, tier_filter=tier_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_histogram_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_histogram_stat** | **str**| This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID. | 
 **id** | **str**|  | 
 **atime_filter** | **int**| Filter according to file accessed time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid atime filter values may be found by performing a histogram breakout by atime and viewing the resulting key values. | [optional] 
 **attribute_filter** | **str**| Filter according to the name of a file user attribute. | [optional] 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **ctime_filter** | **int**| Filter according to file modified time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid ctime filter values may be found by performing a histogram breakout by ctime and viewing the resulting key values. | [optional] 
 **directory_filter** | **str**| Filter according to a specific directory, which includes all of its subdirectories. | [optional] 
 **disk_pool_filter** | **str**| Filter according to the name of a disk pool, which is a set of drives that represent an independent failure domain. | [optional] 
 **log_size_filter** | **int**| Filter according to file logical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by logical size. The list of valid log_size filter values may be found by performing a histogram breakout by log_size and viewing the resulting key values. | [optional] 
 **node_pool_filter** | **str**| Filter according to the name of a node pool, which is a set of disk pools that belong to nodes of the same equivalence class. | [optional] 
 **path_ext_filter** | **str**| Filter according to the name of a single file extension. | [optional] 
 **phys_size_filter** | **int**| Filter according to file physical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by physical size. The list of valid phys_size filter values may be found by performing a histogram breakout by phys_size and viewing the resulting key values. | [optional] 
 **tier_filter** | **str**| Filter according to the name of a storage tier, which is a user-created set of node pools. | [optional] 

### Return type

[**ResultHistogram**](ResultHistogram.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_top_dir**
> ResultTopDirs get_result_top_dir(result_top_dir_id, id, comp_report=comp_report, dir=dir, limit=limit, sort=sort, start=start)



This resource retrieves the top directories. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
result_top_dir_id = 'result_top_dir_id_example' # str | This resource retrieves the top directories. ID in the resource path is the result set ID.
id = 'id_example' # str | 
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Number of results from start index. Default value of 1000. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
start = 56 # int | Starting index for results. Default value of 0. (optional)

try:
    api_response = api_instance.get_result_top_dir(result_top_dir_id, id, comp_report=comp_report, dir=dir, limit=limit, sort=sort, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_top_dir: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_top_dir_id** | **str**| This resource retrieves the top directories. ID in the resource path is the result set ID. | 
 **id** | **str**|  | 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Number of results from start index. Default value of 1000. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **start** | **int**| Starting index for results. Default value of 0. | [optional] 

### Return type

[**ResultTopDirs**](ResultTopDirs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_top_dirs**
> ResultTopDirs get_result_top_dirs(id)



This resource retrieves the top directories. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_result_top_dirs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_top_dirs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResultTopDirs**](ResultTopDirs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_top_file**
> ResultTopFiles get_result_top_file(result_top_file_id, id, comp_report=comp_report, dir=dir, limit=limit, sort=sort, start=start)



This resource retrieves the top files. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
result_top_file_id = 'result_top_file_id_example' # str | This resource retrieves the top files. ID in the resource path is the result set ID.
id = 'id_example' # str | 
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Number of results from start index. Default value of 1000. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
start = 56 # int | Starting index for results. Default value of 0. (optional)

try:
    api_response = api_instance.get_result_top_file(result_top_file_id, id, comp_report=comp_report, dir=dir, limit=limit, sort=sort, start=start)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_top_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_top_file_id** | **str**| This resource retrieves the top files. ID in the resource path is the result set ID. | 
 **id** | **str**|  | 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Number of results from start index. Default value of 1000. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **start** | **int**| Starting index for results. Default value of 0. | [optional] 

### Return type

[**ResultTopFiles**](ResultTopFiles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_top_files**
> ResultTopFiles get_result_top_files(id)



This resource retrieves the top files. ID in the resource path is the result set ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.FsaResultsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.get_result_top_files(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FsaResultsApi->get_result_top_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResultTopFiles**](ResultTopFiles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

