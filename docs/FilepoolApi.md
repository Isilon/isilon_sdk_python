# isi_sdk.FilepoolApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_filepool_policy**](FilepoolApi.md#create_filepool_policy) | **POST** /platform/1/filepool/policies | 
[**delete_filepool_policy**](FilepoolApi.md#delete_filepool_policy) | **DELETE** /platform/1/filepool/policies/{FilepoolPolicyId} | 
[**get_filepool_default_policy**](FilepoolApi.md#get_filepool_default_policy) | **GET** /platform/1/filepool/default-policy | 
[**get_filepool_policy**](FilepoolApi.md#get_filepool_policy) | **GET** /platform/1/filepool/policies/{FilepoolPolicyId} | 
[**get_filepool_template**](FilepoolApi.md#get_filepool_template) | **GET** /platform/1/filepool/templates/{FilepoolTemplateId} | 
[**get_filepool_templates**](FilepoolApi.md#get_filepool_templates) | **GET** /platform/1/filepool/templates | 
[**list_filepool_policies**](FilepoolApi.md#list_filepool_policies) | **GET** /platform/1/filepool/policies | 
[**update_filepool_default_policy**](FilepoolApi.md#update_filepool_default_policy) | **PUT** /platform/1/filepool/default-policy | 
[**update_filepool_policy**](FilepoolApi.md#update_filepool_policy) | **PUT** /platform/1/filepool/policies/{FilepoolPolicyId} | 


# **create_filepool_policy**
> CreateFilepoolPolicyResponse create_filepool_policy(filepool_policy)



Create a new policy.

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
api_instance = isi_sdk.FilepoolApi()
filepool_policy = isi_sdk.FilepoolPolicyCreateParams() # FilepoolPolicyCreateParams | 

try: 
    api_response = api_instance.create_filepool_policy(filepool_policy)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilepoolApi->create_filepool_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_policy** | [**FilepoolPolicyCreateParams**](FilepoolPolicyCreateParams.md)|  | 

### Return type

[**CreateFilepoolPolicyResponse**](CreateFilepoolPolicyResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_filepool_policy**
> delete_filepool_policy(filepool_policy_id)



Delete file pool policy.

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
api_instance = isi_sdk.FilepoolApi()
filepool_policy_id = 'filepool_policy_id_example' # str | Delete file pool policy.

try: 
    api_instance.delete_filepool_policy(filepool_policy_id)
except ApiException as e:
    print "Exception when calling FilepoolApi->delete_filepool_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_policy_id** | **str**| Delete file pool policy. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filepool_default_policy**
> FilepoolDefaultPolicy get_filepool_default_policy()



List default file pool policy.

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
api_instance = isi_sdk.FilepoolApi()

try: 
    api_response = api_instance.get_filepool_default_policy()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilepoolApi->get_filepool_default_policy: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilepoolDefaultPolicy**](FilepoolDefaultPolicy.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filepool_policy**
> FilepoolPolicies get_filepool_policy(filepool_policy_id)



Retrieve file pool policy information.

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
api_instance = isi_sdk.FilepoolApi()
filepool_policy_id = 'filepool_policy_id_example' # str | Retrieve file pool policy information.

try: 
    api_response = api_instance.get_filepool_policy(filepool_policy_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilepoolApi->get_filepool_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_policy_id** | **str**| Retrieve file pool policy information. | 

### Return type

[**FilepoolPolicies**](FilepoolPolicies.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filepool_template**
> FilepoolTemplates get_filepool_template(filepool_template_id)



List all templates.

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
api_instance = isi_sdk.FilepoolApi()
filepool_template_id = 'filepool_template_id_example' # str | List all templates.

try: 
    api_response = api_instance.get_filepool_template(filepool_template_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilepoolApi->get_filepool_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_template_id** | **str**| List all templates. | 

### Return type

[**FilepoolTemplates**](FilepoolTemplates.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_filepool_templates**
> FilepoolTemplates get_filepool_templates()



List all templates.

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
api_instance = isi_sdk.FilepoolApi()

try: 
    api_response = api_instance.get_filepool_templates()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilepoolApi->get_filepool_templates: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilepoolTemplates**](FilepoolTemplates.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_filepool_policies**
> FilepoolPoliciesExtended list_filepool_policies()



List all policies.

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
api_instance = isi_sdk.FilepoolApi()

try: 
    api_response = api_instance.list_filepool_policies()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilepoolApi->list_filepool_policies: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FilepoolPoliciesExtended**](FilepoolPoliciesExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filepool_default_policy**
> update_filepool_default_policy(filepool_default_policy)



Set default file pool policy.

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
api_instance = isi_sdk.FilepoolApi()
filepool_default_policy = isi_sdk.FilepoolDefaultPolicyExtended() # FilepoolDefaultPolicyExtended | 

try: 
    api_instance.update_filepool_default_policy(filepool_default_policy)
except ApiException as e:
    print "Exception when calling FilepoolApi->update_filepool_default_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_default_policy** | [**FilepoolDefaultPolicyExtended**](FilepoolDefaultPolicyExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_filepool_policy**
> update_filepool_policy(filepool_policy, filepool_policy_id)



Modify file pool policy. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.FilepoolApi()
filepool_policy = isi_sdk.FilepoolPolicy() # FilepoolPolicy | 
filepool_policy_id = 'filepool_policy_id_example' # str | Modify file pool policy. All input fields are optional, but one or more must be supplied.

try: 
    api_instance.update_filepool_policy(filepool_policy, filepool_policy_id)
except ApiException as e:
    print "Exception when calling FilepoolApi->update_filepool_policy: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filepool_policy** | [**FilepoolPolicy**](FilepoolPolicy.md)|  | 
 **filepool_policy_id** | **str**| Modify file pool policy. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

