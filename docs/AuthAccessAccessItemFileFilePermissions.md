# AuthAccessAccessItemFileFilePermissions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dacl** | **str** | Returns a status message if the Null ACL is set. | [optional] 
**delete_child** | **str** | Returns a status message if the parent directoryhas the delete_child property set for the user.If the delete_child property is set for a user,that user is able to delete the file.the delete_child for the user. | [optional] 
**expected** | **str** | Specifies the Access Control Entry (ACE) for the user. | [optional] 
**mode** | **str** | Specifies the mode bits on the file. | [optional] 
**ownership** | **str** | Returns a status message if the user owns the file. | [optional] 
**relevant_aces** | [**list[AuthAccessAccessItemShareSharePermissionsShareRelevantAce]**](AuthAccessAccessItemShareSharePermissionsShareRelevantAce.md) | Specifies a list of the relevant Access Control Entrieswith respect to the user in the share. | [optional] 
**relevant_mode** | **str** | Specifies the mode bits that are related to the user. | [optional] 
**sticky** | **str** | Returns a status message if the user owns the file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


