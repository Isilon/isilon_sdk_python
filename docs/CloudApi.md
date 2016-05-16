# isi_sdk.CloudApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_access_item**](CloudApi.md#create_cloud_access_item) | **POST** /platform/3/cloud/access | 
[**create_cloud_account**](CloudApi.md#create_cloud_account) | **POST** /platform/3/cloud/accounts | 
[**create_cloud_job**](CloudApi.md#create_cloud_job) | **POST** /platform/3/cloud/jobs | 
[**create_cloud_pool**](CloudApi.md#create_cloud_pool) | **POST** /platform/3/cloud/pools | 
[**create_settings_encryption_key_item**](CloudApi.md#create_settings_encryption_key_item) | **POST** /platform/3/cloud/settings/encryption-key | 
[**create_settings_reporting_eula_item**](CloudApi.md#create_settings_reporting_eula_item) | **POST** /platform/3/cloud/settings/reporting-eula | 
[**delete_cloud_access_guid**](CloudApi.md#delete_cloud_access_guid) | **DELETE** /platform/3/cloud/access/{CloudAccessGuid} | 
[**delete_cloud_account**](CloudApi.md#delete_cloud_account) | **DELETE** /platform/3/cloud/accounts/{CloudAccountId} | 
[**delete_cloud_pool**](CloudApi.md#delete_cloud_pool) | **DELETE** /platform/3/cloud/pools/{CloudPoolId} | 
[**delete_settings_reporting_eula**](CloudApi.md#delete_settings_reporting_eula) | **DELETE** /platform/3/cloud/settings/reporting-eula | 
[**get_cloud_access_guid**](CloudApi.md#get_cloud_access_guid) | **GET** /platform/3/cloud/access/{CloudAccessGuid} | 
[**get_cloud_account**](CloudApi.md#get_cloud_account) | **GET** /platform/3/cloud/accounts/{CloudAccountId} | 
[**get_cloud_job**](CloudApi.md#get_cloud_job) | **GET** /platform/3/cloud/jobs/{CloudJobId} | 
[**get_cloud_jobs_file**](CloudApi.md#get_cloud_jobs_file) | **GET** /platform/3/cloud/jobs-files/{CloudJobsFileId} | 
[**get_cloud_pool**](CloudApi.md#get_cloud_pool) | **GET** /platform/3/cloud/pools/{CloudPoolId} | 
[**get_cloud_settings**](CloudApi.md#get_cloud_settings) | **GET** /platform/3/cloud/settings | 
[**list_cloud_access**](CloudApi.md#list_cloud_access) | **GET** /platform/3/cloud/access | 
[**list_cloud_accounts**](CloudApi.md#list_cloud_accounts) | **GET** /platform/3/cloud/accounts | 
[**list_cloud_jobs**](CloudApi.md#list_cloud_jobs) | **GET** /platform/3/cloud/jobs | 
[**list_cloud_pools**](CloudApi.md#list_cloud_pools) | **GET** /platform/3/cloud/pools | 
[**list_settings_reporting_eula**](CloudApi.md#list_settings_reporting_eula) | **GET** /platform/3/cloud/settings/reporting-eula | 
[**update_cloud_account**](CloudApi.md#update_cloud_account) | **PUT** /platform/3/cloud/accounts/{CloudAccountId} | 
[**update_cloud_job**](CloudApi.md#update_cloud_job) | **PUT** /platform/3/cloud/jobs/{CloudJobId} | 
[**update_cloud_pool**](CloudApi.md#update_cloud_pool) | **PUT** /platform/3/cloud/pools/{CloudPoolId} | 
[**update_cloud_settings**](CloudApi.md#update_cloud_settings) | **PUT** /platform/3/cloud/settings | 


# **create_cloud_access_item**
> Empty create_cloud_access_item(cloud_access_item)



Add a cluster identifier to access list.

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
api_instance = isi_sdk.CloudApi()
cloud_access_item = isi_sdk.CloudAccessItem() # CloudAccessItem | 

try: 
    api_response = api_instance.create_cloud_access_item(cloud_access_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->create_cloud_access_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_access_item** | [**CloudAccessItem**](CloudAccessItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_account**
> CreateCloudAccountResponse create_cloud_account(cloud_account)



Create a new account.

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
api_instance = isi_sdk.CloudApi()
cloud_account = isi_sdk.CloudAccountCreateParams() # CloudAccountCreateParams | 

try: 
    api_response = api_instance.create_cloud_account(cloud_account)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->create_cloud_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account** | [**CloudAccountCreateParams**](CloudAccountCreateParams.md)|  | 

### Return type

[**CreateCloudAccountResponse**](CreateCloudAccountResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_job**
> CreateCloudJobResponse create_cloud_job(cloud_job)



Create a new job.

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
api_instance = isi_sdk.CloudApi()
cloud_job = isi_sdk.CloudJobCreateParams() # CloudJobCreateParams | 

try: 
    api_response = api_instance.create_cloud_job(cloud_job)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->create_cloud_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_job** | [**CloudJobCreateParams**](CloudJobCreateParams.md)|  | 

### Return type

[**CreateCloudJobResponse**](CreateCloudJobResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_pool**
> CreateCloudPoolResponse create_cloud_pool(cloud_pool)



Create a new pool.

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
api_instance = isi_sdk.CloudApi()
cloud_pool = isi_sdk.CloudPoolCreateParams() # CloudPoolCreateParams | 

try: 
    api_response = api_instance.create_cloud_pool(cloud_pool)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->create_cloud_pool: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool** | [**CloudPoolCreateParams**](CloudPoolCreateParams.md)|  | 

### Return type

[**CreateCloudPoolResponse**](CreateCloudPoolResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_encryption_key_item**
> Empty create_settings_encryption_key_item()



Regenerate master encryption key.

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
api_instance = isi_sdk.CloudApi()

try: 
    api_response = api_instance.create_settings_encryption_key_item()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->create_settings_encryption_key_item: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_reporting_eula_item**
> SettingsReportingEulaItem create_settings_reporting_eula_item(settings_reporting_eula_item)



Accept telemetry collection EULA.

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
api_instance = isi_sdk.CloudApi()
settings_reporting_eula_item = isi_sdk.SettingsReportingEulaItem() # SettingsReportingEulaItem | 

try: 
    api_response = api_instance.create_settings_reporting_eula_item(settings_reporting_eula_item)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->create_settings_reporting_eula_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_reporting_eula_item** | [**SettingsReportingEulaItem**](SettingsReportingEulaItem.md)|  | 

### Return type

[**SettingsReportingEulaItem**](SettingsReportingEulaItem.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_access_guid**
> delete_cloud_access_guid(cloud_access_guid)



Delete cloud access.

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
api_instance = isi_sdk.CloudApi()
cloud_access_guid = 'cloud_access_guid_example' # str | Delete cloud access.

try: 
    api_instance.delete_cloud_access_guid(cloud_access_guid)
except ApiException as e:
    print "Exception when calling CloudApi->delete_cloud_access_guid: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_access_guid** | **str**| Delete cloud access. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_account**
> delete_cloud_account(cloud_account_id)



Delete cloud account.

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
api_instance = isi_sdk.CloudApi()
cloud_account_id = 'cloud_account_id_example' # str | Delete cloud account.

try: 
    api_instance.delete_cloud_account(cloud_account_id)
except ApiException as e:
    print "Exception when calling CloudApi->delete_cloud_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account_id** | **str**| Delete cloud account. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_pool**
> delete_cloud_pool(cloud_pool_id)



Delete a cloud pool.

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
api_instance = isi_sdk.CloudApi()
cloud_pool_id = 'cloud_pool_id_example' # str | Delete a cloud pool.

try: 
    api_instance.delete_cloud_pool(cloud_pool_id)
except ApiException as e:
    print "Exception when calling CloudApi->delete_cloud_pool: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Delete a cloud pool. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_settings_reporting_eula**
> delete_settings_reporting_eula()



Revoke acceptance of telemetry collection EULA.

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
api_instance = isi_sdk.CloudApi()

try: 
    api_instance.delete_settings_reporting_eula()
except ApiException as e:
    print "Exception when calling CloudApi->delete_settings_reporting_eula: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_access_guid**
> CloudAccess get_cloud_access_guid(cloud_access_guid)



Retrieve cloud access information.

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
api_instance = isi_sdk.CloudApi()
cloud_access_guid = 'cloud_access_guid_example' # str | Retrieve cloud access information.

try: 
    api_response = api_instance.get_cloud_access_guid(cloud_access_guid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->get_cloud_access_guid: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_access_guid** | **str**| Retrieve cloud access information. | 

### Return type

[**CloudAccess**](CloudAccess.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_account**
> CloudAccounts get_cloud_account(cloud_account_id)



Retrieve cloud account information.

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
api_instance = isi_sdk.CloudApi()
cloud_account_id = 'cloud_account_id_example' # str | Retrieve cloud account information.

try: 
    api_response = api_instance.get_cloud_account(cloud_account_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->get_cloud_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account_id** | **str**| Retrieve cloud account information. | 

### Return type

[**CloudAccounts**](CloudAccounts.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_job**
> CloudJobs get_cloud_job(cloud_job_id)



Retrieve cloudpool job information.

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
api_instance = isi_sdk.CloudApi()
cloud_job_id = 'cloud_job_id_example' # str | Retrieve cloudpool job information.

try: 
    api_response = api_instance.get_cloud_job(cloud_job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->get_cloud_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_job_id** | **str**| Retrieve cloudpool job information. | 

### Return type

[**CloudJobs**](CloudJobs.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_jobs_file**
> CloudJobsFiles get_cloud_jobs_file(cloud_jobs_file_id, sort=sort, resume=resume, batch=batch, limit=limit, page=page, dir=dir)



Retrieve files associated with a cloudpool job.

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
api_instance = isi_sdk.CloudApi()
cloud_jobs_file_id = 'cloud_jobs_file_id_example' # str | Retrieve files associated with a cloudpool job.
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
batch = true # bool | If true, only \"limit\" and \"page\" arguments are honored.  Query will return all results, unsorted, as quickly as possible. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
page = 56 # int | Works only when \"batch\" parameter and \"limit\" parameters are specified.  Indicates which the page index of results to be returned (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.get_cloud_jobs_file(cloud_jobs_file_id, sort=sort, resume=resume, batch=batch, limit=limit, page=page, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->get_cloud_jobs_file: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_jobs_file_id** | **str**| Retrieve files associated with a cloudpool job. | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **batch** | **bool**| If true, only \&quot;limit\&quot; and \&quot;page\&quot; arguments are honored.  Query will return all results, unsorted, as quickly as possible. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **page** | **int**| Works only when \&quot;batch\&quot; parameter and \&quot;limit\&quot; parameters are specified.  Indicates which the page index of results to be returned | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**CloudJobsFiles**](CloudJobsFiles.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_pool**
> CloudPools get_cloud_pool(cloud_pool_id)



Retrieve cloud pool information

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
api_instance = isi_sdk.CloudApi()
cloud_pool_id = 'cloud_pool_id_example' # str | Retrieve cloud pool information

try: 
    api_response = api_instance.get_cloud_pool(cloud_pool_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->get_cloud_pool: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Retrieve cloud pool information | 

### Return type

[**CloudPools**](CloudPools.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cloud_settings**
> CloudSettings get_cloud_settings()



List all cloud settings.

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
api_instance = isi_sdk.CloudApi()

try: 
    api_response = api_instance.get_cloud_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->get_cloud_settings: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudSettings**](CloudSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_access**
> CloudAccessExtended list_cloud_access(sort=sort, limit=limit, dir=dir)



List all accessible cluster identifiers.

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
api_instance = isi_sdk.CloudApi()
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.list_cloud_access(sort=sort, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->list_cloud_access: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**CloudAccessExtended**](CloudAccessExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_accounts**
> CloudAccountsExtended list_cloud_accounts(sort=sort, limit=limit, dir=dir)



List all accounts.

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
api_instance = isi_sdk.CloudApi()
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.list_cloud_accounts(sort=sort, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->list_cloud_accounts: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_jobs**
> CloudJobsExtended list_cloud_jobs(sort=sort, limit=limit, dir=dir)



List all cloudpools jobs.

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
api_instance = isi_sdk.CloudApi()
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.list_cloud_jobs(sort=sort, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->list_cloud_jobs: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_pools**
> CloudPoolsExtended list_cloud_pools(sort=sort, limit=limit, dir=dir)



List all pools.

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
api_instance = isi_sdk.CloudApi()
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try: 
    api_response = api_instance.list_cloud_pools(sort=sort, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->list_cloud_pools: %s\n" % e
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

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings_reporting_eula**
> SettingsReportingEulaItem list_settings_reporting_eula()



View telemetry collection EULA acceptance and content URI.

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
api_instance = isi_sdk.CloudApi()

try: 
    api_response = api_instance.list_settings_reporting_eula()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CloudApi->list_settings_reporting_eula: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsReportingEulaItem**](SettingsReportingEulaItem.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_account**
> update_cloud_account(cloud_account, cloud_account_id)



Modify cloud account.  All fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.CloudApi()
cloud_account = isi_sdk.CloudAccount() # CloudAccount | 
cloud_account_id = 'cloud_account_id_example' # str | Modify cloud account.  All fields are optional, but one or more must be supplied.

try: 
    api_instance.update_cloud_account(cloud_account, cloud_account_id)
except ApiException as e:
    print "Exception when calling CloudApi->update_cloud_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account** | [**CloudAccount**](CloudAccount.md)|  | 
 **cloud_account_id** | **str**| Modify cloud account.  All fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_job**
> update_cloud_job(cloud_job, cloud_job_id)



Modify a cloud job or operation.

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
api_instance = isi_sdk.CloudApi()
cloud_job = isi_sdk.CloudJob() # CloudJob | 
cloud_job_id = 'cloud_job_id_example' # str | Modify a cloud job or operation.

try: 
    api_instance.update_cloud_job(cloud_job, cloud_job_id)
except ApiException as e:
    print "Exception when calling CloudApi->update_cloud_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_job** | [**CloudJob**](CloudJob.md)|  | 
 **cloud_job_id** | **str**| Modify a cloud job or operation. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_pool**
> update_cloud_pool(cloud_pool, cloud_pool_id)



Modify a cloud pool.  All fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.CloudApi()
cloud_pool = isi_sdk.CloudPool() # CloudPool | 
cloud_pool_id = 'cloud_pool_id_example' # str | Modify a cloud pool.  All fields are optional, but one or more must be supplied.

try: 
    api_instance.update_cloud_pool(cloud_pool, cloud_pool_id)
except ApiException as e:
    print "Exception when calling CloudApi->update_cloud_pool: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool** | [**CloudPool**](CloudPool.md)|  | 
 **cloud_pool_id** | **str**| Modify a cloud pool.  All fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cloud_settings**
> update_cloud_settings(cloud_settings)



Modify one or more settings.

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
api_instance = isi_sdk.CloudApi()
cloud_settings = isi_sdk.CloudSettingsSettings() # CloudSettingsSettings | 

try: 
    api_instance.update_cloud_settings(cloud_settings)
except ApiException as e:
    print "Exception when calling CloudApi->update_cloud_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_settings** | [**CloudSettingsSettings**](CloudSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

