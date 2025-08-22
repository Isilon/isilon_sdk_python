# isilon_sdk.v9_11_0.ConfigCatalogApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_catalog_status**](ConfigCatalogApi.md#get_config_catalog_status) | **GET** /platform/19/config-catalog/status | 
[**update_config_catalog_status**](ConfigCatalogApi.md#update_config_catalog_status) | **PUT** /platform/19/config-catalog/status | 


# **get_config_catalog_status**
> ConfigCatalogStatus get_config_catalog_status()



The config catalog status.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigCatalogApi(isilon_sdk.v9_11_0.ApiClient(configuration))

try:
    api_response = api_instance.get_config_catalog_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigCatalogApi->get_config_catalog_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigCatalogStatus**](ConfigCatalogStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_catalog_status**
> update_config_catalog_status(config_catalog_status)



The config catalog status.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_11_0
from isilon_sdk.v9_11_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_11_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_11_0.ConfigCatalogApi(isilon_sdk.v9_11_0.ApiClient(configuration))
config_catalog_status = isilon_sdk.v9_11_0.ConfigCatalogStatusExtended() # ConfigCatalogStatusExtended | 

try:
    api_instance.update_config_catalog_status(config_catalog_status)
except ApiException as e:
    print("Exception when calling ConfigCatalogApi->update_config_catalog_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_catalog_status** | [**ConfigCatalogStatusExtended**](ConfigCatalogStatusExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

