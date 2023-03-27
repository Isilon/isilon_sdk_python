# isilon_sdk.v9_2_1.KeymanagerApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kmip_server**](KeymanagerApi.md#create_kmip_server) | **POST** /platform/12/keymanager/kmip/servers | 
[**create_sed_migrate_item**](KeymanagerApi.md#create_sed_migrate_item) | **POST** /platform/12/keymanager/sed/migrate | 
[**delete_kmip_server**](KeymanagerApi.md#delete_kmip_server) | **DELETE** /platform/12/keymanager/kmip/servers/{KmipServerId} | 
[**get_kmip_server**](KeymanagerApi.md#get_kmip_server) | **GET** /platform/12/keymanager/kmip/servers/{KmipServerId} | 
[**get_sed_settings**](KeymanagerApi.md#get_sed_settings) | **GET** /platform/12/keymanager/sed/settings | 
[**get_sed_status**](KeymanagerApi.md#get_sed_status) | **GET** /platform/12/keymanager/sed/status | 
[**get_sed_status_lnn**](KeymanagerApi.md#get_sed_status_lnn) | **GET** /platform/12/keymanager/sed/status/{SedStatusLnn} | 
[**list_kmip_servers**](KeymanagerApi.md#list_kmip_servers) | **GET** /platform/12/keymanager/kmip/servers | 
[**update_kmip_server**](KeymanagerApi.md#update_kmip_server) | **PUT** /platform/12/keymanager/kmip/servers/{KmipServerId} | 
[**update_sed_settings**](KeymanagerApi.md#update_sed_settings) | **PUT** /platform/12/keymanager/sed/settings | 


# **create_kmip_server**
> CreateResponse create_kmip_server(kmip_server)



Create a new KMIP server entry.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))
kmip_server = isilon_sdk.v9_2_1.KmipServerCreateParams() # KmipServerCreateParams | 

try:
    api_response = api_instance.create_kmip_server(kmip_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagerApi->create_kmip_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kmip_server** | [**KmipServerCreateParams**](KmipServerCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sed_migrate_item**
> CreateSedMigrateItemResponse create_sed_migrate_item(sed_migrate_item)



Indicates the direction of the migration.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))
sed_migrate_item = isilon_sdk.v9_2_1.SedMigrateItem() # SedMigrateItem | 

try:
    api_response = api_instance.create_sed_migrate_item(sed_migrate_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagerApi->create_sed_migrate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sed_migrate_item** | [**SedMigrateItem**](SedMigrateItem.md)|  | 

### Return type

[**CreateSedMigrateItemResponse**](CreateSedMigrateItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kmip_server**
> delete_kmip_server(kmip_server_id)



Delete a KMIP server entry.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))
kmip_server_id = 'kmip_server_id_example' # str | Delete a KMIP server entry.

try:
    api_instance.delete_kmip_server(kmip_server_id)
except ApiException as e:
    print("Exception when calling KeymanagerApi->delete_kmip_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kmip_server_id** | **str**| Delete a KMIP server entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kmip_server**
> KmipServers get_kmip_server(kmip_server_id)



Retrieve a specific KMIP server entry.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))
kmip_server_id = 'kmip_server_id_example' # str | Retrieve a specific KMIP server entry.

try:
    api_response = api_instance.get_kmip_server(kmip_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagerApi->get_kmip_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kmip_server_id** | **str**| Retrieve a specific KMIP server entry. | 

### Return type

[**KmipServers**](KmipServers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sed_settings**
> SedSettings get_sed_settings()



Retrieve Current SED settings.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_sed_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagerApi->get_sed_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SedSettings**](SedSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sed_status**
> SedStatusExtended get_sed_status()



Retrieve SED status on all nodes in this cluster.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))

try:
    api_response = api_instance.get_sed_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagerApi->get_sed_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SedStatusExtended**](SedStatusExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sed_status_lnn**
> SedStatus get_sed_status_lnn(sed_status_lnn)



Retrieve SED status on a node in this cluster.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))
sed_status_lnn = 56 # int | Retrieve SED status on a node in this cluster.

try:
    api_response = api_instance.get_sed_status_lnn(sed_status_lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagerApi->get_sed_status_lnn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sed_status_lnn** | **int**| Retrieve SED status on a node in this cluster. | 

### Return type

[**SedStatus**](SedStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_kmip_servers**
> KmipServersExtended list_kmip_servers(dir=dir, limit=limit, resume=resume, sort=sort)



Retrieve a list of configured KMIP server entries.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.list_kmip_servers(dir=dir, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KeymanagerApi->list_kmip_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**KmipServersExtended**](KmipServersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kmip_server**
> update_kmip_server(kmip_server, kmip_server_id)



Modify a KMIP server entry.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))
kmip_server = isilon_sdk.v9_2_1.KmipServer() # KmipServer | 
kmip_server_id = 'kmip_server_id_example' # str | Modify a KMIP server entry.

try:
    api_instance.update_kmip_server(kmip_server, kmip_server_id)
except ApiException as e:
    print("Exception when calling KeymanagerApi->update_kmip_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kmip_server** | [**KmipServer**](KmipServer.md)|  | 
 **kmip_server_id** | **str**| Modify a KMIP server entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sed_settings**
> update_sed_settings(sed_settings)



Modify SED settings to allow migration, or forbid it and retrieve all keys.

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
api_instance = isilon_sdk.v9_2_1.KeymanagerApi(isilon_sdk.v9_2_1.ApiClient(configuration))
sed_settings = isilon_sdk.v9_2_1.SedSettingsExtended() # SedSettingsExtended | 

try:
    api_instance.update_sed_settings(sed_settings)
except ApiException as e:
    print("Exception when calling KeymanagerApi->update_sed_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sed_settings** | [**SedSettingsExtended**](SedSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

