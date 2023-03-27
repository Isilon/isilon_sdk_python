# isilon_sdk.v9_4_0.CloudApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cloud_access_item**](CloudApi.md#create_cloud_access_item) | **POST** /platform/3/cloud/access | 
[**create_cloud_account**](CloudApi.md#create_cloud_account) | **POST** /platform/7/cloud/accounts | 
[**create_cloud_certificate**](CloudApi.md#create_cloud_certificate) | **POST** /platform/7/cloud/certificates | 
[**create_cloud_job**](CloudApi.md#create_cloud_job) | **POST** /platform/3/cloud/jobs | 
[**create_cloud_pool**](CloudApi.md#create_cloud_pool) | **POST** /platform/7/cloud/pools | 
[**create_cloud_proxy**](CloudApi.md#create_cloud_proxy) | **POST** /platform/4/cloud/proxies | 
[**create_settings_encryption_key_item**](CloudApi.md#create_settings_encryption_key_item) | **POST** /platform/3/cloud/settings/encryption-key | 
[**create_settings_reporting_eula_item**](CloudApi.md#create_settings_reporting_eula_item) | **POST** /platform/3/cloud/settings/reporting-eula | 
[**delete_cloud_access_guid**](CloudApi.md#delete_cloud_access_guid) | **DELETE** /platform/3/cloud/access/{CloudAccessGuid} | 
[**delete_cloud_account**](CloudApi.md#delete_cloud_account) | **DELETE** /platform/7/cloud/accounts/{CloudAccountId} | 
[**delete_cloud_certificate**](CloudApi.md#delete_cloud_certificate) | **DELETE** /platform/7/cloud/certificates/{CloudCertificateId} | 
[**delete_cloud_pool**](CloudApi.md#delete_cloud_pool) | **DELETE** /platform/7/cloud/pools/{CloudPoolId} | 
[**delete_cloud_proxy**](CloudApi.md#delete_cloud_proxy) | **DELETE** /platform/4/cloud/proxies/{CloudProxyId} | 
[**delete_settings_reporting_eula**](CloudApi.md#delete_settings_reporting_eula) | **DELETE** /platform/3/cloud/settings/reporting-eula | 
[**get_cloud_access_guid**](CloudApi.md#get_cloud_access_guid) | **GET** /platform/3/cloud/access/{CloudAccessGuid} | 
[**get_cloud_account**](CloudApi.md#get_cloud_account) | **GET** /platform/7/cloud/accounts/{CloudAccountId} | 
[**get_cloud_certificate**](CloudApi.md#get_cloud_certificate) | **GET** /platform/7/cloud/certificates/{CloudCertificateId} | 
[**get_cloud_job**](CloudApi.md#get_cloud_job) | **GET** /platform/3/cloud/jobs/{CloudJobId} | 
[**get_cloud_jobs_file**](CloudApi.md#get_cloud_jobs_file) | **GET** /platform/3/cloud/jobs-files/{CloudJobsFileId} | 
[**get_cloud_pool**](CloudApi.md#get_cloud_pool) | **GET** /platform/7/cloud/pools/{CloudPoolId} | 
[**get_cloud_proxy**](CloudApi.md#get_cloud_proxy) | **GET** /platform/4/cloud/proxies/{CloudProxyId} | 
[**get_cloud_settings**](CloudApi.md#get_cloud_settings) | **GET** /platform/3/cloud/settings | 
[**list_cloud_access**](CloudApi.md#list_cloud_access) | **GET** /platform/3/cloud/access | 
[**list_cloud_accounts**](CloudApi.md#list_cloud_accounts) | **GET** /platform/7/cloud/accounts | 
[**list_cloud_certificates**](CloudApi.md#list_cloud_certificates) | **GET** /platform/7/cloud/certificates | 
[**list_cloud_jobs**](CloudApi.md#list_cloud_jobs) | **GET** /platform/3/cloud/jobs | 
[**list_cloud_pools**](CloudApi.md#list_cloud_pools) | **GET** /platform/7/cloud/pools | 
[**list_cloud_proxies**](CloudApi.md#list_cloud_proxies) | **GET** /platform/4/cloud/proxies | 
[**list_settings_reporting_eula**](CloudApi.md#list_settings_reporting_eula) | **GET** /platform/3/cloud/settings/reporting-eula | 
[**update_cloud_account**](CloudApi.md#update_cloud_account) | **PUT** /platform/7/cloud/accounts/{CloudAccountId} | 
[**update_cloud_certificate**](CloudApi.md#update_cloud_certificate) | **PUT** /platform/7/cloud/certificates/{CloudCertificateId} | 
[**update_cloud_job**](CloudApi.md#update_cloud_job) | **PUT** /platform/3/cloud/jobs/{CloudJobId} | 
[**update_cloud_pool**](CloudApi.md#update_cloud_pool) | **PUT** /platform/7/cloud/pools/{CloudPoolId} | 
[**update_cloud_proxy**](CloudApi.md#update_cloud_proxy) | **PUT** /platform/4/cloud/proxies/{CloudProxyId} | 
[**update_cloud_settings**](CloudApi.md#update_cloud_settings) | **PUT** /platform/3/cloud/settings | 


# **create_cloud_access_item**
> Empty create_cloud_access_item(cloud_access_item)



Add a cluster identifier to access list.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_access_item = isilon_sdk.v9_4_0.CloudAccessItem() # CloudAccessItem | 

try:
    api_response = api_instance.create_cloud_access_item(cloud_access_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud_access_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_access_item** | [**CloudAccessItem**](CloudAccessItem.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cloud_account**
> CreateCloudAccountResponse create_cloud_account(cloud_account)



Create a new account.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_account = isilon_sdk.v9_4_0.CloudAccountCreateParams() # CloudAccountCreateParams | 

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

# **create_cloud_certificate**
> CreateResponse create_cloud_certificate(cloud_certificate)



Import a TLS client certificate.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_certificate = isilon_sdk.v9_4_0.CertificateServerItem() # CertificateServerItem | 

try:
    api_response = api_instance.create_cloud_certificate(cloud_certificate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_certificate** | [**CertificateServerItem**](CertificateServerItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_job = isilon_sdk.v9_4_0.CloudJobCreateParams() # CloudJobCreateParams | 

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_pool = isilon_sdk.v9_4_0.CloudPoolCreateParams() # CloudPoolCreateParams | 

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

# **create_cloud_proxy**
> CreateCloudProxyResponse create_cloud_proxy(cloud_proxy)



Create a new proxy.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_proxy = isilon_sdk.v9_4_0.CloudProxyCreateParams() # CloudProxyCreateParams | 

try:
    api_response = api_instance.create_cloud_proxy(cloud_proxy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_cloud_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_proxy** | [**CloudProxyCreateParams**](CloudProxyCreateParams.md)|  | 

### Return type

[**CreateCloudProxyResponse**](CreateCloudProxyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_encryption_key_item**
> Empty create_settings_encryption_key_item(settings_encryption_key_item)



Regenerate master encryption key.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
settings_encryption_key_item = isilon_sdk.v9_4_0.Empty() # Empty | 

try:
    api_response = api_instance.create_settings_encryption_key_item(settings_encryption_key_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_settings_encryption_key_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_encryption_key_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_reporting_eula_item**
> Empty create_settings_reporting_eula_item(settings_reporting_eula_item)



Accept telemetry collection EULA.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
settings_reporting_eula_item = isilon_sdk.v9_4_0.Empty() # Empty | 

try:
    api_response = api_instance.create_settings_reporting_eula_item(settings_reporting_eula_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->create_settings_reporting_eula_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_reporting_eula_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_access_guid**
> delete_cloud_access_guid(cloud_access_guid)



Delete cloud access.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_access_guid = 'cloud_access_guid_example' # str | Delete cloud access.

try:
    api_instance.delete_cloud_access_guid(cloud_access_guid)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_access_guid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_access_guid** | **str**| Delete cloud access. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_account**
> delete_cloud_account(cloud_account_id, acknowledge_force_delete=acknowledge_force_delete)



Delete cloud account.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_account_id = 'cloud_account_id_example' # str | Delete cloud account.
acknowledge_force_delete = 'acknowledge_force_delete_example' # str | A value of 1 acknowledges that the user is deleting data. (optional)

try:
    api_instance.delete_cloud_account(cloud_account_id, acknowledge_force_delete=acknowledge_force_delete)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_account_id** | **str**| Delete cloud account. | 
 **acknowledge_force_delete** | **str**| A value of 1 acknowledges that the user is deleting data. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_certificate**
> delete_cloud_certificate(cloud_certificate_id)



Delete a CloudPools TLS client certificate.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_certificate_id = 'cloud_certificate_id_example' # str | Delete a CloudPools TLS client certificate.

try:
    api_instance.delete_cloud_certificate(cloud_certificate_id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_certificate_id** | **str**| Delete a CloudPools TLS client certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_pool**
> delete_cloud_pool(cloud_pool_id, acknowledge_force_delete=acknowledge_force_delete)



Delete a cloud pool.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_pool_id = 'cloud_pool_id_example' # str | Delete a cloud pool.
acknowledge_force_delete = 'acknowledge_force_delete_example' # str | A value of 1 acknowledges that the user is deleting data. (optional)

try:
    api_instance.delete_cloud_pool(cloud_pool_id, acknowledge_force_delete=acknowledge_force_delete)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_pool_id** | **str**| Delete a cloud pool. | 
 **acknowledge_force_delete** | **str**| A value of 1 acknowledges that the user is deleting data. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cloud_proxy**
> delete_cloud_proxy(cloud_proxy_id)



Delete cloud account.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_proxy_id = 'cloud_proxy_id_example' # str | Delete cloud account.

try:
    api_instance.delete_cloud_proxy(cloud_proxy_id)
except ApiException as e:
    print("Exception when calling CloudApi->delete_cloud_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_proxy_id** | **str**| Delete cloud account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_settings_reporting_eula**
> delete_settings_reporting_eula()



Revoke acceptance of telemetry collection EULA.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_instance.delete_settings_reporting_eula()
except ApiException as e:
    print("Exception when calling CloudApi->delete_settings_reporting_eula: %s\n" % e)
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

# **get_cloud_access_guid**
> CloudAccess get_cloud_access_guid(cloud_access_guid)



Retrieve cloud access information.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_access_guid = 'cloud_access_guid_example' # str | Retrieve cloud access information.

try:
    api_response = api_instance.get_cloud_access_guid(cloud_access_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_access_guid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_access_guid** | **str**| Retrieve cloud access information. | 

### Return type

[**CloudAccess**](CloudAccess.md)

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
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

# **get_cloud_certificate**
> CertificatesCa get_cloud_certificate(cloud_certificate_id)



Retrieve a CloudPools TLS client certificate.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_certificate_id = 'cloud_certificate_id_example' # str | Retrieve a CloudPools TLS client certificate.

try:
    api_response = api_instance.get_cloud_certificate(cloud_certificate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_certificate_id** | **str**| Retrieve a CloudPools TLS client certificate. | 

### Return type

[**CertificatesCa**](CertificatesCa.md)

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
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
> CloudJobsFiles get_cloud_jobs_file(cloud_jobs_file_id, dir=dir, limit=limit, offset=offset, page=page, resume=resume, sort=sort)



Retrieve files associated with a cloudpool job.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_jobs_file_id = 'cloud_jobs_file_id_example' # str | Retrieve files associated with a cloudpool job.
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Number of files to display; range from 1 to 100000. (optional)
offset = 56 # int | Specifies the starting entry to be displayed. (optional)
page = 56 # int | Used with limit option. If exists, specifies the starting page to display where page size is specified by limit. This option will be deprecated; please use offset option instead. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. Output is limited to maximum of 100000 files. (optional)

try:
    api_response = api_instance.get_cloud_jobs_file(cloud_jobs_file_id, dir=dir, limit=limit, offset=offset, page=page, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_jobs_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_jobs_file_id** | **str**| Retrieve files associated with a cloudpool job. | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Number of files to display; range from 1 to 100000. | [optional] 
 **offset** | **int**| Specifies the starting entry to be displayed. | [optional] 
 **page** | **int**| Used with limit option. If exists, specifies the starting page to display where page size is specified by limit. This option will be deprecated; please use offset option instead. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. Output is limited to maximum of 100000 files. | [optional] 

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
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

# **get_cloud_proxy**
> CloudProxies get_cloud_proxy(cloud_proxy_id)



Retrieve cloud account information.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_proxy_id = 'cloud_proxy_id_example' # str | Retrieve cloud account information.

try:
    api_response = api_instance.get_cloud_proxy(cloud_proxy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->get_cloud_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_proxy_id** | **str**| Retrieve cloud account information. | 

### Return type

[**CloudProxies**](CloudProxies.md)

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))

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

# **list_cloud_access**
> CloudAccessExtended list_cloud_access(dir=dir, limit=limit, resume=resume, sort=sort)



List all accessible cluster identifiers.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_cloud_access(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CloudAccessExtended**](CloudAccessExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_accounts**
> CloudAccountsExtended list_cloud_accounts(dir=dir, limit=limit, resume=resume, sort=sort)



List all accounts.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_cloud_accounts(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CloudAccountsExtended**](CloudAccountsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_certificates**
> CloudCertificates list_cloud_certificates(dir=dir, limit=limit, resume=resume, sort=sort)



Retrieve a list of all CloudPools client certificates.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_cloud_certificates(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CloudCertificates**](CloudCertificates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_jobs**
> CloudJobsExtended list_cloud_jobs(dir=dir, limit=limit, resume=resume, sort=sort)



List all cloudpools jobs.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_cloud_jobs(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CloudJobsExtended**](CloudJobsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_pools**
> CloudPoolsExtended list_cloud_pools(dir=dir, limit=limit, resume=resume, sort=sort)



List all pools.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_cloud_pools(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_pools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CloudPoolsExtended**](CloudPoolsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_proxies**
> CloudProxiesExtended list_cloud_proxies(dir=dir, limit=limit, resume=resume, sort=sort)



List all proxies.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_cloud_proxies(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_cloud_proxies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CloudProxiesExtended**](CloudProxiesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings_reporting_eula**
> SettingsReportingEula list_settings_reporting_eula()



View telemetry collection EULA acceptance and content URI.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.list_settings_reporting_eula()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CloudApi->list_settings_reporting_eula: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsReportingEula**](SettingsReportingEula.md)

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_account = isilon_sdk.v9_4_0.CloudAccount() # CloudAccount | 
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

# **update_cloud_certificate**
> update_cloud_certificate(cloud_certificate, cloud_certificate_id)



Modify a CloudPools TLS client certificate.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_certificate = isilon_sdk.v9_4_0.CertificateServerIdParams() # CertificateServerIdParams | 
cloud_certificate_id = 'cloud_certificate_id_example' # str | Modify a CloudPools TLS client certificate.

try:
    api_instance.update_cloud_certificate(cloud_certificate, cloud_certificate_id)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_certificate** | [**CertificateServerIdParams**](CertificateServerIdParams.md)|  | 
 **cloud_certificate_id** | **str**| Modify a CloudPools TLS client certificate. | 

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



Modify a cloud job or operation.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_job = isilon_sdk.v9_4_0.CloudJob() # CloudJob | 
cloud_job_id = 'cloud_job_id_example' # str | Modify a cloud job or operation.

try:
    api_instance.update_cloud_job(cloud_job, cloud_job_id)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_job** | [**CloudJob**](CloudJob.md)|  | 
 **cloud_job_id** | **str**| Modify a cloud job or operation. | 

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_pool = isilon_sdk.v9_4_0.CloudPool() # CloudPool | 
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

# **update_cloud_proxy**
> update_cloud_proxy(cloud_proxy, cloud_proxy_id)



Modify cloud account.  All fields are optional, but one or more must be supplied.

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
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_proxy = isilon_sdk.v9_4_0.CloudProxy() # CloudProxy | 
cloud_proxy_id = 'cloud_proxy_id_example' # str | Modify cloud account.  All fields are optional, but one or more must be supplied.

try:
    api_instance.update_cloud_proxy(cloud_proxy, cloud_proxy_id)
except ApiException as e:
    print("Exception when calling CloudApi->update_cloud_proxy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud_proxy** | [**CloudProxy**](CloudProxy.md)|  | 
 **cloud_proxy_id** | **str**| Modify cloud account.  All fields are optional, but one or more must be supplied. | 

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.CloudApi(isilon_sdk.v9_4_0.ApiClient(configuration))
cloud_settings = isilon_sdk.v9_4_0.CloudSettingsSettings() # CloudSettingsSettings | 

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

