# isi_sdk_9_0_0.FilepoolApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filepool_policy**](FilepoolApi.md#create_filepool_policy) | **POST** /platform/4/filepool/policies | 
[**delete_filepool_policy**](FilepoolApi.md#delete_filepool_policy) | **DELETE** /platform/4/filepool/policies/{FilepoolPolicyId} | 
[**get_filepool_default_policy**](FilepoolApi.md#get_filepool_default_policy) | **GET** /platform/4/filepool/default-policy | 
[**get_filepool_policy**](FilepoolApi.md#get_filepool_policy) | **GET** /platform/4/filepool/policies/{FilepoolPolicyId} | 
[**get_filepool_template**](FilepoolApi.md#get_filepool_template) | **GET** /platform/4/filepool/templates/{FilepoolTemplateId} | 
[**get_filepool_templates**](FilepoolApi.md#get_filepool_templates) | **GET** /platform/4/filepool/templates | 
[**list_filepool_policies**](FilepoolApi.md#list_filepool_policies) | **GET** /platform/4/filepool/policies | 
[**update_filepool_default_policy**](FilepoolApi.md#update_filepool_default_policy) | **PUT** /platform/4/filepool/default-policy | 
[**update_filepool_policy**](FilepoolApi.md#update_filepool_policy) | **PUT** /platform/4/filepool/policies/{FilepoolPolicyId} | 


# **create_filepool_policy**
> CreateFilepoolPolicyResponse create_filepool_policy(filepool_policy)



Create a new policy.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))
filepool_policy = isi_sdk_9_0_0.FilepoolPolicyCreateParams() # FilepoolPolicyCreateParams | 

try:
    api_response = api_instance.create_filepool_policy(filepool_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilepoolApi->create_filepool_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_policy** | [**FilepoolPolicyCreateParams**](FilepoolPolicyCreateParams.md)|  | 

### Return type

[**CreateFilepoolPolicyResponse**](CreateFilepoolPolicyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filepool_policy**
> delete_filepool_policy(filepool_policy_id)



Delete file pool policy.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))
filepool_policy_id = 'filepool_policy_id_example' # str | Delete file pool policy.

try:
    api_instance.delete_filepool_policy(filepool_policy_id)
except ApiException as e:
    print("Exception when calling FilepoolApi->delete_filepool_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_policy_id** | **str**| Delete file pool policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filepool_default_policy**
> FilepoolDefaultPolicy get_filepool_default_policy()



List default file pool policy.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_filepool_default_policy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilepoolApi->get_filepool_default_policy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilepoolDefaultPolicy**](FilepoolDefaultPolicy.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filepool_policy**
> FilepoolPolicies get_filepool_policy(filepool_policy_id)



Retrieve file pool policy information.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))
filepool_policy_id = 'filepool_policy_id_example' # str | Retrieve file pool policy information.

try:
    api_response = api_instance.get_filepool_policy(filepool_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilepoolApi->get_filepool_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_policy_id** | **str**| Retrieve file pool policy information. | 

### Return type

[**FilepoolPolicies**](FilepoolPolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filepool_template**
> FilepoolTemplates get_filepool_template(filepool_template_id)



List all templates.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))
filepool_template_id = 'filepool_template_id_example' # str | List all templates.

try:
    api_response = api_instance.get_filepool_template(filepool_template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilepoolApi->get_filepool_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_template_id** | **str**| List all templates. | 

### Return type

[**FilepoolTemplates**](FilepoolTemplates.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filepool_templates**
> FilepoolTemplatesExtended get_filepool_templates()



List all templates.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_filepool_templates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilepoolApi->get_filepool_templates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilepoolTemplatesExtended**](FilepoolTemplatesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_filepool_policies**
> FilepoolPoliciesExtended list_filepool_policies()



List all policies.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.list_filepool_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FilepoolApi->list_filepool_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilepoolPoliciesExtended**](FilepoolPoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filepool_default_policy**
> update_filepool_default_policy(filepool_default_policy)



Set default file pool policy.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))
filepool_default_policy = isi_sdk_9_0_0.FilepoolDefaultPolicyExtended() # FilepoolDefaultPolicyExtended | 

try:
    api_instance.update_filepool_default_policy(filepool_default_policy)
except ApiException as e:
    print("Exception when calling FilepoolApi->update_filepool_default_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_default_policy** | [**FilepoolDefaultPolicyExtended**](FilepoolDefaultPolicyExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filepool_policy**
> update_filepool_policy(filepool_policy, filepool_policy_id)



Modify file pool policy. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_9_0_0.FilepoolApi(isi_sdk_9_0_0.ApiClient(configuration))
filepool_policy = isi_sdk_9_0_0.FilepoolPolicy() # FilepoolPolicy | 
filepool_policy_id = 'filepool_policy_id_example' # str | Modify file pool policy. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_filepool_policy(filepool_policy, filepool_policy_id)
except ApiException as e:
    print("Exception when calling FilepoolApi->update_filepool_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_policy** | [**FilepoolPolicy**](FilepoolPolicy.md)|  | 
 **filepool_policy_id** | **str**| Modify file pool policy. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

