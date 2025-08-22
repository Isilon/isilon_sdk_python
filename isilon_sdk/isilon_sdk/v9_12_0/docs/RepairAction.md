# RepairAction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A long comment about the repair action. | [optional] 
**conflicts** | **list[str]** | Other repair actions that this repair action conflicts with. | [optional] 
**dependencies** | **list[str]** | Other repair actions that this repair action depends on. | [optional] 
**deprecated** | **list[str]** | List of deprecated repair actions. | [optional] 
**description** | **str** | A short description of the repair action. | [optional] 
**id** | **str** | A unique identifier for the repair action. | [optional] 
**name** | **str** | The name of the repair action. | [optional] 
**no_propagation** | **str** | PKG MCP Propagation. | [optional] 
**nodes** | **list[int]** | The nodes that this repair action is installed on. | [optional] 
**pkgnumber** | **str** | Package number. | [optional] 
**pkgtype** | **str** | Type of package. | [optional] 
**services** | [**list[HealthcheckDefinitionService]**](HealthcheckDefinitionService.md) | The services affected during the repair-action deployment | [optional] 
**signature** | **str** | Signature of file. | [optional] 
**status** | **str** | The installation status of this repair action on the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


