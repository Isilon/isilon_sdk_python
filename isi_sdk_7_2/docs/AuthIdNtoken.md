# AuthIdNtoken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_id** | [**list[GroupMember]**](GroupMember.md) |  | [optional] 
**gid** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**group_sid** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**ifs_restricted** | **bool** | Indicates if this user has restricted access to the /ifs file system. | [optional] 
**local_address** | **str** | The IP address of the node that is servicing the request. | [optional] 
**on_disk_group_id** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**on_disk_user_id** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**privilege** | [**list[AuthIdNtokenPrivilegeItem]**](AuthIdNtokenPrivilegeItem.md) | Privileges held by the currently authenticated user. | [optional] 
**protocol** | **int** |  | [optional] 
**remote_address** | **str** | The IP address of the client making the request for information. | [optional] 
**uid** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**user_sid** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**zid** | **int** | The zone id that is serving the request. | [optional] 
**zone_id** | **str** | The name of the zone serving the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


