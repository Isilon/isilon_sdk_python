# isi_sdk_9_1_0.JobApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_job**](JobApi.md#create_job_job) | **POST** /platform/10/job/jobs | 
[**create_job_policy**](JobApi.md#create_job_policy) | **POST** /platform/1/job/policies | 
[**delete_job_policy**](JobApi.md#delete_job_policy) | **DELETE** /platform/1/job/policies/{JobPolicyId} | 
[**get_job_events**](JobApi.md#get_job_events) | **GET** /platform/3/job/events | 
[**get_job_job**](JobApi.md#get_job_job) | **GET** /platform/10/job/jobs/{JobJobId} | 
[**get_job_job_summary**](JobApi.md#get_job_job_summary) | **GET** /platform/7/job/job-summary | 
[**get_job_policy**](JobApi.md#get_job_policy) | **GET** /platform/1/job/policies/{JobPolicyId} | 
[**get_job_recent**](JobApi.md#get_job_recent) | **GET** /platform/3/job/recent | 
[**get_job_reports**](JobApi.md#get_job_reports) | **GET** /platform/7/job/reports | 
[**get_job_statistics**](JobApi.md#get_job_statistics) | **GET** /platform/1/job/statistics | 
[**get_job_type**](JobApi.md#get_job_type) | **GET** /platform/1/job/types/{JobTypeId} | 
[**get_job_types**](JobApi.md#get_job_types) | **GET** /platform/1/job/types | 
[**list_job_jobs**](JobApi.md#list_job_jobs) | **GET** /platform/10/job/jobs | 
[**list_job_policies**](JobApi.md#list_job_policies) | **GET** /platform/1/job/policies | 
[**update_job_job**](JobApi.md#update_job_job) | **PUT** /platform/10/job/jobs/{JobJobId} | 
[**update_job_policy**](JobApi.md#update_job_policy) | **PUT** /platform/1/job/policies/{JobPolicyId} | 
[**update_job_type**](JobApi.md#update_job_type) | **PUT** /platform/1/job/types/{JobTypeId} | 


# **create_job_job**
> CreateJobJobResponse create_job_job(job_job)



Queue a new instance of a job type.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_job = isi_sdk_9_1_0.JobJobCreateParams() # JobJobCreateParams | 

try:
    api_response = api_instance.create_job_job(job_job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->create_job_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_job** | [**JobJobCreateParams**](JobJobCreateParams.md)|  | 

### Return type

[**CreateJobJobResponse**](CreateJobJobResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job_policy**
> CreateResponse create_job_policy(job_policy)



Create a new job impact policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_policy = isi_sdk_9_1_0.JobPolicyCreateParams() # JobPolicyCreateParams | 

try:
    api_response = api_instance.create_job_policy(job_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->create_job_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_policy** | [**JobPolicyCreateParams**](JobPolicyCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_policy**
> delete_job_policy(job_policy_id)



Delete a job impact policy.  System policies may not be deleted.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_policy_id = 'job_policy_id_example' # str | Delete a job impact policy.  System policies may not be deleted.

try:
    api_instance.delete_job_policy(job_policy_id)
except ApiException as e:
    print("Exception when calling JobApi->delete_job_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_policy_id** | **str**| Delete a job impact policy.  System policies may not be deleted. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_events**
> JobEvents get_job_events(begin=begin, end=end, job_id=job_id, resume=resume, job_type=job_type, timeout_ms=timeout_ms, state=state, ended_jobs_only=ended_jobs_only, limit=limit, key=key)



List job events.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
begin = 56 # int | Restrict the query to events at or after the given time, in seconds since the Epoch. (optional)
end = 56 # int | Restrict the query to events before the given time, in seconds since the Epoch. (optional)
job_id = 56 # int | Restrict the query to the given job ID. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
job_type = 'job_type_example' # str | Restrict the query to the given job type. (optional)
timeout_ms = 56 # int | Query timeout in milliseconds. The default is 10000 ms. (optional)
state = 'state_example' # str | Restrict the query to events containing the given state. This parameter cannot be used with ended_jobs_only (optional)
ended_jobs_only = true # bool | Request all jobs that ended. This parameter cannot be used with the 'state' parameter. Ended states are 'cancelled_user', 'cancelled_system', 'failed' or 'succeeded' (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
key = 'key_example' # str | Restrict the query to the given key name. (optional)

try:
    api_response = api_instance.get_job_events(begin=begin, end=end, job_id=job_id, resume=resume, job_type=job_type, timeout_ms=timeout_ms, state=state, ended_jobs_only=ended_jobs_only, limit=limit, key=key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Restrict the query to events at or after the given time, in seconds since the Epoch. | [optional] 
 **end** | **int**| Restrict the query to events before the given time, in seconds since the Epoch. | [optional] 
 **job_id** | **int**| Restrict the query to the given job ID. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **job_type** | **str**| Restrict the query to the given job type. | [optional] 
 **timeout_ms** | **int**| Query timeout in milliseconds. The default is 10000 ms. | [optional] 
 **state** | **str**| Restrict the query to events containing the given state. This parameter cannot be used with ended_jobs_only | [optional] 
 **ended_jobs_only** | **bool**| Request all jobs that ended. This parameter cannot be used with the &#39;state&#39; parameter. Ended states are &#39;cancelled_user&#39;, &#39;cancelled_system&#39;, &#39;failed&#39; or &#39;succeeded&#39; | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **key** | **str**| Restrict the query to the given key name. | [optional] 

### Return type

[**JobEvents**](JobEvents.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_job**
> JobJobs get_job_job(job_job_id)



View a single job instance.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_job_id = 'job_job_id_example' # str | View a single job instance.

try:
    api_response = api_instance.get_job_job(job_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_job_id** | **str**| View a single job instance. | 

### Return type

[**JobJobs**](JobJobs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_job_summary**
> JobJobSummary get_job_job_summary()



View job engine status.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))

try:
    api_response = api_instance.get_job_job_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_job_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobJobSummary**](JobJobSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_policy**
> JobPolicies get_job_policy(job_policy_id)



View a single job impact policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_policy_id = 'job_policy_id_example' # str | View a single job impact policy.

try:
    api_response = api_instance.get_job_policy(job_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_policy_id** | **str**| View a single job impact policy. | 

### Return type

[**JobPolicies**](JobPolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_recent**
> JobRecent get_job_recent(timeout_ms=timeout_ms, limit=limit)



List recently completed jobs.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
timeout_ms = 56 # int | Query timeout in milliseconds. The default is 10000 ms. (optional)
limit = 56 # int | Max number of recent jobs to return. The default is 8, the max is 100. (optional)

try:
    api_response = api_instance.get_job_recent(timeout_ms=timeout_ms, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_recent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout_ms** | **int**| Query timeout in milliseconds. The default is 10000 ms. | [optional] 
 **limit** | **int**| Max number of recent jobs to return. The default is 8, the max is 100. | [optional] 

### Return type

[**JobRecent**](JobRecent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_reports**
> JobReports get_job_reports(begin=begin, end=end, job_id=job_id, resume=resume, job_type=job_type, timeout_ms=timeout_ms, limit=limit, key=key, last_phase_only=last_phase_only, verbose=verbose)



List job reports.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
begin = 56 # int | Restrict the query to reports at or after the given time, in seconds since the Epoch. (optional)
end = 56 # int | Restrict the query to reports before the given time, in seconds since the Epoch. (optional)
job_id = 56 # int | Restrict the query to the given job ID. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
job_type = 'job_type_example' # str | Restrict the query to the given job type. (optional)
timeout_ms = 56 # int | Query timeout in milliseconds. The default is 10000 ms. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
key = 'key_example' # str | Restrict the query to the given report key. (optional)
last_phase_only = true # bool | if set, the query will return the last reported phase only. (optional)
verbose = true # bool | Display more detailed information, including job engine framework statistics. (optional)

try:
    api_response = api_instance.get_job_reports(begin=begin, end=end, job_id=job_id, resume=resume, job_type=job_type, timeout_ms=timeout_ms, limit=limit, key=key, last_phase_only=last_phase_only, verbose=verbose)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Restrict the query to reports at or after the given time, in seconds since the Epoch. | [optional] 
 **end** | **int**| Restrict the query to reports before the given time, in seconds since the Epoch. | [optional] 
 **job_id** | **int**| Restrict the query to the given job ID. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **job_type** | **str**| Restrict the query to the given job type. | [optional] 
 **timeout_ms** | **int**| Query timeout in milliseconds. The default is 10000 ms. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **key** | **str**| Restrict the query to the given report key. | [optional] 
 **last_phase_only** | **bool**| if set, the query will return the last reported phase only. | [optional] 
 **verbose** | **bool**| Display more detailed information, including job engine framework statistics. | [optional] 

### Return type

[**JobReports**](JobReports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_statistics**
> JobStatistics get_job_statistics(devid=devid, job_id=job_id)



View job engine statistics.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
devid = 56 # int | Restrict the query to the given node. (optional)
job_id = 56 # int | Restrict the query to the given job ID. (optional)

try:
    api_response = api_instance.get_job_statistics(devid=devid, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **devid** | **int**| Restrict the query to the given node. | [optional] 
 **job_id** | **int**| Restrict the query to the given job ID. | [optional] 

### Return type

[**JobStatistics**](JobStatistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_type**
> JobTypes get_job_type(job_type_id)



Retrieve job type information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_type_id = 'job_type_id_example' # str | Retrieve job type information.

try:
    api_response = api_instance.get_job_type(job_type_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type_id** | **str**| Retrieve job type information. | 

### Return type

[**JobTypes**](JobTypes.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_types**
> JobTypesExtended get_job_types(sort=sort, show_all=show_all, dir=dir)



List job types.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
show_all = true # bool | Whether to show all job types, including hidden ones.  Defaults to false. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_job_types(sort=sort, show_all=show_all, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->get_job_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **show_all** | **bool**| Whether to show all job types, including hidden ones.  Defaults to false. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**JobTypesExtended**](JobTypesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_jobs**
> JobJobsExtended list_job_jobs(sort=sort, resume=resume, batch=batch, state=state, limit=limit, dir=dir)



List running and paused jobs.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
batch = true # bool | If true, other arguments are ignored, and the query will return all results, unsorted, as quickly as possible. (optional)
state = 'state_example' # str | Limit the results to jobs in the specified state. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_job_jobs(sort=sort, resume=resume, batch=batch, state=state, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->list_job_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **batch** | **bool**| If true, other arguments are ignored, and the query will return all results, unsorted, as quickly as possible. | [optional] 
 **state** | **str**| Limit the results to jobs in the specified state. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**JobJobsExtended**](JobJobsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_job_policies**
> JobPoliciesExtended list_job_policies(sort=sort, limit=limit, dir=dir, resume=resume)



List job impact policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_job_policies(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobApi->list_job_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**JobPoliciesExtended**](JobPoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_job**
> update_job_job(job_job, job_job_id)



Modify a running or paused job instance.  All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_job = isi_sdk_9_1_0.JobJob() # JobJob | 
job_job_id = 'job_job_id_example' # str | Modify a running or paused job instance.  All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_job_job(job_job, job_job_id)
except ApiException as e:
    print("Exception when calling JobApi->update_job_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_job** | [**JobJob**](JobJob.md)|  | 
 **job_job_id** | **str**| Modify a running or paused job instance.  All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_policy**
> update_job_policy(job_policy, job_policy_id)



Modify a job impact policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_policy = isi_sdk_9_1_0.JobPolicy() # JobPolicy | 
job_policy_id = 'job_policy_id_example' # str | Modify a job impact policy.

try:
    api_instance.update_job_policy(job_policy, job_policy_id)
except ApiException as e:
    print("Exception when calling JobApi->update_job_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_policy** | [**JobPolicy**](JobPolicy.md)|  | 
 **job_policy_id** | **str**| Modify a job impact policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_type**
> update_job_type(job_type, job_type_id)



Modify the job type.  All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.JobApi(isi_sdk_9_1_0.ApiClient(configuration))
job_type = isi_sdk_9_1_0.JobType() # JobType | 
job_type_id = 'job_type_id_example' # str | Modify the job type.  All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_job_type(job_type, job_type_id)
except ApiException as e:
    print("Exception when calling JobApi->update_job_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_type** | [**JobType**](JobType.md)|  | 
 **job_type_id** | **str**| Modify the job type.  All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

