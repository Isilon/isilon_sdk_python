# isilon_sdk.v9_2_1.AuthProvidersApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ads_provider_search_item**](AuthProvidersApi.md#create_ads_provider_search_item) | **POST** /platform/12/auth/providers/ads/{Id}/search | 
[**get_ads_provider_controllers**](AuthProvidersApi.md#get_ads_provider_controllers) | **GET** /platform/7/auth/providers/ads/{Id}/controllers | 
[**get_ads_provider_domain**](AuthProvidersApi.md#get_ads_provider_domain) | **GET** /platform/7/auth/providers/ads/{Id}/domains/{AdsProviderDomainId} | 
[**get_ads_provider_domains**](AuthProvidersApi.md#get_ads_provider_domains) | **GET** /platform/7/auth/providers/ads/{Id}/domains | 


# **create_ads_provider_search_item**
> CreateAdsProviderSearchItemResponse create_ads_provider_search_item(ads_provider_search_item, id)



Retrieve search results via HTTP POST.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.AuthProvidersApi(isilon_sdk.v9_2_1.ApiClient(configuration))
ads_provider_search_item = isilon_sdk.v9_2_1.AdsProviderSearchItem() # AdsProviderSearchItem | 
id = 'id_example' # str | 

try:
    api_response = api_instance.create_ads_provider_search_item(ads_provider_search_item, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthProvidersApi->create_ads_provider_search_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ads_provider_search_item** | [**AdsProviderSearchItem**](AdsProviderSearchItem.md)|  | 
 **id** | **str**|  | 

### Return type

[**CreateAdsProviderSearchItemResponse**](CreateAdsProviderSearchItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ads_provider_controllers**
> AdsProviderControllers get_ads_provider_controllers(id, dc_site=dc_site, groupnet=groupnet)



List all ADS controllers.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.AuthProvidersApi(isilon_sdk.v9_2_1.ApiClient(configuration))
id = 'id_example' # str | 
dc_site = 'dc_site_example' # str | Domain Controller site name (optional)
groupnet = 'groupnet_example' # str | Groupnet identifier (optional)

try:
    api_response = api_instance.get_ads_provider_controllers(id, dc_site=dc_site, groupnet=groupnet)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthProvidersApi->get_ads_provider_controllers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **dc_site** | **str**| Domain Controller site name | [optional] 
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
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.AuthProvidersApi(isilon_sdk.v9_2_1.ApiClient(configuration))
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
import isilon_sdk.v9_2_1
from isilon_sdk.v9_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_2_1.AuthProvidersApi(isilon_sdk.v9_2_1.ApiClient(configuration))
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

