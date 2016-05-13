# isi_sdk.LicenseApi

All URIs are relative to *https://localhost*

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
import time
import isi_sdk
from isi_sdk.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic_auth
isi_sdk.configuration.username = 'YOUR_USERNAME'
isi_sdk.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk.LicenseApi()
license_license = isi_sdk.LicenseLicenseCreateParams() # LicenseLicenseCreateParams | 

try: 
    api_instance.create_license_license(license_license)
except ApiException as e:
    print "Exception when calling LicenseApi->create_license_license: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_license** | [**LicenseLicenseCreateParams**](LicenseLicenseCreateParams.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_license**
> LicenseLicenses get_license_license(license_license_id)



Retrieve license information for the feature.

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
api_instance = isi_sdk.LicenseApi()
license_license_id = 'license_license_id_example' # str | Retrieve license information for the feature.

try: 
    api_response = api_instance.get_license_license(license_license_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LicenseApi->get_license_license: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_license_id** | **str**| Retrieve license information for the feature. | 

### Return type

[**LicenseLicenses**](LicenseLicenses.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_license_licenses**
> LicenseLicenses list_license_licenses()



Retrieve license information for all licensable products.

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
api_instance = isi_sdk.LicenseApi()

try: 
    api_response = api_instance.list_license_licenses()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling LicenseApi->list_license_licenses: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseLicenses**](LicenseLicenses.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

