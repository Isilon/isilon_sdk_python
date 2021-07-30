# isi_sdk_9_1_0.CertificateApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate_authority_item**](CertificateApi.md#create_certificate_authority_item) | **POST** /platform/7/certificate/authority | 
[**create_certificate_server_item**](CertificateApi.md#create_certificate_server_item) | **POST** /platform/4/certificate/server | 
[**delete_certificate_authority_by_id**](CertificateApi.md#delete_certificate_authority_by_id) | **DELETE** /platform/7/certificate/authority/{CertificateAuthorityId} | 
[**delete_certificate_server_by_id**](CertificateApi.md#delete_certificate_server_by_id) | **DELETE** /platform/4/certificate/server/{CertificateServerId} | 
[**get_certificate_authority_by_id**](CertificateApi.md#get_certificate_authority_by_id) | **GET** /platform/7/certificate/authority/{CertificateAuthorityId} | 
[**get_certificate_server_by_id**](CertificateApi.md#get_certificate_server_by_id) | **GET** /platform/4/certificate/server/{CertificateServerId} | 
[**get_certificate_settings**](CertificateApi.md#get_certificate_settings) | **GET** /platform/7/certificate/settings | 
[**list_certificate_authority**](CertificateApi.md#list_certificate_authority) | **GET** /platform/7/certificate/authority | 
[**list_certificate_server**](CertificateApi.md#list_certificate_server) | **GET** /platform/4/certificate/server | 
[**update_certificate_authority_by_id**](CertificateApi.md#update_certificate_authority_by_id) | **PUT** /platform/7/certificate/authority/{CertificateAuthorityId} | 
[**update_certificate_server_by_id**](CertificateApi.md#update_certificate_server_by_id) | **PUT** /platform/4/certificate/server/{CertificateServerId} | 
[**update_certificate_settings**](CertificateApi.md#update_certificate_settings) | **PUT** /platform/7/certificate/settings | 


# **create_certificate_authority_item**
> CreateResponse create_certificate_authority_item(certificate_authority_item)



Import a TLS certificate authority.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_authority_item = isi_sdk_9_1_0.CertificateAuthorityItem() # CertificateAuthorityItem | 

try:
    api_response = api_instance.create_certificate_authority_item(certificate_authority_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->create_certificate_authority_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_authority_item** | [**CertificateAuthorityItem**](CertificateAuthorityItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_certificate_server_item**
> CreateResponse create_certificate_server_item(certificate_server_item)



Import a TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_server_item = isi_sdk_9_1_0.CertificateServerItem() # CertificateServerItem | 

try:
    api_response = api_instance.create_certificate_server_item(certificate_server_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->create_certificate_server_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_server_item** | [**CertificateServerItem**](CertificateServerItem.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate_authority_by_id**
> delete_certificate_authority_by_id(certificate_authority_id)



Delete a TLS certificate authority.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_authority_id = 'certificate_authority_id_example' # str | Delete a TLS certificate authority.

try:
    api_instance.delete_certificate_authority_by_id(certificate_authority_id)
except ApiException as e:
    print("Exception when calling CertificateApi->delete_certificate_authority_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_authority_id** | **str**| Delete a TLS certificate authority. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_certificate_server_by_id**
> delete_certificate_server_by_id(certificate_server_id)



Delete a TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_server_id = 'certificate_server_id_example' # str | Delete a TLS server certificate.

try:
    api_instance.delete_certificate_server_by_id(certificate_server_id)
except ApiException as e:
    print("Exception when calling CertificateApi->delete_certificate_server_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_server_id** | **str**| Delete a TLS server certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_authority_by_id**
> CertificateAuthority get_certificate_authority_by_id(certificate_authority_id)



Retrieve a single TLS certificate authority.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_authority_id = 'certificate_authority_id_example' # str | Retrieve a single TLS certificate authority.

try:
    api_response = api_instance.get_certificate_authority_by_id(certificate_authority_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->get_certificate_authority_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_authority_id** | **str**| Retrieve a single TLS certificate authority. | 

### Return type

[**CertificateAuthority**](CertificateAuthority.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_server_by_id**
> CertificateServer get_certificate_server_by_id(certificate_server_id)



Retrieve a single TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_server_id = 'certificate_server_id_example' # str | Retrieve a single TLS server certificate.

try:
    api_response = api_instance.get_certificate_server_by_id(certificate_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->get_certificate_server_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_server_id** | **str**| Retrieve a single TLS server certificate. | 

### Return type

[**CertificateServer**](CertificateServer.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_certificate_settings**
> CertificateSettings get_certificate_settings()



Retrieve system-wide TLS certificate settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))

try:
    api_response = api_instance.get_certificate_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->get_certificate_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateSettings**](CertificateSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificate_authority**
> CertificateAuthorityExtended list_certificate_authority(sort=sort, limit=limit, dir=dir, resume=resume)



Retrieve a list of all configured TLS certificate authorities.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_certificate_authority(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->list_certificate_authority: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**CertificateAuthorityExtended**](CertificateAuthorityExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_certificate_server**
> CertificateServerExtended list_certificate_server(sort=sort, limit=limit, dir=dir, resume=resume)



Retrieve a list of all configured TLS server certificates.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_certificate_server(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CertificateApi->list_certificate_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**CertificateServerExtended**](CertificateServerExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_authority_by_id**
> update_certificate_authority_by_id(certificate_authority_id_params, certificate_authority_id)



Modify a TLS certificate authority.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_authority_id_params = isi_sdk_9_1_0.CertificateServerIdParams() # CertificateServerIdParams | 
certificate_authority_id = 'certificate_authority_id_example' # str | Modify a TLS certificate authority.

try:
    api_instance.update_certificate_authority_by_id(certificate_authority_id_params, certificate_authority_id)
except ApiException as e:
    print("Exception when calling CertificateApi->update_certificate_authority_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_authority_id_params** | [**CertificateServerIdParams**](CertificateServerIdParams.md)|  | 
 **certificate_authority_id** | **str**| Modify a TLS certificate authority. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_server_by_id**
> update_certificate_server_by_id(certificate_server_id_params, certificate_server_id)



Modify a TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_server_id_params = isi_sdk_9_1_0.CertificateServerIdParams() # CertificateServerIdParams | 
certificate_server_id = 'certificate_server_id_example' # str | Modify a TLS server certificate.

try:
    api_instance.update_certificate_server_by_id(certificate_server_id_params, certificate_server_id)
except ApiException as e:
    print("Exception when calling CertificateApi->update_certificate_server_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_server_id_params** | [**CertificateServerIdParams**](CertificateServerIdParams.md)|  | 
 **certificate_server_id** | **str**| Modify a TLS server certificate. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_certificate_settings**
> update_certificate_settings(certificate_settings)



Modify system-wide TLS certificate settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_1_0
from isi_sdk_9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_1_0.CertificateApi(isi_sdk_9_1_0.ApiClient(configuration))
certificate_settings = isi_sdk_9_1_0.CertificateSettingsExtended() # CertificateSettingsExtended | 

try:
    api_instance.update_certificate_settings(certificate_settings)
except ApiException as e:
    print("Exception when calling CertificateApi->update_certificate_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_settings** | [**CertificateSettingsExtended**](CertificateSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

