# isi_sdk.ZonesSummaryApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zones_summary**](ZonesSummaryApi.md#get_zones_summary) | **GET** /platform/1/zones-summary | 
[**get_zones_summary_zone**](ZonesSummaryApi.md#get_zones_summary_zone) | **GET** /platform/1/zones-summary/{ZonesSummaryZone} | 


# **get_zones_summary**
> ZonesSummaryExtended get_zones_summary()



Retrieve access zone summary information.

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
api_instance = isi_sdk.ZonesSummaryApi()

try: 
    api_response = api_instance.get_zones_summary()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ZonesSummaryApi->get_zones_summary: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ZonesSummaryExtended**](ZonesSummaryExtended.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zones_summary_zone**
> ZonesSummary get_zones_summary_zone(zones_summary_zone)



Retrieve non-privileged access zone information.

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
api_instance = isi_sdk.ZonesSummaryApi()
zones_summary_zone = 56 # int | Retrieve non-privileged access zone information.

try: 
    api_response = api_instance.get_zones_summary_zone(zones_summary_zone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ZonesSummaryApi->get_zones_summary_zone: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zones_summary_zone** | **int**| Retrieve non-privileged access zone information. | 

### Return type

[**ZonesSummary**](ZonesSummary.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

