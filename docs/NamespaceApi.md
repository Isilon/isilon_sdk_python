# isi_sdk_8_2_1.NamespaceApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_directory**](NamespaceApi.md#copy_directory) | **PUT** /namespace/{DirectoryCopyTarget} | 
[**copy_file**](NamespaceApi.md#copy_file) | **PUT** /namespace/{FileCopyTarget} | 
[**create_access_point**](NamespaceApi.md#create_access_point) | **PUT** /namespace/{AccessPointName} | 
[**create_directory**](NamespaceApi.md#create_directory) | **PUT** /namespace/{DirectoryPath} | 
[**create_file**](NamespaceApi.md#create_file) | **PUT** /namespace/{FilePath} | 
[**delete_access_point**](NamespaceApi.md#delete_access_point) | **DELETE** /namespace/{AccessPointName} | 
[**delete_directory**](NamespaceApi.md#delete_directory) | **DELETE** /namespace/{DirectoryPath} | 
[**delete_file**](NamespaceApi.md#delete_file) | **DELETE** /namespace/{FilePath} | 
[**get_acl**](NamespaceApi.md#get_acl) | **GET** /namespace/{NamespacePath} | 
[**get_directory_attributes**](NamespaceApi.md#get_directory_attributes) | **HEAD** /namespace/{DirectoryPath} | 
[**get_directory_contents**](NamespaceApi.md#get_directory_contents) | **GET** /namespace/{DirectoryPath} | 
[**get_directory_metadata**](NamespaceApi.md#get_directory_metadata) | **GET** /namespace/{DirectoryMetadataPath} | 
[**get_file_attributes**](NamespaceApi.md#get_file_attributes) | **HEAD** /namespace/{FilePath} | 
[**get_file_contents**](NamespaceApi.md#get_file_contents) | **GET** /namespace/{FilePath} | 
[**get_file_metadata**](NamespaceApi.md#get_file_metadata) | **GET** /namespace/{FileMetadataPath} | 
[**get_worm_properties**](NamespaceApi.md#get_worm_properties) | **GET** /namespace/{WormFilePath} | 
[**list_access_points**](NamespaceApi.md#list_access_points) | **GET** /namespace | 
[**move_directory**](NamespaceApi.md#move_directory) | **POST** /namespace/{DirectoryPath} | 
[**move_file**](NamespaceApi.md#move_file) | **POST** /namespace/{FilePath} | 
[**query_directory**](NamespaceApi.md#query_directory) | **POST** /namespace/{QueryPath} | 
[**set_acl**](NamespaceApi.md#set_acl) | **PUT** /namespace/{NamespacePath} | 
[**set_directory_metadata**](NamespaceApi.md#set_directory_metadata) | **PUT** /namespace/{DirectoryMetadataPath} | 
[**set_file_metadata**](NamespaceApi.md#set_file_metadata) | **PUT** /namespace/{FileMetadataPath} | 
[**set_worm_properties**](NamespaceApi.md#set_worm_properties) | **PUT** /namespace/{WormFilePath} | 


# **copy_directory**
> CopyErrors copy_directory(directory_copy_target, x_isi_ifs_copy_source, overwrite=overwrite, merge=merge, _continue=_continue)



Recursively copies a directory to a specified destination path. Symbolic links are copied as regular files.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
directory_copy_target = 'directory_copy_target_example' # str | Directory copy destination relative to /.
x_isi_ifs_copy_source = 'x_isi_ifs_copy_source_example' # str | Specifies the full path to the source directory.
overwrite = true # bool | Deletes and replaces the existing user attributes and ACLs of the directory with user-specified attributes and ACLS from the header, when set to true. (optional)
merge = true # bool | Specifies if the contents of a directory should be merged with an existing directory with the same name. (optional)
_continue = true # bool | Specifies whether to continue the copy operation on remaining objects when there is a conflict or error. (optional)

try:
    api_response = api_instance.copy_directory(directory_copy_target, x_isi_ifs_copy_source, overwrite=overwrite, merge=merge, _continue=_continue)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->copy_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_copy_target** | **str**| Directory copy destination relative to /. | 
 **x_isi_ifs_copy_source** | **str**| Specifies the full path to the source directory. | 
 **overwrite** | **bool**| Deletes and replaces the existing user attributes and ACLs of the directory with user-specified attributes and ACLS from the header, when set to true. | [optional] 
 **merge** | **bool**| Specifies if the contents of a directory should be merged with an existing directory with the same name. | [optional] 
 **_continue** | **bool**| Specifies whether to continue the copy operation on remaining objects when there is a conflict or error. | [optional] 

### Return type

[**CopyErrors**](CopyErrors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_file**
> CopyErrors copy_file(file_copy_target, x_isi_ifs_copy_source, clone=clone, snapshot=snapshot, overwrite=overwrite)



Copies a file to the specified destination path.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
file_copy_target = 'file_copy_target_example' # str | File copy destination relative to /.
x_isi_ifs_copy_source = 'x_isi_ifs_copy_source_example' # str | Specifies the full path to the source file.
clone = true # bool | You must set this parameter to true in order to clone a file. (optional)
snapshot = 'snapshot_example' # str | Specifies a snapshot name to clone the file from. (optional)
overwrite = true # bool | Specifies if an existing file should be overwritten by a new file with the same name. (optional)

try:
    api_response = api_instance.copy_file(file_copy_target, x_isi_ifs_copy_source, clone=clone, snapshot=snapshot, overwrite=overwrite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->copy_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_copy_target** | **str**| File copy destination relative to /. | 
 **x_isi_ifs_copy_source** | **str**| Specifies the full path to the source file. | 
 **clone** | **bool**| You must set this parameter to true in order to clone a file. | [optional] 
 **snapshot** | **str**| Specifies a snapshot name to clone the file from. | [optional] 
 **overwrite** | **bool**| Specifies if an existing file should be overwritten by a new file with the same name. | [optional] 

### Return type

[**CopyErrors**](CopyErrors.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_point**
> Empty create_access_point(access_point_name, access_point)



Creates a namespace access point in the file system. Only root users can create or change namespace access points.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
access_point_name = 'access_point_name_example' # str | Access point name.
access_point = isi_sdk_8_2_1.AccessPointCreateParams() # AccessPointCreateParams | Access point parameters model.

try:
    api_response = api_instance.create_access_point(access_point_name, access_point)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->create_access_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_point_name** | **str**| Access point name. | 
 **access_point** | [**AccessPointCreateParams**](AccessPointCreateParams.md)| Access point parameters model. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_directory**
> Empty create_directory(directory_path, x_isi_ifs_target_type, x_isi_ifs_access_control=x_isi_ifs_access_control, x_isi_ifs_node_pool_name=x_isi_ifs_node_pool_name, recursive=recursive, overwrite=overwrite)



Creates a directory with a specified path.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
directory_path = 'directory_path_example' # str | Directory path relative to /.
x_isi_ifs_target_type = 'container' # str | Specifies the resource type. (default to container)
x_isi_ifs_access_control = '0700' # str | Specifies a pre-defined ACL value or POSIX mode with a string in octal string format. (optional) (default to 0700)
x_isi_ifs_node_pool_name = 'x_isi_ifs_node_pool_name_example' # str | Specifies a pre-defined ACL value or POSIX mode with a string. (optional)
recursive = true # bool | Specifies the OneFS node pool name. (optional)
overwrite = true # bool | Deletes and replaces the existing user attributes and ACLs of the directory with user-specified attributes and ACLS from the header, when set to true. (optional)

try:
    api_response = api_instance.create_directory(directory_path, x_isi_ifs_target_type, x_isi_ifs_access_control=x_isi_ifs_access_control, x_isi_ifs_node_pool_name=x_isi_ifs_node_pool_name, recursive=recursive, overwrite=overwrite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->create_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_path** | **str**| Directory path relative to /. | 
 **x_isi_ifs_target_type** | **str**| Specifies the resource type. | [default to container]
 **x_isi_ifs_access_control** | **str**| Specifies a pre-defined ACL value or POSIX mode with a string in octal string format. | [optional] [default to 0700]
 **x_isi_ifs_node_pool_name** | **str**| Specifies a pre-defined ACL value or POSIX mode with a string. | [optional] 
 **recursive** | **bool**| Specifies the OneFS node pool name. | [optional] 
 **overwrite** | **bool**| Deletes and replaces the existing user attributes and ACLs of the directory with user-specified attributes and ACLS from the header, when set to true. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file**
> Empty create_file(file_path, x_isi_ifs_target_type, file_contents, x_isi_ifs_access_control=x_isi_ifs_access_control, content_encoding=content_encoding, content_type=content_type, overwrite=overwrite)



Creates a file object with a given path. Note that file streaming is not supported.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
file_path = 'file_path_example' # str | File path relative to /.
x_isi_ifs_target_type = 'object' # str | Specifies the resource type. (default to object)
file_contents = 'file_contents_example' # str | The contents of the file object.
x_isi_ifs_access_control = '0600' # str | Specifies a pre-defined ACL value or POSIX mode with a string in octal string format. (optional) (default to 0600)
content_encoding = 'content_encoding_example' # str | Specifies the content encoding that was applied to the object content, so that decoding can be applied when retrieving the content. (optional)
content_type = 'binary/octet-stream' # str | Specifies a standard MIME-type description of the content format. (optional) (default to binary/octet-stream)
overwrite = true # bool | Deletes and replaces the existing user attributes and ACLs of the directory with user-specified attributes and ACLS from the header, when set to true. (optional)

try:
    api_response = api_instance.create_file(file_path, x_isi_ifs_target_type, file_contents, x_isi_ifs_access_control=x_isi_ifs_access_control, content_encoding=content_encoding, content_type=content_type, overwrite=overwrite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->create_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| File path relative to /. | 
 **x_isi_ifs_target_type** | **str**| Specifies the resource type. | [default to object]
 **file_contents** | **str**| The contents of the file object. | 
 **x_isi_ifs_access_control** | **str**| Specifies a pre-defined ACL value or POSIX mode with a string in octal string format. | [optional] [default to 0600]
 **content_encoding** | **str**| Specifies the content encoding that was applied to the object content, so that decoding can be applied when retrieving the content. | [optional] 
 **content_type** | **str**| Specifies a standard MIME-type description of the content format. | [optional] [default to binary/octet-stream]
 **overwrite** | **bool**| Deletes and replaces the existing user attributes and ACLs of the directory with user-specified attributes and ACLS from the header, when set to true. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_point**
> Empty delete_access_point(access_point_name)



Deletes a namespace access point. Only root users can delete namespace access points.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
access_point_name = 'access_point_name_example' # str | Access point name.

try:
    api_response = api_instance.delete_access_point(access_point_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->delete_access_point: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_point_name** | **str**| Access point name. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_directory**
> Empty delete_directory(directory_path, recursive=recursive)



Deletes the directory at the specified path.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
directory_path = 'directory_path_example' # str | Directory path relative to /.
recursive = true # bool | Deletes directories recursively, when set to true. (optional)

try:
    api_response = api_instance.delete_directory(directory_path, recursive=recursive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->delete_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_path** | **str**| Directory path relative to /. | 
 **recursive** | **bool**| Deletes directories recursively, when set to true. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> Empty delete_file(file_path)



Deletes the specified file.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
file_path = 'file_path_example' # str | File path relative to /.

try:
    api_response = api_instance.delete_file(file_path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->delete_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| File path relative to /. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acl**
> NamespaceAcl get_acl(namespace_path, acl, nsaccess=nsaccess)



Retrieves the access control list for a namespace object.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
namespace_path = 'namespace_path_example' # str | Namespace path relative to /.
acl = true # bool | Show access control lists.
nsaccess = true # bool | Indicates that the operation is on the access point instead of the store path. (optional)

try:
    api_response = api_instance.get_acl(namespace_path, acl, nsaccess=nsaccess)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->get_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_path** | **str**| Namespace path relative to /. | 
 **acl** | **bool**| Show access control lists. | 
 **nsaccess** | **bool**| Indicates that the operation is on the access point instead of the store path. | [optional] 

### Return type

[**NamespaceAcl**](NamespaceAcl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_attributes**
> Empty get_directory_attributes(directory_path, if_modified_since=if_modified_since, if_unmodified_since=if_unmodified_since)



Retrieves the attribute information for a specified directory without transferring the contents of the directory.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
directory_path = 'directory_path_example' # str | Directory path relative to /.
if_modified_since = 'if_modified_since_example' # str | Returns only files that were modified since the specified time. If no files were modified since this time, a 304 message is returned. (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Returns only files that were not modified since the specified time. If there are no unmodified files since this time, a 412 message is returned to indicate that the precondition failed. (optional)

try:
    api_response = api_instance.get_directory_attributes(directory_path, if_modified_since=if_modified_since, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->get_directory_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_path** | **str**| Directory path relative to /. | 
 **if_modified_since** | **str**| Returns only files that were modified since the specified time. If no files were modified since this time, a 304 message is returned. | [optional] 
 **if_unmodified_since** | **str**| Returns only files that were not modified since the specified time. If there are no unmodified files since this time, a 412 message is returned to indicate that the precondition failed. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_contents**
> NamespaceObjects get_directory_contents(directory_path, detail=detail, limit=limit, resume=resume, sort=sort, dir=dir, type=type, hidden=hidden)



Retrieves a list of files and subdirectories from a directory.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
directory_path = 'directory_path_example' # str | Directory path relative to /.
detail = 'detail_example' # str | Specifies which object attributes are displayed. (optional)
limit = 56 # int | Specifies the maximum number of objects to send to the client. (optional)
resume = 'resume_example' # str | Specifies a token to return in the JSON result to indicate when there is a next page. (optional)
sort = 'sort_example' # str | Specifies one or more attributes to sort on the directory entries. (optional)
dir = 'dir_example' # str | Specifies the sort direction. This value can be either ascending (ASC) or descending (DESC). (optional)
type = 'type_example' # str | Specifies the object type to return, which can be one of the following values: container, object, pipe, character_device, block_device, symbolic_link, socket, or whiteout_file. (optional)
hidden = true # bool | Specifies if hidden objects are returned. (optional)

try:
    api_response = api_instance.get_directory_contents(directory_path, detail=detail, limit=limit, resume=resume, sort=sort, dir=dir, type=type, hidden=hidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->get_directory_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_path** | **str**| Directory path relative to /. | 
 **detail** | **str**| Specifies which object attributes are displayed. | [optional] 
 **limit** | **int**| Specifies the maximum number of objects to send to the client. | [optional] 
 **resume** | **str**| Specifies a token to return in the JSON result to indicate when there is a next page. | [optional] 
 **sort** | **str**| Specifies one or more attributes to sort on the directory entries. | [optional] 
 **dir** | **str**| Specifies the sort direction. This value can be either ascending (ASC) or descending (DESC). | [optional] 
 **type** | **str**| Specifies the object type to return, which can be one of the following values: container, object, pipe, character_device, block_device, symbolic_link, socket, or whiteout_file. | [optional] 
 **hidden** | **bool**| Specifies if hidden objects are returned. | [optional] 

### Return type

[**NamespaceObjects**](NamespaceObjects.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_directory_metadata**
> NamespaceMetadataList get_directory_metadata(directory_metadata_path, metadata)



Retrieves the attribute information for a specified directory with the metadata query argument.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
directory_metadata_path = 'directory_metadata_path_example' # str | Directory path relative to /.
metadata = true # bool | Show directory metadata.

try:
    api_response = api_instance.get_directory_metadata(directory_metadata_path, metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->get_directory_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_metadata_path** | **str**| Directory path relative to /. | 
 **metadata** | **bool**| Show directory metadata. | 

### Return type

[**NamespaceMetadataList**](NamespaceMetadataList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_attributes**
> Empty get_file_attributes(file_path, if_modified_since=if_modified_since, if_unmodified_since=if_unmodified_since)



Retrieves the attribute information for a specified file.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
file_path = 'file_path_example' # str | File path relative to /.
if_modified_since = 'if_modified_since_example' # str | Returns only files that were modified since the specified time. If no files were modified since this time, a 304 message is returned. (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Returns only files that were not modified since the specified time. If there are no unmodified files since this time, a 412 message is returned to indicate that the precondition failed. (optional)

try:
    api_response = api_instance.get_file_attributes(file_path, if_modified_since=if_modified_since, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->get_file_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| File path relative to /. | 
 **if_modified_since** | **str**| Returns only files that were modified since the specified time. If no files were modified since this time, a 304 message is returned. | [optional] 
 **if_unmodified_since** | **str**| Returns only files that were not modified since the specified time. If there are no unmodified files since this time, a 412 message is returned to indicate that the precondition failed. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_contents**
> Empty get_file_contents(file_path, range=range, if_modified_since=if_modified_since, if_unmodified_since=if_unmodified_since)



Retrieves the contents of a file from a specified path. Note that file streaming is not supported.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
file_path = 'file_path_example' # str | File path relative to /.
range = 'range_example' # str | Returns the specified range bytes of an object.  (optional)
if_modified_since = 'if_modified_since_example' # str | Returns only files that were modified since the specified time. If no files were modified since this time, a 304 message is returned. (optional)
if_unmodified_since = 'if_unmodified_since_example' # str | Returns only files that were not modified since the specified time. If there are no unmodified files since this time, a 412 message is returned to indicate that the precondition failed. (optional)

try:
    api_response = api_instance.get_file_contents(file_path, range=range, if_modified_since=if_modified_since, if_unmodified_since=if_unmodified_since)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->get_file_contents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| File path relative to /. | 
 **range** | **str**| Returns the specified range bytes of an object.  | [optional] 
 **if_modified_since** | **str**| Returns only files that were modified since the specified time. If no files were modified since this time, a 304 message is returned. | [optional] 
 **if_unmodified_since** | **str**| Returns only files that were not modified since the specified time. If there are no unmodified files since this time, a 412 message is returned to indicate that the precondition failed. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> NamespaceMetadataList get_file_metadata(file_metadata_path, metadata)



Retrieves the attribute information for a specified file with the metadata query argument.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
file_metadata_path = 'file_metadata_path_example' # str | File path relative to /.
metadata = true # bool | Show file metadata.

try:
    api_response = api_instance.get_file_metadata(file_metadata_path, metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->get_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_metadata_path** | **str**| File path relative to /. | 
 **metadata** | **bool**| Show file metadata. | 

### Return type

[**NamespaceMetadataList**](NamespaceMetadataList.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_worm_properties**
> WormProperties get_worm_properties(worm_file_path, worm)



Retrieves the WORM retention date and committed state of the file.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
worm_file_path = 'worm_file_path_example' # str | Write once read many file path relative to /.
worm = true # bool | View WORM properties

try:
    api_response = api_instance.get_worm_properties(worm_file_path, worm)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->get_worm_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worm_file_path** | **str**| Write once read many file path relative to /. | 
 **worm** | **bool**| View WORM properties | 

### Return type

[**WormProperties**](WormProperties.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_points**
> NamespaceAccessPoints list_access_points(versions=versions)



Retrieves the namespace access points available for the authenticated user.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
versions = true # bool | Protocol versions that are supported for the current namespace access server. (optional)

try:
    api_response = api_instance.list_access_points(versions=versions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->list_access_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **versions** | **bool**| Protocol versions that are supported for the current namespace access server. | [optional] 

### Return type

[**NamespaceAccessPoints**](NamespaceAccessPoints.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_directory**
> Empty move_directory(directory_path, x_isi_ifs_set_location)



Moves a directory from an existing source to a new destination path.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
directory_path = 'directory_path_example' # str | Directory path relative to /.
x_isi_ifs_set_location = 'x_isi_ifs_set_location_example' # str | Specifies the full path for the destination directory.

try:
    api_response = api_instance.move_directory(directory_path, x_isi_ifs_set_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->move_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_path** | **str**| Directory path relative to /. | 
 **x_isi_ifs_set_location** | **str**| Specifies the full path for the destination directory. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_file**
> Empty move_file(file_path, x_isi_ifs_set_location)



Moves a file to a destination path that does not yet exist.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
file_path = 'file_path_example' # str | File path relative to /.
x_isi_ifs_set_location = 'x_isi_ifs_set_location_example' # str | Specifies the full path for the destination file. 

try:
    api_response = api_instance.move_file(file_path, x_isi_ifs_set_location)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->move_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_path** | **str**| File path relative to /. | 
 **x_isi_ifs_set_location** | **str**| Specifies the full path for the destination file.  | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_directory**
> NamespaceObjects query_directory(query_path, query, directory_query, limit=limit, detail=detail, resume=resume, sort=sort, dir=dir, type=type, hidden=hidden, max_depth=max_depth)



Query objects by system-defined and user-defined attributes in a directory.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
query_path = 'query_path_example' # str | Directory path relative to /.
query = true # bool | Enable directory query.
directory_query = isi_sdk_8_2_1.DirectoryQuery() # DirectoryQuery | Directory query parameters model.
limit = 56 # int | Specifies the maximum number of objects to send to the client. You can set the value to a negative number to retrieve all objects. (optional)
detail = 'detail_example' # str | Specifies which object attributes are displayed. If the detail parameter is excluded, only the name of the object is returned. (optional)
resume = 'resume_example' # str | Specifies a token to return in the JSON result to indicate when there is a next page. (optional)
sort = 'sort_example' # str | Specifies one or more attributes to sort on the directory entries. (optional)
dir = 'dir_example' # str | Specifies the sort direction. This value can be either ascending (ASC) or descending (DESC). (optional)
type = 'type_example' # str | Specifies the object type to return, which can be one of the following values: container, object, pipe, character_device, block_device, symbolic_link, socket, or whiteout_file. (optional)
hidden = true # bool | Specifies if hidden objects are returned. (optional)
max_depth = 56 # int | Specifies the maximum directory level depth to search for objects. (optional)

try:
    api_response = api_instance.query_directory(query_path, query, directory_query, limit=limit, detail=detail, resume=resume, sort=sort, dir=dir, type=type, hidden=hidden, max_depth=max_depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->query_directory: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_path** | **str**| Directory path relative to /. | 
 **query** | **bool**| Enable directory query. | 
 **directory_query** | [**DirectoryQuery**](DirectoryQuery.md)| Directory query parameters model. | 
 **limit** | **int**| Specifies the maximum number of objects to send to the client. You can set the value to a negative number to retrieve all objects. | [optional] 
 **detail** | **str**| Specifies which object attributes are displayed. If the detail parameter is excluded, only the name of the object is returned. | [optional] 
 **resume** | **str**| Specifies a token to return in the JSON result to indicate when there is a next page. | [optional] 
 **sort** | **str**| Specifies one or more attributes to sort on the directory entries. | [optional] 
 **dir** | **str**| Specifies the sort direction. This value can be either ascending (ASC) or descending (DESC). | [optional] 
 **type** | **str**| Specifies the object type to return, which can be one of the following values: container, object, pipe, character_device, block_device, symbolic_link, socket, or whiteout_file. | [optional] 
 **hidden** | **bool**| Specifies if hidden objects are returned. | [optional] 
 **max_depth** | **int**| Specifies the maximum directory level depth to search for objects. | [optional] 

### Return type

[**NamespaceObjects**](NamespaceObjects.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_acl**
> Empty set_acl(namespace_path, acl, namespace_acl, nsaccess=nsaccess)



Sets the access control list for a namespace.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
namespace_path = 'namespace_path_example' # str | Namespace path relative to /.
acl = true # bool | Update access control lists.
namespace_acl = isi_sdk_8_2_1.NamespaceAcl() # NamespaceAcl | Namespace ACL parameters model.
nsaccess = true # bool | Indicates that the operation is on the access point instead of the store path. (optional)

try:
    api_response = api_instance.set_acl(namespace_path, acl, namespace_acl, nsaccess=nsaccess)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->set_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_path** | **str**| Namespace path relative to /. | 
 **acl** | **bool**| Update access control lists. | 
 **namespace_acl** | [**NamespaceAcl**](NamespaceAcl.md)| Namespace ACL parameters model. | 
 **nsaccess** | **bool**| Indicates that the operation is on the access point instead of the store path. | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_directory_metadata**
> Empty set_directory_metadata(directory_metadata_path, metadata, directory_metadata)



Sets attributes on a specified directory with the metadata query argument.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
directory_metadata_path = 'directory_metadata_path_example' # str | Directory path relative to /.
metadata = true # bool | Set directory metadata.
directory_metadata = isi_sdk_8_2_1.NamespaceMetadata() # NamespaceMetadata | Directory metadata parameters model.

try:
    api_response = api_instance.set_directory_metadata(directory_metadata_path, metadata, directory_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->set_directory_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_metadata_path** | **str**| Directory path relative to /. | 
 **metadata** | **bool**| Set directory metadata. | 
 **directory_metadata** | [**NamespaceMetadata**](NamespaceMetadata.md)| Directory metadata parameters model. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_file_metadata**
> Empty set_file_metadata(file_metadata_path, metadata, file_metadata)



Sets attributes on a specified file with the metadata query argument through the JSON body.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
file_metadata_path = 'file_metadata_path_example' # str | File path relative to /.
metadata = true # bool | Set file metadata.
file_metadata = isi_sdk_8_2_1.NamespaceMetadata() # NamespaceMetadata | File metadata parameters model.

try:
    api_response = api_instance.set_file_metadata(file_metadata_path, metadata, file_metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->set_file_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_metadata_path** | **str**| File path relative to /. | 
 **metadata** | **bool**| Set file metadata. | 
 **file_metadata** | [**NamespaceMetadata**](NamespaceMetadata.md)| File metadata parameters model. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_worm_properties**
> Empty set_worm_properties(worm_file_path, worm, worm_properties)



Sets the retention period and commits a file in a SmartLock directory.

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
api_instance = isi_sdk_8_2_1.NamespaceApi(isi_sdk_8_2_1.ApiClient(configuration))
worm_file_path = 'worm_file_path_example' # str | Write once read many file path relative to /.
worm = true # bool | View WORM properties
worm_properties = isi_sdk_8_2_1.WormCreateParams() # WormCreateParams | WORM parameters model.

try:
    api_response = api_instance.set_worm_properties(worm_file_path, worm, worm_properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespaceApi->set_worm_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **worm_file_path** | **str**| Write once read many file path relative to /. | 
 **worm** | **bool**| View WORM properties | 
 **worm_properties** | [**WormCreateParams**](WormCreateParams.md)| WORM parameters model. | 

### Return type

[**Empty**](Empty.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

