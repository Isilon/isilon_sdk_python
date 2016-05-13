# isi_sdk.AuthGroupsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_member**](AuthGroupsApi.md#create_group_member) | **POST** /platform/1/auth/groups/{Group}/members | 
[**delete_group_member**](AuthGroupsApi.md#delete_group_member) | **DELETE** /platform/1/auth/groups/{Group}/members/{GroupMemberId} | 
[**list_group_members**](AuthGroupsApi.md#list_group_members) | **GET** /platform/1/auth/groups/{Group}/members | 


# **create_group_member**
> CreateResponse create_group_member(group_member, group, zone=zone, provider=provider)



Add a member to the group.

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
api_instance = isi_sdk.AuthGroupsApi()
group_member = isi_sdk.GroupMember() # GroupMember | 
group = 'group_example' # str | 
zone = 'zone_example' # str | Filter group members by zone. (optional)
provider = 'provider_example' # str | Filter group members by provider. (optional)

try: 
    api_response = api_instance.create_group_member(group_member, group, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthGroupsApi->create_group_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_member** | [**GroupMember**](GroupMember.md)|  | 
 **group** | **str**|  | 
 **zone** | **str**| Filter group members by zone. | [optional] 
 **provider** | **str**| Filter group members by provider. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_member**
> delete_group_member(group_member_id, group, zone=zone, provider=provider)



Remove the member from the group.

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
api_instance = isi_sdk.AuthGroupsApi()
group_member_id = 'group_member_id_example' # str | Remove the member from the group.
group = 'group_example' # str | 
zone = 'zone_example' # str | Filter group members by zone. (optional)
provider = 'provider_example' # str | Filter group members by provider. (optional)

try: 
    api_instance.delete_group_member(group_member_id, group, zone=zone, provider=provider)
except ApiException as e:
    print "Exception when calling AuthGroupsApi->delete_group_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_member_id** | **str**| Remove the member from the group. | 
 **group** | **str**|  | 
 **zone** | **str**| Filter group members by zone. | [optional] 
 **provider** | **str**| Filter group members by provider. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_members**
> GroupMembers list_group_members(group, resolve_names=resolve_names, limit=limit, zone=zone, provider=provider)



List all the members of the group.

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
api_instance = isi_sdk.AuthGroupsApi()
group = 'group_example' # str | 
resolve_names = true # bool | Resolve names of personas. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
zone = 'zone_example' # str | Filter group members by zone. (optional)
provider = 'provider_example' # str | Filter group members by provider. (optional)

try: 
    api_response = api_instance.list_group_members(group, resolve_names=resolve_names, limit=limit, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthGroupsApi->list_group_members: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | **str**|  | 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **zone** | **str**| Filter group members by zone. | [optional] 
 **provider** | **str**| Filter group members by provider. | [optional] 

### Return type

[**GroupMembers**](GroupMembers.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

