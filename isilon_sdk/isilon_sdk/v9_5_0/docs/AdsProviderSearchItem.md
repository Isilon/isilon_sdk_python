# AdsProviderSearchItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The user or group description to search for. | [optional] 
**domain** | **str** | The Active Directory provider name to search for. | [optional] 
**filter** | **str** | The LDAP filter to apply to the search. | [optional] 
**limit** | **int** | Return no more than this many results at once (see resume). | [optional] 
**password** | **str** | The password for the domain if untrusted. | [optional] 
**resume** | **str** | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 
**search_groups** | **bool** | If true, search for groups. | [optional] 
**search_users** | **bool** | If true, search for users. | [optional] 
**user** | **str** | The user name for the domain if untrusted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


