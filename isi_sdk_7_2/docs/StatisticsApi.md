# isi_sdk_7_2.StatisticsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics_current**](StatisticsApi.md#get_statistics_current) | **GET** /platform/1/statistics/current | 
[**get_statistics_history**](StatisticsApi.md#get_statistics_history) | **GET** /platform/1/statistics/history | 
[**get_statistics_key**](StatisticsApi.md#get_statistics_key) | **GET** /platform/1/statistics/keys/{StatisticsKeyId} | 
[**get_statistics_keys**](StatisticsApi.md#get_statistics_keys) | **GET** /platform/1/statistics/keys | 
[**get_statistics_protocols**](StatisticsApi.md#get_statistics_protocols) | **GET** /platform/1/statistics/protocols | 


# **get_statistics_current**
> StatisticsCurrent get_statistics_current(timeout=timeout, degraded=degraded, devid=devid, key=key, expand_clientid=expand_clientid)



Retrieve stats.

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
api_instance = isi_sdk_7_2.StatisticsApi(isi_sdk_7_2.ApiClient(configuration))
timeout = 56 # int | Time in seconds to wait for results from remote nodes. (optional)
degraded = true # bool | If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. (optional)
devid = ['devid_example'] # list[str] | Node devid to query.  Either an <integer> or \"all\".  Can be used more than one time to query multiple nodes.  \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used. (optional)
key = ['key_example'] # list[str] | Key names. Can be used more than one time to query multiple keys. (optional)
expand_clientid = true # bool | If true, use name resolution to expand client addresses and other IDs. (optional)

try:
    api_response = api_instance.get_statistics_current(timeout=timeout, degraded=degraded, devid=devid, key=key, expand_clientid=expand_clientid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_current: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Time in seconds to wait for results from remote nodes. | [optional] 
 **degraded** | **bool**| If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. | [optional] 
 **devid** | [**list[str]**](str.md)| Node devid to query.  Either an &lt;integer&gt; or \&quot;all\&quot;.  Can be used more than one time to query multiple nodes.  \&quot;all\&quot; queries all up nodes. 0 means query the local node. For \&quot;cluster\&quot; scoped keys, in any devid including 0 can be used. | [optional] 
 **key** | [**list[str]**](str.md)| Key names. Can be used more than one time to query multiple keys. | [optional] 
 **expand_clientid** | **bool**| If true, use name resolution to expand client addresses and other IDs. | [optional] 

### Return type

[**StatisticsCurrent**](StatisticsCurrent.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_history**
> StatisticsHistory get_statistics_history(begin=begin, interval=interval, end=end, timeout=timeout, devid=devid, memory_only=memory_only, key=key, degraded=degraded, expand_clientid=expand_clientid)



Retrieve stats.

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
api_instance = isi_sdk_7_2.StatisticsApi(isi_sdk_7_2.ApiClient(configuration))
begin = 56 # int | Earliest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. (optional)
interval = 56 # int | Minimum sampling interval time in seconds.  If native statistics are higher resolution, data will be down-sampled. (optional)
end = 56 # int | Latest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. If not supplied, use now as the end time. (optional)
timeout = 56 # int | Time in seconds to wait for results from remote nodes. (optional)
devid = ['devid_example'] # list[str] | Node devid to query.  Either an <integer> or \"all\".  Can be used more than one time to query multiple nodes.  \"all\" queries all up nodes. 0 means query the local node. For \"cluster\" scoped keys, in any devid including 0 can be used. (optional)
memory_only = true # bool | Only use statistics sources that reside in memory (faster, but with less retention). (optional)
key = ['key_example'] # list[str] | Key names. Can be used more than one time to query multiple keys. (optional)
degraded = true # bool | If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. (optional)
expand_clientid = true # bool | If true, use name resolution to expand client addresses and other IDs. (optional)

try:
    api_response = api_instance.get_statistics_history(begin=begin, interval=interval, end=end, timeout=timeout, devid=devid, memory_only=memory_only, key=key, degraded=degraded, expand_clientid=expand_clientid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin** | **int**| Earliest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. | [optional] 
 **interval** | **int**| Minimum sampling interval time in seconds.  If native statistics are higher resolution, data will be down-sampled. | [optional] 
 **end** | **int**| Latest time (Unix epoch seconds) of interest. Negative times are interpreted as relative (before) now. If not supplied, use now as the end time. | [optional] 
 **timeout** | **int**| Time in seconds to wait for results from remote nodes. | [optional] 
 **devid** | [**list[str]**](str.md)| Node devid to query.  Either an &lt;integer&gt; or \&quot;all\&quot;.  Can be used more than one time to query multiple nodes.  \&quot;all\&quot; queries all up nodes. 0 means query the local node. For \&quot;cluster\&quot; scoped keys, in any devid including 0 can be used. | [optional] 
 **memory_only** | **bool**| Only use statistics sources that reside in memory (faster, but with less retention). | [optional] 
 **key** | [**list[str]**](str.md)| Key names. Can be used more than one time to query multiple keys. | [optional] 
 **degraded** | **bool**| If true, try to continue even if some stats are unavailable. In this case, errors will be present in the per-key returned data. | [optional] 
 **expand_clientid** | **bool**| If true, use name resolution to expand client addresses and other IDs. | [optional] 

### Return type

[**StatisticsHistory**](StatisticsHistory.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_key**
> StatisticsKeys get_statistics_key(statistics_key_id)



List key meta-data.

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
api_instance = isi_sdk_7_2.StatisticsApi(isi_sdk_7_2.ApiClient(configuration))
statistics_key_id = 'statistics_key_id_example' # str | List key meta-data.

try:
    api_response = api_instance.get_statistics_key(statistics_key_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statistics_key_id** | **str**| List key meta-data. | 

### Return type

[**StatisticsKeys**](StatisticsKeys.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_keys**
> StatisticsKeysExtended get_statistics_keys(count=count, limit=limit, queryable=queryable, resume=resume)



List meta-data for matching keys.

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
api_instance = isi_sdk_7_2.StatisticsApi(isi_sdk_7_2.ApiClient(configuration))
count = true # bool | Only count matching keys, do not return meta-data. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
queryable = true # bool | Only list keys that can/cannot be queries. Default is true. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_statistics_keys(count=count, limit=limit, queryable=queryable, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **bool**| Only count matching keys, do not return meta-data. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **queryable** | **bool**| Only list keys that can/cannot be queries. Default is true. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**StatisticsKeysExtended**](StatisticsKeysExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_protocols**
> StatisticsProtocols get_statistics_protocols()



Retrieve protocol list.

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
api_instance = isi_sdk_7_2.StatisticsApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_statistics_protocols()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatisticsApi->get_statistics_protocols: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StatisticsProtocols**](StatisticsProtocols.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

