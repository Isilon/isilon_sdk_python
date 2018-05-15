# isi_sdk_8_1_1.CertificateApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate_server_item**](CertificateApi.md#create_certificate_server_item) | **POST** /platform/4/certificate/server | 
[**delete_certificate_server_by_id**](CertificateApi.md#delete_certificate_server_by_id) | **DELETE** /platform/4/certificate/server/{CertificateServerId} | 
[**get_certificate_server_by_id**](CertificateApi.md#get_certificate_server_by_id) | **GET** /platform/4/certificate/server/{CertificateServerId} | 
[**list_certificate_server**](CertificateApi.md#list_certificate_server) | **GET** /platform/4/certificate/server | 
[**update_certificate_server_by_id**](CertificateApi.md#update_certificate_server_by_id) | **PUT** /platform/4/certificate/server/{CertificateServerId} | 


# **create_certificate_server_item**
> CreateResponse create_certificate_server_item(certificate_server_item)



Import a TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.CertificateApi(isi_sdk_8_1_1.ApiClient(configuration))
certificate_server_item = isi_sdk_8_1_1.CertificateServerItem() # CertificateServerItem | 

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

# **delete_certificate_server_by_id**
> delete_certificate_server_by_id(certificate_server_id)



Delete a TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.CertificateApi(isi_sdk_8_1_1.ApiClient(configuration))
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

# **get_certificate_server_by_id**
> CertificateServer get_certificate_server_by_id(certificate_server_id)



Retrieve a single TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.CertificateApi(isi_sdk_8_1_1.ApiClient(configuration))
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

# **list_certificate_server**
> CertificateServerExtended list_certificate_server(sort=sort, limit=limit, dir=dir, resume=resume)



Retrieve a list of all configured TLS server certificates.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.CertificateApi(isi_sdk_8_1_1.ApiClient(configuration))
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

# **update_certificate_server_by_id**
> update_certificate_server_by_id(certificate_server_id_params, certificate_server_id)



Modify a TLS server certificate.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.CertificateApi(isi_sdk_8_1_1.ApiClient(configuration))
certificate_server_id_params = isi_sdk_8_1_1.CertificateServerIdParams() # CertificateServerIdParams | 
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

