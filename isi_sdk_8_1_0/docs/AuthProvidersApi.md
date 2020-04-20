# isi_sdk_8_1_0.AuthProvidersApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ads_provider_controllers**](AuthProvidersApi.md#get_ads_provider_controllers) | **GET** /platform/3/auth/providers/ads/{Id}/controllers | 
[**get_ads_provider_domain**](AuthProvidersApi.md#get_ads_provider_domain) | **GET** /platform/3/auth/providers/ads/{Id}/domains/{AdsProviderDomainId} | 
[**get_ads_provider_domains**](AuthProvidersApi.md#get_ads_provider_domains) | **GET** /platform/3/auth/providers/ads/{Id}/domains | 
[**get_ads_provider_search**](AuthProvidersApi.md#get_ads_provider_search) | **GET** /platform/1/auth/providers/ads/{Id}/search | 


# **get_ads_provider_controllers**
> AdsProviderControllers get_ads_provider_controllers(id, groupnet=groupnet)



List all ADS controllers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.AuthProvidersApi(isi_sdk_8_1_0.ApiClient(configuration))
id = 'id_example' # str | 
groupnet = 'groupnet_example' # str | Groupnet identifier (optional)

try:
    api_response = api_instance.get_ads_provider_controllers(id, groupnet=groupnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthProvidersApi->get_ads_provider_controllers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **groupnet** | **str**| Groupnet identifier | [optional] 

### Return type

[**AdsProviderControllers**](AdsProviderControllers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ads_provider_domain**
> AdsProviderDomains get_ads_provider_domain(ads_provider_domain_id, id)



Retrieve the ADS domain information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.AuthProvidersApi(isi_sdk_8_1_0.ApiClient(configuration))
ads_provider_domain_id = 'ads_provider_domain_id_example' # str | Retrieve the ADS domain information.
id = 'id_example' # str | 

try:
    api_response = api_instance.get_ads_provider_domain(ads_provider_domain_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthProvidersApi->get_ads_provider_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ads_provider_domain_id** | **str**| Retrieve the ADS domain information. | 
 **id** | **str**|  | 

### Return type

[**AdsProviderDomains**](AdsProviderDomains.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ads_provider_domains**
> AdsProviderDomains get_ads_provider_domains(id, scope=scope)



List all ADS domains.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.AuthProvidersApi(isi_sdk_8_1_0.ApiClient(configuration))
id = 'id_example' # str | 
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_ads_provider_domains(id, scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthProvidersApi->get_ads_provider_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**AdsProviderDomains**](AdsProviderDomains.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ads_provider_search**
> AdsProviderSearch get_ads_provider_search(id, domain=domain, description=description, resume=resume, search_users=search_users, filter=filter, limit=limit, user=user, password=password, search_groups=search_groups)



Retrieve search results.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_0
from isi_sdk_8_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_0.AuthProvidersApi(isi_sdk_8_1_0.ApiClient(configuration))
id = 'id_example' # str | 
domain = 'domain_example' # str | The domain to search in. (optional)
description = 'description_example' # str | The user or group description to search for. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
search_users = true # bool | If true, search for users. (optional)
filter = 'filter_example' # str | The LDAP filter to apply to the search. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
user = 'user_example' # str | The user name for the domain if untrusted. (optional)
password = 'password_example' # str | The password for the domain if untrusted. (optional)
search_groups = true # bool | If true, search for groups. (optional)

try:
    api_response = api_instance.get_ads_provider_search(id, domain=domain, description=description, resume=resume, search_users=search_users, filter=filter, limit=limit, user=user, password=password, search_groups=search_groups)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthProvidersApi->get_ads_provider_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **domain** | **str**| The domain to search in. | [optional] 
 **description** | **str**| The user or group description to search for. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **search_users** | **bool**| If true, search for users. | [optional] 
 **filter** | **str**| The LDAP filter to apply to the search. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **user** | **str**| The user name for the domain if untrusted. | [optional] 
 **password** | **str**| The password for the domain if untrusted. | [optional] 
 **search_groups** | **bool**| If true, search for groups. | [optional] 

### Return type

[**AdsProviderSearch**](AdsProviderSearch.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

