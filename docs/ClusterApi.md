# isi_sdk_7_2.ClusterApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_config**](ClusterApi.md#get_cluster_config) | **GET** /platform/1/cluster/config | 
[**get_cluster_external_ips**](ClusterApi.md#get_cluster_external_ips) | **GET** /platform/2/cluster/external-ips | 
[**get_cluster_identity**](ClusterApi.md#get_cluster_identity) | **GET** /platform/1/cluster/identity | 
[**get_cluster_statfs**](ClusterApi.md#get_cluster_statfs) | **GET** /platform/1/cluster/statfs | 
[**get_cluster_time**](ClusterApi.md#get_cluster_time) | **GET** /platform/1/cluster/time | 


# **get_cluster_config**
> ClusterConfig get_cluster_config()



Retrieve the cluster information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.ClusterApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterConfig**](ClusterConfig.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_external_ips**
> list[str] get_cluster_external_ips()



Retrieve the cluster IP addresses including IPV4 and IPV6.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.ClusterApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_external_ips()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_external_ips: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_identity**
> ClusterIdentity get_cluster_identity()



Retrieve the login information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.ClusterApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_identity()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_identity: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterIdentity**](ClusterIdentity.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_statfs**
> ClusterStatfs get_cluster_statfs()



Retrieve the filesystem statistics.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.ClusterApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_statfs()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_statfs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStatfs**](ClusterStatfs.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_time**
> ClusterTime get_cluster_time()



Retrieve the current cluster time.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_7_2
from isi_sdk_7_2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_7_2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_7_2.ClusterApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_cluster_time()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClusterApi->get_cluster_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterTime**](ClusterTime.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

