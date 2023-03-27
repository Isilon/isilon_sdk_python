# isilon_sdk.v9_4_0.AvscanApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_avscan_job**](AvscanApi.md#create_avscan_job) | **POST** /platform/11/avscan/jobs | 
[**create_avscan_server**](AvscanApi.md#create_avscan_server) | **POST** /platform/11/avscan/servers | 
[**delete_avscan_job**](AvscanApi.md#delete_avscan_job) | **DELETE** /platform/11/avscan/jobs/{AvscanJobId} | 
[**delete_avscan_jobs**](AvscanApi.md#delete_avscan_jobs) | **DELETE** /platform/11/avscan/jobs | 
[**delete_avscan_server**](AvscanApi.md#delete_avscan_server) | **DELETE** /platform/11/avscan/servers/{AvscanServerId} | 
[**delete_avscan_servers**](AvscanApi.md#delete_avscan_servers) | **DELETE** /platform/11/avscan/servers | 
[**get_avscan_filter**](AvscanApi.md#get_avscan_filter) | **GET** /platform/11/avscan/filters/{AvscanFilterId} | 
[**get_avscan_filters**](AvscanApi.md#get_avscan_filters) | **GET** /platform/11/avscan/filters | 
[**get_avscan_job**](AvscanApi.md#get_avscan_job) | **GET** /platform/11/avscan/jobs/{AvscanJobId} | 
[**get_avscan_server**](AvscanApi.md#get_avscan_server) | **GET** /platform/11/avscan/servers/{AvscanServerId} | 
[**get_avscan_settings**](AvscanApi.md#get_avscan_settings) | **GET** /platform/11/avscan/settings | 
[**list_avscan_jobs**](AvscanApi.md#list_avscan_jobs) | **GET** /platform/11/avscan/jobs | 
[**list_avscan_servers**](AvscanApi.md#list_avscan_servers) | **GET** /platform/11/avscan/servers | 
[**update_avscan_filter**](AvscanApi.md#update_avscan_filter) | **PUT** /platform/11/avscan/filters/{AvscanFilterId} | 
[**update_avscan_job**](AvscanApi.md#update_avscan_job) | **PUT** /platform/11/avscan/jobs/{AvscanJobId} | 
[**update_avscan_server**](AvscanApi.md#update_avscan_server) | **PUT** /platform/11/avscan/servers/{AvscanServerId} | 
[**update_avscan_settings**](AvscanApi.md#update_avscan_settings) | **PUT** /platform/11/avscan/settings | 


# **create_avscan_job**
> CreateResponse create_avscan_job(avscan_job)



Create new antivirus jobs.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_job = isilon_sdk.v9_4_0.AvscanJobCreateParams() # AvscanJobCreateParams | 

try:
    api_response = api_instance.create_avscan_job(avscan_job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->create_avscan_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_job** | [**AvscanJobCreateParams**](AvscanJobCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_avscan_server**
> CreateResponse create_avscan_server(avscan_server)



Create new antivirus servers.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_server = isilon_sdk.v9_4_0.AvscanServerCreateParams() # AvscanServerCreateParams | 

try:
    api_response = api_instance.create_avscan_server(avscan_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->create_avscan_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_server** | [**AvscanServerCreateParams**](AvscanServerCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avscan_job**
> delete_avscan_job(avscan_job_id)



Delete an antivirus job entry.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_job_id = 'avscan_job_id_example' # str | Delete an antivirus job entry.

try:
    api_instance.delete_avscan_job(avscan_job_id)
except ApiException as e:
    print("Exception when calling AvscanApi->delete_avscan_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_job_id** | **str**| Delete an antivirus job entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avscan_jobs**
> delete_avscan_jobs()



Delete all antivirus jobs.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_instance.delete_avscan_jobs()
except ApiException as e:
    print("Exception when calling AvscanApi->delete_avscan_jobs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avscan_server**
> delete_avscan_server(avscan_server_id)



Delete an antivirus server entry.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_server_id = 'avscan_server_id_example' # str | Delete an antivirus server entry.

try:
    api_instance.delete_avscan_server(avscan_server_id)
except ApiException as e:
    print("Exception when calling AvscanApi->delete_avscan_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_server_id** | **str**| Delete an antivirus server entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avscan_servers**
> delete_avscan_servers()



Delete all antivirus servers.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_instance.delete_avscan_servers()
except ApiException as e:
    print("Exception when calling AvscanApi->delete_avscan_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avscan_filter**
> AvscanFilters get_avscan_filter(avscan_filter_id)



Retrieve one antivirus filter setting.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_filter_id = 56 # int | Retrieve one antivirus filter setting.

try:
    api_response = api_instance.get_avscan_filter(avscan_filter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->get_avscan_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_filter_id** | **int**| Retrieve one antivirus filter setting. | 

### Return type

[**AvscanFilters**](AvscanFilters.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avscan_filters**
> AvscanFiltersExtended get_avscan_filters(dir=dir, limit=limit, resume=resume, sort=sort)



List Antivirus filters for zones.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_avscan_filters(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->get_avscan_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**AvscanFiltersExtended**](AvscanFiltersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avscan_job**
> AvscanJobs get_avscan_job(avscan_job_id)



Retrieve one antivirus job entry.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_job_id = 'avscan_job_id_example' # str | Retrieve one antivirus job entry.

try:
    api_response = api_instance.get_avscan_job(avscan_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->get_avscan_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_job_id** | **str**| Retrieve one antivirus job entry. | 

### Return type

[**AvscanJobs**](AvscanJobs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avscan_server**
> AvscanServers get_avscan_server(avscan_server_id)



Retrieve one antivirus server entry.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_server_id = 'avscan_server_id_example' # str | Retrieve one antivirus server entry.

try:
    api_response = api_instance.get_avscan_server(avscan_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->get_avscan_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_server_id** | **str**| Retrieve one antivirus server entry. | 

### Return type

[**AvscanServers**](AvscanServers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_avscan_settings**
> AvscanSettings get_avscan_settings()



View Antivirus settings.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_avscan_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->get_avscan_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AvscanSettings**](AvscanSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_avscan_jobs**
> AvscanJobsExtended list_avscan_jobs(dir=dir, limit=limit, resume=resume, sort=sort)



List Antivirus jobs.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_avscan_jobs(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->list_avscan_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**AvscanJobsExtended**](AvscanJobsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_avscan_servers**
> AvscanServersExtended list_avscan_servers(dir=dir, limit=limit, resume=resume, sort=sort)



List Antivirus servers.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_avscan_servers(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AvscanApi->list_avscan_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**AvscanServersExtended**](AvscanServersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avscan_filter**
> update_avscan_filter(avscan_filter, avscan_filter_id)



Modify an antivirus filter setting.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_filter = isilon_sdk.v9_4_0.AvscanFilter() # AvscanFilter | 
avscan_filter_id = 56 # int | Modify an antivirus filter setting.

try:
    api_instance.update_avscan_filter(avscan_filter, avscan_filter_id)
except ApiException as e:
    print("Exception when calling AvscanApi->update_avscan_filter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_filter** | [**AvscanFilter**](AvscanFilter.md)|  | 
 **avscan_filter_id** | **int**| Modify an antivirus filter setting. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avscan_job**
> update_avscan_job(avscan_job, avscan_job_id)



Modify an antivirus job entry.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_job = isilon_sdk.v9_4_0.AvscanJob() # AvscanJob | 
avscan_job_id = 'avscan_job_id_example' # str | Modify an antivirus job entry.

try:
    api_instance.update_avscan_job(avscan_job, avscan_job_id)
except ApiException as e:
    print("Exception when calling AvscanApi->update_avscan_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_job** | [**AvscanJob**](AvscanJob.md)|  | 
 **avscan_job_id** | **str**| Modify an antivirus job entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avscan_server**
> update_avscan_server(avscan_server, avscan_server_id)



Modify an antivirus server entry.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_server = isilon_sdk.v9_4_0.AvscanServer() # AvscanServer | 
avscan_server_id = 'avscan_server_id_example' # str | Modify an antivirus server entry.

try:
    api_instance.update_avscan_server(avscan_server, avscan_server_id)
except ApiException as e:
    print("Exception when calling AvscanApi->update_avscan_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_server** | [**AvscanServer**](AvscanServer.md)|  | 
 **avscan_server_id** | **str**| Modify an antivirus server entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_avscan_settings**
> update_avscan_settings(avscan_settings)



Modify Antivirus settings.

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
api_instance = isilon_sdk.v9_4_0.AvscanApi(isilon_sdk.v9_4_0.ApiClient(configuration))
avscan_settings = isilon_sdk.v9_4_0.AvscanSettingsSettings() # AvscanSettingsSettings | 

try:
    api_instance.update_avscan_settings(avscan_settings)
except ApiException as e:
    print("Exception when calling AvscanApi->update_avscan_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **avscan_settings** | [**AvscanSettingsSettings**](AvscanSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

