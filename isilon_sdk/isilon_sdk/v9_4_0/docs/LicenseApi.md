# isilon_sdk.v9_4_0.LicenseApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_license_activation_item**](LicenseApi.md#create_license_activation_item) | **POST** /platform/11/license/activation | 
[**create_license_license**](LicenseApi.md#create_license_license) | **POST** /platform/5/license/licenses | 
[**get_license_generate**](LicenseApi.md#get_license_generate) | **GET** /platform/5/license/generate | 
[**get_license_license**](LicenseApi.md#get_license_license) | **GET** /platform/5/license/licenses/{LicenseLicenseId} | 
[**list_license_activation**](LicenseApi.md#list_license_activation) | **GET** /platform/11/license/activation | 
[**list_license_licenses**](LicenseApi.md#list_license_licenses) | **GET** /platform/5/license/licenses | 


# **create_license_activation_item**
> create_license_activation_item(license_activation_item)



Start or cancel an activation.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.LicenseApi(isilon_sdk.v9_4_0.ApiClient(configuration))
license_activation_item = isilon_sdk.v9_4_0.LicenseActivationItem() # LicenseActivationItem | 

try:
    api_instance.create_license_activation_item(license_activation_item)
except ApiException as e:
    print("Exception when calling LicenseApi->create_license_activation_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_activation_item** | [**LicenseActivationItem**](LicenseActivationItem.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_license_license**
> Empty create_license_license(license_license)



Install a new license file and/or activate evaluation licenses.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.LicenseApi(isilon_sdk.v9_4_0.ApiClient(configuration))
license_license = isilon_sdk.v9_4_0.LicenseLicenseCreateParams() # LicenseLicenseCreateParams | 

try:
    api_response = api_instance.create_license_license(license_license)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->create_license_license: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_license** | [**LicenseLicenseCreateParams**](LicenseLicenseCreateParams.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_generate**
> LicenseGenerate get_license_generate(action=action, licenses_to_exclude=licenses_to_exclude, licenses_to_include=licenses_to_include, only_these_licenses=only_these_licenses)



Generate license activation file.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.LicenseApi(isilon_sdk.v9_4_0.ApiClient(configuration))
action = 'license_list_only' # str | enum: license_list_only (default), generate_activation, download_activation. Generate an activation file or return a list of activated licenses. If generating an activation file and no licenses are specified, the default configuration is to generate an activation file with the current set of licensed features. download_activation returns HTTP headers and the same XML content as seen in the response activation. (optional) (default to license_list_only)
licenses_to_exclude = 'licenses_to_exclude_example' # str | Licenses to omit from activation file. (optional)
licenses_to_include = 'licenses_to_include_example' # str | Licenses to include in activation file. (optional)
only_these_licenses = 'only_these_licenses_example' # str | Activate only the defined licenses. This setting overrides all other license activation settings. (optional)

try:
    api_response = api_instance.get_license_generate(action=action, licenses_to_exclude=licenses_to_exclude, licenses_to_include=licenses_to_include, only_these_licenses=only_these_licenses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->get_license_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| enum: license_list_only (default), generate_activation, download_activation. Generate an activation file or return a list of activated licenses. If generating an activation file and no licenses are specified, the default configuration is to generate an activation file with the current set of licensed features. download_activation returns HTTP headers and the same XML content as seen in the response activation. | [optional] [default to license_list_only]
 **licenses_to_exclude** | **str**| Licenses to omit from activation file. | [optional] 
 **licenses_to_include** | **str**| Licenses to include in activation file. | [optional] 
 **only_these_licenses** | **str**| Activate only the defined licenses. This setting overrides all other license activation settings. | [optional] 

### Return type

[**LicenseGenerate**](LicenseGenerate.md)

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
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.LicenseApi(isilon_sdk.v9_4_0.ApiClient(configuration))
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

# **list_license_activation**
> LicenseActivation list_license_activation()



Return the current the current phase of the activation process.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.LicenseApi(isilon_sdk.v9_4_0.ApiClient(configuration))

try:
    api_response = api_instance.list_license_activation()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->list_license_activation: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LicenseActivation**](LicenseActivation.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_license_licenses**
> LicenseLicensesExtended list_license_licenses(dir=dir, limit=limit, resume=resume, sort=sort)



Retrieve license information for all licensable products.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_4_0
from isilon_sdk.v9_4_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_4_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_4_0.LicenseApi(isilon_sdk.v9_4_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_license_licenses(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LicenseApi->list_license_licenses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**LicenseLicensesExtended**](LicenseLicensesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

