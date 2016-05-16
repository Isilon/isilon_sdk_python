# isi_sdk.HardwareApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hardware_tape_name**](HardwareApi.md#create_hardware_tape_name) | **POST** /platform/3/hardware/tape/{HardwareTapeName} | 
[**delete_hardware_tape_name**](HardwareApi.md#delete_hardware_tape_name) | **DELETE** /platform/3/hardware/tape/{HardwareTapeName} | 
[**get_hardware_fcport**](HardwareApi.md#get_hardware_fcport) | **GET** /platform/3/hardware/fcports/{HardwareFcportId} | 
[**get_hardware_tapes**](HardwareApi.md#get_hardware_tapes) | **GET** /platform/3/hardware/tapes | 
[**update_hardware_fcport**](HardwareApi.md#update_hardware_fcport) | **PUT** /platform/3/hardware/fcports/{HardwareFcportId} | 
[**update_hardware_tape_name**](HardwareApi.md#update_hardware_tape_name) | **PUT** /platform/3/hardware/tape/{HardwareTapeName} | 


# **create_hardware_tape_name**
> Empty create_hardware_tape_name(hardware_tape_name)



Tape/Changer devices rescan

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
api_instance = isi_sdk.HardwareApi()
hardware_tape_name = isi_sdk.Empty() # Empty | 

try: 
    api_response = api_instance.create_hardware_tape_name(hardware_tape_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling HardwareApi->create_hardware_tape_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_tape_name** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hardware_tape_name**
> delete_hardware_tape_name(hardware_tape_name)



Tape/Changer devices remove

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
api_instance = isi_sdk.HardwareApi()
hardware_tape_name = 'hardware_tape_name_example' # str | Tape/Changer devices remove

try: 
    api_instance.delete_hardware_tape_name(hardware_tape_name)
except ApiException as e:
    print "Exception when calling HardwareApi->delete_hardware_tape_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_tape_name** | **str**| Tape/Changer devices remove | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_fcport**
> HardwareFcports get_hardware_fcport(hardware_fcport_id)



Get one fibre-channel port

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
api_instance = isi_sdk.HardwareApi()
hardware_fcport_id = 56 # int | Get one fibre-channel port

try: 
    api_response = api_instance.get_hardware_fcport(hardware_fcport_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling HardwareApi->get_hardware_fcport: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_fcport_id** | **int**| Get one fibre-channel port | 

### Return type

[**HardwareFcports**](HardwareFcports.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hardware_tapes**
> HardwareTapes get_hardware_tapes()



Get list Tape and Changer devices

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
api_instance = isi_sdk.HardwareApi()

try: 
    api_response = api_instance.get_hardware_tapes()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling HardwareApi->get_hardware_tapes: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HardwareTapes**](HardwareTapes.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hardware_fcport**
> update_hardware_fcport(hardware_fcport, hardware_fcport_id)



Change wwnn, wwpn, state, topology, or rate of a FC port

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
api_instance = isi_sdk.HardwareApi()
hardware_fcport = isi_sdk.HardwareFcport() # HardwareFcport | 
hardware_fcport_id = 56 # int | Change wwnn, wwpn, state, topology, or rate of a FC port

try: 
    api_instance.update_hardware_fcport(hardware_fcport, hardware_fcport_id)
except ApiException as e:
    print "Exception when calling HardwareApi->update_hardware_fcport: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_fcport** | [**HardwareFcport**](HardwareFcport.md)|  | 
 **hardware_fcport_id** | **int**| Change wwnn, wwpn, state, topology, or rate of a FC port | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hardware_tape_name**
> update_hardware_tape_name(hardware_tape_name_params, hardware_tape_name)



Tape/Changer device modify

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
api_instance = isi_sdk.HardwareApi()
hardware_tape_name_params = isi_sdk.HardwareTapeNameParams() # HardwareTapeNameParams | 
hardware_tape_name = 'hardware_tape_name_example' # str | Tape/Changer device modify

try: 
    api_instance.update_hardware_tape_name(hardware_tape_name_params, hardware_tape_name)
except ApiException as e:
    print "Exception when calling HardwareApi->update_hardware_tape_name: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hardware_tape_name_params** | [**HardwareTapeNameParams**](HardwareTapeNameParams.md)|  | 
 **hardware_tape_name** | **str**| Tape/Changer device modify | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

