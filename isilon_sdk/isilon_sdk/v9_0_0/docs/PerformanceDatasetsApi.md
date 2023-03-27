# isilon_sdk.v9_0_0.PerformanceDatasetsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset_filter**](PerformanceDatasetsApi.md#create_dataset_filter) | **POST** /platform/10/performance/datasets/{Dataset}/filters | 
[**create_dataset_workload**](PerformanceDatasetsApi.md#create_dataset_workload) | **POST** /platform/10/performance/datasets/{Dataset}/workloads | 
[**delete_dataset_filter**](PerformanceDatasetsApi.md#delete_dataset_filter) | **DELETE** /platform/10/performance/datasets/{Dataset}/filters/{DatasetFilterId} | 
[**delete_dataset_filters**](PerformanceDatasetsApi.md#delete_dataset_filters) | **DELETE** /platform/10/performance/datasets/{Dataset}/filters | 
[**delete_dataset_workload**](PerformanceDatasetsApi.md#delete_dataset_workload) | **DELETE** /platform/10/performance/datasets/{Dataset}/workloads/{DatasetWorkloadId} | 
[**delete_dataset_workloads**](PerformanceDatasetsApi.md#delete_dataset_workloads) | **DELETE** /platform/10/performance/datasets/{Dataset}/workloads | 
[**get_dataset_filter**](PerformanceDatasetsApi.md#get_dataset_filter) | **GET** /platform/10/performance/datasets/{Dataset}/filters/{DatasetFilterId} | 
[**get_dataset_workload**](PerformanceDatasetsApi.md#get_dataset_workload) | **GET** /platform/10/performance/datasets/{Dataset}/workloads/{DatasetWorkloadId} | 
[**list_dataset_filters**](PerformanceDatasetsApi.md#list_dataset_filters) | **GET** /platform/10/performance/datasets/{Dataset}/filters | 
[**list_dataset_workloads**](PerformanceDatasetsApi.md#list_dataset_workloads) | **GET** /platform/10/performance/datasets/{Dataset}/workloads | 
[**update_dataset_filter**](PerformanceDatasetsApi.md#update_dataset_filter) | **PUT** /platform/10/performance/datasets/{Dataset}/filters/{DatasetFilterId} | 
[**update_dataset_workload**](PerformanceDatasetsApi.md#update_dataset_workload) | **PUT** /platform/10/performance/datasets/{Dataset}/workloads/{DatasetWorkloadId} | 


# **create_dataset_filter**
> CreateDatasetFilterResponse create_dataset_filter(dataset_filter, dataset, force=force)



Create a new filter.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset_filter = isilon_sdk.v9_0_0.DatasetFilterCreateParams() # DatasetFilterCreateParams | 
dataset = 'dataset_example' # str | 
force = true # bool | For use by support only. (optional)

try:
    api_response = api_instance.create_dataset_filter(dataset_filter, dataset, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->create_dataset_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_filter** | [**DatasetFilterCreateParams**](DatasetFilterCreateParams.md)|  | 
 **dataset** | **str**|  | 
 **force** | **bool**| For use by support only. | [optional] 

### Return type

[**CreateDatasetFilterResponse**](CreateDatasetFilterResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset_workload**
> CreateDatasetWorkloadResponse create_dataset_workload(dataset_workload, dataset, force=force)



Create a new workload.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset_workload = isilon_sdk.v9_0_0.DatasetWorkloadCreateParams() # DatasetWorkloadCreateParams | 
dataset = 'dataset_example' # str | 
force = true # bool | For use by support only. (optional)

try:
    api_response = api_instance.create_dataset_workload(dataset_workload, dataset, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->create_dataset_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_workload** | [**DatasetWorkloadCreateParams**](DatasetWorkloadCreateParams.md)|  | 
 **dataset** | **str**|  | 
 **force** | **bool**| For use by support only. | [optional] 

### Return type

[**CreateDatasetWorkloadResponse**](CreateDatasetWorkloadResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_filter**
> delete_dataset_filter(dataset_filter_id, dataset)



Delete the filter.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset_filter_id = 'dataset_filter_id_example' # str | Delete the filter.
dataset = 'dataset_example' # str | 

try:
    api_instance.delete_dataset_filter(dataset_filter_id, dataset)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->delete_dataset_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_filter_id** | **str**| Delete the filter. | 
 **dataset** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_filters**
> delete_dataset_filters(dataset)



Delete all filters associated with the dataset.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset = 'dataset_example' # str | 

try:
    api_instance.delete_dataset_filters(dataset)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->delete_dataset_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_workload**
> delete_dataset_workload(dataset_workload_id, dataset)



Delete the workload.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset_workload_id = 'dataset_workload_id_example' # str | Delete the workload.
dataset = 'dataset_example' # str | 

try:
    api_instance.delete_dataset_workload(dataset_workload_id, dataset)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->delete_dataset_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_workload_id** | **str**| Delete the workload. | 
 **dataset** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_workloads**
> delete_dataset_workloads(dataset)



Delete all workloads associated with the dataset.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset = 'dataset_example' # str | 

try:
    api_instance.delete_dataset_workloads(dataset)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->delete_dataset_workloads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_filter**
> DatasetFilters get_dataset_filter(dataset_filter_id, dataset)



Retrieve the filter.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset_filter_id = 'dataset_filter_id_example' # str | Retrieve the filter.
dataset = 'dataset_example' # str | 

try:
    api_response = api_instance.get_dataset_filter(dataset_filter_id, dataset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->get_dataset_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_filter_id** | **str**| Retrieve the filter. | 
 **dataset** | **str**|  | 

### Return type

[**DatasetFilters**](DatasetFilters.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_workload**
> DatasetWorkloads get_dataset_workload(dataset_workload_id, dataset)



Retrieve the workload.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset_workload_id = 'dataset_workload_id_example' # str | Retrieve the workload.
dataset = 'dataset_example' # str | 

try:
    api_response = api_instance.get_dataset_workload(dataset_workload_id, dataset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->get_dataset_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_workload_id** | **str**| Retrieve the workload. | 
 **dataset** | **str**|  | 

### Return type

[**DatasetWorkloads**](DatasetWorkloads.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dataset_filters**
> DatasetFiltersExtended list_dataset_filters(dataset, dir=dir, limit=limit, resume=resume, sort=sort)



List all filters.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset = 'dataset_example' # str | 
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_dataset_filters(dataset, dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->list_dataset_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**|  | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**DatasetFiltersExtended**](DatasetFiltersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dataset_workloads**
> DatasetWorkloadsExtended list_dataset_workloads(dataset, dir=dir, limit=limit, resume=resume, sort=sort)



List all workloads.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset = 'dataset_example' # str | 
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_dataset_workloads(dataset, dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->list_dataset_workloads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | **str**|  | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**DatasetWorkloadsExtended**](DatasetWorkloadsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_filter**
> update_dataset_filter(dataset_filter, dataset_filter_id, dataset)



Modify the filter.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset_filter = isilon_sdk.v9_0_0.DatasetFilter() # DatasetFilter | 
dataset_filter_id = 'dataset_filter_id_example' # str | Modify the filter.
dataset = 'dataset_example' # str | 

try:
    api_instance.update_dataset_filter(dataset_filter, dataset_filter_id, dataset)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->update_dataset_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_filter** | [**DatasetFilter**](DatasetFilter.md)|  | 
 **dataset_filter_id** | **str**| Modify the filter. | 
 **dataset** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_workload**
> update_dataset_workload(dataset_workload, dataset_workload_id, dataset)



Modify the workload.

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
api_instance = isilon_sdk.v9_0_0.PerformanceDatasetsApi(isilon_sdk.v9_0_0.ApiClient(configuration))
dataset_workload = isilon_sdk.v9_0_0.DatasetWorkload() # DatasetWorkload | 
dataset_workload_id = 'dataset_workload_id_example' # str | Modify the workload.
dataset = 'dataset_example' # str | 

try:
    api_instance.update_dataset_workload(dataset_workload, dataset_workload_id, dataset)
except ApiException as e:
    print("Exception when calling PerformanceDatasetsApi->update_dataset_workload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_workload** | [**DatasetWorkload**](DatasetWorkload.md)|  | 
 **dataset_workload_id** | **str**| Modify the workload. | 
 **dataset** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

