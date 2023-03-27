# isilon_sdk.v9_4_0.AuthGroupsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_member**](AuthGroupsApi.md#create_group_member) | **POST** /platform/1/auth/groups/{Group}/members | 
[**delete_group_member**](AuthGroupsApi.md#delete_group_member) | **DELETE** /platform/1/auth/groups/{Group}/members/{GroupMemberId} | 
[**list_group_members**](AuthGroupsApi.md#list_group_members) | **GET** /platform/1/auth/groups/{Group}/members | 


# **create_group_member**
> CreateResponse create_group_member(group_member, group, provider=provider, zone=zone)



Add a member to the group.

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
api_instance = isilon_sdk.v9_4_0.AuthGroupsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
group_member = isilon_sdk.v9_4_0.AuthAccessAccessItemFileGroup() # AuthAccessAccessItemFileGroup | 
group = 'group_example' # str | 
provider = 'provider_example' # str | Filter group members by provider. (optional)
zone = 'zone_example' # str | Filter group members by zone. (optional)

try:
    api_response = api_instance.create_group_member(group_member, group, provider=provider, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthGroupsApi->create_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_member** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md)|  | 
 **group** | **str**|  | 
 **provider** | **str**| Filter group members by provider. | [optional] 
 **zone** | **str**| Filter group members by zone. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_member**
> delete_group_member(group_member_id, group, provider=provider, zone=zone)



Remove the member from the group.

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
api_instance = isilon_sdk.v9_4_0.AuthGroupsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
group_member_id = 'group_member_id_example' # str | Remove the member from the group.
group = 'group_example' # str | 
provider = 'provider_example' # str | Filter group members by provider. (optional)
zone = 'zone_example' # str | Filter group members by zone. (optional)

try:
    api_instance.delete_group_member(group_member_id, group, provider=provider, zone=zone)
except ApiException as e:
    print("Exception when calling AuthGroupsApi->delete_group_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_member_id** | **str**| Remove the member from the group. | 
 **group** | **str**|  | 
 **provider** | **str**| Filter group members by provider. | [optional] 
 **zone** | **str**| Filter group members by zone. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_members**
> GroupMembers list_group_members(group, limit=limit, provider=provider, resolve_names=resolve_names, resume=resume, zone=zone)



List all the members of the group.

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
api_instance = isilon_sdk.v9_4_0.AuthGroupsApi(isilon_sdk.v9_4_0.ApiClient(configuration))
group = 'group_example' # str | 
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
provider = 'provider_example' # str | Filter group members by provider. (optional)
resolve_names = true # bool | Resolve names of personas. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
zone = 'zone_example' # str | Filter group members by zone. (optional)

try:
    api_response = api_instance.list_group_members(group, limit=limit, provider=provider, resolve_names=resolve_names, resume=resume, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthGroupsApi->list_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**|  | 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **provider** | **str**| Filter group members by provider. | [optional] 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **zone** | **str**| Filter group members by zone. | [optional] 

### Return type

[**GroupMembers**](GroupMembers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

