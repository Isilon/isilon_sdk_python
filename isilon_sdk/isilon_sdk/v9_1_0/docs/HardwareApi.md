# isilon_sdk.v9_1_0.HardwareApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hardware_tape_name**](HardwareApi.md#create_hardware_tape_name) | **POST** /platform/3/hardware/tape/{HardwareTapeName} | 
[**delete_hardware_tape_name**](HardwareApi.md#delete_hardware_tape_name) | **DELETE** /platform/3/hardware/tape/{HardwareTapeName} | 
[**get_hardware_fcport**](HardwareApi.md#get_hardware_fcport) | **GET** /platform/3/hardware/fcports/{HardwareFcportId} | 
[**get_hardware_fcports**](HardwareApi.md#get_hardware_fcports) | **GET** /platform/3/hardware/fcports | 
[**get_hardware_tapes**](HardwareApi.md#get_hardware_tapes) | **GET** /platform/3/hardware/tapes | 
[**update_hardware_fcport**](HardwareApi.md#update_hardware_fcport) | **PUT** /platform/3/hardware/fcports/{HardwareFcportId} | 
[**update_hardware_tape_name**](HardwareApi.md#update_hardware_tape_name) | **PUT** /platform/3/hardware/tape/{HardwareTapeName} | 


# **create_hardware_tape_name**
> CreateHardwareTapeNameResponse create_hardware_tape_name(hardware_tape_name, hardware_tape_name2, lnn=lnn, port=port, reconcile=reconcile, timeout=timeout)



Tape/Changer devices rescan

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.HardwareApi(isilon_sdk.v9_1_0.ApiClient(configuration))
hardware_tape_name = isilon_sdk.v9_1_0.Empty() # Empty | 
hardware_tape_name2 = 'hardware_tape_name_example' # str | Tape/Changer devices rescan
lnn = 'lnn_example' # str | Logical node number. (optional)
port = 56 # int | Scan only specified port. (optional)
reconcile = true # bool | Remove entries for devices or paths that have become inaccessible. (optional)
timeout = 8.14 # float | Timeout for request. (optional)

try:
    api_response = api_instance.create_hardware_tape_name(hardware_tape_name, hardware_tape_name2, lnn=lnn, port=port, reconcile=reconcile, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareApi->create_hardware_tape_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_tape_name** | [**Empty**](Empty.md)|  | 
 **hardware_tape_name2** | **str**| Tape/Changer devices rescan | 
 **lnn** | **str**| Logical node number. | [optional] 
 **port** | **int**| Scan only specified port. | [optional] 
 **reconcile** | **bool**| Remove entries for devices or paths that have become inaccessible. | [optional] 
 **timeout** | **float**| Timeout for request. | [optional] 

### Return type

[**CreateHardwareTapeNameResponse**](CreateHardwareTapeNameResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hardware_tape_name**
> delete_hardware_tape_name(hardware_tape_name)



Tape/Changer devices remove

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.HardwareApi(isilon_sdk.v9_1_0.ApiClient(configuration))
hardware_tape_name = 'hardware_tape_name_example' # str | Tape/Changer devices remove

try:
    api_instance.delete_hardware_tape_name(hardware_tape_name)
except ApiException as e:
    print("Exception when calling HardwareApi->delete_hardware_tape_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_tape_name** | **str**| Tape/Changer devices remove | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_fcport**
> HardwareFcports get_hardware_fcport(hardware_fcport_id, lnn=lnn)



Get one fibre-channel port

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.HardwareApi(isilon_sdk.v9_1_0.ApiClient(configuration))
hardware_fcport_id = 56 # int | Get one fibre-channel port
lnn = 'lnn_example' # str | Logical node number. (optional)

try:
    api_response = api_instance.get_hardware_fcport(hardware_fcport_id, lnn=lnn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareApi->get_hardware_fcport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_fcport_id** | **int**| Get one fibre-channel port | 
 **lnn** | **str**| Logical node number. | [optional] 

### Return type

[**HardwareFcports**](HardwareFcports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_fcports**
> HardwareFcports get_hardware_fcports(limit=limit, lnn=lnn, resume=resume)



Get list of fibre-channel ports

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.HardwareApi(isilon_sdk.v9_1_0.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
lnn = 'lnn_example' # str | Logical node number. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_hardware_fcports(limit=limit, lnn=lnn, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareApi->get_hardware_fcports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **lnn** | **str**| Logical node number. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**HardwareFcports**](HardwareFcports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_tapes**
> HardwareTapes get_hardware_tapes(activepath=activepath, devname=devname, limit=limit, node=node, resume=resume, type=type)



Get list Tape and Changer devices

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.HardwareApi(isilon_sdk.v9_1_0.ApiClient(configuration))
activepath = 'activepath_example' # str | List devices with only active paths. (optional)
devname = 'devname_example' # str | List only the named device. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
node = 'node_example' # str | List only devices on the specified node. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
type = 'type_example' # str | Restrict to list on tape or mc device. (optional)

try:
    api_response = api_instance.get_hardware_tapes(activepath=activepath, devname=devname, limit=limit, node=node, resume=resume, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HardwareApi->get_hardware_tapes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activepath** | **str**| List devices with only active paths. | [optional] 
 **devname** | **str**| List only the named device. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **node** | **str**| List only devices on the specified node. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **type** | **str**| Restrict to list on tape or mc device. | [optional] 

### Return type

[**HardwareTapes**](HardwareTapes.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hardware_fcport**
> update_hardware_fcport(hardware_fcport, hardware_fcport_id, lnn=lnn)



Change wwnn, wwpn, state, topology, or rate of a FC port

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.HardwareApi(isilon_sdk.v9_1_0.ApiClient(configuration))
hardware_fcport = isilon_sdk.v9_1_0.HardwareFcport() # HardwareFcport | 
hardware_fcport_id = 56 # int | Change wwnn, wwpn, state, topology, or rate of a FC port
lnn = 'lnn_example' # str | Logical node number. (optional)

try:
    api_instance.update_hardware_fcport(hardware_fcport, hardware_fcport_id, lnn=lnn)
except ApiException as e:
    print("Exception when calling HardwareApi->update_hardware_fcport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_fcport** | [**HardwareFcport**](HardwareFcport.md)|  | 
 **hardware_fcport_id** | **int**| Change wwnn, wwpn, state, topology, or rate of a FC port | 
 **lnn** | **str**| Logical node number. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hardware_tape_name**
> update_hardware_tape_name(hardware_tape_name_params, hardware_tape_name)



Tape/Changer device modify

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_1_0
from isilon_sdk.v9_1_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_1_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_1_0.HardwareApi(isilon_sdk.v9_1_0.ApiClient(configuration))
hardware_tape_name_params = isilon_sdk.v9_1_0.HardwareTapeNameParams() # HardwareTapeNameParams | 
hardware_tape_name = 'hardware_tape_name_example' # str | Tape/Changer device modify

try:
    api_instance.update_hardware_tape_name(hardware_tape_name_params, hardware_tape_name)
except ApiException as e:
    print("Exception when calling HardwareApi->update_hardware_tape_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_tape_name_params** | [**HardwareTapeNameParams**](HardwareTapeNameParams.md)|  | 
 **hardware_tape_name** | **str**| Tape/Changer device modify | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

