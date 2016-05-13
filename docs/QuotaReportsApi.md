# isi_sdk.QuotaReportsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_about**](QuotaReportsApi.md#get_report_about) | **GET** /platform/1/quota/reports/{Rid}/about | 


# **get_report_about**
> ReportAbout get_report_about(rid)



Retrieve report meta-data information.

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
api_instance = isi_sdk.QuotaReportsApi()
rid = 'rid_example' # str | 

try: 
    api_response = api_instance.get_report_about(rid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling QuotaReportsApi->get_report_about: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 

### Return type

[**ReportAbout**](ReportAbout.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

