# isilon_sdk.v9_4_0.DatamoverApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificates_ca_item**](DatamoverApi.md#create_certificates_ca_item) | **POST** /platform/15/datamover/certificates/ca | 
[**create_certificates_identity_item**](DatamoverApi.md#create_certificates_identity_item) | **POST** /platform/15/datamover/certificates/identity | 
[**create_datamover_account**](DatamoverApi.md#create_datamover_account) | **POST** /platform/15/datamover/accounts | 
[**create_datamover_base_policy**](DatamoverApi.md#create_datamover_base_policy) | **POST** /platform/15/datamover/base-policies | 
[**create_datamover_policy**](DatamoverApi.md#create_datamover_policy) | **POST** /platform/15/datamover/policies | 
[**create_throttling_bw_rule**](DatamoverApi.md#create_throttling_bw_rule) | **POST** /platform/15/datamover/throttling/bw-rules | 
[**delete_certificates_ca_by_id**](DatamoverApi.md#delete_certificates_ca_by_id) | **DELETE** /platform/15/datamover/certificates/ca/{CertificatesCaId} | 
[**delete_certificates_identity_by_id**](DatamoverApi.md#delete_certificates_identity_by_id) | **DELETE** /platform/15/datamover/certificates/identity/{CertificatesIdentityId} | 
[**delete_datamover_account**](DatamoverApi.md#delete_datamover_account) | **DELETE** /platform/15/datamover/accounts/{DatamoverAccountId} | 
[**delete_datamover_base_policy**](DatamoverApi.md#delete_datamover_base_policy) | **DELETE** /platform/15/datamover/base-policies/{DatamoverBasePolicyId} | 
[**delete_datamover_historical_jobs**](DatamoverApi.md#delete_datamover_historical_jobs) | **DELETE** /platform/15/datamover/historical-jobs | 
[**delete_datamover_policy**](DatamoverApi.md#delete_datamover_policy) | **DELETE** /platform/15/datamover/policies/{DatamoverPolicyId} | 
[**delete_throttling_bw_rule**](DatamoverApi.md#delete_throttling_bw_rule) | **DELETE** /platform/15/datamover/throttling/bw-rules/{ThrottlingBwRuleId} | 
[**get_certificates_ca_by_id**](DatamoverApi.md#get_certificates_ca_by_id) | **GET** /platform/15/datamover/certificates/ca/{CertificatesCaId} | 
[**get_certificates_identity_by_id**](DatamoverApi.md#get_certificates_identity_by_id) | **GET** /platform/15/datamover/certificates/identity/{CertificatesIdentityId} | 
[**get_datamover_account**](DatamoverApi.md#get_datamover_account) | **GET** /platform/15/datamover/accounts/{DatamoverAccountId} | 
[**get_datamover_base_policy**](DatamoverApi.md#get_datamover_base_policy) | **GET** /platform/15/datamover/base-policies/{DatamoverBasePolicyId} | 
[**get_datamover_dataset**](DatamoverApi.md#get_datamover_dataset) | **GET** /platform/15/datamover/datasets/{DatamoverDatasetId} | 
[**get_datamover_datasets**](DatamoverApi.md#get_datamover_datasets) | **GET** /platform/15/datamover/datasets | 
[**get_datamover_historical_jobs**](DatamoverApi.md#get_datamover_historical_jobs) | **GET** /platform/15/datamover/historical-jobs | 
[**get_datamover_job**](DatamoverApi.md#get_datamover_job) | **GET** /platform/15/datamover/jobs/{DatamoverJobId} | 
[**get_datamover_jobs**](DatamoverApi.md#get_datamover_jobs) | **GET** /platform/15/datamover/jobs | 
[**get_datamover_policy**](DatamoverApi.md#get_datamover_policy) | **GET** /platform/15/datamover/policies/{DatamoverPolicyId} | 
[**get_throttling_bw_rule**](DatamoverApi.md#get_throttling_bw_rule) | **GET** /platform/15/datamover/throttling/bw-rules/{ThrottlingBwRuleId} | 
[**get_throttling_settings**](DatamoverApi.md#get_throttling_settings) | **GET** /platform/15/datamover/throttling/settings | 
[**list_certificates_ca**](DatamoverApi.md#list_certificates_ca) | **GET** /platform/15/datamover/certificates/ca | 
[**list_certificates_identity**](DatamoverApi.md#list_certificates_identity) | **GET** /platform/15/datamover/certificates/identity | 
[**list_datamover_accounts**](DatamoverApi.md#list_datamover_accounts) | **GET** /platform/15/datamover/accounts | 
[**list_datamover_base_policies**](DatamoverApi.md#list_datamover_base_policies) | **GET** /platform/15/datamover/base-policies | 
[**list_datamover_policies**](DatamoverApi.md#list_datamover_policies) | **GET** /platform/15/datamover/policies | 
[**list_throttling_bw_rules**](DatamoverApi.md#list_throttling_bw_rules) | **GET** /platform/15/datamover/throttling/bw-rules | 
[**update_certificates_ca_by_id**](DatamoverApi.md#update_certificates_ca_by_id) | **PUT** /platform/15/datamover/certificates/ca/{CertificatesCaId} | 
[**update_certificates_identity_by_id**](DatamoverApi.md#update_certificates_identity_by_id) | **PUT** /platform/15/datamover/certificates/identity/{CertificatesIdentityId} | 
[**update_datamover_account**](DatamoverApi.md#update_datamover_account) | **PUT** /platform/15/datamover/accounts/{DatamoverAccountId} | 
[**update_datamover_base_policy**](DatamoverApi.md#update_datamover_base_policy) | **PUT** /platform/15/datamover/base-policies/{DatamoverBasePolicyId} | 
[**update_datamover_job**](DatamoverApi.md#update_datamover_job) | **PUT** /platform/15/datamover/jobs/{DatamoverJobId} | 
[**update_datamover_policy**](DatamoverApi.md#update_datamover_policy) | **PUT** /platform/15/datamover/policies/{DatamoverPolicyId} | 
[**update_throttling_bw_rule**](DatamoverApi.md#update_throttling_bw_rule) | **PUT** /platform/15/datamover/throttling/bw-rules/{ThrottlingBwRuleId} | 
[**update_throttling_settings**](DatamoverApi.md#update_throttling_settings) | **PUT** /platform/15/datamover/throttling/settings | 


# **create_certificates_ca_item**
> CreateResponse create_certificates_ca_item(certificates_ca_item)



Import a trusted Datamover TLS CA certificate.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
certificates_ca_item = isilon_sdk.v9_4_0.CertificatesCaItem() # CertificatesCaItem | 

try:
    api_response = api_instance.create_certificates_ca_item(certificates_ca_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->create_certificates_ca_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_ca_item** | [**CertificatesCaItem**](CertificatesCaItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_certificates_identity_item**
> CreateResponse create_certificates_identity_item(certificates_identity_item)



Import a trusted Datamover TLS Identity certificate.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
certificates_identity_item = isilon_sdk.v9_4_0.CertificatesIdentityItem() # CertificatesIdentityItem | 

try:
    api_response = api_instance.create_certificates_identity_item(certificates_identity_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->create_certificates_identity_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_identity_item** | [**CertificatesIdentityItem**](CertificatesIdentityItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_datamover_account**
> CreateDatamoverAccountResponse create_datamover_account(datamover_account)



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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_account = isilon_sdk.v9_4_0.DatamoverAccountCreateParams() # DatamoverAccountCreateParams | 

try:
    api_response = api_instance.create_datamover_account(datamover_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->create_datamover_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_account** | [**DatamoverAccountCreateParams**](DatamoverAccountCreateParams.md)|  | 

### Return type

[**CreateDatamoverAccountResponse**](CreateDatamoverAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_datamover_base_policy**
> CreateDatamoverBasePolicyResponse create_datamover_base_policy(datamover_base_policy)



Create a new Data Mover base policy.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_base_policy = isilon_sdk.v9_4_0.DatamoverBasePolicyCreateParams() # DatamoverBasePolicyCreateParams | 

try:
    api_response = api_instance.create_datamover_base_policy(datamover_base_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->create_datamover_base_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_base_policy** | [**DatamoverBasePolicyCreateParams**](DatamoverBasePolicyCreateParams.md)|  | 

### Return type

[**CreateDatamoverBasePolicyResponse**](CreateDatamoverBasePolicyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_datamover_policy**
> CreateDatamoverBasePolicyResponse create_datamover_policy(datamover_policy)



Create a new datamover policy.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_policy = isilon_sdk.v9_4_0.DatamoverPolicyCreateParams() # DatamoverPolicyCreateParams | 

try:
    api_response = api_instance.create_datamover_policy(datamover_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->create_datamover_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_policy** | [**DatamoverPolicyCreateParams**](DatamoverPolicyCreateParams.md)|  | 

### Return type

[**CreateDatamoverBasePolicyResponse**](CreateDatamoverBasePolicyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_throttling_bw_rule**
> CreateThrottlingBwRuleResponse create_throttling_bw_rule(throttling_bw_rule)



Create a new bandwidth throttling rule.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
throttling_bw_rule = isilon_sdk.v9_4_0.ThrottlingBwRuleCreateParams() # ThrottlingBwRuleCreateParams | 

try:
    api_response = api_instance.create_throttling_bw_rule(throttling_bw_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->create_throttling_bw_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **throttling_bw_rule** | [**ThrottlingBwRuleCreateParams**](ThrottlingBwRuleCreateParams.md)|  | 

### Return type

[**CreateThrottlingBwRuleResponse**](CreateThrottlingBwRuleResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificates_ca_by_id**
> delete_certificates_ca_by_id(certificates_ca_id)



Delete a trusted Datamover TLS CA certificate.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
certificates_ca_id = 'certificates_ca_id_example' # str | Delete a trusted Datamover TLS CA certificate.

try:
    api_instance.delete_certificates_ca_by_id(certificates_ca_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->delete_certificates_ca_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_ca_id** | **str**| Delete a trusted Datamover TLS CA certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificates_identity_by_id**
> delete_certificates_identity_by_id(certificates_identity_id)



Delete a trusted Datamover TLS Identity certificate.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
certificates_identity_id = 'certificates_identity_id_example' # str | Delete a trusted Datamover TLS Identity certificate.

try:
    api_instance.delete_certificates_identity_by_id(certificates_identity_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->delete_certificates_identity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_identity_id** | **str**| Delete a trusted Datamover TLS Identity certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datamover_account**
> delete_datamover_account(datamover_account_id)



Delete the account.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_account_id = 'datamover_account_id_example' # str | Delete the account.

try:
    api_instance.delete_datamover_account(datamover_account_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->delete_datamover_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_account_id** | **str**| Delete the account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datamover_base_policy**
> delete_datamover_base_policy(datamover_base_policy_id)



Delete the base policy.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_base_policy_id = 'datamover_base_policy_id_example' # str | Delete the base policy.

try:
    api_instance.delete_datamover_base_policy(datamover_base_policy_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->delete_datamover_base_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_base_policy_id** | **str**| Delete the base policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datamover_historical_jobs**
> delete_datamover_historical_jobs(after_time=after_time)



List/Delete finished jobs based on their end time. Capped at 1000. If 'after-time' is specified, latest 1000 jobs ended after this time will be listed/deleted. If 'after-time' is not specified, latest 1000 jobs finished in last 24 hours will be listed/deleted.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
after_time = 'after_time_example' # str | The time in '%Y-%m-%d %H:%M:%S' format. The year range is 2001-2099. (optional)

try:
    api_instance.delete_datamover_historical_jobs(after_time=after_time)
except ApiException as e:
    print("Exception when calling DatamoverApi->delete_datamover_historical_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after_time** | **str**| The time in &#39;%Y-%m-%d %H:%M:%S&#39; format. The year range is 2001-2099. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_datamover_policy**
> delete_datamover_policy(datamover_policy_id)



Delete the policy.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_policy_id = 'datamover_policy_id_example' # str | Delete the policy.

try:
    api_instance.delete_datamover_policy(datamover_policy_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->delete_datamover_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_policy_id** | **str**| Delete the policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_throttling_bw_rule**
> delete_throttling_bw_rule(throttling_bw_rule_id)



Delete a bandwidth throttling rule.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
throttling_bw_rule_id = 'throttling_bw_rule_id_example' # str | Delete a bandwidth throttling rule.

try:
    api_instance.delete_throttling_bw_rule(throttling_bw_rule_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->delete_throttling_bw_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **throttling_bw_rule_id** | **str**| Delete a bandwidth throttling rule. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificates_ca_by_id**
> CertificatesCa get_certificates_ca_by_id(certificates_ca_id)



Retrieve a single trusted Datamover TLS CA certificate.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
certificates_ca_id = 'certificates_ca_id_example' # str | Retrieve a single trusted Datamover TLS CA certificate.

try:
    api_response = api_instance.get_certificates_ca_by_id(certificates_ca_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_certificates_ca_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_ca_id** | **str**| Retrieve a single trusted Datamover TLS CA certificate. | 

### Return type

[**CertificatesCa**](CertificatesCa.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificates_identity_by_id**
> CertificatesIdentity get_certificates_identity_by_id(certificates_identity_id)



Retrieve a single trusted Datamover TLS Identity certificate.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
certificates_identity_id = 'certificates_identity_id_example' # str | Retrieve a single trusted Datamover TLS Identity certificate.

try:
    api_response = api_instance.get_certificates_identity_by_id(certificates_identity_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_certificates_identity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_identity_id** | **str**| Retrieve a single trusted Datamover TLS Identity certificate. | 

### Return type

[**CertificatesIdentity**](CertificatesIdentity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datamover_account**
> DatamoverAccounts get_datamover_account(datamover_account_id)



Retrieve account information.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_account_id = 'datamover_account_id_example' # str | Retrieve account information.

try:
    api_response = api_instance.get_datamover_account(datamover_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_datamover_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_account_id** | **str**| Retrieve account information. | 

### Return type

[**DatamoverAccounts**](DatamoverAccounts.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datamover_base_policy**
> DatamoverBasePolicies get_datamover_base_policy(datamover_base_policy_id)



Retrieve base policy information.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_base_policy_id = 'datamover_base_policy_id_example' # str | Retrieve base policy information.

try:
    api_response = api_instance.get_datamover_base_policy(datamover_base_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_datamover_base_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_base_policy_id** | **str**| Retrieve base policy information. | 

### Return type

[**DatamoverBasePolicies**](DatamoverBasePolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datamover_dataset**
> DatamoverDatasets get_datamover_dataset(datamover_dataset_id, account_id=account_id)



Retrieve dataset information.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_dataset_id = 'datamover_dataset_id_example' # str | Retrieve dataset information.
account_id = 'account_id_example' # str | Unique account ID (optional)

try:
    api_response = api_instance.get_datamover_dataset(datamover_dataset_id, account_id=account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_datamover_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_dataset_id** | **str**| Retrieve dataset information. | 
 **account_id** | **str**| Unique account ID | [optional] 

### Return type

[**DatamoverDatasets**](DatamoverDatasets.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datamover_datasets**
> DatamoverDatasetsExtended get_datamover_datasets(account_id=account_id, base_path=base_path, limit=limit, resume=resume)



List all datasets or retrieve datasets of the specified type.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
account_id = 'account_id_example' # str | Unique account ID (optional)
base_path = 'base_path_example' # str |  (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_datamover_datasets(account_id=account_id, base_path=base_path, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_datamover_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Unique account ID | [optional] 
 **base_path** | **str**|  | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**DatamoverDatasetsExtended**](DatamoverDatasetsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datamover_historical_jobs**
> DatamoverHistoricalJobs get_datamover_historical_jobs(after_time=after_time)



List/Delete finished jobs based on their end time. Capped at 1000. If 'after-time' is specified, latest 1000 jobs ended after this time will be listed/deleted. If 'after-time' is not specified, latest 1000 jobs finished in last 24 hours will be listed/deleted.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
after_time = 'after_time_example' # str | The time in '%Y-%m-%d %H:%M:%S' format. The year range is 2001-2099. (optional)

try:
    api_response = api_instance.get_datamover_historical_jobs(after_time=after_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_datamover_historical_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after_time** | **str**| The time in &#39;%Y-%m-%d %H:%M:%S&#39; format. The year range is 2001-2099. | [optional] 

### Return type

[**DatamoverHistoricalJobs**](DatamoverHistoricalJobs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datamover_job**
> DatamoverJobs get_datamover_job(datamover_job_id)



Retrieve job information.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_job_id = 'datamover_job_id_example' # str | Retrieve job information.

try:
    api_response = api_instance.get_datamover_job(datamover_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_datamover_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_job_id** | **str**| Retrieve job information. | 

### Return type

[**DatamoverJobs**](DatamoverJobs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datamover_jobs**
> DatamoverHistoricalJobs get_datamover_jobs(limit=limit, resume=resume)



List all jobs.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_datamover_jobs(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_datamover_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**DatamoverHistoricalJobs**](DatamoverHistoricalJobs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datamover_policy**
> DatamoverPolicies get_datamover_policy(datamover_policy_id)



Retrieve policy information.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_policy_id = 'datamover_policy_id_example' # str | Retrieve policy information.

try:
    api_response = api_instance.get_datamover_policy(datamover_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_datamover_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_policy_id** | **str**| Retrieve policy information. | 

### Return type

[**DatamoverPolicies**](DatamoverPolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_throttling_bw_rule**
> ThrottlingBwRules get_throttling_bw_rule(throttling_bw_rule_id)



Retrieve a bandwidth throttling rule.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
throttling_bw_rule_id = 'throttling_bw_rule_id_example' # str | Retrieve a bandwidth throttling rule.

try:
    api_response = api_instance.get_throttling_bw_rule(throttling_bw_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_throttling_bw_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **throttling_bw_rule_id** | **str**| Retrieve a bandwidth throttling rule. | 

### Return type

[**ThrottlingBwRules**](ThrottlingBwRules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_throttling_settings**
> ThrottlingSettings get_throttling_settings()



View Datamover throttling settings.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.get_throttling_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->get_throttling_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ThrottlingSettings**](ThrottlingSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificates_ca**
> CertificatesCaExtended list_certificates_ca(dir=dir, limit=limit, resume=resume, sort=sort)



Retrieve a list of all trusted Datamover TLS CA certificates.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_certificates_ca(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->list_certificates_ca: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CertificatesCaExtended**](CertificatesCaExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificates_identity**
> CertificatesIdentityExtended list_certificates_identity(dir=dir, limit=limit, resume=resume, sort=sort)



Retrieve a list of all trusted Datamover TLS Identity certificates.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_certificates_identity(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->list_certificates_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**CertificatesIdentityExtended**](CertificatesIdentityExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datamover_accounts**
> DatamoverAccountsExtended list_datamover_accounts(limit=limit, resume=resume)



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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_datamover_accounts(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->list_datamover_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**DatamoverAccountsExtended**](DatamoverAccountsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datamover_base_policies**
> DatamoverBasePoliciesExtended list_datamover_base_policies(limit=limit, resume=resume)



List all base policies.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_datamover_base_policies(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->list_datamover_base_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**DatamoverBasePoliciesExtended**](DatamoverBasePoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_datamover_policies**
> DatamoverPoliciesExtended list_datamover_policies(limit=limit, resume=resume)



List all policies.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_datamover_policies(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->list_datamover_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**DatamoverPoliciesExtended**](DatamoverPoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_throttling_bw_rules**
> ThrottlingBwRulesExtended list_throttling_bw_rules()



List all bandwidth throttling rules.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.list_throttling_bw_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverApi->list_throttling_bw_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ThrottlingBwRulesExtended**](ThrottlingBwRulesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificates_ca_by_id**
> update_certificates_ca_by_id(certificates_ca_id_params, certificates_ca_id)



Modify a trusted Datamover TLS CA certificate.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
certificates_ca_id_params = isilon_sdk.v9_4_0.CertificatesCaIdParams() # CertificatesCaIdParams | 
certificates_ca_id = 'certificates_ca_id_example' # str | Modify a trusted Datamover TLS CA certificate.

try:
    api_instance.update_certificates_ca_by_id(certificates_ca_id_params, certificates_ca_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->update_certificates_ca_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_ca_id_params** | [**CertificatesCaIdParams**](CertificatesCaIdParams.md)|  | 
 **certificates_ca_id** | **str**| Modify a trusted Datamover TLS CA certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificates_identity_by_id**
> update_certificates_identity_by_id(certificates_identity_id_params, certificates_identity_id)



Modify a trusted Datamover TLS Identity certificate.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
certificates_identity_id_params = isilon_sdk.v9_4_0.CertificatesCaIdParams() # CertificatesCaIdParams | 
certificates_identity_id = 'certificates_identity_id_example' # str | Modify a trusted Datamover TLS Identity certificate.

try:
    api_instance.update_certificates_identity_by_id(certificates_identity_id_params, certificates_identity_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->update_certificates_identity_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_identity_id_params** | [**CertificatesCaIdParams**](CertificatesCaIdParams.md)|  | 
 **certificates_identity_id** | **str**| Modify a trusted Datamover TLS Identity certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datamover_account**
> update_datamover_account(datamover_account, datamover_account_id)



Modify account information.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_account = isilon_sdk.v9_4_0.DatamoverAccount() # DatamoverAccount | 
datamover_account_id = 'datamover_account_id_example' # str | Modify account information.

try:
    api_instance.update_datamover_account(datamover_account, datamover_account_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->update_datamover_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_account** | [**DatamoverAccount**](DatamoverAccount.md)|  | 
 **datamover_account_id** | **str**| Modify account information. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datamover_base_policy**
> update_datamover_base_policy(datamover_base_policy, datamover_base_policy_id)



Modify base policy information.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_base_policy = isilon_sdk.v9_4_0.DatamoverBasePolicy() # DatamoverBasePolicy | 
datamover_base_policy_id = 'datamover_base_policy_id_example' # str | Modify base policy information.

try:
    api_instance.update_datamover_base_policy(datamover_base_policy, datamover_base_policy_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->update_datamover_base_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_base_policy** | [**DatamoverBasePolicy**](DatamoverBasePolicy.md)|  | 
 **datamover_base_policy_id** | **str**| Modify base policy information. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datamover_job**
> update_datamover_job(action, datamover_job, datamover_job_id)



Modify job state.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
action = 'action_example' # str | Job control request.
datamover_job = isilon_sdk.v9_4_0.Empty() # Empty | 
datamover_job_id = 'datamover_job_id_example' # str | Modify job state.

try:
    api_instance.update_datamover_job(action, datamover_job, datamover_job_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->update_datamover_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Job control request. | 
 **datamover_job** | [**Empty**](Empty.md)|  | 
 **datamover_job_id** | **str**| Modify job state. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datamover_policy**
> update_datamover_policy(datamover_policy, datamover_policy_id)



Modify policy information.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
datamover_policy = isilon_sdk.v9_4_0.DatamoverPolicy() # DatamoverPolicy | 
datamover_policy_id = 'datamover_policy_id_example' # str | Modify policy information.

try:
    api_instance.update_datamover_policy(datamover_policy, datamover_policy_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->update_datamover_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datamover_policy** | [**DatamoverPolicy**](DatamoverPolicy.md)|  | 
 **datamover_policy_id** | **str**| Modify policy information. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_throttling_bw_rule**
> update_throttling_bw_rule(throttling_bw_rule, throttling_bw_rule_id)



Modify a bandwidth throttling rule.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
throttling_bw_rule = isilon_sdk.v9_4_0.ThrottlingBwRule() # ThrottlingBwRule | 
throttling_bw_rule_id = 'throttling_bw_rule_id_example' # str | Modify a bandwidth throttling rule.

try:
    api_instance.update_throttling_bw_rule(throttling_bw_rule, throttling_bw_rule_id)
except ApiException as e:
    print("Exception when calling DatamoverApi->update_throttling_bw_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **throttling_bw_rule** | [**ThrottlingBwRule**](ThrottlingBwRule.md)|  | 
 **throttling_bw_rule_id** | **str**| Modify a bandwidth throttling rule. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_throttling_settings**
> update_throttling_settings(throttling_settings)



Modify Datamover throttling settings.

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
api_instance = isilon_sdk.v9_4_0.DatamoverApi(isilon_sdk.v9_4_0.ApiClient(configuration))
throttling_settings = isilon_sdk.v9_4_0.ThrottlingSettingsSettings() # ThrottlingSettingsSettings | 

try:
    api_instance.update_throttling_settings(throttling_settings)
except ApiException as e:
    print("Exception when calling DatamoverApi->update_throttling_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **throttling_settings** | [**ThrottlingSettingsSettings**](ThrottlingSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

