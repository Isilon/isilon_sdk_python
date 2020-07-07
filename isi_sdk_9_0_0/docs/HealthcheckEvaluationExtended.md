# HealthcheckEvaluationExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checklist_id** | **str** | Checklist to be run | [optional] 
**delivery** | [**list[HealthcheckChecklistDeliveryItem]**](HealthcheckChecklistDeliveryItem.md) |  | [optional] 
**details** | [**list[HealthcheckEvaluationDetail]**](HealthcheckEvaluationDetail.md) | Evaluation results by item - only if COMPLETED | [optional] 
**id** | **str** | Unique identifier | [optional] 
**overrides** | [**list[HealthcheckEvaluationOverride]**](HealthcheckEvaluationOverride.md) | Optional overrides for thresholds etc. | [optional] 
**parameters** | [**Empty**](Empty.md) | Parameters supplied for this evaluation | [optional] 
**result** | **str** | Overall result of evaluation - only if COMPLETED | [optional] 
**run_status** | **str** | Execution status | [optional] 
**start_time** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


