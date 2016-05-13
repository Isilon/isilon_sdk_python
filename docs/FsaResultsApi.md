# isi_sdk.FsaResultsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_result_histogram**](FsaResultsApi.md#get_result_histogram) | **GET** /platform/3/fsa/results/{Id}/histogram | 
[**get_result_histogram_stat**](FsaResultsApi.md#get_result_histogram_stat) | **GET** /platform/3/fsa/results/{Id}/histogram/{ResultHistogramStat} | 
[**get_result_top_dir**](FsaResultsApi.md#get_result_top_dir) | **GET** /platform/3/fsa/results/{Id}/top-dirs/{ResultTopDirId} | 
[**get_result_top_dirs**](FsaResultsApi.md#get_result_top_dirs) | **GET** /platform/3/fsa/results/{Id}/top-dirs | 
[**get_result_top_file**](FsaResultsApi.md#get_result_top_file) | **GET** /platform/3/fsa/results/{Id}/top-files/{ResultTopFileId} | 
[**get_result_top_files**](FsaResultsApi.md#get_result_top_files) | **GET** /platform/3/fsa/results/{Id}/top-files | 


# **get_result_histogram**
> ResultHistogram get_result_histogram(id)



This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID.

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
api_instance = isi_sdk.FsaResultsApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_result_histogram(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FsaResultsApi->get_result_histogram: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResultHistogram**](ResultHistogram.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_histogram_stat**
> ResultHistogram get_result_histogram_stat(result_histogram_stat, id, directory_filter=directory_filter, attribute_filter=attribute_filter, node_pool_filter=node_pool_filter, disk_pool_filter=disk_pool_filter, tier_filter=tier_filter, comp_report=comp_report, log_size_filter=log_size_filter, phys_size_filter=phys_size_filter, path_ext_filter=path_ext_filter, ctime_filter=ctime_filter, atime_filter=atime_filter)



This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID.

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
api_instance = isi_sdk.FsaResultsApi()
result_histogram_stat = 'result_histogram_stat_example' # str | This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID.
id = 'id_example' # str | 
directory_filter = 'directory_filter_example' # str | Filter according to a specific directory, which includes all of its subdirectories. (optional)
attribute_filter = 'attribute_filter_example' # str | Filter according to the name of a file user attribute. (optional)
node_pool_filter = 'node_pool_filter_example' # str | Filter according to the name of a node pool, which is a set of disk pools that belong to nodes of the same equivalence class. (optional)
disk_pool_filter = 'disk_pool_filter_example' # str | Filter according to the name of a disk pool, which is a set of drives that represent an independent failure domain. (optional)
tier_filter = 'tier_filter_example' # str | Filter according to the name of a storage tier, which is a user-created set of node pools. (optional)
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
log_size_filter = 56 # int | Filter according to file logical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by logical size. The list of valid log_size filter values may be found by performing a histogram breakout by log_size and viewing the resulting key values. (optional)
phys_size_filter = 56 # int | Filter according to file physical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by physical size. The list of valid phys_size filter values may be found by performing a histogram breakout by phys_size and viewing the resulting key values. (optional)
path_ext_filter = 'path_ext_filter_example' # str | Filter according to the name of a single file extension. (optional)
ctime_filter = 56 # int | Filter according to file modified time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid ctime filter values may be found by performing a histogram breakout by ctime and viewing the resulting key values. (optional)
atime_filter = 56 # int | Filter according to file accessed time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid atime filter values may be found by performing a histogram breakout by atime and viewing the resulting key values. (optional)

try: 
    api_response = api_instance.get_result_histogram_stat(result_histogram_stat, id, directory_filter=directory_filter, attribute_filter=attribute_filter, node_pool_filter=node_pool_filter, disk_pool_filter=disk_pool_filter, tier_filter=tier_filter, comp_report=comp_report, log_size_filter=log_size_filter, phys_size_filter=phys_size_filter, path_ext_filter=path_ext_filter, ctime_filter=ctime_filter, atime_filter=atime_filter)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FsaResultsApi->get_result_histogram_stat: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_histogram_stat** | **str**| This resource retrieves a histogram of file counts for an individual FSA result set. ID in the resource path is the result set ID. | 
 **id** | **str**|  | 
 **directory_filter** | **str**| Filter according to a specific directory, which includes all of its subdirectories. | [optional] 
 **attribute_filter** | **str**| Filter according to the name of a file user attribute. | [optional] 
 **node_pool_filter** | **str**| Filter according to the name of a node pool, which is a set of disk pools that belong to nodes of the same equivalence class. | [optional] 
 **disk_pool_filter** | **str**| Filter according to the name of a disk pool, which is a set of drives that represent an independent failure domain. | [optional] 
 **tier_filter** | **str**| Filter according to the name of a storage tier, which is a user-created set of node pools. | [optional] 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **log_size_filter** | **int**| Filter according to file logical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by logical size. The list of valid log_size filter values may be found by performing a histogram breakout by log_size and viewing the resulting key values. | [optional] 
 **phys_size_filter** | **int**| Filter according to file physical size, where the filter value specifies the lower bound in bytes to a set of files that have been grouped by physical size. The list of valid phys_size filter values may be found by performing a histogram breakout by phys_size and viewing the resulting key values. | [optional] 
 **path_ext_filter** | **str**| Filter according to the name of a single file extension. | [optional] 
 **ctime_filter** | **int**| Filter according to file modified time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid ctime filter values may be found by performing a histogram breakout by ctime and viewing the resulting key values. | [optional] 
 **atime_filter** | **int**| Filter according to file accessed time, where the filter value specifies a negative number of seconds representing a time before the begin time of the report. The list of valid atime filter values may be found by performing a histogram breakout by atime and viewing the resulting key values. | [optional] 

### Return type

[**ResultHistogram**](ResultHistogram.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_top_dir**
> ResultTopDirs get_result_top_dir(result_top_dir_id, id, sort=sort, start=start, limit=limit, comp_report=comp_report, dir=dir)



This resource retrieves the top directories. ID in the resource path is the result set ID.

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
api_instance = isi_sdk.FsaResultsApi()
result_top_dir_id = 'result_top_dir_id_example' # str | This resource retrieves the top directories. ID in the resource path is the result set ID.
id = 'id_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
start = 56 # int | Starting index for results. Default value of 0. (optional)
limit = 56 # int | Number of results from start index. Default value of 1000. (optional)
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.get_result_top_dir(result_top_dir_id, id, sort=sort, start=start, limit=limit, comp_report=comp_report, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FsaResultsApi->get_result_top_dir: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_top_dir_id** | **str**| This resource retrieves the top directories. ID in the resource path is the result set ID. | 
 **id** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **start** | **int**| Starting index for results. Default value of 0. | [optional] 
 **limit** | **int**| Number of results from start index. Default value of 1000. | [optional] 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**ResultTopDirs**](ResultTopDirs.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_top_dirs**
> ResultTopDirs get_result_top_dirs(id)



This resource retrieves the top directories. ID in the resource path is the result set ID.

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
api_instance = isi_sdk.FsaResultsApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_result_top_dirs(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FsaResultsApi->get_result_top_dirs: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResultTopDirs**](ResultTopDirs.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_top_file**
> ResultTopFiles get_result_top_file(result_top_file_id, id, sort=sort, start=start, limit=limit, comp_report=comp_report, dir=dir)



This resource retrieves the top files. ID in the resource path is the result set ID.

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
api_instance = isi_sdk.FsaResultsApi()
result_top_file_id = 'result_top_file_id_example' # str | This resource retrieves the top files. ID in the resource path is the result set ID.
id = 'id_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
start = 56 # int | Starting index for results. Default value of 0. (optional)
limit = 56 # int | Number of results from start index. Default value of 1000. (optional)
comp_report = 56 # int | Result set identifier for comparison of database results. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.get_result_top_file(result_top_file_id, id, sort=sort, start=start, limit=limit, comp_report=comp_report, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FsaResultsApi->get_result_top_file: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **result_top_file_id** | **str**| This resource retrieves the top files. ID in the resource path is the result set ID. | 
 **id** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **start** | **int**| Starting index for results. Default value of 0. | [optional] 
 **limit** | **int**| Number of results from start index. Default value of 1000. | [optional] 
 **comp_report** | **int**| Result set identifier for comparison of database results. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**ResultTopFiles**](ResultTopFiles.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_result_top_files**
> ResultTopFiles get_result_top_files(id)



This resource retrieves the top files. ID in the resource path is the result set ID.

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
api_instance = isi_sdk.FsaResultsApi()
id = 'id_example' # str | 

try: 
    api_response = api_instance.get_result_top_files(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FsaResultsApi->get_result_top_files: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ResultTopFiles**](ResultTopFiles.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

