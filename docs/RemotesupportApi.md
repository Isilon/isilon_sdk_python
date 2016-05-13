# isi_sdk.RemotesupportApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_remotesupport_connectemc**](RemotesupportApi.md#get_remotesupport_connectemc) | **GET** /platform/1/remotesupport/connectemc | 
[**update_remotesupport_connectemc**](RemotesupportApi.md#update_remotesupport_connectemc) | **PUT** /platform/1/remotesupport/connectemc | 


# **get_remotesupport_connectemc**
> RemotesupportConnectemc get_remotesupport_connectemc()



List all settings.

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
api_instance = isi_sdk.RemotesupportApi()

try: 
    api_response = api_instance.get_remotesupport_connectemc()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RemotesupportApi->get_remotesupport_connectemc: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RemotesupportConnectemc**](RemotesupportConnectemc.md)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_remotesupport_connectemc**
> update_remotesupport_connectemc(remotesupport_connectemc)



Modify one or more settings.

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
api_instance = isi_sdk.RemotesupportApi()
remotesupport_connectemc = isi_sdk.RemotesupportConnectemcConnectemc() # RemotesupportConnectemcConnectemc | 

try: 
    api_instance.update_remotesupport_connectemc(remotesupport_connectemc)
except ApiException as e:
    print "Exception when calling RemotesupportApi->update_remotesupport_connectemc: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remotesupport_connectemc** | [**RemotesupportConnectemcConnectemc**](RemotesupportConnectemcConnectemc.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

