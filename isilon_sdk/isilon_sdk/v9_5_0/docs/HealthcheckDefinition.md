# HealthcheckDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A long comment about the definition. | [optional] 
**conflicts** | **list[str]** | Other definitions that this definition conflicts with. | [optional] 
**dependencies** | **list[str]** | Other definitions that this definition depends on. | [optional] 
**description** | **str** | A short description of the definition. | [optional] 
**files** | [**list[HealthcheckDefinitionFile]**](HealthcheckDefinitionFile.md) | The files contained in this definition. | [optional] 
**id** | **str** | A unique identifier for the definition. | [optional] 
**name** | **str** | The name of the definition. | [optional] 
**nodes** | **list[int]** | The nodes that this definition is installed on. | [optional] 
**services** | [**list[HealthcheckDefinitionService]**](HealthcheckDefinitionService.md) | The services affected during the definition deployment | [optional] 
**status** | **str** | The installation status of this definition on the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


