# isi_sdk_8_0.AntivirusApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_antivirus_policy**](AntivirusApi.md#create_antivirus_policy) | **POST** /platform/3/antivirus/policies | 
[**create_antivirus_scan_item**](AntivirusApi.md#create_antivirus_scan_item) | **POST** /platform/3/antivirus/scan | 
[**create_antivirus_server**](AntivirusApi.md#create_antivirus_server) | **POST** /platform/3/antivirus/servers | 
[**delete_antivirus_policies**](AntivirusApi.md#delete_antivirus_policies) | **DELETE** /platform/3/antivirus/policies | 
[**delete_antivirus_policy**](AntivirusApi.md#delete_antivirus_policy) | **DELETE** /platform/3/antivirus/policies/{AntivirusPolicyId} | 
[**delete_antivirus_server**](AntivirusApi.md#delete_antivirus_server) | **DELETE** /platform/3/antivirus/servers/{AntivirusServerId} | 
[**delete_antivirus_servers**](AntivirusApi.md#delete_antivirus_servers) | **DELETE** /platform/3/antivirus/servers | 
[**delete_reports_scan**](AntivirusApi.md#delete_reports_scan) | **DELETE** /platform/3/antivirus/reports/scans/{ReportsScanId} | 
[**delete_reports_scans**](AntivirusApi.md#delete_reports_scans) | **DELETE** /platform/3/antivirus/reports/scans | 
[**get_antivirus_policy**](AntivirusApi.md#get_antivirus_policy) | **GET** /platform/3/antivirus/policies/{AntivirusPolicyId} | 
[**get_antivirus_quarantine_path**](AntivirusApi.md#get_antivirus_quarantine_path) | **GET** /platform/3/antivirus/quarantine/{AntivirusQuarantinePath} | 
[**get_antivirus_server**](AntivirusApi.md#get_antivirus_server) | **GET** /platform/3/antivirus/servers/{AntivirusServerId} | 
[**get_antivirus_settings**](AntivirusApi.md#get_antivirus_settings) | **GET** /platform/3/antivirus/settings | 
[**get_reports_scan**](AntivirusApi.md#get_reports_scan) | **GET** /platform/3/antivirus/reports/scans/{ReportsScanId} | 
[**get_reports_scans**](AntivirusApi.md#get_reports_scans) | **GET** /platform/3/antivirus/reports/scans | 
[**get_reports_threat**](AntivirusApi.md#get_reports_threat) | **GET** /platform/3/antivirus/reports/threats/{ReportsThreatId} | 
[**get_reports_threats**](AntivirusApi.md#get_reports_threats) | **GET** /platform/3/antivirus/reports/threats | 
[**list_antivirus_policies**](AntivirusApi.md#list_antivirus_policies) | **GET** /platform/3/antivirus/policies | 
[**list_antivirus_servers**](AntivirusApi.md#list_antivirus_servers) | **GET** /platform/3/antivirus/servers | 
[**update_antivirus_policy**](AntivirusApi.md#update_antivirus_policy) | **PUT** /platform/3/antivirus/policies/{AntivirusPolicyId} | 
[**update_antivirus_quarantine_path**](AntivirusApi.md#update_antivirus_quarantine_path) | **PUT** /platform/3/antivirus/quarantine/{AntivirusQuarantinePath} | 
[**update_antivirus_server**](AntivirusApi.md#update_antivirus_server) | **PUT** /platform/3/antivirus/servers/{AntivirusServerId} | 
[**update_antivirus_settings**](AntivirusApi.md#update_antivirus_settings) | **PUT** /platform/3/antivirus/settings | 


# **create_antivirus_policy**
> CreateResponse create_antivirus_policy(antivirus_policy)



Create new antivirus scan policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_policy = isi_sdk_8_0.AntivirusPolicyCreateParams() # AntivirusPolicyCreateParams | 

try:
    api_response = api_instance.create_antivirus_policy(antivirus_policy)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->create_antivirus_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_policy** | [**AntivirusPolicyCreateParams**](AntivirusPolicyCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_antivirus_scan_item**
> CreateAntivirusScanItemResponse create_antivirus_scan_item(antivirus_scan_item)



Manually scan a file.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_scan_item = isi_sdk_8_0.AntivirusScanItem() # AntivirusScanItem | 

try:
    api_response = api_instance.create_antivirus_scan_item(antivirus_scan_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->create_antivirus_scan_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_scan_item** | [**AntivirusScanItem**](AntivirusScanItem.md)|  | 

### Return type

[**CreateAntivirusScanItemResponse**](CreateAntivirusScanItemResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_antivirus_server**
> CreateResponse create_antivirus_server(antivirus_server)



Create new antivirus servers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_server = isi_sdk_8_0.AntivirusServerCreateParams() # AntivirusServerCreateParams | 

try:
    api_response = api_instance.create_antivirus_server(antivirus_server)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->create_antivirus_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_server** | [**AntivirusServerCreateParams**](AntivirusServerCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_antivirus_policies**
> delete_antivirus_policies()



Delete all antivirus scan policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_instance.delete_antivirus_policies()
except ApiException as e:
    print("Exception when calling AntivirusApi->delete_antivirus_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_antivirus_policy**
> delete_antivirus_policy(antivirus_policy_id)



Delete an antivirus scan policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_policy_id = 'antivirus_policy_id_example' # str | Delete an antivirus scan policy.

try:
    api_instance.delete_antivirus_policy(antivirus_policy_id)
except ApiException as e:
    print("Exception when calling AntivirusApi->delete_antivirus_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_policy_id** | **str**| Delete an antivirus scan policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_antivirus_server**
> delete_antivirus_server(antivirus_server_id)



Delete an antivirus server entry.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_server_id = 'antivirus_server_id_example' # str | Delete an antivirus server entry.

try:
    api_instance.delete_antivirus_server(antivirus_server_id)
except ApiException as e:
    print("Exception when calling AntivirusApi->delete_antivirus_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_server_id** | **str**| Delete an antivirus server entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_antivirus_servers**
> delete_antivirus_servers()



Delete all antivirus servers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_instance.delete_antivirus_servers()
except ApiException as e:
    print("Exception when calling AntivirusApi->delete_antivirus_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reports_scan**
> delete_reports_scan(reports_scan_id)



Delete one antivirus scan report, and all of its associated threat reports.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
reports_scan_id = 'reports_scan_id_example' # str | Delete one antivirus scan report, and all of its associated threat reports.

try:
    api_instance.delete_reports_scan(reports_scan_id)
except ApiException as e:
    print("Exception when calling AntivirusApi->delete_reports_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reports_scan_id** | **str**| Delete one antivirus scan report, and all of its associated threat reports. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reports_scans**
> delete_reports_scans(age=age)



Delete antivirus scan reports, and any threat reports associated with those scans.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
age = 56 # int | An amount of time in seconds. If present, only reports older than this age are deleted. (optional)

try:
    api_instance.delete_reports_scans(age=age)
except ApiException as e:
    print("Exception when calling AntivirusApi->delete_reports_scans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **age** | **int**| An amount of time in seconds. If present, only reports older than this age are deleted. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_antivirus_policy**
> AntivirusPolicies get_antivirus_policy(antivirus_policy_id)



Retrieve one antivirus scan policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_policy_id = 'antivirus_policy_id_example' # str | Retrieve one antivirus scan policy.

try:
    api_response = api_instance.get_antivirus_policy(antivirus_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->get_antivirus_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_policy_id** | **str**| Retrieve one antivirus scan policy. | 

### Return type

[**AntivirusPolicies**](AntivirusPolicies.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_antivirus_quarantine_path**
> AntivirusQuarantine get_antivirus_quarantine_path(antivirus_quarantine_path)



Retrieve the quarantine status of the file at the specified path.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_quarantine_path = 'antivirus_quarantine_path_example' # str | Retrieve the quarantine status of the file at the specified path.

try:
    api_response = api_instance.get_antivirus_quarantine_path(antivirus_quarantine_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->get_antivirus_quarantine_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_quarantine_path** | **str**| Retrieve the quarantine status of the file at the specified path. | 

### Return type

[**AntivirusQuarantine**](AntivirusQuarantine.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_antivirus_server**
> AntivirusServers get_antivirus_server(antivirus_server_id)



Retrieve one antivirus server entry.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_server_id = 'antivirus_server_id_example' # str | Retrieve one antivirus server entry.

try:
    api_response = api_instance.get_antivirus_server(antivirus_server_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->get_antivirus_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_server_id** | **str**| Retrieve one antivirus server entry. | 

### Return type

[**AntivirusServers**](AntivirusServers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_antivirus_settings**
> AntivirusSettings get_antivirus_settings()



Retrieve the Antivirus settings.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))

try:
    api_response = api_instance.get_antivirus_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->get_antivirus_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AntivirusSettings**](AntivirusSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_scan**
> ReportsScans get_reports_scan(reports_scan_id)



Retrieve one antivirus scan report.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
reports_scan_id = 'reports_scan_id_example' # str | Retrieve one antivirus scan report.

try:
    api_response = api_instance.get_reports_scan(reports_scan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->get_reports_scan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reports_scan_id** | **str**| Retrieve one antivirus scan report. | 

### Return type

[**ReportsScans**](ReportsScans.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_scans**
> ReportsScansExtended get_reports_scans(sort=sort, status=status, resume=resume, limit=limit, dir=dir, policy_id=policy_id)



List antivirus scan reports.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
status = 'status_example' # str | If present, only scan reports with this status will be returned. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
policy_id = 'policy_id_example' # str | If present, only reports for scans associated with this policy will be returned. (optional)

try:
    api_response = api_instance.get_reports_scans(sort=sort, status=status, resume=resume, limit=limit, dir=dir, policy_id=policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->get_reports_scans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **status** | **str**| If present, only scan reports with this status will be returned. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **policy_id** | **str**| If present, only reports for scans associated with this policy will be returned. | [optional] 

### Return type

[**ReportsScansExtended**](ReportsScansExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_threat**
> ReportsThreats get_reports_threat(reports_threat_id)



Retrieve one antivirus threat report.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
reports_threat_id = 'reports_threat_id_example' # str | Retrieve one antivirus threat report.

try:
    api_response = api_instance.get_reports_threat(reports_threat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->get_reports_threat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reports_threat_id** | **str**| Retrieve one antivirus threat report. | 

### Return type

[**ReportsThreats**](ReportsThreats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports_threats**
> ReportsThreatsExtended get_reports_threats(sort=sort, scan_id=scan_id, resume=resume, limit=limit, file=file, remediation=remediation, dir=dir)



List antivirus threat reports.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
scan_id = 'scan_id_example' # str | If present, only returns threat reports associated with the given scan report. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
file = 'file_example' # str | If present, only returns threat reports for the given file. (optional)
remediation = 'remediation_example' # str | If present, only returns threat reports with the given remediation. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.get_reports_threats(sort=sort, scan_id=scan_id, resume=resume, limit=limit, file=file, remediation=remediation, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->get_reports_threats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **scan_id** | **str**| If present, only returns threat reports associated with the given scan report. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **file** | **str**| If present, only returns threat reports for the given file. | [optional] 
 **remediation** | **str**| If present, only returns threat reports with the given remediation. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**ReportsThreatsExtended**](ReportsThreatsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_antivirus_policies**
> AntivirusPoliciesExtended list_antivirus_policies(sort=sort, limit=limit, dir=dir, resume=resume)



List antivirus scan policies.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_antivirus_policies(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->list_antivirus_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**AntivirusPoliciesExtended**](AntivirusPoliciesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_antivirus_servers**
> AntivirusServersExtended list_antivirus_servers(sort=sort, limit=limit, dir=dir, resume=resume)



List antivirus servers.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_antivirus_servers(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AntivirusApi->list_antivirus_servers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**AntivirusServersExtended**](AntivirusServersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_antivirus_policy**
> update_antivirus_policy(antivirus_policy, antivirus_policy_id)



Modify an antivirus scan policy.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_policy = isi_sdk_8_0.AntivirusPolicy() # AntivirusPolicy | 
antivirus_policy_id = 'antivirus_policy_id_example' # str | Modify an antivirus scan policy.

try:
    api_instance.update_antivirus_policy(antivirus_policy, antivirus_policy_id)
except ApiException as e:
    print("Exception when calling AntivirusApi->update_antivirus_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_policy** | [**AntivirusPolicy**](AntivirusPolicy.md)|  | 
 **antivirus_policy_id** | **str**| Modify an antivirus scan policy. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_antivirus_quarantine_path**
> update_antivirus_quarantine_path(antivirus_quarantine_path_params, antivirus_quarantine_path)



Set the quarantine status of the file at the specified path.  Use either an empty object {} in the request body or {\"quarantined\":true} to quarantine the file, and {\"quarantined\":false} to unquarantine the file.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_quarantine_path_params = isi_sdk_8_0.AntivirusQuarantinePathParams() # AntivirusQuarantinePathParams | 
antivirus_quarantine_path = 'antivirus_quarantine_path_example' # str | Set the quarantine status of the file at the specified path.  Use either an empty object {} in the request body or {\"quarantined\":true} to quarantine the file, and {\"quarantined\":false} to unquarantine the file.

try:
    api_instance.update_antivirus_quarantine_path(antivirus_quarantine_path_params, antivirus_quarantine_path)
except ApiException as e:
    print("Exception when calling AntivirusApi->update_antivirus_quarantine_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_quarantine_path_params** | [**AntivirusQuarantinePathParams**](AntivirusQuarantinePathParams.md)|  | 
 **antivirus_quarantine_path** | **str**| Set the quarantine status of the file at the specified path.  Use either an empty object {} in the request body or {\&quot;quarantined\&quot;:true} to quarantine the file, and {\&quot;quarantined\&quot;:false} to unquarantine the file. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_antivirus_server**
> update_antivirus_server(antivirus_server, antivirus_server_id)



Modify an antivirus server entry.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_server = isi_sdk_8_0.AntivirusServer() # AntivirusServer | 
antivirus_server_id = 'antivirus_server_id_example' # str | Modify an antivirus server entry.

try:
    api_instance.update_antivirus_server(antivirus_server, antivirus_server_id)
except ApiException as e:
    print("Exception when calling AntivirusApi->update_antivirus_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_server** | [**AntivirusServer**](AntivirusServer.md)|  | 
 **antivirus_server_id** | **str**| Modify an antivirus server entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_antivirus_settings**
> update_antivirus_settings(antivirus_settings)



Modify the Antivirus settings. All input fields are optional, but one or more must be supplied.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_0.AntivirusApi(isi_sdk_8_0.ApiClient(configuration))
antivirus_settings = isi_sdk_8_0.AntivirusSettingsSettings() # AntivirusSettingsSettings | 

try:
    api_instance.update_antivirus_settings(antivirus_settings)
except ApiException as e:
    print("Exception when calling AntivirusApi->update_antivirus_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **antivirus_settings** | [**AntivirusSettingsSettings**](AntivirusSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

