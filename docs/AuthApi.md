# isi_sdk_7_2.AuthApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_group**](AuthApi.md#create_auth_group) | **POST** /platform/1/auth/groups | 
[**create_auth_role**](AuthApi.md#create_auth_role) | **POST** /platform/1/auth/roles | 
[**create_auth_user**](AuthApi.md#create_auth_user) | **POST** /platform/1/auth/users | 
[**create_mapping_identity**](AuthApi.md#create_mapping_identity) | **POST** /platform/1/auth/mapping/identities | 
[**create_mapping_identity_0**](AuthApi.md#create_mapping_identity_0) | **POST** /platform/1/auth/mapping/identities/{MappingIdentityId} | 
[**create_providers_ads_item**](AuthApi.md#create_providers_ads_item) | **POST** /platform/1/auth/providers/ads | 
[**create_providers_file_item**](AuthApi.md#create_providers_file_item) | **POST** /platform/1/auth/providers/file | 
[**create_providers_krb5_item**](AuthApi.md#create_providers_krb5_item) | **POST** /platform/1/auth/providers/krb5 | 
[**create_providers_ldap_item**](AuthApi.md#create_providers_ldap_item) | **POST** /platform/1/auth/providers/ldap | 
[**create_providers_nis_item**](AuthApi.md#create_providers_nis_item) | **POST** /platform/1/auth/providers/nis | 
[**create_settings_krb5_domain**](AuthApi.md#create_settings_krb5_domain) | **POST** /platform/1/auth/settings/krb5/domains | 
[**create_settings_krb5_realm**](AuthApi.md#create_settings_krb5_realm) | **POST** /platform/1/auth/settings/krb5/realms | 
[**delete_auth_group**](AuthApi.md#delete_auth_group) | **DELETE** /platform/1/auth/groups/{AuthGroupId} | 
[**delete_auth_groups**](AuthApi.md#delete_auth_groups) | **DELETE** /platform/1/auth/groups | 
[**delete_auth_role**](AuthApi.md#delete_auth_role) | **DELETE** /platform/1/auth/roles/{AuthRoleId} | 
[**delete_auth_user**](AuthApi.md#delete_auth_user) | **DELETE** /platform/1/auth/users/{AuthUserId} | 
[**delete_auth_users**](AuthApi.md#delete_auth_users) | **DELETE** /platform/1/auth/users | 
[**delete_mapping_identities**](AuthApi.md#delete_mapping_identities) | **DELETE** /platform/1/auth/mapping/identities | 
[**delete_mapping_identity**](AuthApi.md#delete_mapping_identity) | **DELETE** /platform/1/auth/mapping/identities/{MappingIdentityId} | 
[**delete_providers_ads_by_id**](AuthApi.md#delete_providers_ads_by_id) | **DELETE** /platform/1/auth/providers/ads/{ProvidersAdsId} | 
[**delete_providers_file_by_id**](AuthApi.md#delete_providers_file_by_id) | **DELETE** /platform/1/auth/providers/file/{ProvidersFileId} | 
[**delete_providers_krb5_by_id**](AuthApi.md#delete_providers_krb5_by_id) | **DELETE** /platform/1/auth/providers/krb5/{ProvidersKrb5Id} | 
[**delete_providers_ldap_by_id**](AuthApi.md#delete_providers_ldap_by_id) | **DELETE** /platform/1/auth/providers/ldap/{ProvidersLdapId} | 
[**delete_providers_local_by_id**](AuthApi.md#delete_providers_local_by_id) | **DELETE** /platform/1/auth/providers/local/{ProvidersLocalId} | 
[**delete_providers_nis_by_id**](AuthApi.md#delete_providers_nis_by_id) | **DELETE** /platform/1/auth/providers/nis/{ProvidersNisId} | 
[**delete_settings_krb5_domain**](AuthApi.md#delete_settings_krb5_domain) | **DELETE** /platform/1/auth/settings/krb5/domains/{SettingsKrb5DomainId} | 
[**delete_settings_krb5_realm**](AuthApi.md#delete_settings_krb5_realm) | **DELETE** /platform/1/auth/settings/krb5/realms/{SettingsKrb5RealmId} | 
[**get_auth_access_user**](AuthApi.md#get_auth_access_user) | **GET** /platform/1/auth/access/{AuthAccessUser} | 
[**get_auth_group**](AuthApi.md#get_auth_group) | **GET** /platform/1/auth/groups/{AuthGroupId} | 
[**get_auth_id**](AuthApi.md#get_auth_id) | **GET** /platform/1/auth/id | 
[**get_auth_netgroup**](AuthApi.md#get_auth_netgroup) | **GET** /platform/1/auth/netgroups/{AuthNetgroupId} | 
[**get_auth_privileges**](AuthApi.md#get_auth_privileges) | **GET** /platform/1/auth/privileges | 
[**get_auth_role**](AuthApi.md#get_auth_role) | **GET** /platform/1/auth/roles/{AuthRoleId} | 
[**get_auth_shells**](AuthApi.md#get_auth_shells) | **GET** /platform/1/auth/shells | 
[**get_auth_user**](AuthApi.md#get_auth_user) | **GET** /platform/1/auth/users/{AuthUserId} | 
[**get_auth_wellknown**](AuthApi.md#get_auth_wellknown) | **GET** /platform/1/auth/wellknowns/{AuthWellknownId} | 
[**get_auth_wellknowns**](AuthApi.md#get_auth_wellknowns) | **GET** /platform/1/auth/wellknowns | 
[**get_mapping_identity**](AuthApi.md#get_mapping_identity) | **GET** /platform/1/auth/mapping/identities/{MappingIdentityId} | 
[**get_mapping_users_lookup**](AuthApi.md#get_mapping_users_lookup) | **GET** /platform/1/auth/mapping/users/lookup | 
[**get_mapping_users_rules**](AuthApi.md#get_mapping_users_rules) | **GET** /platform/1/auth/mapping/users/rules | 
[**get_providers_ads_by_id**](AuthApi.md#get_providers_ads_by_id) | **GET** /platform/1/auth/providers/ads/{ProvidersAdsId} | 
[**get_providers_file_by_id**](AuthApi.md#get_providers_file_by_id) | **GET** /platform/1/auth/providers/file/{ProvidersFileId} | 
[**get_providers_krb5_by_id**](AuthApi.md#get_providers_krb5_by_id) | **GET** /platform/1/auth/providers/krb5/{ProvidersKrb5Id} | 
[**get_providers_ldap_by_id**](AuthApi.md#get_providers_ldap_by_id) | **GET** /platform/1/auth/providers/ldap/{ProvidersLdapId} | 
[**get_providers_local**](AuthApi.md#get_providers_local) | **GET** /platform/1/auth/providers/local | 
[**get_providers_local_by_id**](AuthApi.md#get_providers_local_by_id) | **GET** /platform/1/auth/providers/local/{ProvidersLocalId} | 
[**get_providers_nis_by_id**](AuthApi.md#get_providers_nis_by_id) | **GET** /platform/1/auth/providers/nis/{ProvidersNisId} | 
[**get_providers_summary**](AuthApi.md#get_providers_summary) | **GET** /platform/1/auth/providers/summary | 
[**get_settings_global**](AuthApi.md#get_settings_global) | **GET** /platform/1/auth/settings/global | 
[**get_settings_krb5_defaults**](AuthApi.md#get_settings_krb5_defaults) | **GET** /platform/1/auth/settings/krb5/defaults | 
[**get_settings_krb5_domain**](AuthApi.md#get_settings_krb5_domain) | **GET** /platform/1/auth/settings/krb5/domains/{SettingsKrb5DomainId} | 
[**get_settings_krb5_realm**](AuthApi.md#get_settings_krb5_realm) | **GET** /platform/1/auth/settings/krb5/realms/{SettingsKrb5RealmId} | 
[**get_settings_mapping**](AuthApi.md#get_settings_mapping) | **GET** /platform/1/auth/settings/mapping | 
[**list_auth_groups**](AuthApi.md#list_auth_groups) | **GET** /platform/1/auth/groups | 
[**list_auth_roles**](AuthApi.md#list_auth_roles) | **GET** /platform/1/auth/roles | 
[**list_auth_users**](AuthApi.md#list_auth_users) | **GET** /platform/1/auth/users | 
[**list_providers_ads**](AuthApi.md#list_providers_ads) | **GET** /platform/1/auth/providers/ads | 
[**list_providers_file**](AuthApi.md#list_providers_file) | **GET** /platform/1/auth/providers/file | 
[**list_providers_krb5**](AuthApi.md#list_providers_krb5) | **GET** /platform/1/auth/providers/krb5 | 
[**list_providers_ldap**](AuthApi.md#list_providers_ldap) | **GET** /platform/1/auth/providers/ldap | 
[**list_providers_nis**](AuthApi.md#list_providers_nis) | **GET** /platform/1/auth/providers/nis | 
[**list_settings_krb5_domains**](AuthApi.md#list_settings_krb5_domains) | **GET** /platform/1/auth/settings/krb5/domains | 
[**list_settings_krb5_realms**](AuthApi.md#list_settings_krb5_realms) | **GET** /platform/1/auth/settings/krb5/realms | 
[**update_auth_group**](AuthApi.md#update_auth_group) | **PUT** /platform/1/auth/groups/{AuthGroupId} | 
[**update_auth_role**](AuthApi.md#update_auth_role) | **PUT** /platform/1/auth/roles/{AuthRoleId} | 
[**update_auth_user**](AuthApi.md#update_auth_user) | **PUT** /platform/1/auth/users/{AuthUserId} | 
[**update_mapping_users_rules**](AuthApi.md#update_mapping_users_rules) | **PUT** /platform/1/auth/mapping/users/rules | 
[**update_providers_ads_by_id**](AuthApi.md#update_providers_ads_by_id) | **PUT** /platform/1/auth/providers/ads/{ProvidersAdsId} | 
[**update_providers_file_by_id**](AuthApi.md#update_providers_file_by_id) | **PUT** /platform/1/auth/providers/file/{ProvidersFileId} | 
[**update_providers_krb5_by_id**](AuthApi.md#update_providers_krb5_by_id) | **PUT** /platform/1/auth/providers/krb5/{ProvidersKrb5Id} | 
[**update_providers_ldap_by_id**](AuthApi.md#update_providers_ldap_by_id) | **PUT** /platform/1/auth/providers/ldap/{ProvidersLdapId} | 
[**update_providers_local_by_id**](AuthApi.md#update_providers_local_by_id) | **PUT** /platform/1/auth/providers/local/{ProvidersLocalId} | 
[**update_providers_nis_by_id**](AuthApi.md#update_providers_nis_by_id) | **PUT** /platform/1/auth/providers/nis/{ProvidersNisId} | 
[**update_settings_global**](AuthApi.md#update_settings_global) | **PUT** /platform/1/auth/settings/global | 
[**update_settings_krb5_defaults**](AuthApi.md#update_settings_krb5_defaults) | **PUT** /platform/1/auth/settings/krb5/defaults | 
[**update_settings_krb5_domain**](AuthApi.md#update_settings_krb5_domain) | **PUT** /platform/1/auth/settings/krb5/domains/{SettingsKrb5DomainId} | 
[**update_settings_krb5_realm**](AuthApi.md#update_settings_krb5_realm) | **PUT** /platform/1/auth/settings/krb5/realms/{SettingsKrb5RealmId} | 
[**update_settings_mapping**](AuthApi.md#update_settings_mapping) | **PUT** /platform/1/auth/settings/mapping | 


# **create_auth_group**
> CreateResponse create_auth_group(auth_group, zone=zone, provider=provider)



Create a new group.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_group = isi_sdk_7_2.AuthGroupCreateParams() # AuthGroupCreateParams | 
zone = 'zone_example' # str | Optional zone. (optional)
provider = 'provider_example' # str | Optional provider type. (optional)

try:
    api_response = api_instance.create_auth_group(auth_group, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_auth_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_group** | [**AuthGroupCreateParams**](AuthGroupCreateParams.md)|  | 
 **zone** | **str**| Optional zone. | [optional] 
 **provider** | **str**| Optional provider type. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_role**
> CreateResponse create_auth_role(auth_role)



Create a new role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_role = isi_sdk_7_2.AuthRoleCreateParams() # AuthRoleCreateParams | 

try:
    api_response = api_instance.create_auth_role(auth_role)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_auth_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_role** | [**AuthRoleCreateParams**](AuthRoleCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_user**
> CreateResponse create_auth_user(auth_user, zone=zone, provider=provider)



Create a new user.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_user = isi_sdk_7_2.AuthUserCreateParams() # AuthUserCreateParams | 
zone = 'zone_example' # str | Optional zone. (optional)
provider = 'provider_example' # str | Optional provider type. (optional)

try:
    api_response = api_instance.create_auth_user(auth_user, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_auth_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user** | [**AuthUserCreateParams**](AuthUserCreateParams.md)|  | 
 **zone** | **str**| Optional zone. | [optional] 
 **provider** | **str**| Optional provider type. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mapping_identity**
> Empty create_mapping_identity(mapping_identity, _2way=_2way, zone=zone, replace=replace)



Manually set or modify a mapping between two personae.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
mapping_identity = isi_sdk_7_2.MappingIdentityCreateParams() # MappingIdentityCreateParams | 
_2way = true # bool | Create a bi-directional mapping from source to target and target to source. (optional)
zone = 'zone_example' # str | Optional zone. (optional)
replace = true # bool | Replace existing mappings. (optional)

try:
    api_response = api_instance.create_mapping_identity(mapping_identity, _2way=_2way, zone=zone, replace=replace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_mapping_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_identity** | [**MappingIdentityCreateParams**](MappingIdentityCreateParams.md)|  | 
 **_2way** | **bool**| Create a bi-directional mapping from source to target and target to source. | [optional] 
 **zone** | **str**| Optional zone. | [optional] 
 **replace** | **bool**| Replace existing mappings. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mapping_identity_0**
> MappingIdentities create_mapping_identity_0(mapping_identity, mapping_identity_id, type=type, zone=zone)



Manually set or modify a mapping between two personae.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
mapping_identity = isi_sdk_7_2.Empty() # Empty | 
mapping_identity_id = 'mapping_identity_id_example' # str | Manually set or modify a mapping between two personae.
type = 'type_example' # str | Desired mapping target to fetch/generate. (optional)
zone = 'zone_example' # str | Optional zone. (optional)

try:
    api_response = api_instance.create_mapping_identity_0(mapping_identity, mapping_identity_id, type=type, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_mapping_identity_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_identity** | [**Empty**](Empty.md)|  | 
 **mapping_identity_id** | **str**| Manually set or modify a mapping between two personae. | 
 **type** | **str**| Desired mapping target to fetch/generate. | [optional] 
 **zone** | **str**| Optional zone. | [optional] 

### Return type

[**MappingIdentities**](MappingIdentities.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_providers_ads_item**
> CreateResponse create_providers_ads_item(providers_ads_item)



Create a new ADS provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_ads_item = isi_sdk_7_2.ProvidersAdsItem() # ProvidersAdsItem | 

try:
    api_response = api_instance.create_providers_ads_item(providers_ads_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_providers_ads_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_ads_item** | [**ProvidersAdsItem**](ProvidersAdsItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_providers_file_item**
> CreateResponse create_providers_file_item(providers_file_item)



Create a new file provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_file_item = isi_sdk_7_2.ProvidersFileItem() # ProvidersFileItem | 

try:
    api_response = api_instance.create_providers_file_item(providers_file_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_providers_file_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_file_item** | [**ProvidersFileItem**](ProvidersFileItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_providers_krb5_item**
> CreateResponse create_providers_krb5_item(providers_krb5_item)



Create a new KRB5 provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_krb5_item = isi_sdk_7_2.ProvidersKrb5Item() # ProvidersKrb5Item | 

try:
    api_response = api_instance.create_providers_krb5_item(providers_krb5_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_providers_krb5_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_krb5_item** | [**ProvidersKrb5Item**](ProvidersKrb5Item.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_providers_ldap_item**
> CreateResponse create_providers_ldap_item(providers_ldap_item)



Create a new LDAP provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_ldap_item = isi_sdk_7_2.ProvidersLdapItem() # ProvidersLdapItem | 

try:
    api_response = api_instance.create_providers_ldap_item(providers_ldap_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_providers_ldap_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_ldap_item** | [**ProvidersLdapItem**](ProvidersLdapItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_providers_nis_item**
> CreateResponse create_providers_nis_item(providers_nis_item)



Create a new NIS provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_nis_item = isi_sdk_7_2.ProvidersNisItem() # ProvidersNisItem | 

try:
    api_response = api_instance.create_providers_nis_item(providers_nis_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_providers_nis_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_nis_item** | [**ProvidersNisItem**](ProvidersNisItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_krb5_domain**
> CreateResponse create_settings_krb5_domain(settings_krb5_domain)



Create a new krb5 domain.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_domain = isi_sdk_7_2.SettingsKrb5DomainCreateParams() # SettingsKrb5DomainCreateParams | 

try:
    api_response = api_instance.create_settings_krb5_domain(settings_krb5_domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_settings_krb5_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_domain** | [**SettingsKrb5DomainCreateParams**](SettingsKrb5DomainCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_settings_krb5_realm**
> CreateResponse create_settings_krb5_realm(settings_krb5_realm)



Create a new krb5 realm.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_realm = isi_sdk_7_2.SettingsKrb5RealmCreateParams() # SettingsKrb5RealmCreateParams | 

try:
    api_response = api_instance.create_settings_krb5_realm(settings_krb5_realm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->create_settings_krb5_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_realm** | [**SettingsKrb5RealmCreateParams**](SettingsKrb5RealmCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_group**
> delete_auth_group(auth_group_id, cached=cached, zone=zone, provider=provider)



Delete the group.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_group_id = 'auth_group_id_example' # str | Delete the group.
cached = true # bool | If true, flush the group from the cache. (optional)
zone = 'zone_example' # str | Filter groups by zone. (optional)
provider = 'provider_example' # str | Filter groups by provider. (optional)

try:
    api_instance.delete_auth_group(auth_group_id, cached=cached, zone=zone, provider=provider)
except ApiException as e:
    print("Exception when calling AuthApi->delete_auth_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_group_id** | **str**| Delete the group. | 
 **cached** | **bool**| If true, flush the group from the cache. | [optional] 
 **zone** | **str**| Filter groups by zone. | [optional] 
 **provider** | **str**| Filter groups by provider. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_groups**
> delete_auth_groups(cached=cached, zone=zone, provider=provider)



Flush the groups cache.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
cached = true # bool | If true, only flush cached objects. (optional)
zone = 'zone_example' # str | Filter groups by zone. (optional)
provider = 'provider_example' # str | Filter groups by provider. (optional)

try:
    api_instance.delete_auth_groups(cached=cached, zone=zone, provider=provider)
except ApiException as e:
    print("Exception when calling AuthApi->delete_auth_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cached** | **bool**| If true, only flush cached objects. | [optional] 
 **zone** | **str**| Filter groups by zone. | [optional] 
 **provider** | **str**| Filter groups by provider. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_role**
> delete_auth_role(auth_role_id)



Delete the role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_role_id = 'auth_role_id_example' # str | Delete the role.

try:
    api_instance.delete_auth_role(auth_role_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_auth_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_role_id** | **str**| Delete the role. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_user**
> delete_auth_user(auth_user_id, cached=cached, zone=zone, provider=provider)



Delete the user.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_user_id = 'auth_user_id_example' # str | Delete the user.
cached = true # bool | If true, flush the user from the cache. (optional)
zone = 'zone_example' # str | Filter users by zone. (optional)
provider = 'provider_example' # str | Filter users by provider. (optional)

try:
    api_instance.delete_auth_user(auth_user_id, cached=cached, zone=zone, provider=provider)
except ApiException as e:
    print("Exception when calling AuthApi->delete_auth_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user_id** | **str**| Delete the user. | 
 **cached** | **bool**| If true, flush the user from the cache. | [optional] 
 **zone** | **str**| Filter users by zone. | [optional] 
 **provider** | **str**| Filter users by provider. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_users**
> delete_auth_users(cached=cached, zone=zone, provider=provider)



Flush the users cache.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
cached = true # bool | If true, only flush cached objects. (optional)
zone = 'zone_example' # str | Filter users by zone. (optional)
provider = 'provider_example' # str | Filter users by provider. (optional)

try:
    api_instance.delete_auth_users(cached=cached, zone=zone, provider=provider)
except ApiException as e:
    print("Exception when calling AuthApi->delete_auth_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cached** | **bool**| If true, only flush cached objects. | [optional] 
 **zone** | **str**| Filter users by zone. | [optional] 
 **provider** | **str**| Filter users by provider. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mapping_identities**
> delete_mapping_identities(filter=filter, zone=zone, remove=remove)



Flush the entire idmap cache.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
filter = 'filter_example' # str | Filter to apply when deleting identity mappings. (optional)
zone = 'zone_example' # str | Optional zone. (optional)
remove = true # bool | Delete mapping instead of flush mapping cache. (optional)

try:
    api_instance.delete_mapping_identities(filter=filter, zone=zone, remove=remove)
except ApiException as e:
    print("Exception when calling AuthApi->delete_mapping_identities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter to apply when deleting identity mappings. | [optional] 
 **zone** | **str**| Optional zone. | [optional] 
 **remove** | **bool**| Delete mapping instead of flush mapping cache. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mapping_identity**
> delete_mapping_identity(mapping_identity_id, zone=zone, _2way=_2way, target=target, remove=remove)



Flush the entire idmap cache.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
mapping_identity_id = 'mapping_identity_id_example' # str | Flush the entire idmap cache.
zone = 'zone_example' # str | Optional zone. (optional)
_2way = true # bool | Delete the bi-directional mapping from source to target and target to source. (optional)
target = 'target_example' # str | Target identity persona. (optional)
remove = true # bool | Delete mapping instead of flush mapping from cache. (optional)

try:
    api_instance.delete_mapping_identity(mapping_identity_id, zone=zone, _2way=_2way, target=target, remove=remove)
except ApiException as e:
    print("Exception when calling AuthApi->delete_mapping_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_identity_id** | **str**| Flush the entire idmap cache. | 
 **zone** | **str**| Optional zone. | [optional] 
 **_2way** | **bool**| Delete the bi-directional mapping from source to target and target to source. | [optional] 
 **target** | **str**| Target identity persona. | [optional] 
 **remove** | **bool**| Delete mapping instead of flush mapping from cache. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_providers_ads_by_id**
> delete_providers_ads_by_id(providers_ads_id)



Delete the ADS provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_ads_id = 'providers_ads_id_example' # str | Delete the ADS provider.

try:
    api_instance.delete_providers_ads_by_id(providers_ads_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_providers_ads_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_ads_id** | **str**| Delete the ADS provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_providers_file_by_id**
> delete_providers_file_by_id(providers_file_id)



Delete the file provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_file_id = 'providers_file_id_example' # str | Delete the file provider.

try:
    api_instance.delete_providers_file_by_id(providers_file_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_providers_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_file_id** | **str**| Delete the file provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_providers_krb5_by_id**
> delete_providers_krb5_by_id(providers_krb5_id)



Delete the KRB5 provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_krb5_id = 'providers_krb5_id_example' # str | Delete the KRB5 provider.

try:
    api_instance.delete_providers_krb5_by_id(providers_krb5_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_providers_krb5_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_krb5_id** | **str**| Delete the KRB5 provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_providers_ldap_by_id**
> delete_providers_ldap_by_id(providers_ldap_id)



Delete the LDAP provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_ldap_id = 'providers_ldap_id_example' # str | Delete the LDAP provider.

try:
    api_instance.delete_providers_ldap_by_id(providers_ldap_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_providers_ldap_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_ldap_id** | **str**| Delete the LDAP provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_providers_local_by_id**
> delete_providers_local_by_id(providers_local_id)



Delete the local provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_local_id = 'providers_local_id_example' # str | Delete the local provider.

try:
    api_instance.delete_providers_local_by_id(providers_local_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_providers_local_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_local_id** | **str**| Delete the local provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_providers_nis_by_id**
> delete_providers_nis_by_id(providers_nis_id)



Delete the NIS provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_nis_id = 'providers_nis_id_example' # str | Delete the NIS provider.

try:
    api_instance.delete_providers_nis_by_id(providers_nis_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_providers_nis_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_nis_id** | **str**| Delete the NIS provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_settings_krb5_domain**
> delete_settings_krb5_domain(settings_krb5_domain_id)



Remove a krb5 domain.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_domain_id = 'settings_krb5_domain_id_example' # str | Remove a krb5 domain.

try:
    api_instance.delete_settings_krb5_domain(settings_krb5_domain_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_settings_krb5_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_domain_id** | **str**| Remove a krb5 domain. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_settings_krb5_realm**
> delete_settings_krb5_realm(settings_krb5_realm_id)



Remove a realm.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_realm_id = 'settings_krb5_realm_id_example' # str | Remove a realm.

try:
    api_instance.delete_settings_krb5_realm(settings_krb5_realm_id)
except ApiException as e:
    print("Exception when calling AuthApi->delete_settings_krb5_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_realm_id** | **str**| Remove a realm. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_access_user**
> AuthAccess get_auth_access_user(auth_access_user, path=path, zone=zone, numeric=numeric)



Determine user's access rights to a file

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_access_user = 'auth_access_user_example' # str | Determine user's access rights to a file
path = 'path_example' # str | Path to the file. Must be within /ifs. (optional)
zone = 'zone_example' # str | Access zone the user is in. (optional)
numeric = true # bool | Show the user's numeric identifier. (optional)

try:
    api_response = api_instance.get_auth_access_user(auth_access_user, path=path, zone=zone, numeric=numeric)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_access_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_access_user** | **str**| Determine user&#39;s access rights to a file | 
 **path** | **str**| Path to the file. Must be within /ifs. | [optional] 
 **zone** | **str**| Access zone the user is in. | [optional] 
 **numeric** | **bool**| Show the user&#39;s numeric identifier. | [optional] 

### Return type

[**AuthAccess**](AuthAccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_group**
> AuthGroups get_auth_group(auth_group_id, cached=cached, resolve_names=resolve_names, zone=zone, provider=provider)



Retrieve the group information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_group_id = 'auth_group_id_example' # str | Retrieve the group information.
cached = true # bool | If true, only return cached objects. (optional)
resolve_names = true # bool | Resolve names of personas. (optional)
zone = 'zone_example' # str | Filter groups by zone. (optional)
provider = 'provider_example' # str | Filter groups by provider. (optional)

try:
    api_response = api_instance.get_auth_group(auth_group_id, cached=cached, resolve_names=resolve_names, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_group_id** | **str**| Retrieve the group information. | 
 **cached** | **bool**| If true, only return cached objects. | [optional] 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **zone** | **str**| Filter groups by zone. | [optional] 
 **provider** | **str**| Filter groups by provider. | [optional] 

### Return type

[**AuthGroups**](AuthGroups.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_id**
> AuthId get_auth_id()



Retrieve the current security token.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_auth_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthId**](AuthId.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_netgroup**
> AuthNetgroups get_auth_netgroup(auth_netgroup_id, ignore_errors=ignore_errors, recursive=recursive, zone=zone, provider=provider)



Retrieve the user information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_netgroup_id = 'auth_netgroup_id_example' # str | Retrieve the user information.
ignore_errors = true # bool | Ignore netgroup errors. (optional)
recursive = true # bool | Perform recursive search. (optional)
zone = 'zone_example' # str | Filter users by zone. (optional)
provider = 'provider_example' # str | Filter users by provider. (optional)

try:
    api_response = api_instance.get_auth_netgroup(auth_netgroup_id, ignore_errors=ignore_errors, recursive=recursive, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_netgroup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_netgroup_id** | **str**| Retrieve the user information. | 
 **ignore_errors** | **bool**| Ignore netgroup errors. | [optional] 
 **recursive** | **bool**| Perform recursive search. | [optional] 
 **zone** | **str**| Filter users by zone. | [optional] 
 **provider** | **str**| Filter users by provider. | [optional] 

### Return type

[**AuthNetgroups**](AuthNetgroups.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_privileges**
> AuthPrivileges get_auth_privileges()



List all privileges.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_auth_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthPrivileges**](AuthPrivileges.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_role**
> AuthRoles get_auth_role(auth_role_id, resolve_names=resolve_names)



Retrieve the role information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_role_id = 'auth_role_id_example' # str | Retrieve the role information.
resolve_names = true # bool | Resolve names of personas. (optional)

try:
    api_response = api_instance.get_auth_role(auth_role_id, resolve_names=resolve_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_role_id** | **str**| Retrieve the role information. | 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 

### Return type

[**AuthRoles**](AuthRoles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_shells**
> AuthShells get_auth_shells()



List all shells.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_auth_shells()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_shells: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthShells**](AuthShells.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_user**
> AuthUsers get_auth_user(auth_user_id, cached=cached, resolve_names=resolve_names, zone=zone, provider=provider)



Retrieve the user information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_user_id = 'auth_user_id_example' # str | Retrieve the user information.
cached = true # bool | If true, only return cached objects. (optional)
resolve_names = true # bool | Resolve names of personas. (optional)
zone = 'zone_example' # str | Filter users by zone. (optional)
provider = 'provider_example' # str | Filter users by provider. (optional)

try:
    api_response = api_instance.get_auth_user(auth_user_id, cached=cached, resolve_names=resolve_names, zone=zone, provider=provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user_id** | **str**| Retrieve the user information. | 
 **cached** | **bool**| If true, only return cached objects. | [optional] 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **zone** | **str**| Filter users by zone. | [optional] 
 **provider** | **str**| Filter users by provider. | [optional] 

### Return type

[**AuthUsers**](AuthUsers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_wellknown**
> AuthWellknowns get_auth_wellknown(auth_wellknown_id, scope=scope)



Retrieve the wellknown persona.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_wellknown_id = 'auth_wellknown_id_example' # str | Retrieve the wellknown persona.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_auth_wellknown(auth_wellknown_id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_wellknown: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_wellknown_id** | **str**| Retrieve the wellknown persona. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**AuthWellknowns**](AuthWellknowns.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_wellknowns**
> AuthWellknowns get_auth_wellknowns()



List all wellknown personas.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_auth_wellknowns()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_wellknowns: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthWellknowns**](AuthWellknowns.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_identity**
> MappingIdentities get_mapping_identity(mapping_identity_id, nocreate=nocreate, zone=zone)



Retrieve all identity mappings (uid, gid, sid, and on-disk) for the supplied source persona.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
mapping_identity_id = 'mapping_identity_id_example' # str | Retrieve all identity mappings (uid, gid, sid, and on-disk) for the supplied source persona.
nocreate = true # bool | Idmap should attempt to create missing identity mappings. (optional)
zone = 'zone_example' # str | Optional zone. (optional)

try:
    api_response = api_instance.get_mapping_identity(mapping_identity_id, nocreate=nocreate, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_mapping_identity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_identity_id** | **str**| Retrieve all identity mappings (uid, gid, sid, and on-disk) for the supplied source persona. | 
 **nocreate** | **bool**| Idmap should attempt to create missing identity mappings. | [optional] 
 **zone** | **str**| Optional zone. | [optional] 

### Return type

[**MappingIdentities**](MappingIdentities.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_users_lookup**
> MappingUsersLookup get_mapping_users_lookup(primary_gid=primary_gid, gid=gid, uid=uid, zone=zone, user=user)



Retrieve the user information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
primary_gid = 56 # int | The user's primary group ID. (optional)
gid = [56] # list[int] | The IDs of the groups that the user belongs to. (optional)
uid = 56 # int | The user ID. (optional)
zone = 'zone_example' # str | The zone the user bolongs to. (optional)
user = 'user_example' # str | The user name. (optional)

try:
    api_response = api_instance.get_mapping_users_lookup(primary_gid=primary_gid, gid=gid, uid=uid, zone=zone, user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_mapping_users_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_gid** | **int**| The user&#39;s primary group ID. | [optional] 
 **gid** | [**list[int]**](int.md)| The IDs of the groups that the user belongs to. | [optional] 
 **uid** | **int**| The user ID. | [optional] 
 **zone** | **str**| The zone the user bolongs to. | [optional] 
 **user** | **str**| The user name. | [optional] 

### Return type

[**MappingUsersLookup**](MappingUsersLookup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_users_rules**
> MappingUsersRules get_mapping_users_rules(zone=zone)



Retrieve the user mapping rules.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
zone = 'zone_example' # str | The zone to which the user mapping applies. (optional)

try:
    api_response = api_instance.get_mapping_users_rules(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_mapping_users_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| The zone to which the user mapping applies. | [optional] 

### Return type

[**MappingUsersRules**](MappingUsersRules.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_ads_by_id**
> ProvidersAds get_providers_ads_by_id(providers_ads_id, scope=scope)



Retrieve the ADS provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_ads_id = 'providers_ads_id_example' # str | Retrieve the ADS provider.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_providers_ads_by_id(providers_ads_id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_providers_ads_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_ads_id** | **str**| Retrieve the ADS provider. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersAds**](ProvidersAds.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_file_by_id**
> ProvidersFile get_providers_file_by_id(providers_file_id, scope=scope)



Retrieve the file provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_file_id = 'providers_file_id_example' # str | Retrieve the file provider.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_providers_file_by_id(providers_file_id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_providers_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_file_id** | **str**| Retrieve the file provider. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersFile**](ProvidersFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_krb5_by_id**
> ProvidersKrb5 get_providers_krb5_by_id(providers_krb5_id, scope=scope)



Retrieve the KRB5 provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_krb5_id = 'providers_krb5_id_example' # str | Retrieve the KRB5 provider.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_providers_krb5_by_id(providers_krb5_id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_providers_krb5_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_krb5_id** | **str**| Retrieve the KRB5 provider. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersKrb5**](ProvidersKrb5.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_ldap_by_id**
> ProvidersLdap get_providers_ldap_by_id(providers_ldap_id, scope=scope)



Retrieve the LDAP provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_ldap_id = 'providers_ldap_id_example' # str | Retrieve the LDAP provider.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_providers_ldap_by_id(providers_ldap_id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_providers_ldap_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_ldap_id** | **str**| Retrieve the LDAP provider. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersLdap**](ProvidersLdap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_local**
> ProvidersLocal get_providers_local(scope=scope)



List all local providers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_providers_local(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_providers_local: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersLocal**](ProvidersLocal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_local_by_id**
> ProvidersLocal get_providers_local_by_id(providers_local_id, scope=scope)



Retrieve the local provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_local_id = 'providers_local_id_example' # str | Retrieve the local provider.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_providers_local_by_id(providers_local_id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_providers_local_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_local_id** | **str**| Retrieve the local provider. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersLocal**](ProvidersLocal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_nis_by_id**
> ProvidersNis get_providers_nis_by_id(providers_nis_id, scope=scope)



Retrieve the NIS provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_nis_id = 'providers_nis_id_example' # str | Retrieve the NIS provider.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_providers_nis_by_id(providers_nis_id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_providers_nis_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_nis_id** | **str**| Retrieve the NIS provider. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersNis**](ProvidersNis.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_providers_summary**
> ProvidersSummary get_providers_summary()



Retrieve the summary information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_providers_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_providers_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProvidersSummary**](ProvidersSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_global**
> SettingsGlobal get_settings_global(scope=scope, zone=zone)



Retrieve the global settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
zone = 'zone_example' # str | Zone which contains any per-zone settings. (optional)

try:
    api_response = api_instance.get_settings_global(scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **zone** | **str**| Zone which contains any per-zone settings. | [optional] 

### Return type

[**SettingsGlobal**](SettingsGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_krb5_defaults**
> SettingsKrb5Defaults get_settings_krb5_defaults()



Retrieve the krb5 settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_settings_krb5_defaults()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_settings_krb5_defaults: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsKrb5Defaults**](SettingsKrb5Defaults.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_krb5_domain**
> SettingsKrb5Domains get_settings_krb5_domain(settings_krb5_domain_id)



View the krb5 domain settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_domain_id = 'settings_krb5_domain_id_example' # str | View the krb5 domain settings.

try:
    api_response = api_instance.get_settings_krb5_domain(settings_krb5_domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_settings_krb5_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_domain_id** | **str**| View the krb5 domain settings. | 

### Return type

[**SettingsKrb5Domains**](SettingsKrb5Domains.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_krb5_realm**
> Empty get_settings_krb5_realm(settings_krb5_realm_id)



Retrieve the krb5 settings for realms.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_realm_id = 'settings_krb5_realm_id_example' # str | Retrieve the krb5 settings for realms.

try:
    api_response = api_instance.get_settings_krb5_realm(settings_krb5_realm_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_settings_krb5_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_realm_id** | **str**| Retrieve the krb5 settings for realms. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_mapping**
> SettingsMapping get_settings_mapping(scope=scope, zone=zone)



Retrieve the mapping settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
zone = 'zone_example' # str | Access zone which contains mapping settings. (optional)

try:
    api_response = api_instance.get_settings_mapping(scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_settings_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **zone** | **str**| Access zone which contains mapping settings. | [optional] 

### Return type

[**SettingsMapping**](SettingsMapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auth_groups**
> AuthGroupsExtended list_auth_groups(domain=domain, zone=zone, resume=resume, cached=cached, resolve_names=resolve_names, filter=filter, limit=limit, provider=provider, query_member_of=query_member_of)



List all groups.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
domain = 'domain_example' # str | Filter groups by domain. (optional)
zone = 'zone_example' # str | Filter groups by zone. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
cached = true # bool | If true, only return cached objects. (optional)
resolve_names = true # bool | Resolve names of personas. (optional)
filter = 'filter_example' # str | Filter groups by name prefix. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
provider = 'provider_example' # str | Filter groups by provider. (optional)
query_member_of = true # bool | Enumerate all groups that a group is a member of. (optional)

try:
    api_response = api_instance.list_auth_groups(domain=domain, zone=zone, resume=resume, cached=cached, resolve_names=resolve_names, filter=filter, limit=limit, provider=provider, query_member_of=query_member_of)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_auth_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Filter groups by domain. | [optional] 
 **zone** | **str**| Filter groups by zone. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **cached** | **bool**| If true, only return cached objects. | [optional] 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **filter** | **str**| Filter groups by name prefix. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **provider** | **str**| Filter groups by provider. | [optional] 
 **query_member_of** | **bool**| Enumerate all groups that a group is a member of. | [optional] 

### Return type

[**AuthGroupsExtended**](AuthGroupsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auth_roles**
> AuthRolesExtended list_auth_roles(sort=sort, resolve_names=resolve_names, limit=limit, dir=dir, resume=resume)



List all roles.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resolve_names = true # bool | Filter users by zone. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_auth_roles(sort=sort, resolve_names=resolve_names, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_auth_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resolve_names** | **bool**| Filter users by zone. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**AuthRolesExtended**](AuthRolesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auth_users**
> AuthUsersExtended list_auth_users(domain=domain, zone=zone, resume=resume, cached=cached, resolve_names=resolve_names, filter=filter, limit=limit, provider=provider, query_member_of=query_member_of)



List all users.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
domain = 'domain_example' # str | Filter users by domain. (optional)
zone = 'zone_example' # str | Filter users by zone. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
cached = true # bool | If true, only return cached objects. (optional)
resolve_names = true # bool | Resolve names of personas. (optional)
filter = 'filter_example' # str | Filter users by name prefix. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
provider = 'provider_example' # str | Filter users by provider. (optional)
query_member_of = true # bool | Enumerate all users that a group is a member of. (optional)

try:
    api_response = api_instance.list_auth_users(domain=domain, zone=zone, resume=resume, cached=cached, resolve_names=resolve_names, filter=filter, limit=limit, provider=provider, query_member_of=query_member_of)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_auth_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **str**| Filter users by domain. | [optional] 
 **zone** | **str**| Filter users by zone. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **cached** | **bool**| If true, only return cached objects. | [optional] 
 **resolve_names** | **bool**| Resolve names of personas. | [optional] 
 **filter** | **str**| Filter users by name prefix. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **provider** | **str**| Filter users by provider. | [optional] 
 **query_member_of** | **bool**| Enumerate all users that a group is a member of. | [optional] 

### Return type

[**AuthUsersExtended**](AuthUsersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers_ads**
> ProvidersAds list_providers_ads(scope=scope)



List all ADS providers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.list_providers_ads(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_providers_ads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersAds**](ProvidersAds.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers_file**
> ProvidersFile list_providers_file(scope=scope)



List all file providers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.list_providers_file(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_providers_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersFile**](ProvidersFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers_krb5**
> ProvidersKrb5Extended list_providers_krb5(scope=scope)



List all KRB5 providers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.list_providers_krb5(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_providers_krb5: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersKrb5Extended**](ProvidersKrb5Extended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers_ldap**
> ProvidersLdap list_providers_ldap(scope=scope)



List all LDAP providers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.list_providers_ldap(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_providers_ldap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersLdap**](ProvidersLdap.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_providers_nis**
> ProvidersNis list_providers_nis(scope=scope)



List all NIS providers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.list_providers_nis(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_providers_nis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**ProvidersNis**](ProvidersNis.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings_krb5_domains**
> SettingsKrb5DomainsExtended list_settings_krb5_domains()



Retrieve the krb5 settings for domains.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.list_settings_krb5_domains()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_settings_krb5_domains: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SettingsKrb5DomainsExtended**](SettingsKrb5DomainsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_settings_krb5_realms**
> Empty list_settings_krb5_realms()



Retrieve the krb5 settings for realms.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.list_settings_krb5_realms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->list_settings_krb5_realms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_group**
> update_auth_group(auth_group, auth_group_id, zone=zone, provider=provider)



Modify the group.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_group = isi_sdk_7_2.AuthGroup() # AuthGroup | 
auth_group_id = 'auth_group_id_example' # str | Modify the group.
zone = 'zone_example' # str | Optional zone. (optional)
provider = 'provider_example' # str | Optional provider type. (optional)

try:
    api_instance.update_auth_group(auth_group, auth_group_id, zone=zone, provider=provider)
except ApiException as e:
    print("Exception when calling AuthApi->update_auth_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_group** | [**AuthGroup**](AuthGroup.md)|  | 
 **auth_group_id** | **str**| Modify the group. | 
 **zone** | **str**| Optional zone. | [optional] 
 **provider** | **str**| Optional provider type. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_role**
> update_auth_role(auth_role, auth_role_id)



Modify the role.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_role = isi_sdk_7_2.AuthRole() # AuthRole | 
auth_role_id = 'auth_role_id_example' # str | Modify the role.

try:
    api_instance.update_auth_role(auth_role, auth_role_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_auth_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_role** | [**AuthRole**](AuthRole.md)|  | 
 **auth_role_id** | **str**| Modify the role. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_user**
> update_auth_user(auth_user, auth_user_id, zone=zone, provider=provider)



Modify the user.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
auth_user = isi_sdk_7_2.AuthUser() # AuthUser | 
auth_user_id = 'auth_user_id_example' # str | Modify the user.
zone = 'zone_example' # str | Optional zone. (optional)
provider = 'provider_example' # str | Optional provider type. (optional)

try:
    api_instance.update_auth_user(auth_user, auth_user_id, zone=zone, provider=provider)
except ApiException as e:
    print("Exception when calling AuthApi->update_auth_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_user** | [**AuthUser**](AuthUser.md)|  | 
 **auth_user_id** | **str**| Modify the user. | 
 **zone** | **str**| Optional zone. | [optional] 
 **provider** | **str**| Optional provider type. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapping_users_rules**
> update_mapping_users_rules(mapping_users_rules)



Modify the user mapping rules.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
mapping_users_rules = isi_sdk_7_2.MappingUsersRulesExtended() # MappingUsersRulesExtended | 

try:
    api_instance.update_mapping_users_rules(mapping_users_rules)
except ApiException as e:
    print("Exception when calling AuthApi->update_mapping_users_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_users_rules** | [**MappingUsersRulesExtended**](MappingUsersRulesExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_providers_ads_by_id**
> update_providers_ads_by_id(providers_ads_id_params, providers_ads_id)



Modify the ADS provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_ads_id_params = isi_sdk_7_2.ProvidersAdsIdParams() # ProvidersAdsIdParams | 
providers_ads_id = 'providers_ads_id_example' # str | Modify the ADS provider.

try:
    api_instance.update_providers_ads_by_id(providers_ads_id_params, providers_ads_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_providers_ads_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_ads_id_params** | [**ProvidersAdsIdParams**](ProvidersAdsIdParams.md)|  | 
 **providers_ads_id** | **str**| Modify the ADS provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_providers_file_by_id**
> update_providers_file_by_id(providers_file_id_params, providers_file_id)



Modify the file provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_file_id_params = isi_sdk_7_2.ProvidersFileIdParams() # ProvidersFileIdParams | 
providers_file_id = 'providers_file_id_example' # str | Modify the file provider.

try:
    api_instance.update_providers_file_by_id(providers_file_id_params, providers_file_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_providers_file_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_file_id_params** | [**ProvidersFileIdParams**](ProvidersFileIdParams.md)|  | 
 **providers_file_id** | **str**| Modify the file provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_providers_krb5_by_id**
> update_providers_krb5_by_id(providers_krb5_id_params, providers_krb5_id)



Modify the KRB5 provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_krb5_id_params = isi_sdk_7_2.ProvidersKrb5IdParams() # ProvidersKrb5IdParams | 
providers_krb5_id = 'providers_krb5_id_example' # str | Modify the KRB5 provider.

try:
    api_instance.update_providers_krb5_by_id(providers_krb5_id_params, providers_krb5_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_providers_krb5_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_krb5_id_params** | [**ProvidersKrb5IdParams**](ProvidersKrb5IdParams.md)|  | 
 **providers_krb5_id** | **str**| Modify the KRB5 provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_providers_ldap_by_id**
> update_providers_ldap_by_id(providers_ldap_id_params, providers_ldap_id)



Modify the LDAP provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_ldap_id_params = isi_sdk_7_2.ProvidersLdapIdParams() # ProvidersLdapIdParams | 
providers_ldap_id = 'providers_ldap_id_example' # str | Modify the LDAP provider.

try:
    api_instance.update_providers_ldap_by_id(providers_ldap_id_params, providers_ldap_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_providers_ldap_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_ldap_id_params** | [**ProvidersLdapIdParams**](ProvidersLdapIdParams.md)|  | 
 **providers_ldap_id** | **str**| Modify the LDAP provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_providers_local_by_id**
> update_providers_local_by_id(providers_local_id_params, providers_local_id)



Modify the local provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_local_id_params = isi_sdk_7_2.ProvidersLocalIdParams() # ProvidersLocalIdParams | 
providers_local_id = 'providers_local_id_example' # str | Modify the local provider.

try:
    api_instance.update_providers_local_by_id(providers_local_id_params, providers_local_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_providers_local_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_local_id_params** | [**ProvidersLocalIdParams**](ProvidersLocalIdParams.md)|  | 
 **providers_local_id** | **str**| Modify the local provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_providers_nis_by_id**
> update_providers_nis_by_id(providers_nis_id_params, providers_nis_id)



Modify the NIS provider.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
providers_nis_id_params = isi_sdk_7_2.ProvidersNisIdParams() # ProvidersNisIdParams | 
providers_nis_id = 'providers_nis_id_example' # str | Modify the NIS provider.

try:
    api_instance.update_providers_nis_by_id(providers_nis_id_params, providers_nis_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_providers_nis_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **providers_nis_id_params** | [**ProvidersNisIdParams**](ProvidersNisIdParams.md)|  | 
 **providers_nis_id** | **str**| Modify the NIS provider. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_global**
> update_settings_global(settings_global, zone=zone)



Modify the global settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_global = isi_sdk_7_2.SettingsGlobalGlobalSettings() # SettingsGlobalGlobalSettings | 
zone = 'zone_example' # str | Zone which contains any per-zone settings. (optional)

try:
    api_instance.update_settings_global(settings_global, zone=zone)
except ApiException as e:
    print("Exception when calling AuthApi->update_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_global** | [**SettingsGlobalGlobalSettings**](SettingsGlobalGlobalSettings.md)|  | 
 **zone** | **str**| Zone which contains any per-zone settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_krb5_defaults**
> update_settings_krb5_defaults(settings_krb5_defaults)



Modify the krb5 settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_defaults = isi_sdk_7_2.SettingsKrb5DefaultsKrb5Settings() # SettingsKrb5DefaultsKrb5Settings | 

try:
    api_instance.update_settings_krb5_defaults(settings_krb5_defaults)
except ApiException as e:
    print("Exception when calling AuthApi->update_settings_krb5_defaults: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_defaults** | [**SettingsKrb5DefaultsKrb5Settings**](SettingsKrb5DefaultsKrb5Settings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_krb5_domain**
> update_settings_krb5_domain(settings_krb5_domain, settings_krb5_domain_id)



Modify the krb5 domain settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_domain = isi_sdk_7_2.SettingsKrb5Domain() # SettingsKrb5Domain | 
settings_krb5_domain_id = 'settings_krb5_domain_id_example' # str | Modify the krb5 domain settings.

try:
    api_instance.update_settings_krb5_domain(settings_krb5_domain, settings_krb5_domain_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_settings_krb5_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_domain** | [**SettingsKrb5Domain**](SettingsKrb5Domain.md)|  | 
 **settings_krb5_domain_id** | **str**| Modify the krb5 domain settings. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_krb5_realm**
> update_settings_krb5_realm(settings_krb5_realm, settings_krb5_realm_id)



Modify the krb5 realm settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_krb5_realm = isi_sdk_7_2.SettingsKrb5Realm() # SettingsKrb5Realm | 
settings_krb5_realm_id = 'settings_krb5_realm_id_example' # str | Modify the krb5 realm settings.

try:
    api_instance.update_settings_krb5_realm(settings_krb5_realm, settings_krb5_realm_id)
except ApiException as e:
    print("Exception when calling AuthApi->update_settings_krb5_realm: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_krb5_realm** | [**SettingsKrb5Realm**](SettingsKrb5Realm.md)|  | 
 **settings_krb5_realm_id** | **str**| Modify the krb5 realm settings. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_settings_mapping**
> update_settings_mapping(settings_mapping, zone=zone)



Modify the mapping settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.AuthApi(isi_sdk_7_2.ApiClient(configuration))
settings_mapping = isi_sdk_7_2.SettingsMappingMappingSettings() # SettingsMappingMappingSettings | 
zone = 'zone_example' # str | Access zone which contains mapping settings. (optional)

try:
    api_instance.update_settings_mapping(settings_mapping, zone=zone)
except ApiException as e:
    print("Exception when calling AuthApi->update_settings_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settings_mapping** | [**SettingsMappingMappingSettings**](SettingsMappingMappingSettings.md)|  | 
 **zone** | **str**| Access zone which contains mapping settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

