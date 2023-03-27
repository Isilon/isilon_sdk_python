# isilon_sdk.v9_5_0.PerformanceApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_performance_dataset**](PerformanceApi.md#create_performance_dataset) | **POST** /platform/12/performance/datasets | 
[**delete_datasets_dataset_workloads_workload_limit**](PerformanceApi.md#delete_datasets_dataset_workloads_workload_limit) | **DELETE** /platform/16/performance/datasets/{Dataset}/workloads/{Workload}/limits/{DatasetsDatasetWorkloadsWorkloadLimitId} | 
[**delete_performance_dataset**](PerformanceApi.md#delete_performance_dataset) | **DELETE** /platform/12/performance/datasets/{PerformanceDatasetId} | 
[**get_performance_dataset**](PerformanceApi.md#get_performance_dataset) | **GET** /platform/12/performance/datasets/{PerformanceDatasetId} | 
[**get_performance_metric**](PerformanceApi.md#get_performance_metric) | **GET** /platform/12/performance/metrics/{PerformanceMetricId} | 
[**get_performance_metrics**](PerformanceApi.md#get_performance_metrics) | **GET** /platform/12/performance/metrics | 
[**get_performance_settings**](PerformanceApi.md#get_performance_settings) | **GET** /platform/16/performance/settings | 
[**list_performance_datasets**](PerformanceApi.md#list_performance_datasets) | **GET** /platform/12/performance/datasets | 
[**update_performance_dataset**](PerformanceApi.md#update_performance_dataset) | **PUT** /platform/12/performance/datasets/{PerformanceDatasetId} | 
[**update_performance_settings**](PerformanceApi.md#update_performance_settings) | **PUT** /platform/16/performance/settings | 


# **create_performance_dataset**
> CreatePerformanceDatasetResponse create_performance_dataset(performance_dataset, force=force)



Create a new dataset.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
performance_dataset = isilon_sdk.v9_5_0.PerformanceDatasetCreateParams() # PerformanceDatasetCreateParams | 
force = true # bool | For use by support only. (optional)

try:
    api_response = api_instance.create_performance_dataset(performance_dataset, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->create_performance_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_dataset** | [**PerformanceDatasetCreateParams**](PerformanceDatasetCreateParams.md)|  | 
 **force** | **bool**| For use by support only. | [optional] 

### Return type

[**CreatePerformanceDatasetResponse**](CreatePerformanceDatasetResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datasets_dataset_workloads_workload_limit**
> delete_datasets_dataset_workloads_workload_limit(datasets_dataset_workloads_workload_limit_id, dataset, workload)



Delete the workload limit.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
datasets_dataset_workloads_workload_limit_id = 'datasets_dataset_workloads_workload_limit_id_example' # str | Delete the workload limit.
dataset = 'dataset_example' # str | 
workload = 'workload_example' # str | 

try:
    api_instance.delete_datasets_dataset_workloads_workload_limit(datasets_dataset_workloads_workload_limit_id, dataset, workload)
except ApiException as e:
    print("Exception when calling PerformanceApi->delete_datasets_dataset_workloads_workload_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasets_dataset_workloads_workload_limit_id** | **str**| Delete the workload limit. | 
 **dataset** | **str**|  | 
 **workload** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_performance_dataset**
> delete_performance_dataset(performance_dataset_id)



Delete the performance dataset.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
performance_dataset_id = 'performance_dataset_id_example' # str | Delete the performance dataset.

try:
    api_instance.delete_performance_dataset(performance_dataset_id)
except ApiException as e:
    print("Exception when calling PerformanceApi->delete_performance_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_dataset_id** | **str**| Delete the performance dataset. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_dataset**
> PerformanceDatasets get_performance_dataset(performance_dataset_id)



Retrieve the performance dataset.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
performance_dataset_id = 'performance_dataset_id_example' # str | Retrieve the performance dataset.

try:
    api_response = api_instance.get_performance_dataset(performance_dataset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->get_performance_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_dataset_id** | **str**| Retrieve the performance dataset. | 

### Return type

[**PerformanceDatasets**](PerformanceDatasets.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metric**
> PerformanceMetrics get_performance_metric(performance_metric_id)



View a single performance metric.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
performance_metric_id = 'performance_metric_id_example' # str | View a single performance metric.

try:
    api_response = api_instance.get_performance_metric(performance_metric_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->get_performance_metric: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_metric_id** | **str**| View a single performance metric. | 

### Return type

[**PerformanceMetrics**](PerformanceMetrics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_metrics**
> PerformanceMetricsExtended get_performance_metrics(dir=dir, sort=sort)



List all metrics.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_performance_metrics(dir=dir, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->get_performance_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**PerformanceMetricsExtended**](PerformanceMetricsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_performance_settings**
> PerformanceSettings get_performance_settings()



List all performance settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_performance_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->get_performance_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PerformanceSettings**](PerformanceSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_performance_datasets**
> PerformanceDatasetsExtended list_performance_datasets(dir=dir, limit=limit, resume=resume, sort=sort)



List all datasets.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_performance_datasets(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->list_performance_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**PerformanceDatasetsExtended**](PerformanceDatasetsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_dataset**
> update_performance_dataset(performance_dataset, performance_dataset_id)



Modify the name of the performance dataset.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
performance_dataset = isilon_sdk.v9_5_0.PerformanceDataset() # PerformanceDataset | 
performance_dataset_id = 'performance_dataset_id_example' # str | Modify the name of the performance dataset.

try:
    api_instance.update_performance_dataset(performance_dataset, performance_dataset_id)
except ApiException as e:
    print("Exception when calling PerformanceApi->update_performance_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_dataset** | [**PerformanceDataset**](PerformanceDataset.md)|  | 
 **performance_dataset_id** | **str**| Modify the name of the performance dataset. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_performance_settings**
> update_performance_settings(performance_settings, force=force)



Configure performance settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.PerformanceApi(isilon_sdk.v9_5_0.ApiClient(configuration))
performance_settings = isilon_sdk.v9_5_0.PerformanceSettingsExtended() # PerformanceSettingsExtended | 
force = true # bool | Allow modification of settings outside of recommended limits (optional)

try:
    api_instance.update_performance_settings(performance_settings, force=force)
except ApiException as e:
    print("Exception when calling PerformanceApi->update_performance_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_settings** | [**PerformanceSettingsExtended**](PerformanceSettingsExtended.md)|  | 
 **force** | **bool**| Allow modification of settings outside of recommended limits | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

