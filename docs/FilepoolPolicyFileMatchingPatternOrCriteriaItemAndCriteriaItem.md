# FilepoolPolicyFileMatchingPatternOrCriteriaItemAndCriteriaItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_exists** | **bool** | Indicates whether the existence of an attribute indicates a match (valid only with &#39;type&#39; &#x3D; &#39;custom_attribute&#39;) | [optional] 
**begins_with** | **bool** | True to match files recursively under the given path. (valid only with &#39;type&#39; &#x3D; &#39;path&#39;) | [optional] 
**case_sensitive** | **bool** | True to indicate case sensitivity when comparing file attributes (valid only with &#39;type&#39; &#x3D; &#39;name&#39; or &#39;type&#39; &#x3D; &#39;path&#39;) | [optional] 
**field** | **str** | File attribute field name to be compared in a custom comparison (valid only with &#39;type&#39; &#x3D; &#39;custom_attribute&#39;) | [optional] 
**operator** | **str** | The comparison operator to use while comparing an attribute with its value | [optional] 
**type** | **str** | The file attribute to be compared to a given value | 
**units** | **str** | Size unit value. One of &#39;B&#39;,&#39;KB&#39;,&#39;MB&#39;,&#39;GB&#39;,&#39;TB&#39;,&#39;PB&#39;,&#39;EB&#39; (valid only with &#39;type&#39; &#x3D; &#39;size&#39;) | [optional] 
**use_relative_time** | **bool** | Whether time units refer to a calendar date and time (e.g., Jun 3, 2009) or a relative duration (e.g., 2 weeks) (valid only with &#39;type&#39; in {accessed_time, birth_time, changed_time or metadata_changed_time} | [optional] 
**value** | **str** | The value to be compared against a file attribute | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


