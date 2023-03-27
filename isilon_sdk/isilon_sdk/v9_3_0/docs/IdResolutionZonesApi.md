# isilon_sdk.v9_3_0.IdResolutionZonesApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_zone_group**](IdResolutionZonesApi.md#get_zone_group) | **GET** /platform/7/id-resolution/zones/{Zid}/groups/{ZoneGroupId} | 
[**get_zone_groups**](IdResolutionZonesApi.md#get_zone_groups) | **GET** /platform/7/id-resolution/zones/{Zid}/groups | 
[**get_zone_user**](IdResolutionZonesApi.md#get_zone_user) | **GET** /platform/7/id-resolution/zones/{Zid}/users/{ZoneUserId} | 
[**get_zone_users**](IdResolutionZonesApi.md#get_zone_users) | **GET** /platform/7/id-resolution/zones/{Zid}/users | 


# **get_zone_group**
> ZoneGroups get_zone_group(zone_group_id, zid)



List a mapping of gid/gsid to groupname.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.IdResolutionZonesApi(isilon_sdk.v9_3_0.ApiClient(configuration))
zone_group_id = 'zone_group_id_example' # str | List a mapping of gid/gsid to groupname.
zid = 'zid_example' # str | 

try:
    api_response = api_instance.get_zone_group(zone_group_id, zid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionZonesApi->get_zone_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_group_id** | **str**| List a mapping of gid/gsid to groupname. | 
 **zid** | **str**|  | 

### Return type

[**ZoneGroups**](ZoneGroups.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_groups**
> ZoneGroupsExtended get_zone_groups(zid, dir=dir, gids=gids, gsids=gsids, limit=limit, resume=resume, sort=sort)



List gid/gsid to groupname mappings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.IdResolutionZonesApi(isilon_sdk.v9_3_0.ApiClient(configuration))
zid = 'zid_example' # str | 
dir = 'dir_example' # str | The direction of the sort. (optional)
gids = 'gids_example' # str | A comma separated list specifying the gids to map with a groupname. (optional)
gsids = 'gsids_example' # str | A comma separated list specifying the gsids to map with a groupname. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)

try:
    api_response = api_instance.get_zone_groups(zid, dir=dir, gids=gids, gsids=gsids, limit=limit, resume=resume, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionZonesApi->get_zone_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zid** | **str**|  | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **gids** | **str**| A comma separated list specifying the gids to map with a groupname. | [optional] 
 **gsids** | **str**| A comma separated list specifying the gsids to map with a groupname. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 

### Return type

[**ZoneGroupsExtended**](ZoneGroupsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_user**
> ZoneUsers get_zone_user(zone_user_id, zid)



List a mapping of uid/sid to username.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.IdResolutionZonesApi(isilon_sdk.v9_3_0.ApiClient(configuration))
zone_user_id = 'zone_user_id_example' # str | List a mapping of uid/sid to username.
zid = 'zid_example' # str | 

try:
    api_response = api_instance.get_zone_user(zone_user_id, zid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionZonesApi->get_zone_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone_user_id** | **str**| List a mapping of uid/sid to username. | 
 **zid** | **str**|  | 

### Return type

[**ZoneUsers**](ZoneUsers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_zone_users**
> ZoneUsersExtended get_zone_users(zid, dir=dir, limit=limit, resume=resume, sids=sids, sort=sort, uids=uids)



List uid/sid to username mappings.

### Example
```python
from __future__ import print_function
import time
import isilon_sdk.v9_3_0
from isilon_sdk.v9_3_0.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isilon_sdk.v9_3_0.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isilon_sdk.v9_3_0.IdResolutionZonesApi(isilon_sdk.v9_3_0.ApiClient(configuration))
zid = 'zid_example' # str | 
dir = 'dir_example' # str | The direction of the sort. (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)
sids = 'sids_example' # str | A comma separated list specifying the sids to map with a username. (optional)
sort = 'sort_example' # str | The field that will be used for sorting. (optional)
uids = 'uids_example' # str | A comma separated list specifying the uids to map with a username. (optional)

try:
    api_response = api_instance.get_zone_users(zid, dir=dir, limit=limit, resume=resume, sids=sids, sort=sort, uids=uids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IdResolutionZonesApi->get_zone_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zid** | **str**|  | 
 **dir** | **str**| The direction of the sort. | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
 **sids** | **str**| A comma separated list specifying the sids to map with a username. | [optional] 
 **sort** | **str**| The field that will be used for sorting. | [optional] 
 **uids** | **str**| A comma separated list specifying the uids to map with a username. | [optional] 

### Return type

[**ZoneUsersExtended**](ZoneUsersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

