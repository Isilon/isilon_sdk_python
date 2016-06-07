# isi_sdk.WormApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_worm_domain**](WormApi.md#create_worm_domain) | **POST** /platform/1/worm/domains | 
[**get_worm_domain**](WormApi.md#get_worm_domain) | **GET** /platform/1/worm/domains/{WormDomainId} | 
[**get_worm_settings**](WormApi.md#get_worm_settings) | **GET** /platform/1/worm/settings | 
[**list_worm_domains**](WormApi.md#list_worm_domains) | **GET** /platform/1/worm/domains | 
[**update_worm_domain**](WormApi.md#update_worm_domain) | **PUT** /platform/1/worm/domains/{WormDomainId} | 
[**update_worm_settings**](WormApi.md#update_worm_settings) | **PUT** /platform/1/worm/settings | 


# **create_worm_domain**
> WormDomainExtended create_worm_domain(worm_domain)



Create a WORM domain.

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
api_instance = isi_sdk.WormApi()
worm_domain = isi_sdk.WormDomainCreateParams() # WormDomainCreateParams | 

try: 
    api_response = api_instance.create_worm_domain(worm_domain)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WormApi->create_worm_domain: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worm_domain** | [**WormDomainCreateParams**](WormDomainCreateParams.md)|  | 

### Return type

[**WormDomainExtended**](WormDomainExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worm_domain**
> WormDomains get_worm_domain(worm_domain_id)



View a single WORM domain.

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
api_instance = isi_sdk.WormApi()
worm_domain_id = 'worm_domain_id_example' # str | View a single WORM domain.

try: 
    api_response = api_instance.get_worm_domain(worm_domain_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WormApi->get_worm_domain: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worm_domain_id** | **str**| View a single WORM domain. | 

### Return type

[**WormDomains**](WormDomains.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worm_settings**
> WormSettings get_worm_settings()



Get the global WORM settings.

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
api_instance = isi_sdk.WormApi()

try: 
    api_response = api_instance.get_worm_settings()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WormApi->get_worm_settings: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WormSettings**](WormSettings.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_worm_domains**
> WormDomainsExtended list_worm_domains(sort=sort, limit=limit, dir=dir, resume=resume)



List all WORM domains.

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
api_instance = isi_sdk.WormApi()
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try: 
    api_response = api_instance.list_worm_domains(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling WormApi->list_worm_domains: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**WormDomainsExtended**](WormDomainsExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_worm_domain**
> update_worm_domain(worm_domain, worm_domain_id)



Modify a single WORM domain.

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
api_instance = isi_sdk.WormApi()
worm_domain = isi_sdk.WormDomain() # WormDomain | 
worm_domain_id = 'worm_domain_id_example' # str | Modify a single WORM domain.

try: 
    api_instance.update_worm_domain(worm_domain, worm_domain_id)
except ApiException as e:
    print "Exception when calling WormApi->update_worm_domain: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worm_domain** | [**WormDomain**](WormDomain.md)|  | 
 **worm_domain_id** | **str**| Modify a single WORM domain. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_worm_settings**
> update_worm_settings(worm_settings)



Modify the global WORM settings.  All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.WormApi()
worm_settings = isi_sdk.WormSettingsExtended() # WormSettingsExtended | 

try: 
    api_instance.update_worm_settings(worm_settings)
except ApiException as e:
    print "Exception when calling WormApi->update_worm_settings: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worm_settings** | [**WormSettingsExtended**](WormSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

