# HealthcheckItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Optional extended description of item | [optional] 
**freshness** | **int** | Maximum age in seconds of acceptable earlier results | [optional] 
**id** | **str** | Unique identifier | [optional] 
**node** | **bool** | True if this item is to be evaluated on each node | [optional] 
**parameters** | [**list[HealthcheckItemParameter]**](HealthcheckItemParameter.md) | Accepted and required parameters | [optional] 
**reference** | **str** | KB URL or similar reference link | [optional] 
**repair_behavior** | **str** | The repair behavior for this item. | [optional] 
**repair_description** | **str** | The description of the repair for this item. | [optional] 
**repair_enabled** | **bool** | Is repair enabled for this check. | [optional] 
**repair_risk** | **str** | The repair risk for this item. | [optional] 
**repair_script** | **str** | The script to execute for this item. | [optional] 
**repair_script_type** | **str** | The type of script to execute for this item. | [optional] 
**resolution** | **str** | Generalized resolution statement for this item. | [optional] 
**scope** | **str** | The scope of the repair for this item. | [optional] 
**summary** | **str** | Brief description of item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


