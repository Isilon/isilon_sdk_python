# isilon_sdk.v9_5_0.AuthUsersApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_member_of_item**](AuthUsersApi.md#create_user_member_of_item) | **POST** /platform/3/auth/users/{User}/member-of | 
[**create_user_reset_password_item**](AuthUsersApi.md#create_user_reset_password_item) | **POST** /platform/16/auth/users/{User}/reset-password | 
[**delete_user_member_of_member_of**](AuthUsersApi.md#delete_user_member_of_member_of) | **DELETE** /platform/3/auth/users/{User}/member-of/{UserMemberOfMemberOf} | 
[**list_user_member_of**](AuthUsersApi.md#list_user_member_of) | **GET** /platform/3/auth/users/{User}/member-of | 
[**update_user_change_password**](AuthUsersApi.md#update_user_change_password) | **PUT** /platform/3/auth/users/{User}/change-password | 


# **create_user_member_of_item**
> CreateResponse create_user_member_of_item(user_member_of_item, user, provider=provider, zone=zone)



Add the user to a group.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuthUsersApi(isilon_sdk.v9_5_0.ApiClient(configuration))
user_member_of_item = isilon_sdk.v9_5_0.AuthAccessAccessItemFileGroup() # AuthAccessAccessItemFileGroup | 
user = 'user_example' # str | 
provider = 'provider_example' # str | Filter groups by provider. (optional)
zone = 'zone_example' # str | Filter groups by zone. (optional)

try:
    api_response = api_instance.create_user_member_of_item(user_member_of_item, user, provider=provider, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthUsersApi->create_user_member_of_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_member_of_item** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md)|  | 
 **user** | **str**|  | 
 **provider** | **str**| Filter groups by provider. | [optional] 
 **zone** | **str**| Filter groups by zone. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_reset_password_item**
> CreateUserResetPasswordItemResponse create_user_reset_password_item(user_reset_password_item, user, provider=provider, zone=zone)



Reset the user's password.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuthUsersApi(isilon_sdk.v9_5_0.ApiClient(configuration))
user_reset_password_item = isilon_sdk.v9_5_0.Empty() # Empty | 
user = 'user_example' # str | 
provider = 'provider_example' # str | Optional provider type. (optional)
zone = 'zone_example' # str | Specifies access zone containing user. (optional)

try:
    api_response = api_instance.create_user_reset_password_item(user_reset_password_item, user, provider=provider, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthUsersApi->create_user_reset_password_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_reset_password_item** | [**Empty**](Empty.md)|  | 
 **user** | **str**|  | 
 **provider** | **str**| Optional provider type. | [optional] 
 **zone** | **str**| Specifies access zone containing user. | [optional] 

### Return type

[**CreateUserResetPasswordItemResponse**](CreateUserResetPasswordItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_member_of_member_of**
> delete_user_member_of_member_of(user_member_of_member_of, user, provider=provider, zone=zone)



Remove the user from the group.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuthUsersApi(isilon_sdk.v9_5_0.ApiClient(configuration))
user_member_of_member_of = 'user_member_of_member_of_example' # str | Remove the user from the group.
user = 'user_example' # str | 
provider = 'provider_example' # str | Filter groups by provider. (optional)
zone = 'zone_example' # str | Filter groups by zone. (optional)

try:
    api_instance.delete_user_member_of_member_of(user_member_of_member_of, user, provider=provider, zone=zone)
except ApiException as e:
    print("Exception when calling AuthUsersApi->delete_user_member_of_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_member_of_member_of** | **str**| Remove the user from the group. | 
 **user** | **str**|  | 
 **provider** | **str**| Filter groups by provider. | [optional] 
 **zone** | **str**| Filter groups by zone. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_member_of**
> UserMemberOf list_user_member_of(user, provider=provider, resolve_names=resolve_names, zone=zone)



List all groups the user is a member of.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuthUsersApi(isilon_sdk.v9_5_0.ApiClient(configuration))
user = 'user_example' # str | 
provider = 'provider_example' # str | Filter groups by provider. (optional)
resolve_names = true # bool | Resolve names of personas. (optional)
zone = 'zone_example' # str | Filter groups by zone. (optional)

try:
    api_response = api_instance.list_user_member_of(user, provider=provider, resolve_names=resolve_names, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthUsersApi->list_user_member_of: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | 
 **provider** | **str**| Filter groups by provider. | [optional] 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **zone** | **str**| Filter groups by zone. | [optional] 

### Return type

[**UserMemberOf**](UserMemberOf.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_change_password**
> update_user_change_password(user_change_password, user, zone=zone)



Change the user's password.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.AuthUsersApi(isilon_sdk.v9_5_0.ApiClient(configuration))
user_change_password = isilon_sdk.v9_5_0.UserChangePassword() # UserChangePassword | 
user = 'user_example' # str | 
zone = 'zone_example' # str | Specifies access zone containing user. (optional)

try:
    api_instance.update_user_change_password(user_change_password, user, zone=zone)
except ApiException as e:
    print("Exception when calling AuthUsersApi->update_user_change_password: %s\n" % e)
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

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

