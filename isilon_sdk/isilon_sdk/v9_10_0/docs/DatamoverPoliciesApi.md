# isilon_sdk.v9_10_0.DatamoverPoliciesApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_policy_last_job**](DatamoverPoliciesApi.md#get_policy_last_job) | **GET** /platform/19/datamover/policies/{Policyid}/last-job | 


# **get_policy_last_job**
> PolicyLastJob get_policy_last_job(policyid)



Retrieve job ID and last execution time using policy ID.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_10_0
from isilon_sdk.v9_10_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_10_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_10_0.DatamoverPoliciesApi(isilon_sdk.v9_10_0.ApiClient(configuration))
policyid = 'policyid_example' # str | 

try:
    api_response = api_instance.get_policy_last_job(policyid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatamoverPoliciesApi->get_policy_last_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policyid** | **str**|  | 

### Return type

[**PolicyLastJob**](PolicyLastJob.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

