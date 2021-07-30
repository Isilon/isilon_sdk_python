# CloudJobCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **list[str]** | The names of accounts for COI restore | [optional] 
**directories** | **list[str]** | Directories addressed by this job | [optional] 
**expiration_date** | **int** | The new expiration date in seconds | [optional] 
**file_matching_pattern** | [**Empty**](Empty.md) | The file filtering logic to find files for this job. (Only applicable for &#39;recall&#39; jobs) | [optional] 
**files** | **list[str]** | Filenames addressed by this job | [optional] 
**policy** | **str** | The name of an existing cloudpool policy to apply to this job. (Only applicable for &#39;archive&#39; jobs) | [optional] 
**type** | **str** | The type of cloud action to be performed by this job. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


