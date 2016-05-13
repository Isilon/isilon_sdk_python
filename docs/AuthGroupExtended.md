# AuthGroupExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **int** | Specifies the numeric group identifier. | [optional] 
**dn** | **str** | Specifies the distinguished name for the user. | 
**dns_domain** | **str** | Specifies the DNS domain. | 
**domain** | **str** | Specifies the domain that the object is part of. | 
**generated_gid** | **bool** | If true, the GID was generated. | 
**id** | **str** | Specifies the user or group ID. | 
**member_of** | [**list[GroupMember]**](GroupMember.md) |  | 
**name** | **str** | Specifies a user or group name. | 
**provider** | **str** | Specifies the authentication provider that the object belongs to. | 
**sam_account_name** | **str** | Specifies a user or group name. | 
**sid** | [**GroupMember**](GroupMember.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | 
**type** | **str** | Specifies the object type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


