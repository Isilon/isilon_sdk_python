# NamespaceAcl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | [**list[AclObject]**](AclObject.md) | Provides the JSON array of access rights. | [optional] 
**authoritative** | **str** | If the directory has access rights set, then this field is returned as acl. If the directory has POSIX permissions set, then this field is returned as mode. | [optional] 
**group** | [**MemberObject**](MemberObject.md) | Provides the JSON object for the group persona of the owner. | [optional] 
**mode** | **str** | Provides the POSIX mode. | [optional] 
**owner** | [**MemberObject**](MemberObject.md) | Provides the JSON object for the owner persona. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


