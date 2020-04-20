# isi_sdk_7_2.CloudApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_account**](CloudApi.md#create_cloud_account) | **POST** /platform/1/cloud/accounts | 
[**create_cloud_job**](CloudApi.md#create_cloud_job) | **POST** /platform/1/cloud/jobs | 
[**create_cloud_pool**](CloudApi.md#create_cloud_pool) | **POST** /platform/1/cloud/pools | 
[**create_settings_encryption_key_item**](CloudApi.md#create_settings_encryption_key_item) | **POST** /platform/1/cloud/settings/encryption_key | 
[**delete_cloud_account**](CloudApi.md#delete_cloud_account) | **DELETE** /platform/1/cloud/accounts/{CloudAccountId} | 
[**delete_cloud_pool**](CloudApi.md#delete_cloud_pool) | **DELETE** /platform/1/cloud/pools/{CloudPoolId} | 
[**get_cloud_account**](CloudApi.md#get_cloud_account) | **GET** /platform/1/cloud/accounts/{CloudAccountId} | 
[**get_cloud_job**](CloudApi.md#get_cloud_job) | **GET** /platform/1/cloud/jobs/{CloudJobId} | 
[**get_cloud_jobs_file**](CloudApi.md#get_cloud_jobs_file) | **GET** /platform/1/cloud/jobs-files/{CloudJobsFileId} | 
[**get_cloud_pool**](CloudApi.md#get_cloud_pool) | **GET** /platform/1/cloud/pools/{CloudPoolId} | 
[**get_cloud_settings**](CloudApi.md#get_cloud_settings) | **GET** /platform/1/cloud/settings | 
[**list_cloud_accounts**](CloudApi.md#list_cloud_accounts) | **GET** /platform/1/cloud/accounts | 
[**list_cloud_jobs**](CloudApi.md#list_cloud_jobs) | **GET** /platform/1/cloud/jobs | 
[**list_cloud_pools**](CloudApi.md#list_cloud_pools) | **GET** /platform/1/cloud/pools | 
[**update_cloud_account**](CloudApi.md#update_cloud_account) | **PUT** /platform/1/cloud/accounts/{CloudAccountId} | 
[**update_cloud_job**](CloudApi.md#update_cloud_job) | **PUT** /platform/1/cloud/jobs/{CloudJobId} | 
[**update_cloud_pool**](CloudApi.md#update_cloud_pool) | **PUT** /platform/1/cloud/pools/{CloudPoolId} | 
[**update_cloud_settings**](CloudApi.md#update_cloud_settings) | **PUT** /platform/1/cloud/settings | 


# **create_cloud_account**
> CreateCloudAccountResponse create_cloud_account(cloud_account)



Create a new account.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_account = isi_sdk_7_2.CloudAccountCreateParams() # CloudAccountCreateParams | 

try:
    api_response = api_instance.create_cloud_account(cloud_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account** | [**CloudAccountCreateParams**](CloudAccountCreateParams.md)|  | 

### Return type

[**CreateCloudAccountResponse**](CreateCloudAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_job**
> CreateCloudJobResponse create_cloud_job(cloud_job)



Create a new job.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_job = isi_sdk_7_2.CloudJobCreateParams() # CloudJobCreateParams | 

try:
    api_response = api_instance.create_cloud_job(cloud_job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_job** | [**CloudJobCreateParams**](CloudJobCreateParams.md)|  | 

### Return type

[**CreateCloudJobResponse**](CreateCloudJobResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_pool**
> CreateCloudPoolResponse create_cloud_pool(cloud_pool)



Create a new pool.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_pool = isi_sdk_7_2.CloudPoolCreateParams() # CloudPoolCreateParams | 

try:
    api_response = api_instance.create_cloud_pool(cloud_pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool** | [**CloudPoolCreateParams**](CloudPoolCreateParams.md)|  | 

### Return type

[**CreateCloudPoolResponse**](CreateCloudPoolResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_encryption_key_item**
> Empty create_settings_encryption_key_item()



Regenerate master encryption key.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.create_settings_encryption_key_item()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_settings_encryption_key_item: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_account**
> delete_cloud_account(cloud_account_id)



Delete cloud account.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_account_id = 'cloud_account_id_example' # str | Delete cloud account.

try:
    api_instance.delete_cloud_account(cloud_account_id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account_id** | **str**| Delete cloud account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_pool**
> delete_cloud_pool(cloud_pool_id)



Delete a cloud pool.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Delete a cloud pool.

try:
    api_instance.delete_cloud_pool(cloud_pool_id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Delete a cloud pool. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_account**
> CloudAccounts get_cloud_account(cloud_account_id)



Retrieve cloud account information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_account_id = 'cloud_account_id_example' # str | Retrieve cloud account information.

try:
    api_response = api_instance.get_cloud_account(cloud_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account_id** | **str**| Retrieve cloud account information. | 

### Return type

[**CloudAccounts**](CloudAccounts.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_job**
> CloudJobs get_cloud_job(cloud_job_id)



Retrieve cloudpool job information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_job_id = 'cloud_job_id_example' # str | Retrieve cloudpool job information.

try:
    api_response = api_instance.get_cloud_job(cloud_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_job_id** | **str**| Retrieve cloudpool job information. | 

### Return type

[**CloudJobs**](CloudJobs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_jobs_file**
> CloudJobsFiles get_cloud_jobs_file(cloud_jobs_file_id)



Retrieve files associated with a cloudpool job.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_jobs_file_id = 'cloud_jobs_file_id_example' # str | Retrieve files associated with a cloudpool job.

try:
    api_response = api_instance.get_cloud_jobs_file(cloud_jobs_file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_jobs_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_jobs_file_id** | **str**| Retrieve files associated with a cloudpool job. | 

### Return type

[**CloudJobsFiles**](CloudJobsFiles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_pool**
> CloudPools get_cloud_pool(cloud_pool_id)



Retrieve cloud pool information

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Retrieve cloud pool information

try:
    api_response = api_instance.get_cloud_pool(cloud_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Retrieve cloud pool information | 

### Return type

[**CloudPools**](CloudPools.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_settings**
> CloudSettings get_cloud_settings()



List all cloud settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_cloud_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudSettings**](CloudSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_accounts**
> CloudAccountsExtended list_cloud_accounts(sort=sort, limit=limit, dir=dir)



List all accounts.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_cloud_accounts(sort=sort, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**CloudAccountsExtended**](CloudAccountsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_jobs**
> CloudJobsExtended list_cloud_jobs(sort=sort, limit=limit, dir=dir)



List all cloudpools jobs.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_cloud_jobs(sort=sort, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**CloudJobsExtended**](CloudJobsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_pools**
> CloudPoolsExtended list_cloud_pools(sort=sort, limit=limit, dir=dir)



List all pools.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_cloud_pools(sort=sort, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**CloudPoolsExtended**](CloudPoolsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_account**
> update_cloud_account(cloud_account, cloud_account_id)



Modify cloud account.  All fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_account = isi_sdk_7_2.CloudAccount() # CloudAccount | 
cloud_account_id = 'cloud_account_id_example' # str | Modify cloud account.  All fields are optional, but one or more must be supplied.

try:
    api_instance.update_cloud_account(cloud_account, cloud_account_id)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account** | [**CloudAccount**](CloudAccount.md)|  | 
 **cloud_account_id** | **str**| Modify cloud account.  All fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_job**
> update_cloud_job(cloud_job, cloud_job_id)



Modify a running cloudpool job.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_job = isi_sdk_7_2.CloudJob() # CloudJob | 
cloud_job_id = 'cloud_job_id_example' # str | Modify a running cloudpool job.

try:
    api_instance.update_cloud_job(cloud_job, cloud_job_id)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_job** | [**CloudJob**](CloudJob.md)|  | 
 **cloud_job_id** | **str**| Modify a running cloudpool job. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_pool**
> update_cloud_pool(cloud_pool, cloud_pool_id)



Modify a cloud pool.  All fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_pool = isi_sdk_7_2.CloudPool() # CloudPool | 
cloud_pool_id = 'cloud_pool_id_example' # str | Modify a cloud pool.  All fields are optional, but one or more must be supplied.

try:
    api_instance.update_cloud_pool(cloud_pool, cloud_pool_id)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool** | [**CloudPool**](CloudPool.md)|  | 
 **cloud_pool_id** | **str**| Modify a cloud pool.  All fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_settings**
> update_cloud_settings(cloud_settings)



Modify one or more settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.CloudApi(isi_sdk_7_2.ApiClient(configuration))
cloud_settings = isi_sdk_7_2.CloudSettingsSettings() # CloudSettingsSettings | 

try:
    api_instance.update_cloud_settings(cloud_settings)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_settings** | [**CloudSettingsSettings**](CloudSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

