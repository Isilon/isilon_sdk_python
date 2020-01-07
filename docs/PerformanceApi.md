# isi_sdk_8_2_1.PerformanceApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_performance_dataset**](PerformanceApi.md#create_performance_dataset) | **POST** /platform/7/performance/datasets | 
[**delete_performance_dataset**](PerformanceApi.md#delete_performance_dataset) | **DELETE** /platform/7/performance/datasets/{PerformanceDatasetId} | 
[**get_performance_dataset**](PerformanceApi.md#get_performance_dataset) | **GET** /platform/7/performance/datasets/{PerformanceDatasetId} | 
[**get_performance_metric**](PerformanceApi.md#get_performance_metric) | **GET** /platform/7/performance/metrics/{PerformanceMetricId} | 
[**get_performance_metrics**](PerformanceApi.md#get_performance_metrics) | **GET** /platform/7/performance/metrics | 
[**get_performance_settings**](PerformanceApi.md#get_performance_settings) | **GET** /platform/7/performance/settings | 
[**list_performance_datasets**](PerformanceApi.md#list_performance_datasets) | **GET** /platform/7/performance/datasets | 
[**update_performance_dataset**](PerformanceApi.md#update_performance_dataset) | **PUT** /platform/7/performance/datasets/{PerformanceDatasetId} | 
[**update_performance_settings**](PerformanceApi.md#update_performance_settings) | **PUT** /platform/7/performance/settings | 


# **create_performance_dataset**
> CreatePerformanceDatasetResponse create_performance_dataset(performance_dataset)



Create a new dataset.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))
performance_dataset = isi_sdk_8_2_1.PerformanceDatasetCreateParams() # PerformanceDatasetCreateParams | 

try:
    api_response = api_instance.create_performance_dataset(performance_dataset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->create_performance_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **performance_dataset** | [**PerformanceDatasetCreateParams**](PerformanceDatasetCreateParams.md)|  | 

### Return type

[**CreatePerformanceDatasetResponse**](CreatePerformanceDatasetResponse.md)

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
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))
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
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))
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
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))
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
> PerformanceMetricsExtended get_performance_metrics(sort=sort, dir=dir)



List all metrics.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_performance_metrics(sort=sort, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->get_performance_metrics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

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
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))

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
> PerformanceDatasetsExtended list_performance_datasets(sort=sort, limit=limit, dir=dir, resume=resume)



List all datasets.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_performance_datasets(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceApi->list_performance_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

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
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))
performance_dataset = isi_sdk_8_2_1.PerformanceDataset() # PerformanceDataset | 
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
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.PerformanceApi(isi_sdk_8_2_1.ApiClient(configuration))
performance_settings = isi_sdk_8_2_1.PerformanceSettingsExtended() # PerformanceSettingsExtended | 
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

