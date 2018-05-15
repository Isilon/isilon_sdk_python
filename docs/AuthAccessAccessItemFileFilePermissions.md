# AuthAccessAccessItemFileFilePermissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_child** | **bool** | Specifies if the parent directory has the delete_child property set for the user.  If the delete_child property is set for a user, that user is able to delete the file. | [optional] 
**expected** | **str** | Specifies the expected access rights for the user on the file. | [optional] 
**mode** | **str** | Specifies the mode bits on the file. | [optional] 
**ownership** | **bool** | True if the user owns the file. | [optional] 
**relevant_aces** | [**list[AuthAccessAccessItemShareSharePermissionsShareRelevantAce]**](AuthAccessAccessItemShareSharePermissionsShareRelevantAce.md) | Specifies a list of the relevant Access Control Entrieswith respect to the user in the share. | [optional] 
**relevant_mode** | **str** | Specifies the mode bits that are related to the user. | [optional] 
**sticky** | **bool** | Specifies if the parent directory has the stick bit property set indicating only the file&#39;s owner may delete the file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


