# SessionsInvalidationExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the serialized form of a persona, which can be &#39;UID:0&#39;, &#39;USER:name&#39;, &#39;GID:0&#39;, &#39;GROUP:wheel&#39;, or &#39;SID:S-1-1&#39;. | [optional] 
**name** | **str** | Specifies the persona name, which must be combined with a type. | [optional] 
**not_before** | **int** | The time since the UNIX epoch to not allow sessions for a user. | [optional] 
**type** | **str** | Specifies the type of persona, which must be combined with a name. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


