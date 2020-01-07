# isi_sdk_8_2_1.SyncReportsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_subreport**](SyncReportsApi.md#get_report_subreport) | **GET** /platform/7/sync/reports/{Rid}/subreports/{ReportSubreportId} | 
[**get_report_subreports**](SyncReportsApi.md#get_report_subreports) | **GET** /platform/7/sync/reports/{Rid}/subreports | 


# **get_report_subreport**
> ReportSubreports get_report_subreport(report_subreport_id, rid)



View a single SyncIQ subreport.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.SyncReportsApi(isi_sdk_8_2_1.ApiClient(configuration))
report_subreport_id = 'report_subreport_id_example' # str | View a single SyncIQ subreport.
rid = 'rid_example' # str | 

try:
    api_response = api_instance.get_report_subreport(report_subreport_id, rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncReportsApi->get_report_subreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_subreport_id** | **str**| View a single SyncIQ subreport. | 
 **rid** | **str**|  | 

### Return type

[**ReportSubreports**](ReportSubreports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_subreports**
> ReportSubreportsExtended get_report_subreports(rid, sort=sort, resume=resume, newer_than=newer_than, state=state, limit=limit, dir=dir)



Get a list of SyncIQ subreports for a report.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.SyncReportsApi(isi_sdk_8_2_1.ApiClient(configuration))
rid = 'rid_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
newer_than = 56 # int | Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago. (optional)
state = 'state_example' # str | Filter the returned reports to include only those whose jobs are in this state. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_report_subreports(rid, sort=sort, resume=resume, newer_than=newer_than, state=state, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncReportsApi->get_report_subreports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rid** | **str**|  | 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **newer_than** | **int**| Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago. | [optional] 
 **state** | **str**| Filter the returned reports to include only those whose jobs are in this state. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**ReportSubreportsExtended**](ReportSubreportsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

