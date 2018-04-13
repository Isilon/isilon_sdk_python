# AuthGroupExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dn** | **str** | Specifies the distinguished name for the user. | [optional] 
**dns_domain** | **str** | Specifies the DNS domain. | [optional] 
**domain** | **str** | Specifies the domain that the object is part of. | [optional] 
**generated_gid** | **bool** | If true, the GID was generated. | [optional] 
**gid** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**id** | **str** | Specifies the user or group ID. | 
**member_of** | [**list[AuthAccessAccessItemFileGroup]**](AuthAccessAccessItemFileGroup.md) |  | [optional] 
**name** | **str** | Specifies a user or group name. | 
**object_history** | [**list[AuthGroupObjectHistoryItem]**](AuthGroupObjectHistoryItem.md) |  | [optional] 
**provider** | **str** | Specifies the authentication provider that the object belongs to. | [optional] 
**sam_account_name** | **str** | Specifies a user or group name. | [optional] 
**sid** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**type** | **str** | Specifies the object type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


