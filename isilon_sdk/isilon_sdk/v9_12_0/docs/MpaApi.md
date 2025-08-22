# isilon_sdk.v9_12_0.MpaApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mpa_approval_by_id**](MpaApi.md#create_mpa_approval_by_id) | **POST** /platform/23/mpa/approval/{MpaApprovalId} | 
[**create_mpa_initiate_registration_item**](MpaApi.md#create_mpa_initiate_registration_item) | **POST** /platform/23/mpa/initiate-registration | 
[**create_mpa_request**](MpaApi.md#create_mpa_request) | **POST** /platform/23/mpa/requests | 
[**create_mpa_trust_anchor**](MpaApi.md#create_mpa_trust_anchor) | **POST** /platform/23/mpa/trust-anchors | 
[**get_mpa_approver**](MpaApi.md#get_mpa_approver) | **GET** /platform/23/mpa/approvers/{MpaApproverId} | 
[**get_mpa_approvers**](MpaApi.md#get_mpa_approvers) | **GET** /platform/23/mpa/approvers | 
[**get_mpa_request**](MpaApi.md#get_mpa_request) | **GET** /platform/23/mpa/requests/{MpaRequestId} | 
[**get_settings_config_request_lifecycle**](MpaApi.md#get_settings_config_request_lifecycle) | **GET** /platform/23/mpa/settings/config/request-lifecycle | 
[**get_settings_global**](MpaApi.md#get_settings_global) | **GET** /platform/23/mpa/settings/global | 
[**get_settings_privilege_action_metadata**](MpaApi.md#get_settings_privilege_action_metadata) | **GET** /platform/23/mpa/settings/privilege-action/metadata | 
[**list_mpa_requests**](MpaApi.md#list_mpa_requests) | **GET** /platform/23/mpa/requests | 
[**list_mpa_trust_anchors**](MpaApi.md#list_mpa_trust_anchors) | **GET** /platform/23/mpa/trust-anchors | 
[**update_mpa_complete_registration**](MpaApi.md#update_mpa_complete_registration) | **PUT** /platform/23/mpa/complete-registration | 
[**update_mpa_request**](MpaApi.md#update_mpa_request) | **PUT** /platform/23/mpa/requests/{MpaRequestId} | 
[**update_mpa_signed_approval_by_id**](MpaApi.md#update_mpa_signed_approval_by_id) | **PUT** /platform/23/mpa/signed-approval/{MpaSignedApprovalId} | 
[**update_settings_global**](MpaApi.md#update_settings_global) | **PUT** /platform/23/mpa/settings/global | 


# **create_mpa_approval_by_id**
> Empty create_mpa_approval_by_id(mpa_approval_id, mpa_approval_id2, zone=zone)



MPA request approval decision.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_approval_id = isilon_sdk.v9_12_0.MpaApprovalId() # MpaApprovalId | 
mpa_approval_id2 = 'mpa_approval_id_example' # str | MPA request approval decision.
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.create_mpa_approval_by_id(mpa_approval_id, mpa_approval_id2, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->create_mpa_approval_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_approval_id** | [**MpaApprovalId**](MpaApprovalId.md)|  | 
 **mpa_approval_id2** | **str**| MPA request approval decision. | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mpa_initiate_registration_item**
> CreateMpaInitiateRegistrationItemResponse create_mpa_initiate_registration_item(mpa_initiate_registration_item, force=force)



Specifies the properties to initiate approver registration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_initiate_registration_item = isilon_sdk.v9_12_0.Empty() # Empty | 
force = true # bool | Flag to force approver registration re-initiation. (optional)

try:
    api_response = api_instance.create_mpa_initiate_registration_item(mpa_initiate_registration_item, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->create_mpa_initiate_registration_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_initiate_registration_item** | [**Empty**](Empty.md)|  | 
 **force** | **bool**| Flag to force approver registration re-initiation. | [optional] 

### Return type

[**CreateMpaInitiateRegistrationItemResponse**](CreateMpaInitiateRegistrationItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mpa_request**
> CreateMpaRequestResponse create_mpa_request(mpa_request, zone=zone)



Create a new MPA Request.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_request = isilon_sdk.v9_12_0.MpaRequestCreateParams() # MpaRequestCreateParams | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.create_mpa_request(mpa_request, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->create_mpa_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_request** | [**MpaRequestCreateParams**](MpaRequestCreateParams.md)|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**CreateMpaRequestResponse**](CreateMpaRequestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mpa_trust_anchor**
> CreateMpaTrustAnchorResponse create_mpa_trust_anchor(mpa_trust_anchor, force=force)



Upload trusted root CA for MPA

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_trust_anchor = isilon_sdk.v9_12_0.MpaTrustAnchor() # MpaTrustAnchor | 
force = true # bool | Flag to force upload trust anchor. (optional)

try:
    api_response = api_instance.create_mpa_trust_anchor(mpa_trust_anchor, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->create_mpa_trust_anchor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_trust_anchor** | [**MpaTrustAnchor**](MpaTrustAnchor.md)|  | 
 **force** | **bool**| Flag to force upload trust anchor. | [optional] 

### Return type

[**CreateMpaTrustAnchorResponse**](CreateMpaTrustAnchorResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mpa_approver**
> MpaApprovers get_mpa_approver(mpa_approver_id)



Get information of an MPA approver.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_approver_id = 'mpa_approver_id_example' # str | Get information of an MPA approver.

try:
    api_response = api_instance.get_mpa_approver(mpa_approver_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->get_mpa_approver: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_approver_id** | **str**| Get information of an MPA approver. | 

### Return type

[**MpaApprovers**](MpaApprovers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mpa_approvers**
> MpaApprovers get_mpa_approvers(registration_status=registration_status)



List MPA approvers

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
registration_status = 'registration_status_example' # str | Registration status of a MPA approver. (optional)

try:
    api_response = api_instance.get_mpa_approvers(registration_status=registration_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->get_mpa_approvers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_status** | **str**| Registration status of a MPA approver. | [optional] 

### Return type

[**MpaApprovers**](MpaApprovers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mpa_request**
> MpaRequests get_mpa_request(mpa_request_id, zone=zone)



Get information for given MPA request.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_request_id = 'mpa_request_id_example' # str | Get information for given MPA request.
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.get_mpa_request(mpa_request_id, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->get_mpa_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_request_id** | **str**| Get information for given MPA request. | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**MpaRequests**](MpaRequests.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_config_request_lifecycle**
> SettingsConfigRequestLifecycle get_settings_config_request_lifecycle()



GET MPA request lifecycle configuration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_config_request_lifecycle()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->get_settings_config_request_lifecycle: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsConfigRequestLifecycle**](SettingsConfigRequestLifecycle.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_global**
> SettingsGlobalExtendedExtended get_settings_global()



Multi party authorization global configuration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->get_settings_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsGlobalExtendedExtended**](SettingsGlobalExtendedExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_privilege_action_metadata**
> SettingsPrivilegeActionMetadata get_settings_privilege_action_metadata(action=action, manual=manual, service=service)



Get MPA privileged action metadata.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
action = 'action_example' # str | Name of privileged action (optional)
manual = true # bool | Flag indicates privileged action MPA request allow manual creation via UI or MPA CLI/API. (optional)
service = 'service_example' # str | Name of service or component in system that owns the privileged action (optional)

try:
    api_response = api_instance.get_settings_privilege_action_metadata(action=action, manual=manual, service=service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->get_settings_privilege_action_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Name of privileged action | [optional] 
 **manual** | **bool**| Flag indicates privileged action MPA request allow manual creation via UI or MPA CLI/API. | [optional] 
 **service** | **str**| Name of service or component in system that owns the privileged action | [optional] 

### Return type

[**SettingsPrivilegeActionMetadata**](SettingsPrivilegeActionMetadata.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mpa_requests**
> MpaRequestsExtended list_mpa_requests(action=action, created_by=created_by, limit=limit, request_for=request_for, resume=resume, service=service, status=status, zone=zone)



List all my MPA requests.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
action = 'action_example' # str | Name of privileged action (optional)
created_by = 'created_by_example' # str | filter by user who created MPA request. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
request_for = 'request_for_example' # str | filter by user MPA request for. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
service = 'service_example' # str | Name of service or component in system that owns the privileged action (optional)
status = 'status_example' # str | status of MPA request (optional)
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.list_mpa_requests(action=action, created_by=created_by, limit=limit, request_for=request_for, resume=resume, service=service, status=status, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->list_mpa_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Name of privileged action | [optional] 
 **created_by** | **str**| filter by user who created MPA request. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **request_for** | **str**| filter by user MPA request for. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **service** | **str**| Name of service or component in system that owns the privileged action | [optional] 
 **status** | **str**| status of MPA request | [optional] 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**MpaRequestsExtended**](MpaRequestsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mpa_trust_anchors**
> MpaTrustAnchors list_mpa_trust_anchors()



Get trusted root CA for MPA

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))

try:
    api_response = api_instance.list_mpa_trust_anchors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MpaApi->list_mpa_trust_anchors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MpaTrustAnchors**](MpaTrustAnchors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mpa_complete_registration**
> update_mpa_complete_registration(mpa_complete_registration)



Specifies the properties to complete approver registration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_complete_registration = isilon_sdk.v9_12_0.MpaCompleteRegistration() # MpaCompleteRegistration | 

try:
    api_instance.update_mpa_complete_registration(mpa_complete_registration)
except ApiException as e:
    print("Exception when calling MpaApi->update_mpa_complete_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_complete_registration** | [**MpaCompleteRegistration**](MpaCompleteRegistration.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mpa_request**
> update_mpa_request(mpa_request, mpa_request_id, zone=zone)



Update a existing MPA Request.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_request = isilon_sdk.v9_12_0.MpaRequest() # MpaRequest | 
mpa_request_id = 'mpa_request_id_example' # str | Update a existing MPA Request.
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.update_mpa_request(mpa_request, mpa_request_id, zone=zone)
except ApiException as e:
    print("Exception when calling MpaApi->update_mpa_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_request** | [**MpaRequest**](MpaRequest.md)|  | 
 **mpa_request_id** | **str**| Update a existing MPA Request. | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mpa_signed_approval_by_id**
> update_mpa_signed_approval_by_id(mpa_signed_approval_id_params, mpa_signed_approval_id)



Upload MPA signed approval.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
mpa_signed_approval_id_params = isilon_sdk.v9_12_0.MpaSignedApprovalIdParams() # MpaSignedApprovalIdParams | 
mpa_signed_approval_id = 'mpa_signed_approval_id_example' # str | Upload MPA signed approval.

try:
    api_instance.update_mpa_signed_approval_by_id(mpa_signed_approval_id_params, mpa_signed_approval_id)
except ApiException as e:
    print("Exception when calling MpaApi->update_mpa_signed_approval_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mpa_signed_approval_id_params** | [**MpaSignedApprovalIdParams**](MpaSignedApprovalIdParams.md)|  | 
 **mpa_signed_approval_id** | **str**| Upload MPA signed approval. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_global**
> update_settings_global(settings_global, mpa_enabled=mpa_enabled)



Input schema for PUT method for /mpa/settings/global.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_12_0
from isilon_sdk.v9_12_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_12_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_12_0.MpaApi(isilon_sdk.v9_12_0.ApiClient(configuration))
settings_global = isilon_sdk.v9_12_0.SettingsGlobalExtendedExtendedExtended() # SettingsGlobalExtendedExtendedExtended | 
mpa_enabled = true # bool | Indicates whether the MPA feature is enabled. (optional)

try:
    api_instance.update_settings_global(settings_global, mpa_enabled=mpa_enabled)
except ApiException as e:
    print("Exception when calling MpaApi->update_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_global** | [**SettingsGlobalExtendedExtendedExtended**](SettingsGlobalExtendedExtendedExtended.md)|  | 
 **mpa_enabled** | **bool**| Indicates whether the MPA feature is enabled. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

