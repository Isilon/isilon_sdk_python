# isi_sdk_9_0_0.SyncApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificates_peer_item**](SyncApi.md#create_certificates_peer_item) | **POST** /platform/7/sync/certificates/peer | 
[**create_certificates_server_item**](SyncApi.md#create_certificates_server_item) | **POST** /platform/7/sync/certificates/server | 
[**create_service_policy**](SyncApi.md#create_service_policy) | **POST** /platform/7/sync/service/policies | 
[**create_sync_job**](SyncApi.md#create_sync_job) | **POST** /platform/7/sync/jobs | 
[**create_sync_policy**](SyncApi.md#create_sync_policy) | **POST** /platform/7/sync/policies | 
[**create_sync_reports_rotate_item**](SyncApi.md#create_sync_reports_rotate_item) | **POST** /platform/1/sync/reports-rotate | 
[**create_sync_rule**](SyncApi.md#create_sync_rule) | **POST** /platform/3/sync/rules | 
[**delete_certificates_peer_by_id**](SyncApi.md#delete_certificates_peer_by_id) | **DELETE** /platform/7/sync/certificates/peer/{CertificatesPeerId} | 
[**delete_certificates_server_by_id**](SyncApi.md#delete_certificates_server_by_id) | **DELETE** /platform/7/sync/certificates/server/{CertificatesServerId} | 
[**delete_service_policies**](SyncApi.md#delete_service_policies) | **DELETE** /platform/7/sync/service/policies | 
[**delete_service_policy**](SyncApi.md#delete_service_policy) | **DELETE** /platform/7/sync/service/policies/{ServicePolicyId} | 
[**delete_service_target_policy**](SyncApi.md#delete_service_target_policy) | **DELETE** /platform/7/sync/service/target/policies/{ServiceTargetPolicyId} | 
[**delete_sync_jobs**](SyncApi.md#delete_sync_jobs) | **DELETE** /platform/7/sync/jobs | 
[**delete_sync_policies**](SyncApi.md#delete_sync_policies) | **DELETE** /platform/7/sync/policies | 
[**delete_sync_policy**](SyncApi.md#delete_sync_policy) | **DELETE** /platform/7/sync/policies/{SyncPolicyId} | 
[**delete_sync_rule**](SyncApi.md#delete_sync_rule) | **DELETE** /platform/3/sync/rules/{SyncRuleId} | 
[**delete_sync_rules**](SyncApi.md#delete_sync_rules) | **DELETE** /platform/3/sync/rules | 
[**delete_target_policy**](SyncApi.md#delete_target_policy) | **DELETE** /platform/1/sync/target/policies/{TargetPolicyId} | 
[**get_certificates_peer_by_id**](SyncApi.md#get_certificates_peer_by_id) | **GET** /platform/7/sync/certificates/peer/{CertificatesPeerId} | 
[**get_certificates_server_by_id**](SyncApi.md#get_certificates_server_by_id) | **GET** /platform/7/sync/certificates/server/{CertificatesServerId} | 
[**get_history_cpu**](SyncApi.md#get_history_cpu) | **GET** /platform/3/sync/history/cpu | 
[**get_history_file**](SyncApi.md#get_history_file) | **GET** /platform/1/sync/history/file | 
[**get_history_network**](SyncApi.md#get_history_network) | **GET** /platform/7/sync/history/network | 
[**get_history_worker**](SyncApi.md#get_history_worker) | **GET** /platform/3/sync/history/worker | 
[**get_service_policy**](SyncApi.md#get_service_policy) | **GET** /platform/7/sync/service/policies/{ServicePolicyId} | 
[**get_service_target_policies**](SyncApi.md#get_service_target_policies) | **GET** /platform/7/sync/service/target/policies | 
[**get_service_target_policy**](SyncApi.md#get_service_target_policy) | **GET** /platform/7/sync/service/target/policies/{ServiceTargetPolicyId} | 
[**get_sync_job**](SyncApi.md#get_sync_job) | **GET** /platform/7/sync/jobs/{SyncJobId} | 
[**get_sync_license**](SyncApi.md#get_sync_license) | **GET** /platform/5/sync/license | 
[**get_sync_policy**](SyncApi.md#get_sync_policy) | **GET** /platform/7/sync/policies/{SyncPolicyId} | 
[**get_sync_report**](SyncApi.md#get_sync_report) | **GET** /platform/7/sync/reports/{SyncReportId} | 
[**get_sync_reports**](SyncApi.md#get_sync_reports) | **GET** /platform/7/sync/reports | 
[**get_sync_rule**](SyncApi.md#get_sync_rule) | **GET** /platform/3/sync/rules/{SyncRuleId} | 
[**get_sync_settings**](SyncApi.md#get_sync_settings) | **GET** /platform/7/sync/settings | 
[**get_target_policies**](SyncApi.md#get_target_policies) | **GET** /platform/1/sync/target/policies | 
[**get_target_policy**](SyncApi.md#get_target_policy) | **GET** /platform/1/sync/target/policies/{TargetPolicyId} | 
[**get_target_report**](SyncApi.md#get_target_report) | **GET** /platform/7/sync/target/reports/{TargetReportId} | 
[**get_target_reports**](SyncApi.md#get_target_reports) | **GET** /platform/7/sync/target/reports | 
[**list_certificates_peer**](SyncApi.md#list_certificates_peer) | **GET** /platform/7/sync/certificates/peer | 
[**list_certificates_server**](SyncApi.md#list_certificates_server) | **GET** /platform/7/sync/certificates/server | 
[**list_service_policies**](SyncApi.md#list_service_policies) | **GET** /platform/7/sync/service/policies | 
[**list_sync_jobs**](SyncApi.md#list_sync_jobs) | **GET** /platform/7/sync/jobs | 
[**list_sync_policies**](SyncApi.md#list_sync_policies) | **GET** /platform/7/sync/policies | 
[**list_sync_reports_rotate**](SyncApi.md#list_sync_reports_rotate) | **GET** /platform/1/sync/reports-rotate | 
[**list_sync_rules**](SyncApi.md#list_sync_rules) | **GET** /platform/3/sync/rules | 
[**update_certificates_peer_by_id**](SyncApi.md#update_certificates_peer_by_id) | **PUT** /platform/7/sync/certificates/peer/{CertificatesPeerId} | 
[**update_certificates_server_by_id**](SyncApi.md#update_certificates_server_by_id) | **PUT** /platform/7/sync/certificates/server/{CertificatesServerId} | 
[**update_service_policy**](SyncApi.md#update_service_policy) | **PUT** /platform/7/sync/service/policies/{ServicePolicyId} | 
[**update_sync_job**](SyncApi.md#update_sync_job) | **PUT** /platform/7/sync/jobs/{SyncJobId} | 
[**update_sync_policy**](SyncApi.md#update_sync_policy) | **PUT** /platform/7/sync/policies/{SyncPolicyId} | 
[**update_sync_rule**](SyncApi.md#update_sync_rule) | **PUT** /platform/3/sync/rules/{SyncRuleId} | 
[**update_sync_settings**](SyncApi.md#update_sync_settings) | **PUT** /platform/7/sync/settings | 


# **create_certificates_peer_item**
> CreateResponse create_certificates_peer_item(certificates_peer_item)



Import a trusted SyncIQ TLS certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
certificates_peer_item = isi_sdk_9_0_0.CertificateAuthorityItem() # CertificateAuthorityItem | 

try:
    api_response = api_instance.create_certificates_peer_item(certificates_peer_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->create_certificates_peer_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_peer_item** | [**CertificateAuthorityItem**](CertificateAuthorityItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_certificates_server_item**
> CreateResponse create_certificates_server_item(certificates_server_item)



Import a SyncIQ TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
certificates_server_item = isi_sdk_9_0_0.CertificateServerItem() # CertificateServerItem | 

try:
    api_response = api_instance.create_certificates_server_item(certificates_server_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->create_certificates_server_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_server_item** | [**CertificateServerItem**](CertificateServerItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_service_policy**
> CreateResponse create_service_policy(service_policy)



Create a SyncIQ service replication policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
service_policy = isi_sdk_9_0_0.ServicePolicyCreateParams() # ServicePolicyCreateParams | 

try:
    api_response = api_instance.create_service_policy(service_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->create_service_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_policy** | [**ServicePolicyCreateParams**](ServicePolicyCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sync_job**
> CreateResponse create_sync_job(sync_job)



Start a SyncIQ job.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_job = isi_sdk_9_0_0.SyncJobCreateParams() # SyncJobCreateParams | 

try:
    api_response = api_instance.create_sync_job(sync_job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->create_sync_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_job** | [**SyncJobCreateParams**](SyncJobCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sync_policy**
> CreateResponse create_sync_policy(sync_policy)



Create a SyncIQ policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_policy = isi_sdk_9_0_0.SyncPolicyCreateParams() # SyncPolicyCreateParams | 

try:
    api_response = api_instance.create_sync_policy(sync_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->create_sync_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_policy** | [**SyncPolicyCreateParams**](SyncPolicyCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sync_reports_rotate_item**
> CreateSyncReportsRotateItemResponse create_sync_reports_rotate_item(sync_reports_rotate_item)



Rotate the records in the database(s).

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_reports_rotate_item = isi_sdk_9_0_0.Empty() # Empty | 

try:
    api_response = api_instance.create_sync_reports_rotate_item(sync_reports_rotate_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->create_sync_reports_rotate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_reports_rotate_item** | [**Empty**](Empty.md)|  | 

### Return type

[**CreateSyncReportsRotateItemResponse**](CreateSyncReportsRotateItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sync_rule**
> CreateResponse create_sync_rule(sync_rule)



Create a new SyncIQ performance rule.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_rule = isi_sdk_9_0_0.SyncRuleCreateParams() # SyncRuleCreateParams | 

try:
    api_response = api_instance.create_sync_rule(sync_rule)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->create_sync_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_rule** | [**SyncRuleCreateParams**](SyncRuleCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificates_peer_by_id**
> delete_certificates_peer_by_id(certificates_peer_id)



Delete a trusted SyncIQ TLS certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
certificates_peer_id = 'certificates_peer_id_example' # str | Delete a trusted SyncIQ TLS certificate.

try:
    api_instance.delete_certificates_peer_by_id(certificates_peer_id)
except ApiException as e:
    print("Exception when calling SyncApi->delete_certificates_peer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_peer_id** | **str**| Delete a trusted SyncIQ TLS certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificates_server_by_id**
> delete_certificates_server_by_id(certificates_server_id)



Delete a SyncIQ TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
certificates_server_id = 'certificates_server_id_example' # str | Delete a SyncIQ TLS server certificate.

try:
    api_instance.delete_certificates_server_by_id(certificates_server_id)
except ApiException as e:
    print("Exception when calling SyncApi->delete_certificates_server_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_server_id** | **str**| Delete a SyncIQ TLS server certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_policies**
> delete_service_policies(local_only=local_only, force=force)



Delete all SyncIQ service replication policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
local_only = true # bool | Skip deleting the policy association on the target. (optional)
force = true # bool | Ignore any running jobs when preparing to delete a policy. (optional)

try:
    api_instance.delete_service_policies(local_only=local_only, force=force)
except ApiException as e:
    print("Exception when calling SyncApi->delete_service_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_only** | **bool**| Skip deleting the policy association on the target. | [optional] 
 **force** | **bool**| Ignore any running jobs when preparing to delete a policy. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_policy**
> delete_service_policy(service_policy_id, local_only=local_only, force=force)



Delete a single SyncIQ service replication policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
service_policy_id = 'service_policy_id_example' # str | Delete a single SyncIQ service replication policy.
local_only = true # bool | Skip deleting the policy association on the target. (optional)
force = true # bool | Ignore any running jobs when preparing to delete a policy. (optional)

try:
    api_instance.delete_service_policy(service_policy_id, local_only=local_only, force=force)
except ApiException as e:
    print("Exception when calling SyncApi->delete_service_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_policy_id** | **str**| Delete a single SyncIQ service replication policy. | 
 **local_only** | **bool**| Skip deleting the policy association on the target. | [optional] 
 **force** | **bool**| Ignore any running jobs when preparing to delete a policy. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_target_policy**
> delete_service_target_policy(service_target_policy_id, force=force)



Break the target association with this cluster for this policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
service_target_policy_id = 'service_target_policy_id_example' # str | Break the target association with this cluster for this policy.
force = true # bool | Ignore any running jobs when preparing to delete the policy target association. (optional)

try:
    api_instance.delete_service_target_policy(service_target_policy_id, force=force)
except ApiException as e:
    print("Exception when calling SyncApi->delete_service_target_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_target_policy_id** | **str**| Break the target association with this cluster for this policy. | 
 **force** | **bool**| Ignore any running jobs when preparing to delete the policy target association. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sync_jobs**
> delete_sync_jobs()



Cancel all SyncIQ jobs.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_instance.delete_sync_jobs()
except ApiException as e:
    print("Exception when calling SyncApi->delete_sync_jobs: %s\n" % e)
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

# **delete_sync_policies**
> delete_sync_policies(local_only=local_only, force=force)



Delete all SyncIQ policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
local_only = true # bool | Skip deleting the policy association on the target. (optional)
force = true # bool | Ignore any running jobs when preparing to delete a policy. (optional)

try:
    api_instance.delete_sync_policies(local_only=local_only, force=force)
except ApiException as e:
    print("Exception when calling SyncApi->delete_sync_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_only** | **bool**| Skip deleting the policy association on the target. | [optional] 
 **force** | **bool**| Ignore any running jobs when preparing to delete a policy. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sync_policy**
> delete_sync_policy(sync_policy_id, local_only=local_only, force=force)



Delete a single SyncIQ policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_policy_id = 'sync_policy_id_example' # str | Delete a single SyncIQ policy.
local_only = true # bool | Skip deleting the policy association on the target. (optional)
force = true # bool | Ignore any running jobs when preparing to delete a policy. (optional)

try:
    api_instance.delete_sync_policy(sync_policy_id, local_only=local_only, force=force)
except ApiException as e:
    print("Exception when calling SyncApi->delete_sync_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_policy_id** | **str**| Delete a single SyncIQ policy. | 
 **local_only** | **bool**| Skip deleting the policy association on the target. | [optional] 
 **force** | **bool**| Ignore any running jobs when preparing to delete a policy. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sync_rule**
> delete_sync_rule(sync_rule_id)



Delete a single SyncIQ performance rule.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_rule_id = 'sync_rule_id_example' # str | Delete a single SyncIQ performance rule.

try:
    api_instance.delete_sync_rule(sync_rule_id)
except ApiException as e:
    print("Exception when calling SyncApi->delete_sync_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_rule_id** | **str**| Delete a single SyncIQ performance rule. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sync_rules**
> delete_sync_rules(type=type)



Delete all SyncIQ performance rules or all rules of a specified type.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
type = 'type_example' # str | Delete all rules of the specified rule type only. (optional)

try:
    api_instance.delete_sync_rules(type=type)
except ApiException as e:
    print("Exception when calling SyncApi->delete_sync_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Delete all rules of the specified rule type only. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_target_policy**
> delete_target_policy(target_policy_id, force=force)



Break the target association with this cluster for this policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
target_policy_id = 'target_policy_id_example' # str | Break the target association with this cluster for this policy.
force = true # bool | Ignore any running jobs when preparing to delete the policy target association. (optional)

try:
    api_instance.delete_target_policy(target_policy_id, force=force)
except ApiException as e:
    print("Exception when calling SyncApi->delete_target_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_policy_id** | **str**| Break the target association with this cluster for this policy. | 
 **force** | **bool**| Ignore any running jobs when preparing to delete the policy target association. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificates_peer_by_id**
> CertificateAuthority get_certificates_peer_by_id(certificates_peer_id)



Retrieve a single trusted SyncIQ TLS certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
certificates_peer_id = 'certificates_peer_id_example' # str | Retrieve a single trusted SyncIQ TLS certificate.

try:
    api_response = api_instance.get_certificates_peer_by_id(certificates_peer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_certificates_peer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_peer_id** | **str**| Retrieve a single trusted SyncIQ TLS certificate. | 

### Return type

[**CertificateAuthority**](CertificateAuthority.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificates_server_by_id**
> CertificateServer get_certificates_server_by_id(certificates_server_id)



Retrieve a SyncIQ TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
certificates_server_id = 'certificates_server_id_example' # str | Retrieve a SyncIQ TLS server certificate.

try:
    api_response = api_instance.get_certificates_server_by_id(certificates_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_certificates_server_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_server_id** | **str**| Retrieve a SyncIQ TLS server certificate. | 

### Return type

[**CertificateServer**](CertificateServer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_cpu**
> HistoryFile get_history_cpu(begin=begin, end=end)



List cpu performance data.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
begin = 56 # int | Begin timestamp for time-series report. (optional)
end = 56 # int | End timestamp for time-series report. (optional)

try:
    api_response = api_instance.get_history_cpu(begin=begin, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_history_cpu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Begin timestamp for time-series report. | [optional] 
 **end** | **int**| End timestamp for time-series report. | [optional] 

### Return type

[**HistoryFile**](HistoryFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_file**
> HistoryFile get_history_file(begin=begin, end=end)



List file operations performance data.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
begin = 56 # int | Begin timestamp for time-series report. (optional)
end = 56 # int | End timestamp for time-series report. (optional)

try:
    api_response = api_instance.get_history_file(begin=begin, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_history_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Begin timestamp for time-series report. | [optional] 
 **end** | **int**| End timestamp for time-series report. | [optional] 

### Return type

[**HistoryFile**](HistoryFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_network**
> HistoryFile get_history_network(running_jobs=running_jobs, end=end, start=start, policy_id=policy_id)



List network operations performance data.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
running_jobs = true # bool | Receive network history for all currently running SyncIQ jobs. (optional)
end = 56 # int | End timestamp for time-series report. (optional)
start = 56 # int | Begin timestamp for time-series report. (optional)
policy_id = 'policy_id_example' # str | Receive network history for only the given policy. (optional)

try:
    api_response = api_instance.get_history_network(running_jobs=running_jobs, end=end, start=start, policy_id=policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_history_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **running_jobs** | **bool**| Receive network history for all currently running SyncIQ jobs. | [optional] 
 **end** | **int**| End timestamp for time-series report. | [optional] 
 **start** | **int**| Begin timestamp for time-series report. | [optional] 
 **policy_id** | **str**| Receive network history for only the given policy. | [optional] 

### Return type

[**HistoryFile**](HistoryFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_worker**
> HistoryFile get_history_worker(begin=begin, end=end)



List worker performance data.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
begin = 56 # int | Begin timestamp for time-series report. (optional)
end = 56 # int | End timestamp for time-series report. (optional)

try:
    api_response = api_instance.get_history_worker(begin=begin, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_history_worker: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Begin timestamp for time-series report. | [optional] 
 **end** | **int**| End timestamp for time-series report. | [optional] 

### Return type

[**HistoryFile**](HistoryFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_policy**
> ServicePolicies get_service_policy(service_policy_id)



View a single SyncIQ service replication policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
service_policy_id = 'service_policy_id_example' # str | View a single SyncIQ service replication policy.

try:
    api_response = api_instance.get_service_policy(service_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_service_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_policy_id** | **str**| View a single SyncIQ service replication policy. | 

### Return type

[**ServicePolicies**](ServicePolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_target_policies**
> TargetPoliciesExtended get_service_target_policies(sort=sort, target_path=target_path, limit=limit, dir=dir, resume=resume)



List all SyncIQ target service replication policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
target_path = 'target_path_example' # str | Filter the returned policies to include only those with this target path. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_service_target_policies(sort=sort, target_path=target_path, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_service_target_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **target_path** | **str**| Filter the returned policies to include only those with this target path. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**TargetPoliciesExtended**](TargetPoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_target_policy**
> TargetPolicies get_service_target_policy(service_target_policy_id)



View a single SyncIQ target service replication policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
service_target_policy_id = 'service_target_policy_id_example' # str | View a single SyncIQ target service replication policy.

try:
    api_response = api_instance.get_service_target_policy(service_target_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_service_target_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_target_policy_id** | **str**| View a single SyncIQ target service replication policy. | 

### Return type

[**TargetPolicies**](TargetPolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_job**
> SyncJobs get_sync_job(sync_job_id)



View a single SyncIQ job.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_job_id = 'sync_job_id_example' # str | View a single SyncIQ job.

try:
    api_response = api_instance.get_sync_job(sync_job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_sync_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_job_id** | **str**| View a single SyncIQ job. | 

### Return type

[**SyncJobs**](SyncJobs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_license**
> LicenseLicense get_sync_license()



Retrieve license information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_sync_license()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_sync_license: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseLicense**](LicenseLicense.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_policy**
> SyncPolicies get_sync_policy(sync_policy_id)



View a single SyncIQ policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_policy_id = 'sync_policy_id_example' # str | View a single SyncIQ policy.

try:
    api_response = api_instance.get_sync_policy(sync_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_sync_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_policy_id** | **str**| View a single SyncIQ policy. | 

### Return type

[**SyncPolicies**](SyncPolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_report**
> SyncReports get_sync_report(sync_report_id)



View a single SyncIQ report.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_report_id = 'sync_report_id_example' # str | View a single SyncIQ report.

try:
    api_response = api_instance.get_sync_report(sync_report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_sync_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_report_id** | **str**| View a single SyncIQ report. | 

### Return type

[**SyncReports**](SyncReports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_reports**
> SyncReportsExtended get_sync_reports(sort=sort, resume=resume, newer_than=newer_than, policy_name=policy_name, state=state, limit=limit, reports_per_policy=reports_per_policy, summary=summary, dir=dir)



Get a list of SyncIQ reports.  By default 1 report is returned per policy, unless otherwise specified by 'reports_per_policy'.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
newer_than = 56 # int | Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago. (optional)
policy_name = 'policy_name_example' # str | Filter the returned reports to include only those with this policy name. (optional)
state = 'state_example' # str | Filter the returned reports to include only those whose jobs are in this state. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
reports_per_policy = 56 # int | If specified, only the N most recent reports will be returned per policy.  If no other query args are present this argument defaults to 1.  (optional)
summary = true # bool | Return a summary rather than entire objects (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_sync_reports(sort=sort, resume=resume, newer_than=newer_than, policy_name=policy_name, state=state, limit=limit, reports_per_policy=reports_per_policy, summary=summary, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_sync_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **newer_than** | **int**| Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago. | [optional] 
 **policy_name** | **str**| Filter the returned reports to include only those with this policy name. | [optional] 
 **state** | **str**| Filter the returned reports to include only those whose jobs are in this state. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **reports_per_policy** | **int**| If specified, only the N most recent reports will be returned per policy.  If no other query args are present this argument defaults to 1.  | [optional] 
 **summary** | **bool**| Return a summary rather than entire objects | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**SyncReportsExtended**](SyncReportsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_rule**
> SyncRules get_sync_rule(sync_rule_id)



View a single SyncIQ performance rule.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_rule_id = 'sync_rule_id_example' # str | View a single SyncIQ performance rule.

try:
    api_response = api_instance.get_sync_rule(sync_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_sync_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_rule_id** | **str**| View a single SyncIQ performance rule. | 

### Return type

[**SyncRules**](SyncRules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sync_settings**
> SyncSettings get_sync_settings()



Retrieve the global SyncIQ settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_sync_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_sync_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SyncSettings**](SyncSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_policies**
> TargetPoliciesExtended get_target_policies(sort=sort, target_path=target_path, limit=limit, dir=dir, resume=resume)



List all SyncIQ target policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
target_path = 'target_path_example' # str | Filter the returned policies to include only those with this target path. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_target_policies(sort=sort, target_path=target_path, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_target_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **target_path** | **str**| Filter the returned policies to include only those with this target path. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**TargetPoliciesExtended**](TargetPoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_policy**
> TargetPolicies get_target_policy(target_policy_id)



View a single SyncIQ target policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
target_policy_id = 'target_policy_id_example' # str | View a single SyncIQ target policy.

try:
    api_response = api_instance.get_target_policy(target_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_target_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_policy_id** | **str**| View a single SyncIQ target policy. | 

### Return type

[**TargetPolicies**](TargetPolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_report**
> TargetReports get_target_report(target_report_id)



View a single SyncIQ target report.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
target_report_id = 'target_report_id_example' # str | View a single SyncIQ target report.

try:
    api_response = api_instance.get_target_report(target_report_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_target_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target_report_id** | **str**| View a single SyncIQ target report. | 

### Return type

[**TargetReports**](TargetReports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_target_reports**
> TargetReportsExtended get_target_reports(sort=sort, resume=resume, newer_than=newer_than, policy_name=policy_name, state=state, limit=limit, reports_per_policy=reports_per_policy, summary=summary, dir=dir)



Get a list of SyncIQ target reports.  By default 1 report is returned per policy, unless otherwise specified by 'reports_per_policy'.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
newer_than = 56 # int | Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago. (optional)
policy_name = 'policy_name_example' # str | Filter the returned reports to include only those with this policy name. (optional)
state = 'state_example' # str | Filter the returned reports to include only those whose jobs are in this state. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
reports_per_policy = 56 # int | If specified, only the N most recent reports will be returned per policy.  If no other query args are present this argument defaults to 1.  (optional)
summary = true # bool | Return a summary rather than entire objects. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_target_reports(sort=sort, resume=resume, newer_than=newer_than, policy_name=policy_name, state=state, limit=limit, reports_per_policy=reports_per_policy, summary=summary, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->get_target_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **newer_than** | **int**| Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago. | [optional] 
 **policy_name** | **str**| Filter the returned reports to include only those with this policy name. | [optional] 
 **state** | **str**| Filter the returned reports to include only those whose jobs are in this state. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **reports_per_policy** | **int**| If specified, only the N most recent reports will be returned per policy.  If no other query args are present this argument defaults to 1.  | [optional] 
 **summary** | **bool**| Return a summary rather than entire objects. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**TargetReportsExtended**](TargetReportsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificates_peer**
> CertificateAuthorityExtended list_certificates_peer(sort=sort, limit=limit, dir=dir, resume=resume)



Retrieve a list of all trusted SyncIQ peer TLS certificates.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_certificates_peer(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->list_certificates_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**CertificateAuthorityExtended**](CertificateAuthorityExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificates_server**
> CertificateServerExtended list_certificates_server(sort=sort, limit=limit, dir=dir, resume=resume)



Retrieve a list of all SyncIQ TLS server certificates.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_certificates_server(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->list_certificates_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**CertificateServerExtended**](CertificateServerExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_policies**
> ServicePoliciesExtended list_service_policies(sort=sort, resume=resume, summary=summary, limit=limit, scope=scope, dir=dir)



List all SyncIQ service replication policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
summary = true # bool | Return a summary rather than entire objects. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_service_policies(sort=sort, resume=resume, summary=summary, limit=limit, scope=scope, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->list_service_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **summary** | **bool**| Return a summary rather than entire objects. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**ServicePoliciesExtended**](ServicePoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sync_jobs**
> SyncJobsExtended list_sync_jobs(sort=sort, state=state, limit=limit, dir=dir, resume=resume)



Get a list of SyncIQ jobs.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
state = 'state_example' # str | The state of the job. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_sync_jobs(sort=sort, state=state, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->list_sync_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **state** | **str**| The state of the job. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SyncJobsExtended**](SyncJobsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sync_policies**
> SyncPoliciesExtended list_sync_policies(sort=sort, resume=resume, summary=summary, limit=limit, scope=scope, dir=dir)



List all SyncIQ policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
summary = true # bool | Return a summary rather than entire objects. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_sync_policies(sort=sort, resume=resume, summary=summary, limit=limit, scope=scope, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->list_sync_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **summary** | **bool**| Return a summary rather than entire objects. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**SyncPoliciesExtended**](SyncPoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sync_reports_rotate**
> SyncReportsRotate list_sync_reports_rotate()



Whether the rotation is still running or not.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.list_sync_reports_rotate()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->list_sync_reports_rotate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SyncReportsRotate**](SyncReportsRotate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sync_rules**
> SyncRulesExtended list_sync_rules(sort=sort, type=type, limit=limit, dir=dir, resume=resume)



List all SyncIQ performance rules.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
type = 'type_example' # str | Filter the returned rules to include only those with this rule type. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_sync_rules(sort=sort, type=type, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncApi->list_sync_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **type** | **str**| Filter the returned rules to include only those with this rule type. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SyncRulesExtended**](SyncRulesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificates_peer_by_id**
> update_certificates_peer_by_id(certificates_peer_id_params, certificates_peer_id)



Modify a trusted SyncIQ TLS certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
certificates_peer_id_params = isi_sdk_9_0_0.CertificateServerIdParams() # CertificateServerIdParams | 
certificates_peer_id = 'certificates_peer_id_example' # str | Modify a trusted SyncIQ TLS certificate.

try:
    api_instance.update_certificates_peer_by_id(certificates_peer_id_params, certificates_peer_id)
except ApiException as e:
    print("Exception when calling SyncApi->update_certificates_peer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_peer_id_params** | [**CertificateServerIdParams**](CertificateServerIdParams.md)|  | 
 **certificates_peer_id** | **str**| Modify a trusted SyncIQ TLS certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificates_server_by_id**
> update_certificates_server_by_id(certificates_server_id_params, certificates_server_id)



Modify a SyncIQ TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
certificates_server_id_params = isi_sdk_9_0_0.CertificateServerIdParams() # CertificateServerIdParams | 
certificates_server_id = 'certificates_server_id_example' # str | Modify a SyncIQ TLS server certificate.

try:
    api_instance.update_certificates_server_by_id(certificates_server_id_params, certificates_server_id)
except ApiException as e:
    print("Exception when calling SyncApi->update_certificates_server_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificates_server_id_params** | [**CertificateServerIdParams**](CertificateServerIdParams.md)|  | 
 **certificates_server_id** | **str**| Modify a SyncIQ TLS server certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_policy**
> update_service_policy(service_policy, service_policy_id)



Modify a single SyncIQ service replication policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
service_policy = isi_sdk_9_0_0.ServicePolicy() # ServicePolicy | 
service_policy_id = 'service_policy_id_example' # str | Modify a single SyncIQ service replication policy.

try:
    api_instance.update_service_policy(service_policy, service_policy_id)
except ApiException as e:
    print("Exception when calling SyncApi->update_service_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_policy** | [**ServicePolicy**](ServicePolicy.md)|  | 
 **service_policy_id** | **str**| Modify a single SyncIQ service replication policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sync_job**
> update_sync_job(sync_job, sync_job_id)



Perform an action (pause, cancel, etc...) on a single job.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_job = isi_sdk_9_0_0.SyncJob() # SyncJob | 
sync_job_id = 'sync_job_id_example' # str | Perform an action (pause, cancel, etc...) on a single job.

try:
    api_instance.update_sync_job(sync_job, sync_job_id)
except ApiException as e:
    print("Exception when calling SyncApi->update_sync_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_job** | [**SyncJob**](SyncJob.md)|  | 
 **sync_job_id** | **str**| Perform an action (pause, cancel, etc...) on a single job. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sync_policy**
> update_sync_policy(sync_policy, sync_policy_id)



Modify a single SyncIQ policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_policy = isi_sdk_9_0_0.SyncPolicy() # SyncPolicy | 
sync_policy_id = 'sync_policy_id_example' # str | Modify a single SyncIQ policy.

try:
    api_instance.update_sync_policy(sync_policy, sync_policy_id)
except ApiException as e:
    print("Exception when calling SyncApi->update_sync_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_policy** | [**SyncPolicy**](SyncPolicy.md)|  | 
 **sync_policy_id** | **str**| Modify a single SyncIQ policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sync_rule**
> update_sync_rule(sync_rule, sync_rule_id)



Modify a single SyncIQ performance rule.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_rule = isi_sdk_9_0_0.SyncRule() # SyncRule | 
sync_rule_id = 'sync_rule_id_example' # str | Modify a single SyncIQ performance rule.

try:
    api_instance.update_sync_rule(sync_rule, sync_rule_id)
except ApiException as e:
    print("Exception when calling SyncApi->update_sync_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_rule** | [**SyncRule**](SyncRule.md)|  | 
 **sync_rule_id** | **str**| Modify a single SyncIQ performance rule. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sync_settings**
> update_sync_settings(sync_settings)



Modify the global SyncIQ settings.  All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.SyncApi(isi_sdk_9_0_0.ApiClient(configuration))
sync_settings = isi_sdk_9_0_0.SyncSettingsExtended() # SyncSettingsExtended | 

try:
    api_instance.update_sync_settings(sync_settings)
except ApiException as e:
    print("Exception when calling SyncApi->update_sync_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_settings** | [**SyncSettingsExtended**](SyncSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

