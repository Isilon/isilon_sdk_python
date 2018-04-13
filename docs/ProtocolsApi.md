# isi_sdk_7_2.ProtocolsApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hdfs_proxyuser**](ProtocolsApi.md#create_hdfs_proxyuser) | **POST** /platform/1/protocols/hdfs/proxyusers | 
[**create_hdfs_rack**](ProtocolsApi.md#create_hdfs_rack) | **POST** /platform/1/protocols/hdfs/racks | 
[**create_nfs_alias**](ProtocolsApi.md#create_nfs_alias) | **POST** /platform/2/protocols/nfs/aliases | 
[**create_nfs_export**](ProtocolsApi.md#create_nfs_export) | **POST** /platform/2/protocols/nfs/exports | 
[**create_nfs_reload_item**](ProtocolsApi.md#create_nfs_reload_item) | **POST** /platform/2/protocols/nfs/reload | 
[**create_smb_share**](ProtocolsApi.md#create_smb_share) | **POST** /platform/1/protocols/smb/shares | 
[**delete_hdfs_proxyuser**](ProtocolsApi.md#delete_hdfs_proxyuser) | **DELETE** /platform/1/protocols/hdfs/proxyusers/{HdfsProxyuserId} | 
[**delete_hdfs_rack**](ProtocolsApi.md#delete_hdfs_rack) | **DELETE** /platform/1/protocols/hdfs/racks/{HdfsRackId} | 
[**delete_nfs_alias**](ProtocolsApi.md#delete_nfs_alias) | **DELETE** /platform/2/protocols/nfs/aliases/{NfsAliasId} | 
[**delete_nfs_export**](ProtocolsApi.md#delete_nfs_export) | **DELETE** /platform/2/protocols/nfs/exports/{NfsExportId} | 
[**delete_nfs_nlm_session**](ProtocolsApi.md#delete_nfs_nlm_session) | **DELETE** /platform/2/protocols/nfs/nlm/sessions/{NfsNlmSessionId} | 
[**delete_smb_openfile**](ProtocolsApi.md#delete_smb_openfile) | **DELETE** /platform/1/protocols/smb/openfiles/{SmbOpenfileId} | 
[**delete_smb_session**](ProtocolsApi.md#delete_smb_session) | **DELETE** /platform/1/protocols/smb/sessions/{SmbSessionId} | 
[**delete_smb_sessions_computer_user**](ProtocolsApi.md#delete_smb_sessions_computer_user) | **DELETE** /platform/1/protocols/smb/sessions/{Computer}/{SmbSessionsComputerUser} | 
[**delete_smb_share**](ProtocolsApi.md#delete_smb_share) | **DELETE** /platform/1/protocols/smb/shares/{SmbShareId} | 
[**delete_smb_shares**](ProtocolsApi.md#delete_smb_shares) | **DELETE** /platform/1/protocols/smb/shares | 
[**get_hdfs_proxyuser**](ProtocolsApi.md#get_hdfs_proxyuser) | **GET** /platform/1/protocols/hdfs/proxyusers/{HdfsProxyuserId} | 
[**get_hdfs_rack**](ProtocolsApi.md#get_hdfs_rack) | **GET** /platform/1/protocols/hdfs/racks/{HdfsRackId} | 
[**get_hdfs_settings**](ProtocolsApi.md#get_hdfs_settings) | **GET** /platform/1/protocols/hdfs/settings | 
[**get_nfs_alias**](ProtocolsApi.md#get_nfs_alias) | **GET** /platform/2/protocols/nfs/aliases/{NfsAliasId} | 
[**get_nfs_check**](ProtocolsApi.md#get_nfs_check) | **GET** /platform/2/protocols/nfs/check | 
[**get_nfs_export**](ProtocolsApi.md#get_nfs_export) | **GET** /platform/2/protocols/nfs/exports/{NfsExportId} | 
[**get_nfs_exports_summary**](ProtocolsApi.md#get_nfs_exports_summary) | **GET** /platform/2/protocols/nfs/exports-summary | 
[**get_nfs_nlm_locks**](ProtocolsApi.md#get_nfs_nlm_locks) | **GET** /platform/2/protocols/nfs/nlm/locks | 
[**get_nfs_nlm_sessions**](ProtocolsApi.md#get_nfs_nlm_sessions) | **GET** /platform/2/protocols/nfs/nlm/sessions | 
[**get_nfs_nlm_waiters**](ProtocolsApi.md#get_nfs_nlm_waiters) | **GET** /platform/2/protocols/nfs/nlm/waiters | 
[**get_nfs_settings_export**](ProtocolsApi.md#get_nfs_settings_export) | **GET** /platform/2/protocols/nfs/settings/export | 
[**get_nfs_settings_global**](ProtocolsApi.md#get_nfs_settings_global) | **GET** /platform/2/protocols/nfs/settings/global | 
[**get_nfs_settings_zone**](ProtocolsApi.md#get_nfs_settings_zone) | **GET** /platform/2/protocols/nfs/settings/zone | 
[**get_smb_openfiles**](ProtocolsApi.md#get_smb_openfiles) | **GET** /platform/1/protocols/smb/openfiles | 
[**get_smb_sessions**](ProtocolsApi.md#get_smb_sessions) | **GET** /platform/1/protocols/smb/sessions | 
[**get_smb_settings_global**](ProtocolsApi.md#get_smb_settings_global) | **GET** /platform/1/protocols/smb/settings/global | 
[**get_smb_settings_share**](ProtocolsApi.md#get_smb_settings_share) | **GET** /platform/1/protocols/smb/settings/share | 
[**get_smb_share**](ProtocolsApi.md#get_smb_share) | **GET** /platform/1/protocols/smb/shares/{SmbShareId} | 
[**get_smb_shares_summary**](ProtocolsApi.md#get_smb_shares_summary) | **GET** /platform/1/protocols/smb/shares-summary | 
[**list_hdfs_proxyusers**](ProtocolsApi.md#list_hdfs_proxyusers) | **GET** /platform/1/protocols/hdfs/proxyusers | 
[**list_hdfs_racks**](ProtocolsApi.md#list_hdfs_racks) | **GET** /platform/1/protocols/hdfs/racks | 
[**list_nfs_aliases**](ProtocolsApi.md#list_nfs_aliases) | **GET** /platform/2/protocols/nfs/aliases | 
[**list_nfs_exports**](ProtocolsApi.md#list_nfs_exports) | **GET** /platform/2/protocols/nfs/exports | 
[**list_smb_shares**](ProtocolsApi.md#list_smb_shares) | **GET** /platform/1/protocols/smb/shares | 
[**update_hdfs_proxyuser**](ProtocolsApi.md#update_hdfs_proxyuser) | **PUT** /platform/1/protocols/hdfs/proxyusers/{HdfsProxyuserId} | 
[**update_hdfs_rack**](ProtocolsApi.md#update_hdfs_rack) | **PUT** /platform/1/protocols/hdfs/racks/{HdfsRackId} | 
[**update_hdfs_settings**](ProtocolsApi.md#update_hdfs_settings) | **PUT** /platform/1/protocols/hdfs/settings | 
[**update_nfs_alias**](ProtocolsApi.md#update_nfs_alias) | **PUT** /platform/2/protocols/nfs/aliases/{NfsAliasId} | 
[**update_nfs_export**](ProtocolsApi.md#update_nfs_export) | **PUT** /platform/2/protocols/nfs/exports/{NfsExportId} | 
[**update_nfs_settings_export**](ProtocolsApi.md#update_nfs_settings_export) | **PUT** /platform/2/protocols/nfs/settings/export | 
[**update_nfs_settings_global**](ProtocolsApi.md#update_nfs_settings_global) | **PUT** /platform/2/protocols/nfs/settings/global | 
[**update_nfs_settings_zone**](ProtocolsApi.md#update_nfs_settings_zone) | **PUT** /platform/2/protocols/nfs/settings/zone | 
[**update_smb_settings_global**](ProtocolsApi.md#update_smb_settings_global) | **PUT** /platform/1/protocols/smb/settings/global | 
[**update_smb_settings_share**](ProtocolsApi.md#update_smb_settings_share) | **PUT** /platform/1/protocols/smb/settings/share | 
[**update_smb_share**](ProtocolsApi.md#update_smb_share) | **PUT** /platform/1/protocols/smb/shares/{SmbShareId} | 


# **create_hdfs_proxyuser**
> CreateResponse create_hdfs_proxyuser(hdfs_proxyuser)



Create a new HDFS proxyuser.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_proxyuser = isi_sdk_7_2.HdfsProxyuserCreateParams() # HdfsProxyuserCreateParams | 

try:
    api_response = api_instance.create_hdfs_proxyuser(hdfs_proxyuser)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_hdfs_proxyuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_proxyuser** | [**HdfsProxyuserCreateParams**](HdfsProxyuserCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hdfs_rack**
> CreateResponse create_hdfs_rack(hdfs_rack)



Create a new HDFS rack.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_rack = isi_sdk_7_2.HdfsRackCreateParams() # HdfsRackCreateParams | 

try:
    api_response = api_instance.create_hdfs_rack(hdfs_rack)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_hdfs_rack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_rack** | [**HdfsRackCreateParams**](HdfsRackCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_alias**
> CreateNfsAliasResponse create_nfs_alias(nfs_alias, zone=zone)



Create a new NFS alias.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_alias = isi_sdk_7_2.NfsAliasCreateParams() # NfsAliasCreateParams | 
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.create_nfs_alias(nfs_alias, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_alias** | [**NfsAliasCreateParams**](NfsAliasCreateParams.md)|  | 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**CreateNfsAliasResponse**](CreateNfsAliasResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_export**
> CreateQuotaReportResponse create_nfs_export(nfs_export, force=force, zone=zone)



Create a new NFS export.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_export = isi_sdk_7_2.NfsExportCreateParams() # NfsExportCreateParams | 
force = true # bool | If true, the export will be created even if it conflicts with another export. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.create_nfs_export(nfs_export, force=force, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export** | [**NfsExportCreateParams**](NfsExportCreateParams.md)|  | 
 **force** | **bool**| If true, the export will be created even if it conflicts with another export. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**CreateQuotaReportResponse**](CreateQuotaReportResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nfs_reload_item**
> Empty create_nfs_reload_item(nfs_reload_item)



Reload default NFS export configuration.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_reload_item = isi_sdk_7_2.Empty() # Empty | 

try:
    api_response = api_instance.create_nfs_reload_item(nfs_reload_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_nfs_reload_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_reload_item** | [**Empty**](Empty.md)|  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_smb_share**
> CreateResponse create_smb_share(smb_share, zone=zone)



Create a new share.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_share = isi_sdk_7_2.SmbShareCreateParams() # SmbShareCreateParams | 
zone = 'zone_example' # str | Zone which contains this share. (optional)

try:
    api_response = api_instance.create_smb_share(smb_share, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->create_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_share** | [**SmbShareCreateParams**](SmbShareCreateParams.md)|  | 
 **zone** | **str**| Zone which contains this share. | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hdfs_proxyuser**
> delete_hdfs_proxyuser(hdfs_proxyuser_id)



Delete a a HDFS proxyuser.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_proxyuser_id = 'hdfs_proxyuser_id_example' # str | Delete a a HDFS proxyuser.

try:
    api_instance.delete_hdfs_proxyuser(hdfs_proxyuser_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_hdfs_proxyuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_proxyuser_id** | **str**| Delete a a HDFS proxyuser. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hdfs_rack**
> delete_hdfs_rack(hdfs_rack_id)



Delete the HDFS rack.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_rack_id = 'hdfs_rack_id_example' # str | Delete the HDFS rack.

try:
    api_instance.delete_hdfs_rack(hdfs_rack_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_hdfs_rack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_rack_id** | **str**| Delete the HDFS rack. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_alias**
> delete_nfs_alias(nfs_alias_id, zone=zone)



Delete the export.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_alias_id = 'nfs_alias_id_example' # str | Delete the export.
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.delete_nfs_alias(nfs_alias_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_nfs_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_alias_id** | **str**| Delete the export. | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_export**
> delete_nfs_export(nfs_export_id, zone=zone)



Delete the export.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_export_id = 'nfs_export_id_example' # str | Delete the export.
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.delete_nfs_export(nfs_export_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export_id** | **str**| Delete the export. | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nfs_nlm_session**
> delete_nfs_nlm_session(nfs_nlm_session_id)



Delete an NLM session.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_nlm_session_id = 'nfs_nlm_session_id_example' # str | Delete an NLM session.

try:
    api_instance.delete_nfs_nlm_session(nfs_nlm_session_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_nfs_nlm_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_nlm_session_id** | **str**| Delete an NLM session. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_openfile**
> delete_smb_openfile(smb_openfile_id)



Close the file in the SMB server.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_openfile_id = 'smb_openfile_id_example' # str | Close the file in the SMB server.

try:
    api_instance.delete_smb_openfile(smb_openfile_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_openfile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_openfile_id** | **str**| Close the file in the SMB server. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_session**
> delete_smb_session(smb_session_id)



Close the SMB session.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_session_id = 'smb_session_id_example' # str | Close the SMB session.

try:
    api_instance.delete_smb_session(smb_session_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_session_id** | **str**| Close the SMB session. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_sessions_computer_user**
> delete_smb_sessions_computer_user(smb_sessions_computer_user, computer)



Close the SMB session.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_sessions_computer_user = 'smb_sessions_computer_user_example' # str | Close the SMB session.
computer = 'computer_example' # str | 

try:
    api_instance.delete_smb_sessions_computer_user(smb_sessions_computer_user, computer)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_sessions_computer_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_sessions_computer_user** | **str**| Close the SMB session. | 
 **computer** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_share**
> delete_smb_share(smb_share_id, zone=zone)



Delete the share.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_share_id = 'smb_share_id_example' # str | Delete the share.
zone = 'zone_example' # str | Zone which contains this share. (optional)

try:
    api_instance.delete_smb_share(smb_share_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_share_id** | **str**| Delete the share. | 
 **zone** | **str**| Zone which contains this share. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_smb_shares**
> delete_smb_shares()



Delete multiple smb shares.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_instance.delete_smb_shares()
except ApiException as e:
    print("Exception when calling ProtocolsApi->delete_smb_shares: %s\n" % e)
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

# **get_hdfs_proxyuser**
> HdfsProxyusers get_hdfs_proxyuser(hdfs_proxyuser_id)



List all proxyusers.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_proxyuser_id = 'hdfs_proxyuser_id_example' # str | List all proxyusers.

try:
    api_response = api_instance.get_hdfs_proxyuser(hdfs_proxyuser_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_proxyuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_proxyuser_id** | **str**| List all proxyusers. | 

### Return type

[**HdfsProxyusers**](HdfsProxyusers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_rack**
> HdfsRacks get_hdfs_rack(hdfs_rack_id)



Retrieve the HDFS rack.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_rack_id = 'hdfs_rack_id_example' # str | Retrieve the HDFS rack.

try:
    api_response = api_instance.get_hdfs_rack(hdfs_rack_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_rack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_rack_id** | **str**| Retrieve the HDFS rack. | 

### Return type

[**HdfsRacks**](HdfsRacks.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hdfs_settings**
> HdfsSettings get_hdfs_settings()



Retrieve HDFS properties.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_hdfs_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_hdfs_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HdfsSettings**](HdfsSettings.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_alias**
> NfsAliases get_nfs_alias(nfs_alias_id, scope=scope, zone=zone)



Retrieve export information.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_alias_id = 'nfs_alias_id_example' # str | Retrieve export information.
scope = 'scope_example' # str | If specified as effective or not specified, all export fields are shown.  If specified as user, only fields with non-default values are shown. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_alias(nfs_alias_id, scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_alias_id** | **str**| Retrieve export information. | 
 **scope** | **str**| If specified as effective or not specified, all export fields are shown.  If specified as user, only fields with non-default values are shown. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsAliases**](NfsAliases.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_check**
> NfsCheckExtended get_nfs_check(zone=zone)



Retrieve NFS export validation information.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_check(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsCheckExtended**](NfsCheckExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_export**
> NfsExports get_nfs_export(nfs_export_id, scope=scope, zone=zone)



Retrieve export information.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_export_id = 'nfs_export_id_example' # str | Retrieve export information.
scope = 'scope_example' # str | If specified as effective or not specified, all export fields are shown.  If specified as user, only fields with non-default values are shown. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_export(nfs_export_id, scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export_id** | **str**| Retrieve export information. | 
 **scope** | **str**| If specified as effective or not specified, all export fields are shown.  If specified as user, only fields with non-default values are shown. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsExports**](NfsExports.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_exports_summary**
> NfsExportsSummary get_nfs_exports_summary(zone=zone)



Retrieve NFS export summary information.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_exports_summary(zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_exports_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsExportsSummary**](NfsExportsSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_nlm_locks**
> NfsNlmLocks get_nfs_nlm_locks(sort=sort, limit=limit, dir=dir, resume=resume)



List all NLM locks.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_nfs_nlm_locks(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_nlm_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NfsNlmLocks**](NfsNlmLocks.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_nlm_sessions**
> NfsNlmSessions get_nfs_nlm_sessions(sort=sort, limit=limit, dir=dir, resume=resume)



List all NLM sessions.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_nfs_nlm_sessions(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_nlm_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NfsNlmSessions**](NfsNlmSessions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_nlm_waiters**
> NfsNlmWaiters get_nfs_nlm_waiters(sort=sort, limit=limit, dir=dir, resume=resume)



List all NLM lock waiters.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_nfs_nlm_waiters(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_nlm_waiters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**NfsNlmWaiters**](NfsNlmWaiters.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_settings_export**
> NfsSettingsExport get_nfs_settings_export(scope=scope, zone=zone)



Retrieve export information.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_response = api_instance.get_nfs_settings_export(scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_settings_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

[**NfsSettingsExport**](NfsSettingsExport.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_settings_global**
> NfsSettingsGlobal get_nfs_settings_global()



Retrieve the NFS configuration.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_nfs_settings_global()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_settings_global: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NfsSettingsGlobal**](NfsSettingsGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nfs_settings_zone**
> NfsSettingsZone get_nfs_settings_zone()



Retrieve the NFS server settings for this zone.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_nfs_settings_zone()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_nfs_settings_zone: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NfsSettingsZone**](NfsSettingsZone.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_openfiles**
> SmbOpenfiles get_smb_openfiles(sort=sort, limit=limit, dir=dir, resume=resume)



List open files.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | Order results by this field. Default is id. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_smb_openfiles(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_openfiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Order results by this field. Default is id. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SmbOpenfiles**](SmbOpenfiles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_sessions**
> SmbSessions get_smb_sessions(sort=sort, limit=limit, dir=dir, resume=resume)



List open sessions.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | Order results by this field. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_smb_sessions(sort=sort, limit=limit, dir=dir, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Order results by this field. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**SmbSessions**](SmbSessions.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_settings_global**
> SmbSettingsGlobal get_smb_settings_global(scope=scope)



List all settings.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)

try:
    api_response = api_instance.get_smb_settings_global(scope=scope)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 

### Return type

[**SmbSettingsGlobal**](SmbSettingsGlobal.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_settings_share**
> SmbSettingsShare get_smb_settings_share(scope=scope, zone=zone)



List all settings.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
zone = 'zone_example' # str | Zone which contains these share settings. (optional)

try:
    api_response = api_instance.get_smb_settings_share(scope=scope, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_settings_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **zone** | **str**| Zone which contains these share settings. | [optional] 

### Return type

[**SmbSettingsShare**](SmbSettingsShare.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_share**
> SmbShares get_smb_share(smb_share_id, scope=scope, resolve_names=resolve_names, zone=zone)



Retrieve share.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_share_id = 'smb_share_id_example' # str | Retrieve share.
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
resolve_names = true # bool | If true, resolve group and user names in personas. (optional)
zone = 'zone_example' # str | Zone which contains this share. (optional)

try:
    api_response = api_instance.get_smb_share(smb_share_id, scope=scope, resolve_names=resolve_names, zone=zone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_share_id** | **str**| Retrieve share. | 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **resolve_names** | **bool**| If true, resolve group and user names in personas. | [optional] 
 **zone** | **str**| Zone which contains this share. | [optional] 

### Return type

[**SmbShares**](SmbShares.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_smb_shares_summary**
> SmbSharesSummary get_smb_shares_summary()



Return summary information about shares.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.get_smb_shares_summary()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->get_smb_shares_summary: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SmbSharesSummary**](SmbSharesSummary.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hdfs_proxyusers**
> HdfsProxyusers list_hdfs_proxyusers()



List all proxyusers.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.list_hdfs_proxyusers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_hdfs_proxyusers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HdfsProxyusers**](HdfsProxyusers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hdfs_racks**
> HdfsRacksExtended list_hdfs_racks()



List all racks.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))

try:
    api_response = api_instance.list_hdfs_racks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_hdfs_racks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HdfsRacksExtended**](HdfsRacksExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nfs_aliases**
> NfsAliasesExtended list_nfs_aliases(sort=sort, zone=zone, resume=resume, limit=limit, check=check, dir=dir)



List all NFS aliases.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
zone = 'zone_example' # str | Access zone (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
check = true # bool | Check for conflicts when listing exports. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_nfs_aliases(sort=sort, zone=zone, resume=resume, limit=limit, check=check, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **zone** | **str**| Access zone | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **check** | **bool**| Check for conflicts when listing exports. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**NfsAliasesExtended**](NfsAliasesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nfs_exports**
> NfsExportsExtended list_nfs_exports(sort=sort, zone=zone, resume=resume, limit=limit, scope=scope, check=check, dir=dir)



List all NFS exports.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
zone = 'zone_example' # str | Access zone (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
scope = 'scope_example' # str | If specified as effective or not specified, all export fields are shown.  If specified as user, only fields with non-default values are shown. (optional)
check = true # bool | Check for conflicts when listing exports. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_nfs_exports(sort=sort, zone=zone, resume=resume, limit=limit, scope=scope, check=check, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_nfs_exports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **zone** | **str**| Access zone | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **scope** | **str**| If specified as effective or not specified, all export fields are shown.  If specified as user, only fields with non-default values are shown. | [optional] 
 **check** | **bool**| Check for conflicts when listing exports. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**NfsExportsExtended**](NfsExportsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_smb_shares**
> SmbSharesExtended list_smb_shares(sort=sort, zone=zone, resume=resume, resolve_names=resolve_names, limit=limit, scope=scope, dir=dir)



List all shares.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
sort = 'sort_example' # str | Order results by this field. Default is id. (optional)
zone = 'zone_example' # str | Zone which contains this share. (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
resolve_names = true # bool | If true, resolve group and user names in personas. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
scope = 'scope_example' # str | If specified as \"effective\" or not specified, all fields are returned.  If specified as \"user\", only fields with non-default values are shown.  If specified as \"default\", the original values are returned. (optional)
dir = 'dir_example' # str | The direction of the sort. (optional)

try:
    api_response = api_instance.list_smb_shares(sort=sort, zone=zone, resume=resume, resolve_names=resolve_names, limit=limit, scope=scope, dir=dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtocolsApi->list_smb_shares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Order results by this field. Default is id. | [optional] 
 **zone** | **str**| Zone which contains this share. | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **resolve_names** | **bool**| If true, resolve group and user names in personas. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **scope** | **str**| If specified as \&quot;effective\&quot; or not specified, all fields are returned.  If specified as \&quot;user\&quot;, only fields with non-default values are shown.  If specified as \&quot;default\&quot;, the original values are returned. | [optional] 
 **dir** | **str**| The direction of the sort. | [optional] 

### Return type

[**SmbSharesExtended**](SmbSharesExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_proxyuser**
> update_hdfs_proxyuser(hdfs_proxyuser, hdfs_proxyuser_id)



Create a new HDFS proxyuser.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_proxyuser = isi_sdk_7_2.Empty() # Empty | 
hdfs_proxyuser_id = 'hdfs_proxyuser_id_example' # str | Create a new HDFS proxyuser.

try:
    api_instance.update_hdfs_proxyuser(hdfs_proxyuser, hdfs_proxyuser_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_proxyuser: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_proxyuser** | [**Empty**](Empty.md)|  | 
 **hdfs_proxyuser_id** | **str**| Create a new HDFS proxyuser. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_rack**
> update_hdfs_rack(hdfs_rack, hdfs_rack_id)



Modify the HDFS rack

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_rack = isi_sdk_7_2.HdfsRack() # HdfsRack | 
hdfs_rack_id = 'hdfs_rack_id_example' # str | Modify the HDFS rack

try:
    api_instance.update_hdfs_rack(hdfs_rack, hdfs_rack_id)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_rack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_rack** | [**HdfsRack**](HdfsRack.md)|  | 
 **hdfs_rack_id** | **str**| Modify the HDFS rack | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hdfs_settings**
> update_hdfs_settings(hdfs_settings)



Modify HDFS properties.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
hdfs_settings = isi_sdk_7_2.HdfsSettingsSettings() # HdfsSettingsSettings | 

try:
    api_instance.update_hdfs_settings(hdfs_settings)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_hdfs_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hdfs_settings** | [**HdfsSettingsSettings**](HdfsSettingsSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_alias**
> update_nfs_alias(nfs_alias, nfs_alias_id, zone=zone)



Modify the alias. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_alias = isi_sdk_7_2.NfsAlias() # NfsAlias | 
nfs_alias_id = 'nfs_alias_id_example' # str | Modify the alias. All input fields are optional, but one or more must be supplied.
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.update_nfs_alias(nfs_alias, nfs_alias_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_alias** | [**NfsAlias**](NfsAlias.md)|  | 
 **nfs_alias_id** | **str**| Modify the alias. All input fields are optional, but one or more must be supplied. | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_export**
> update_nfs_export(nfs_export, nfs_export_id, force=force, zone=zone)



Modify the export. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_export = isi_sdk_7_2.NfsExport() # NfsExport | 
nfs_export_id = 'nfs_export_id_example' # str | Modify the export. All input fields are optional, but one or more must be supplied.
force = true # bool | If true, the export will be updated even if that change conflicts with another export. (optional)
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.update_nfs_export(nfs_export, nfs_export_id, force=force, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_export** | [**NfsExport**](NfsExport.md)|  | 
 **nfs_export_id** | **str**| Modify the export. All input fields are optional, but one or more must be supplied. | 
 **force** | **bool**| If true, the export will be updated even if that change conflicts with another export. | [optional] 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_settings_export**
> update_nfs_settings_export(nfs_settings_export, zone=zone)



Modify the default values for NFS exports. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_settings_export = isi_sdk_7_2.NfsSettingsExportSettings() # NfsSettingsExportSettings | 
zone = 'zone_example' # str | Access zone (optional)

try:
    api_instance.update_nfs_settings_export(nfs_settings_export, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_settings_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_settings_export** | [**NfsSettingsExportSettings**](NfsSettingsExportSettings.md)|  | 
 **zone** | **str**| Access zone | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_settings_global**
> update_nfs_settings_global(nfs_settings_global)



Modify the default values for NFS exports. All input fields are optional, but one or more must be supplied.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_settings_global = isi_sdk_7_2.NfsSettingsGlobalSettings() # NfsSettingsGlobalSettings | 

try:
    api_instance.update_nfs_settings_global(nfs_settings_global)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_settings_global** | [**NfsSettingsGlobalSettings**](NfsSettingsGlobalSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nfs_settings_zone**
> update_nfs_settings_zone(nfs_settings_zone)



Modify the NFS server settings for this zone.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
nfs_settings_zone = isi_sdk_7_2.NfsSettingsZoneSettings() # NfsSettingsZoneSettings | 

try:
    api_instance.update_nfs_settings_zone(nfs_settings_zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_nfs_settings_zone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nfs_settings_zone** | [**NfsSettingsZoneSettings**](NfsSettingsZoneSettings.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smb_settings_global**
> update_smb_settings_global(smb_settings_global)



Modify one or more settings.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_settings_global = isi_sdk_7_2.SmbSettingsGlobalExtended() # SmbSettingsGlobalExtended | 

try:
    api_instance.update_smb_settings_global(smb_settings_global)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_smb_settings_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_settings_global** | [**SmbSettingsGlobalExtended**](SmbSettingsGlobalExtended.md)|  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smb_settings_share**
> update_smb_settings_share(smb_settings_share, zone=zone)



Modify one or more settings.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_settings_share = isi_sdk_7_2.SmbSettingsShareExtended() # SmbSettingsShareExtended | 
zone = 'zone_example' # str | Zone which contains these share settings. (optional)

try:
    api_instance.update_smb_settings_share(smb_settings_share, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_smb_settings_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_settings_share** | [**SmbSettingsShareExtended**](SmbSettingsShareExtended.md)|  | 
 **zone** | **str**| Zone which contains these share settings. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_smb_share**
> update_smb_share(smb_share, smb_share_id, zone=zone)



Modify share. All input fields are optional, but one or must be supplied.

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
api_instance = isi_sdk_7_2.ProtocolsApi(isi_sdk_7_2.ApiClient(configuration))
smb_share = isi_sdk_7_2.SmbShare() # SmbShare | 
smb_share_id = 'smb_share_id_example' # str | Modify share. All input fields are optional, but one or must be supplied.
zone = 'zone_example' # str | Zone which contains this share. (optional)

try:
    api_instance.update_smb_share(smb_share, smb_share_id, zone=zone)
except ApiException as e:
    print("Exception when calling ProtocolsApi->update_smb_share: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smb_share** | [**SmbShare**](SmbShare.md)|  | 
 **smb_share_id** | **str**| Modify share. All input fields are optional, but one or must be supplied. | 
 **zone** | **str**| Zone which contains this share. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

