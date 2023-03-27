# isilon_sdk.v9_5_0.StoragepoolApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_storagepool_nodepool**](StoragepoolApi.md#create_storagepool_nodepool) | **POST** /platform/16/storagepool/nodepools | 
[**create_storagepool_tier**](StoragepoolApi.md#create_storagepool_tier) | **POST** /platform/16/storagepool/tiers | 
[**delete_storagepool_nodepool**](StoragepoolApi.md#delete_storagepool_nodepool) | **DELETE** /platform/16/storagepool/nodepools/{StoragepoolNodepoolId} | 
[**delete_storagepool_nodepools**](StoragepoolApi.md#delete_storagepool_nodepools) | **DELETE** /platform/16/storagepool/nodepools | 
[**delete_storagepool_tier**](StoragepoolApi.md#delete_storagepool_tier) | **DELETE** /platform/16/storagepool/tiers/{StoragepoolTierId} | 
[**delete_storagepool_tiers**](StoragepoolApi.md#delete_storagepool_tiers) | **DELETE** /platform/16/storagepool/tiers | 
[**get_storagepool_nodepool**](StoragepoolApi.md#get_storagepool_nodepool) | **GET** /platform/16/storagepool/nodepools/{StoragepoolNodepoolId} | 
[**get_storagepool_nodetype**](StoragepoolApi.md#get_storagepool_nodetype) | **GET** /platform/12/storagepool/nodetypes/{StoragepoolNodetypeId} | 
[**get_storagepool_nodetypes**](StoragepoolApi.md#get_storagepool_nodetypes) | **GET** /platform/12/storagepool/nodetypes | 
[**get_storagepool_settings**](StoragepoolApi.md#get_storagepool_settings) | **GET** /platform/16/storagepool/settings | 
[**get_storagepool_status**](StoragepoolApi.md#get_storagepool_status) | **GET** /platform/1/storagepool/status | 
[**get_storagepool_storagepools**](StoragepoolApi.md#get_storagepool_storagepools) | **GET** /platform/16/storagepool/storagepools | 
[**get_storagepool_suggested_protection_nid**](StoragepoolApi.md#get_storagepool_suggested_protection_nid) | **GET** /platform/3/storagepool/suggested-protection/{StoragepoolSuggestedProtectionNid} | 
[**get_storagepool_tier**](StoragepoolApi.md#get_storagepool_tier) | **GET** /platform/16/storagepool/tiers/{StoragepoolTierId} | 
[**get_storagepool_unprovisioned**](StoragepoolApi.md#get_storagepool_unprovisioned) | **GET** /platform/1/storagepool/unprovisioned | 
[**list_storagepool_nodepools**](StoragepoolApi.md#list_storagepool_nodepools) | **GET** /platform/16/storagepool/nodepools | 
[**list_storagepool_tiers**](StoragepoolApi.md#list_storagepool_tiers) | **GET** /platform/16/storagepool/tiers | 
[**update_storagepool_nodepool**](StoragepoolApi.md#update_storagepool_nodepool) | **PUT** /platform/16/storagepool/nodepools/{StoragepoolNodepoolId} | 
[**update_storagepool_settings**](StoragepoolApi.md#update_storagepool_settings) | **PUT** /platform/16/storagepool/settings | 
[**update_storagepool_tier**](StoragepoolApi.md#update_storagepool_tier) | **PUT** /platform/16/storagepool/tiers/{StoragepoolTierId} | 


# **create_storagepool_nodepool**
> CreateStoragepoolNodepoolResponse create_storagepool_nodepool(storagepool_nodepool)



Create a new node pool.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_nodepool = isilon_sdk.v9_5_0.StoragepoolNodepoolCreateParams() # StoragepoolNodepoolCreateParams | 

try:
    api_response = api_instance.create_storagepool_nodepool(storagepool_nodepool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->create_storagepool_nodepool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodepool** | [**StoragepoolNodepoolCreateParams**](StoragepoolNodepoolCreateParams.md)|  | 

### Return type

[**CreateStoragepoolNodepoolResponse**](CreateStoragepoolNodepoolResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storagepool_tier**
> CreateStoragepoolNodepoolResponse create_storagepool_tier(storagepool_tier)



Create a new tier.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_tier = isilon_sdk.v9_5_0.StoragepoolTierCreateParams() # StoragepoolTierCreateParams | 

try:
    api_response = api_instance.create_storagepool_tier(storagepool_tier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->create_storagepool_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_tier** | [**StoragepoolTierCreateParams**](StoragepoolTierCreateParams.md)|  | 

### Return type

[**CreateStoragepoolNodepoolResponse**](CreateStoragepoolNodepoolResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storagepool_nodepool**
> delete_storagepool_nodepool(storagepool_nodepool_id)



Delete node pool.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_nodepool_id = 'storagepool_nodepool_id_example' # str | Delete node pool.

try:
    api_instance.delete_storagepool_nodepool(storagepool_nodepool_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_storagepool_nodepool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodepool_id** | **str**| Delete node pool. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storagepool_nodepools**
> delete_storagepool_nodepools()



Delete node pool.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_instance.delete_storagepool_nodepools()
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_storagepool_nodepools: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storagepool_tier**
> delete_storagepool_tier(storagepool_tier_id)



Delete tier.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_tier_id = 'storagepool_tier_id_example' # str | Delete tier.

try:
    api_instance.delete_storagepool_tier(storagepool_tier_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_storagepool_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_tier_id** | **str**| Delete tier. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storagepool_tiers**
> delete_storagepool_tiers()



Delete all tiers.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_instance.delete_storagepool_tiers()
except ApiException as e:
    print("Exception when calling StoragepoolApi->delete_storagepool_tiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_nodepool**
> StoragepoolNodepools get_storagepool_nodepool(storagepool_nodepool_id)



Retrieve node pool information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_nodepool_id = 'storagepool_nodepool_id_example' # str | Retrieve node pool information.

try:
    api_response = api_instance.get_storagepool_nodepool(storagepool_nodepool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_nodepool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodepool_id** | **str**| Retrieve node pool information. | 

### Return type

[**StoragepoolNodepools**](StoragepoolNodepools.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_nodetype**
> StoragepoolNodetypes get_storagepool_nodetype(storagepool_nodetype_id)



Retrieve node type information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_nodetype_id = 'storagepool_nodetype_id_example' # str | Retrieve node type information.

try:
    api_response = api_instance.get_storagepool_nodetype(storagepool_nodetype_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_nodetype: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodetype_id** | **str**| Retrieve node type information. | 

### Return type

[**StoragepoolNodetypes**](StoragepoolNodetypes.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_nodetypes**
> StoragepoolNodetypesExtended get_storagepool_nodetypes()



List all node types.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_storagepool_nodetypes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_nodetypes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolNodetypesExtended**](StoragepoolNodetypesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_settings**
> StoragepoolSettings get_storagepool_settings()



List all storagepool settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_storagepool_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolSettings**](StoragepoolSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_status**
> StoragepoolStatus get_storagepool_status()



List any health conditions detected.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_storagepool_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolStatus**](StoragepoolStatus.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_storagepools**
> StoragepoolStoragepools get_storagepool_storagepools(dir=dir, sort=sort, toplevels=toplevels)



List all storage pools.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
dir = 'dir_example' # str | The direction of the sort. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
toplevels = 'toplevels_example' # str | If true, node pools contained within tiers will be filtered out of results. (optional)

try:
    api_response = api_instance.get_storagepool_storagepools(dir=dir, sort=sort, toplevels=toplevels)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_storagepools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dir** | **str**| The direction of the sort. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **toplevels** | **str**| If true, node pools contained within tiers will be filtered out of results. | [optional] 

### Return type

[**StoragepoolStoragepools**](StoragepoolStoragepools.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_suggested_protection_nid**
> StoragepoolSuggestedProtection get_storagepool_suggested_protection_nid(storagepool_suggested_protection_nid)



Retrieve the suggested protection policy.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_suggested_protection_nid = 'storagepool_suggested_protection_nid_example' # str | Retrieve the suggested protection policy.

try:
    api_response = api_instance.get_storagepool_suggested_protection_nid(storagepool_suggested_protection_nid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_suggested_protection_nid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_suggested_protection_nid** | **str**| Retrieve the suggested protection policy. | 

### Return type

[**StoragepoolSuggestedProtection**](StoragepoolSuggestedProtection.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_tier**
> StoragepoolTiers get_storagepool_tier(storagepool_tier_id)



Retrieve tier information.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_tier_id = 'storagepool_tier_id_example' # str | Retrieve tier information.

try:
    api_response = api_instance.get_storagepool_tier(storagepool_tier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_tier_id** | **str**| Retrieve tier information. | 

### Return type

[**StoragepoolTiers**](StoragepoolTiers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storagepool_unprovisioned**
> StoragepoolUnprovisioned get_storagepool_unprovisioned()



Get the unprovisioned nodes and drives

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.get_storagepool_unprovisioned()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->get_storagepool_unprovisioned: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolUnprovisioned**](StoragepoolUnprovisioned.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_storagepool_nodepools**
> StoragepoolNodepoolsExtended list_storagepool_nodepools()



List all node pools.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.list_storagepool_nodepools()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->list_storagepool_nodepools: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolNodepoolsExtended**](StoragepoolNodepoolsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_storagepool_tiers**
> StoragepoolTiersExtended list_storagepool_tiers()



List all tiers.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))

try:
    api_response = api_instance.list_storagepool_tiers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragepoolApi->list_storagepool_tiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StoragepoolTiersExtended**](StoragepoolTiersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storagepool_nodepool**
> update_storagepool_nodepool(storagepool_nodepool, storagepool_nodepool_id)



Modify node pool. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_nodepool = isilon_sdk.v9_5_0.StoragepoolNodepool() # StoragepoolNodepool | 
storagepool_nodepool_id = 'storagepool_nodepool_id_example' # str | Modify node pool. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_storagepool_nodepool(storagepool_nodepool, storagepool_nodepool_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->update_storagepool_nodepool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_nodepool** | [**StoragepoolNodepool**](StoragepoolNodepool.md)|  | 
 **storagepool_nodepool_id** | **str**| Modify node pool. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storagepool_settings**
> update_storagepool_settings(storagepool_settings)



Modify one or more settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_settings = isilon_sdk.v9_5_0.StoragepoolSettingsExtended() # StoragepoolSettingsExtended | 

try:
    api_instance.update_storagepool_settings(storagepool_settings)
except ApiException as e:
    print("Exception when calling StoragepoolApi->update_storagepool_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_settings** | [**StoragepoolSettingsExtended**](StoragepoolSettingsExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storagepool_tier**
> update_storagepool_tier(storagepool_tier, storagepool_tier_id)



Modify tier. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_5_0
from isilon_sdk.v9_5_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_5_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_5_0.StoragepoolApi(isilon_sdk.v9_5_0.ApiClient(configuration))
storagepool_tier = isilon_sdk.v9_5_0.StoragepoolTier() # StoragepoolTier | 
storagepool_tier_id = 'storagepool_tier_id_example' # str | Modify tier. All input fields are optional, but one or more must be supplied.

try:
    api_instance.update_storagepool_tier(storagepool_tier, storagepool_tier_id)
except ApiException as e:
    print("Exception when calling StoragepoolApi->update_storagepool_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storagepool_tier** | [**StoragepoolTier**](StoragepoolTier.md)|  | 
 **storagepool_tier_id** | **str**| Modify tier. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

