# isi_sdk_8_2_0.IdResolutionApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_id_resolution_domain**](IdResolutionApi.md#get_id_resolution_domain) | **GET** /platform/7/id-resolution/domains/{IdResolutionDomainId} | 
[**get_id_resolution_domains**](IdResolutionApi.md#get_id_resolution_domains) | **GET** /platform/7/id-resolution/domains | 
[**get_id_resolution_lin**](IdResolutionApi.md#get_id_resolution_lin) | **GET** /platform/7/id-resolution/lins/{IdResolutionLinId} | 
[**get_id_resolution_lins**](IdResolutionApi.md#get_id_resolution_lins) | **GET** /platform/7/id-resolution/lins | 
[**get_id_resolution_zone**](IdResolutionApi.md#get_id_resolution_zone) | **GET** /platform/7/id-resolution/zones/{IdResolutionZoneId} | 
[**get_id_resolution_zones**](IdResolutionApi.md#get_id_resolution_zones) | **GET** /platform/7/id-resolution/zones | 


# **get_id_resolution_domain**
> IdResolutionDomains get_id_resolution_domain(id_resolution_domain_id)



List domain to path mappings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.IdResolutionApi(isi_sdk_8_2_0.ApiClient(configuration))
id_resolution_domain_id = 'id_resolution_domain_id_example' # str | List domain to path mappings.

try:
    api_response = api_instance.get_id_resolution_domain(id_resolution_domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionApi->get_id_resolution_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_resolution_domain_id** | **str**| List domain to path mappings. | 

### Return type

[**IdResolutionDomains**](IdResolutionDomains.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id_resolution_domains**
> IdResolutionDomainsExtended get_id_resolution_domains(domains=domains, sort=sort, limit=limit, dir=dir, resume=resume)



List domain to path mappings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.IdResolutionApi(isi_sdk_8_2_0.ApiClient(configuration))
domains = 'domains_example' # str | A comma separated list specifying the domains that will be mapped with a path. Only the domains specified in this list will be mapped. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_id_resolution_domains(domains=domains, sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionApi->get_id_resolution_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domains** | **str**| A comma separated list specifying the domains that will be mapped with a path. Only the domains specified in this list will be mapped. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**IdResolutionDomainsExtended**](IdResolutionDomainsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id_resolution_lin**
> IdResolutionDomains get_id_resolution_lin(id_resolution_lin_id)



List lin to path mappings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.IdResolutionApi(isi_sdk_8_2_0.ApiClient(configuration))
id_resolution_lin_id = 56 # int | List lin to path mappings.

try:
    api_response = api_instance.get_id_resolution_lin(id_resolution_lin_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionApi->get_id_resolution_lin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_resolution_lin_id** | **int**| List lin to path mappings. | 

### Return type

[**IdResolutionDomains**](IdResolutionDomains.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id_resolution_lins**
> IdResolutionDomainsExtended get_id_resolution_lins(sort=sort, lins=lins, limit=limit, dir=dir, resume=resume)



List lin to path mappings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.IdResolutionApi(isi_sdk_8_2_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
lins = 'lins_example' # str | A comma separated list specifying the lins that will be mapped with a path. Only the lins specified in this list will be mapped. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_id_resolution_lins(sort=sort, lins=lins, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionApi->get_id_resolution_lins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **lins** | **str**| A comma separated list specifying the lins that will be mapped with a path. Only the lins specified in this list will be mapped. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**IdResolutionDomainsExtended**](IdResolutionDomainsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id_resolution_zone**
> IdResolutionZones get_id_resolution_zone(id_resolution_zone_id)



List zone id to zone name mappings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.IdResolutionApi(isi_sdk_8_2_0.ApiClient(configuration))
id_resolution_zone_id = 'id_resolution_zone_id_example' # str | List zone id to zone name mappings.

try:
    api_response = api_instance.get_id_resolution_zone(id_resolution_zone_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionApi->get_id_resolution_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_resolution_zone_id** | **str**| List zone id to zone name mappings. | 

### Return type

[**IdResolutionZones**](IdResolutionZones.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_id_resolution_zones**
> IdResolutionZonesExtended get_id_resolution_zones(sort=sort, limit=limit, zone_ids=zone_ids, dir=dir, resume=resume)



List zone id to zone name mappings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_0
from isi_sdk_8_2_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_0.IdResolutionApi(isi_sdk_8_2_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
zone_ids = 'zone_ids_example' # str | A comma separated list specifying the zone IDs to map with a zone name. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_id_resolution_zones(sort=sort, limit=limit, zone_ids=zone_ids, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionApi->get_id_resolution_zones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **zone_ids** | **str**| A comma separated list specifying the zone IDs to map with a zone name. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**IdResolutionZonesExtended**](IdResolutionZonesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

