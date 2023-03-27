# isilon_sdk.v9_4_0.CatalogApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_list**](CatalogApi.md#get_catalog_list) | **GET** /platform/14/catalog/list | 
[**get_catalog_readme**](CatalogApi.md#get_catalog_readme) | **GET** /platform/14/catalog/readme | 
[**get_catalog_verify**](CatalogApi.md#get_catalog_verify) | **GET** /platform/14/catalog/verify | 
[**update_catalog_clean**](CatalogApi.md#update_catalog_clean) | **PUT** /platform/14/catalog/clean | 
[**update_catalog_export**](CatalogApi.md#update_catalog_export) | **PUT** /platform/14/catalog/export | 
[**update_catalog_import**](CatalogApi.md#update_catalog_import) | **PUT** /platform/14/catalog/import | 
[**update_catalog_remove**](CatalogApi.md#update_catalog_remove) | **PUT** /platform/14/catalog/remove | 
[**update_catalog_repair**](CatalogApi.md#update_catalog_repair) | **PUT** /platform/14/catalog/repair | 


# **get_catalog_list**
> CatalogList get_catalog_list(content_type=content_type, onefs_version=onefs_version, reference=reference)



List metadata for artifacts in the catalog.

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
api_instance = isilon_sdk.v9_4_0.CatalogApi(isilon_sdk.v9_4_0.ApiClient(configuration))
content_type = 'content_type_example' # str | the type of upgrade (optional)
onefs_version = 56 # int | onefs version (optional)
reference = 'reference_example' # str | onefs component that references this entry. (optional)

try:
    api_response = api_instance.get_catalog_list(content_type=content_type, onefs_version=onefs_version, reference=reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| the type of upgrade | [optional] 
 **onefs_version** | **int**| onefs version | [optional] 
 **reference** | **str**| onefs component that references this entry. | [optional] 

### Return type

[**CatalogList**](CatalogList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_readme**
> CatalogReadme get_catalog_readme(file=file, hash=hash)



README file content for artifact in the catalog.

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
api_instance = isilon_sdk.v9_4_0.CatalogApi(isilon_sdk.v9_4_0.ApiClient(configuration))
file = 'file_example' # str | Path of the signed file to import in the catalog (optional)
hash = 'hash_example' # str | The sha256 hash of the file stored in catalog (optional)

try:
    api_response = api_instance.get_catalog_readme(file=file, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_readme: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| Path of the signed file to import in the catalog | [optional] 
 **hash** | **str**| The sha256 hash of the file stored in catalog | [optional] 

### Return type

[**CatalogReadme**](CatalogReadme.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_verify**
> CatalogVerify get_catalog_verify(file=file, hash=hash)



Verification of the signatures of any specified file, a specific artifact in the catalog, or all artifacts in the catalog.

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
api_instance = isilon_sdk.v9_4_0.CatalogApi(isilon_sdk.v9_4_0.ApiClient(configuration))
file = 'file_example' # str | Path to unsigned file to verify (optional)
hash = 'hash_example' # str | The sha256 hash of the file stored in catalog (optional)

try:
    api_response = api_instance.get_catalog_verify(file=file, hash=hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->get_catalog_verify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| Path to unsigned file to verify | [optional] 
 **hash** | **str**| The sha256 hash of the file stored in catalog | [optional] 

### Return type

[**CatalogVerify**](CatalogVerify.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_clean**
> update_catalog_clean(catalog_clean)



Removes any unreferenced artifacts.

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
api_instance = isilon_sdk.v9_4_0.CatalogApi(isilon_sdk.v9_4_0.ApiClient(configuration))
catalog_clean = isilon_sdk.v9_4_0.Empty() # Empty | 

try:
    api_instance.update_catalog_clean(catalog_clean)
except ApiException as e:
    print("Exception when calling CatalogApi->update_catalog_clean: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_clean** | [**Empty**](Empty.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_export**
> update_catalog_export(catalog_export)



Allows a catalog artifact to be exported out of the catalog to a file that the user can access. A typical use case would be if a user needs to export artifacts prior to a full catalog wipe or if a specific package is needed so that it can be applied on another cluster.

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
api_instance = isilon_sdk.v9_4_0.CatalogApi(isilon_sdk.v9_4_0.ApiClient(configuration))
catalog_export = isilon_sdk.v9_4_0.CatalogExport() # CatalogExport | 

try:
    api_instance.update_catalog_export(catalog_export)
except ApiException as e:
    print("Exception when calling CatalogApi->update_catalog_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_export** | [**CatalogExport**](CatalogExport.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_import**
> update_catalog_import(catalog_import)



Allow a signed package to be re-imported into the catalog. A typical use case would be if a required package is missing or damaged.  All user imported files will be subjected to a full signature verification including verifying the sha256 hashes for all data regions. Files that are not correctly signed will not be allowed in the catalog.

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
api_instance = isilon_sdk.v9_4_0.CatalogApi(isilon_sdk.v9_4_0.ApiClient(configuration))
catalog_import = isilon_sdk.v9_4_0.CatalogImport() # CatalogImport | 

try:
    api_instance.update_catalog_import(catalog_import)
except ApiException as e:
    print("Exception when calling CatalogApi->update_catalog_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_import** | [**CatalogImport**](CatalogImport.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_remove**
> update_catalog_remove(catalog_remove)



Allows a user to remove a specific sha256 artifact and  all related metadata. If the file is needed again in the future it will  need to be re-imported.

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
api_instance = isilon_sdk.v9_4_0.CatalogApi(isilon_sdk.v9_4_0.ApiClient(configuration))
catalog_remove = isilon_sdk.v9_4_0.CatalogRemove() # CatalogRemove | 

try:
    api_instance.update_catalog_remove(catalog_remove)
except ApiException as e:
    print("Exception when calling CatalogApi->update_catalog_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_remove** | [**CatalogRemove**](CatalogRemove.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_repair**
> update_catalog_repair(catalog_repair)



Repairs a damaged catalog. Erases catalog database, creates a new catalog database, and automatically reverifies and reimports all the artifacts.

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
api_instance = isilon_sdk.v9_4_0.CatalogApi(isilon_sdk.v9_4_0.ApiClient(configuration))
catalog_repair = isilon_sdk.v9_4_0.Empty() # Empty | 

try:
    api_instance.update_catalog_repair(catalog_repair)
except ApiException as e:
    print("Exception when calling CatalogApi->update_catalog_repair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_repair** | [**Empty**](Empty.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

