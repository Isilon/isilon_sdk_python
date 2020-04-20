# AuthIdNtoken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_id** | [**list[GroupMember]**](GroupMember.md) | Specifies additional UIDs, GIDs, and SIDs. | [optional] 
**gid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**group_sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**ifs_restricted** | **bool** | Indicates if this user has restricted access to the /ifs file system. | [optional] 
**local_address** | **str** | Specifies the IP address of the node that is serving the request. | [optional] 
**on_disk_group_id** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**on_disk_user_id** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**privilege** | [**list[AuthIdNtokenPrivilegeItem]**](AuthIdNtokenPrivilegeItem.md) | Specifies the privileges granted to the currently authenticated user. | [optional] 
**protocol** | **int** | Specifies the protocol that is responsible for the creation of the token. The integer values for each protcol are as follows: NFS (1), SMB (2), NLM (3), FTP (4), HTTP (5), ISCSI (7), SMB2 (8), NFS4 (9), OneFS API (10), HDFS (15), console (16), and SSH (17). | [optional] 
**remote_address** | **str** | Specifies the IP address of the client requesting information. | [optional] 
**uid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**user_sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**zid** | **int** | Specifies the zone ID of the access zone that is serving the request. | [optional] 
**zone_id** | **str** | Specifies the name of the access zone that is serving the request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


