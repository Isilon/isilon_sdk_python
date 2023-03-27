# isilon_sdk.v9_0_0.IpmiApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_config_feature**](IpmiApi.md#get_config_feature) | **GET** /platform/10/ipmi/config/features/{ConfigFeatureId} | 
[**get_config_features**](IpmiApi.md#get_config_features) | **GET** /platform/10/ipmi/config/features | 
[**get_config_network**](IpmiApi.md#get_config_network) | **GET** /platform/10/ipmi/config/network | 
[**get_config_node**](IpmiApi.md#get_config_node) | **GET** /platform/10/ipmi/config/nodes/{ConfigNodeId} | 
[**get_config_nodes**](IpmiApi.md#get_config_nodes) | **GET** /platform/10/ipmi/config/nodes | 
[**get_config_settings**](IpmiApi.md#get_config_settings) | **GET** /platform/10/ipmi/config/settings | 
[**get_config_user**](IpmiApi.md#get_config_user) | **GET** /platform/10/ipmi/config/user | 
[**update_config_feature**](IpmiApi.md#update_config_feature) | **PUT** /platform/10/ipmi/config/features/{ConfigFeatureId} | 
[**update_config_network**](IpmiApi.md#update_config_network) | **PUT** /platform/10/ipmi/config/network | 
[**update_config_settings**](IpmiApi.md#update_config_settings) | **PUT** /platform/10/ipmi/config/settings | 
[**update_config_user**](IpmiApi.md#update_config_user) | **PUT** /platform/10/ipmi/config/user | 


# **get_config_feature**
> ConfigFeatures get_config_feature(config_feature_id)



Retrieve the Remote IPMI Management feature configuration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))
config_feature_id = 'config_feature_id_example' # str | Retrieve the Remote IPMI Management feature configuration.

try:
    api_response = api_instance.get_config_feature(config_feature_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpmiApi->get_config_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_feature_id** | **str**| Retrieve the Remote IPMI Management feature configuration. | 

### Return type

[**ConfigFeatures**](ConfigFeatures.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_features**
> ConfigFeaturesExtended get_config_features()



Get detailed information for all remote IPMI features.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_config_features()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpmiApi->get_config_features: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigFeaturesExtended**](ConfigFeaturesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_network**
> ConfigNetwork get_config_network()



Retrieve the Remote IPMI Management static network configuration settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_config_network()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpmiApi->get_config_network: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigNetwork**](ConfigNetwork.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_node**
> ConfigNodes get_config_node(config_node_id)



Retrieve the Remote IPMI Management node configuration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))
config_node_id = 56 # int | Retrieve the Remote IPMI Management node configuration.

try:
    api_response = api_instance.get_config_node(config_node_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpmiApi->get_config_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_node_id** | **int**| Retrieve the Remote IPMI Management node configuration. | 

### Return type

[**ConfigNodes**](ConfigNodes.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_nodes**
> ConfigNodesExtended get_config_nodes()



Retrieve the Remote IPMI Management nodes configuration.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_config_nodes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpmiApi->get_config_nodes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigNodesExtended**](ConfigNodesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_settings**
> ConfigSettings get_config_settings()



View the Remote IPMI Management configuration settings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_config_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpmiApi->get_config_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigSettings**](ConfigSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_user**
> ConfigUser get_config_user()



View the Remote IPMI Management user.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_config_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpmiApi->get_config_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigUser**](ConfigUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_feature**
> update_config_feature(config_feature, config_feature_id)



Modify remote IPMI Management feature settings

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))
config_feature = isilon_sdk.v9_0_0.ConfigFeature() # ConfigFeature | 
config_feature_id = 'config_feature_id_example' # str | Modify remote IPMI Management feature settings

try:
    api_instance.update_config_feature(config_feature, config_feature_id)
except ApiException as e:
    print("Exception when calling IpmiApi->update_config_feature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_feature** | [**ConfigFeature**](ConfigFeature.md)|  | 
 **config_feature_id** | **str**| Modify remote IPMI Management feature settings | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_network**
> update_config_network(config_network)



Modify the remote IPMI Management static network configuration settings

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))
config_network = isilon_sdk.v9_0_0.ConfigNetworkExtended() # ConfigNetworkExtended | 

try:
    api_instance.update_config_network(config_network)
except ApiException as e:
    print("Exception when calling IpmiApi->update_config_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_network** | [**ConfigNetworkExtended**](ConfigNetworkExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_settings**
> update_config_settings(config_settings)



Modify remote IPMI Management configuration settings

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))
config_settings = isilon_sdk.v9_0_0.ConfigSettingsSettings() # ConfigSettingsSettings | 

try:
    api_instance.update_config_settings(config_settings)
except ApiException as e:
    print("Exception when calling IpmiApi->update_config_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_settings** | [**ConfigSettingsSettings**](ConfigSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_config_user**
> update_config_user(config_user)



Modify remote IPMI Management user

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_0_0
from isilon_sdk.v9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_0_0.IpmiApi(isilon_sdk.v9_0_0.ApiClient(configuration))
config_user = isilon_sdk.v9_0_0.ConfigUserUser() # ConfigUserUser | 

try:
    api_instance.update_config_user(config_user)
except ApiException as e:
    print("Exception when calling IpmiApi->update_config_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_user** | [**ConfigUserUser**](ConfigUserUser.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

