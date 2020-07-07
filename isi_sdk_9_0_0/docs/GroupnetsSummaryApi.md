# isi_sdk_9_0_0.GroupnetsSummaryApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_groupnets_summary**](GroupnetsSummaryApi.md#get_groupnets_summary) | **GET** /platform/5/groupnets-summary | 


# **get_groupnets_summary**
> GroupnetsSummary get_groupnets_summary()



Retrieve groupnet summary information.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_9_0_0
from isi_sdk_9_0_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_9_0_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_9_0_0.GroupnetsSummaryApi(isi_sdk_9_0_0.ApiClient(configuration))

try:
    api_response = api_instance.get_groupnets_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupnetsSummaryApi->get_groupnets_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupnetsSummary**](GroupnetsSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

