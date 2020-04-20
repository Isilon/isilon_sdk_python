# isi_sdk_8_2_1.AuthRolesApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_member**](AuthRolesApi.md#create_role_member) | **POST** /platform/8/auth/roles/{Role}/members | 
[**create_role_privilege**](AuthRolesApi.md#create_role_privilege) | **POST** /platform/7/auth/roles/{Role}/privileges | 
[**delete_role_member**](AuthRolesApi.md#delete_role_member) | **DELETE** /platform/8/auth/roles/{Role}/members/{RoleMemberId} | 
[**delete_role_privilege**](AuthRolesApi.md#delete_role_privilege) | **DELETE** /platform/7/auth/roles/{Role}/privileges/{RolePrivilegeId} | 
[**list_role_members**](AuthRolesApi.md#list_role_members) | **GET** /platform/8/auth/roles/{Role}/members | 
[**list_role_privileges**](AuthRolesApi.md#list_role_privileges) | **GET** /platform/7/auth/roles/{Role}/privileges | 


# **create_role_member**
> CreateResponse create_role_member(role_member, role, zone=zone)



Add a member to the role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.AuthRolesApi(isi_sdk_8_2_1.ApiClient(configuration))
role_member = isi_sdk_8_2_1.AuthAccessAccessItemFileGroup() # AuthAccessAccessItemFileGroup | 
role = 'role_example' # str | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.create_role_member(role_member, role, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->create_role_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_member** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md)|  | 
 **role** | **str**|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role_privilege**
> CreateResponse create_role_privilege(role_privilege, role, zone=zone)



Add a privilege to the role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.AuthRolesApi(isi_sdk_8_2_1.ApiClient(configuration))
role_privilege = isi_sdk_8_2_1.AuthIdNtokenPrivilegeItem() # AuthIdNtokenPrivilegeItem | 
role = 'role_example' # str | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.create_role_privilege(role_privilege, role, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->create_role_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_privilege** | [**AuthIdNtokenPrivilegeItem**](AuthIdNtokenPrivilegeItem.md)|  | 
 **role** | **str**|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_member**
> delete_role_member(role_member_id, role, zone=zone)



Remove a member from the role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.AuthRolesApi(isi_sdk_8_2_1.ApiClient(configuration))
role_member_id = 'role_member_id_example' # str | Remove a member from the role.
role = 'role_example' # str | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.delete_role_member(role_member_id, role, zone=zone)
except ApiException as e:
    print("Exception when calling AuthRolesApi->delete_role_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_member_id** | **str**| Remove a member from the role. | 
 **role** | **str**|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_privilege**
> delete_role_privilege(role_privilege_id, role, zone=zone)



Remove a privilege from a role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.AuthRolesApi(isi_sdk_8_2_1.ApiClient(configuration))
role_privilege_id = 'role_privilege_id_example' # str | Remove a privilege from a role.
role = 'role_example' # str | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_instance.delete_role_privilege(role_privilege_id, role, zone=zone)
except ApiException as e:
    print("Exception when calling AuthRolesApi->delete_role_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_privilege_id** | **str**| Remove a privilege from a role. | 
 **role** | **str**|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_members**
> GroupMembers list_role_members(role, sort=sort, zone=zone, resume=resume, resolve_names=resolve_names, limit=limit, dir=dir)



List all the members of the role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.AuthRolesApi(isi_sdk_8_2_1.ApiClient(configuration))
role = 'role_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
zone = 'zone_example' # str | Specifies which access zone to use. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
resolve_names = true # bool | Resolve names of personas. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_role_members(role, sort=sort, zone=zone, resume=resume, resolve_names=resolve_names, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->list_role_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **zone** | **str**| Specifies which access zone to use. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**GroupMembers**](GroupMembers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_role_privileges**
> RolePrivileges list_role_privileges(role, zone=zone)



List all privileges in the role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.AuthRolesApi(isi_sdk_8_2_1.ApiClient(configuration))
role = 'role_example' # str | 
zone = 'zone_example' # str | Specifies which access zone to use. (optional)

try:
    api_response = api_instance.list_role_privileges(role, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthRolesApi->list_role_privileges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | **str**|  | 
 **zone** | **str**| Specifies which access zone to use. | [optional] 

### Return type

[**RolePrivileges**](RolePrivileges.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

