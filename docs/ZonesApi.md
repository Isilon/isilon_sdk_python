# isi_sdk.ZonesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_zone**](ZonesApi.md#create_zone) | **POST** /platform/3/zones | 
[**delete_zone**](ZonesApi.md#delete_zone) | **DELETE** /platform/3/zones/{ZoneId} | 
[**get_zone**](ZonesApi.md#get_zone) | **GET** /platform/3/zones/{ZoneId} | 
[**list_zones**](ZonesApi.md#list_zones) | **GET** /platform/3/zones | 
[**update_zone**](ZonesApi.md#update_zone) | **PUT** /platform/3/zones/{ZoneId} | 


# **create_zone**
> CreateResponse create_zone(zone)



Create a new access zone.

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
api_instance = isi_sdk.ZonesApi()
zone = isi_sdk.ZoneCreateParams() # ZoneCreateParams | 

try: 
    api_response = api_instance.create_zone(zone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ZonesApi->create_zone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**ZoneCreateParams**](ZoneCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_zone**
> delete_zone(zone_id)



Delete the access zone.

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
api_instance = isi_sdk.ZonesApi()
zone_id = 56 # int | Delete the access zone.

try: 
    api_instance.delete_zone(zone_id)
except ApiException as e:
    print "Exception when calling ZonesApi->delete_zone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Delete the access zone. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone**
> Zones get_zone(zone_id)



Retrieve the access zone information.

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
api_instance = isi_sdk.ZonesApi()
zone_id = 56 # int | Retrieve the access zone information.

try: 
    api_response = api_instance.get_zone(zone_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ZonesApi->get_zone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_id** | **int**| Retrieve the access zone information. | 

### Return type

[**Zones**](Zones.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_zones**
> Zones list_zones()



List all access zones.

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
api_instance = isi_sdk.ZonesApi()

try: 
    api_response = api_instance.list_zones()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ZonesApi->list_zones: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Zones**](Zones.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_zone**
> update_zone(zone, zone_id)



Modify the access zone. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk.ZonesApi()
zone = isi_sdk.Zone() # Zone | 
zone_id = 56 # int | Modify the access zone. All input fields are optional, but one or more must be supplied.

try: 
    api_instance.update_zone(zone, zone_id)
except ApiException as e:
    print "Exception when calling ZonesApi->update_zone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | [**Zone**](Zone.md)|  | 
 **zone_id** | **int**| Modify the access zone. All input fields are optional, but one or more must be supplied. | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

