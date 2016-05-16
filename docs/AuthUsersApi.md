# isi_sdk.AuthUsersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_member_of_item**](AuthUsersApi.md#create_user_member_of_item) | **POST** /platform/3/auth/users/{User}/member-of | 
[**delete_user_member_of_member_of**](AuthUsersApi.md#delete_user_member_of_member_of) | **DELETE** /platform/3/auth/users/{User}/member-of/{UserMemberOfMemberOf} | 
[**list_user_member_of**](AuthUsersApi.md#list_user_member_of) | **GET** /platform/3/auth/users/{User}/member-of | 
[**update_user_change_password**](AuthUsersApi.md#update_user_change_password) | **PUT** /platform/3/auth/users/{User}/change-password | 


# **create_user_member_of_item**
> CreateResponse create_user_member_of_item(user_member_of_item, user, zone=zone, provider=provider)



Add the user to a group.

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
api_instance = isi_sdk.AuthUsersApi()
user_member_of_item = isi_sdk.GroupMember() # GroupMember | 
user = 'user_example' # str | 
zone = 'zone_example' # str | Filter groups by zone. (optional)
provider = 'provider_example' # str | Filter groups by provider. (optional)

try: 
    api_response = api_instance.create_user_member_of_item(user_member_of_item, user, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthUsersApi->create_user_member_of_item: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_member_of_item** | [**GroupMember**](GroupMember.md)|  | 
 **user** | **str**|  | 
 **zone** | **str**| Filter groups by zone. | [optional] 
 **provider** | **str**| Filter groups by provider. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_member_of_member_of**
> delete_user_member_of_member_of(user_member_of_member_of, user, zone=zone, provider=provider)



Remove the user from the group.

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
api_instance = isi_sdk.AuthUsersApi()
user_member_of_member_of = 'user_member_of_member_of_example' # str | Remove the user from the group.
user = 'user_example' # str | 
zone = 'zone_example' # str | Filter groups by zone. (optional)
provider = 'provider_example' # str | Filter groups by provider. (optional)

try: 
    api_instance.delete_user_member_of_member_of(user_member_of_member_of, user, zone=zone, provider=provider)
except ApiException as e:
    print "Exception when calling AuthUsersApi->delete_user_member_of_member_of: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_member_of_member_of** | **str**| Remove the user from the group. | 
 **user** | **str**|  | 
 **zone** | **str**| Filter groups by zone. | [optional] 
 **provider** | **str**| Filter groups by provider. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_member_of**
> UserMemberOf list_user_member_of(user, resolve_names=resolve_names, zone=zone, provider=provider)



List all groups the user is a member of.

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
api_instance = isi_sdk.AuthUsersApi()
user = 'user_example' # str | 
resolve_names = true # bool | Resolve names of personas. (optional)
zone = 'zone_example' # str | Filter groups by zone. (optional)
provider = 'provider_example' # str | Filter groups by provider. (optional)

try: 
    api_response = api_instance.list_user_member_of(user, resolve_names=resolve_names, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AuthUsersApi->list_user_member_of: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **zone** | **str**| Filter groups by zone. | [optional] 
 **provider** | **str**| Filter groups by provider. | [optional] 

### Return type

[**UserMemberOf**](UserMemberOf.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_change_password**
> update_user_change_password(user_change_password, user, zone=zone)



Change the user's password.

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
api_instance = isi_sdk.AuthUsersApi()
user_change_password = isi_sdk.UserChangePassword() # UserChangePassword | 
user = 'user_example' # str | 
zone = 'zone_example' # str | Specifies access zone containing user. (optional)

try: 
    api_instance.update_user_change_password(user_change_password, user, zone=zone)
except ApiException as e:
    print "Exception when calling AuthUsersApi->update_user_change_password: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_change_password** | [**UserChangePassword**](UserChangePassword.md)|  | 
 **user** | **str**|  | 
 **zone** | **str**| Specifies access zone containing user. | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

