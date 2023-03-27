# AuthAccessAccessItemShareSharePermissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_permissions** | **str** | Returns Share level permissions for the user.{ &#39;read&#39; , &#39;write&#39; , &#39;full&#39; or &#39;none&#39; will be the values} | [optional] 
**impersonate_guest** | **bool** | Returns whether impersonate guest setting is enabled for the user on the share. | [optional] 
**impersonate_user** | **bool** | Returns whether impersonate user setting is enabled on the share | [optional] 
**run_as_root** | **bool** | Returns whether run as root is enabled for the user on the share | [optional] 
**share_relevant_aces** | [**list[AuthAccessAccessItemFileFilePermissionsRelevantAce]**](AuthAccessAccessItemFileFilePermissionsRelevantAce.md) | Specifies a list of the relevant Access Control Entries withrespect to the user in the share. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


