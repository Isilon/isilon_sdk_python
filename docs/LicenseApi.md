# isi_sdk_8_0_1.LicenseApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_license_license**](LicenseApi.md#create_license_license) | **POST** /platform/1/license/licenses | 
[**get_license_license**](LicenseApi.md#get_license_license) | **GET** /platform/1/license/licenses/{LicenseLicenseId} | 
[**list_license_licenses**](LicenseApi.md#list_license_licenses) | **GET** /platform/1/license/licenses | 


# **create_license_license**
> create_license_license(license_license)



Install a new license key.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.LicenseApi(isi_sdk_8_0_1.ApiClient(configuration))
license_license = isi_sdk_8_0_1.LicenseLicenseCreateParams() # LicenseLicenseCreateParams | 

try:
    api_instance.create_license_license(license_license)
except ApiException as e:
    print("Exception when calling LicenseApi->create_license_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_license** | [**LicenseLicenseCreateParams**](LicenseLicenseCreateParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_license**
> LicenseLicenses get_license_license(license_license_id)



Retrieve license information for the feature.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.LicenseApi(isi_sdk_8_0_1.ApiClient(configuration))
license_license_id = 'license_license_id_example' # str | Retrieve license information for the feature.

try:
    api_response = api_instance.get_license_license(license_license_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_license_id** | **str**| Retrieve license information for the feature. | 

### Return type

[**LicenseLicenses**](LicenseLicenses.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_license_licenses**
> LicenseLicenses list_license_licenses()



Retrieve license information for all licensable products.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0_1
from isi_sdk_8_0_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0_1.LicenseApi(isi_sdk_8_0_1.ApiClient(configuration))

try:
    api_response = api_instance.list_license_licenses()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->list_license_licenses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseLicenses**](LicenseLicenses.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

