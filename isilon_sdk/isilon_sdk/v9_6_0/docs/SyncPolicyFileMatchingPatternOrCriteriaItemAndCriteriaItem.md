# SyncPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_exists** | **bool** | For \&quot;custom_attribute\&quot; type criteria.  The file will match as long as the attribute named by \&quot;field\&quot; exists.  Default is true. | [optional] 
**case_sensitive** | **bool** | If true, the value comparison will be case sensitive.  Default is true. | [optional] 
**field** | **str** | The name of the file attribute to match on (only required if this is a custom_attribute type criterion).  Default is an empty string \&quot;\&quot;. | [optional] 
**operator** | **str** | How to compare the specified attribute of each file to the specified value. | [optional] 
**type** | **str** | The type of this criterion, that is, which file attribute to match on. | 
**value** | **str** | The value to compare the specified attribute of each file to. | [optional] 
**whole_word** | **bool** | If true, the attribute must match the entire word.  Default is true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


