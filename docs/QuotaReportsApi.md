# isi_sdk_7_2.QuotaReportsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_about**](QuotaReportsApi.md#get_report_about) | **GET** /platform/1/quota/reports/{Rid}/about | 


# **get_report_about**
> ReportAbout get_report_about(rid)



Retrieve report meta-data information.

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
api_instance = isi_sdk_7_2.QuotaReportsApi(isi_sdk_7_2.ApiClient(configuration))
rid = 'rid_example' # str | 

try:
    api_response = api_instance.get_report_about(rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaReportsApi->get_report_about: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 

### Return type

[**ReportAbout**](ReportAbout.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

