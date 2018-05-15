# isi_sdk_8_1_1.SyncTargetApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policies_policy_cancel_item**](SyncTargetApi.md#create_policies_policy_cancel_item) | **POST** /platform/1/sync/target/policies/{Policy}/cancel | 
[**get_reports_report_subreport**](SyncTargetApi.md#get_reports_report_subreport) | **GET** /platform/4/sync/target/reports/{Rid}/subreports/{ReportsReportSubreportId} | 
[**get_reports_report_subreports**](SyncTargetApi.md#get_reports_report_subreports) | **GET** /platform/4/sync/target/reports/{Rid}/subreports | 


# **create_policies_policy_cancel_item**
> CreateResponse create_policies_policy_cancel_item(policies_policy_cancel_item, policy)



Cancel the most recent SyncIQ job for this policy from the target side.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.SyncTargetApi(isi_sdk_8_1_1.ApiClient(configuration))
policies_policy_cancel_item = isi_sdk_8_1_1.Empty() # Empty | 
policy = 'policy_example' # str | 

try:
    api_response = api_instance.create_policies_policy_cancel_item(policies_policy_cancel_item, policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncTargetApi->create_policies_policy_cancel_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policies_policy_cancel_item** | [**Empty**](Empty.md)|  | 
 **policy** | **str**|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_report_subreport**
> ReportsReportSubreports get_reports_report_subreport(reports_report_subreport_id, rid)



View a single SyncIQ target subreport.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.SyncTargetApi(isi_sdk_8_1_1.ApiClient(configuration))
reports_report_subreport_id = 'reports_report_subreport_id_example' # str | View a single SyncIQ target subreport.
rid = 'rid_example' # str | 

try:
    api_response = api_instance.get_reports_report_subreport(reports_report_subreport_id, rid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncTargetApi->get_reports_report_subreport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reports_report_subreport_id** | **str**| View a single SyncIQ target subreport. | 
 **rid** | **str**|  | 

### Return type

[**ReportsReportSubreports**](ReportsReportSubreports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_report_subreports**
> ReportsReportSubreportsExtended get_reports_report_subreports(rid, sort=sort, resume=resume, newer_than=newer_than, state=state, limit=limit, dir=dir)



Get a list of SyncIQ target subreports for a report.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_1_1
from isi_sdk_8_1_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_1_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_1_1.SyncTargetApi(isi_sdk_8_1_1.ApiClient(configuration))
rid = 'rid_example' # str | 
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
newer_than = 56 # int | Filter the returned reports to include only those whose jobs started more recently than the specified number of days ago. (optional)
state = 'state_example' # str | Filter the returned reports to include only those whose jobs are in this state. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_reports_report_subreports(rid, sort=sort, resume=resume, newer_than=newer_than, state=state, limit=limit, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SyncTargetApi->get_reports_report_subreports: %s\n" % e)
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

[**ReportsReportSubreportsExtended**](ReportsReportSubreportsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

