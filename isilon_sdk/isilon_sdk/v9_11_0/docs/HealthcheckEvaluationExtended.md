# HealthcheckEvaluationExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checklist_id** | **str** | Checklist to be run | [optional] 
**delivery** | [**list[HealthcheckChecklistDeliveryItem]**](HealthcheckChecklistDeliveryItem.md) | List of delivery addresses/methods for results | [optional] 
**details** | [**list[HealthcheckEvaluationDetail]**](HealthcheckEvaluationDetail.md) | Evaluation results by item - only if COMPLETED | [optional] 
**id** | **str** | Unique identifier | [optional] 
**overrides** | [**list[HealthcheckEvaluationOverride]**](HealthcheckEvaluationOverride.md) | Optional overrides for thresholds etc. | [optional] 
**parameters** | [**Empty**](Empty.md) | Parameters supplied for this evaluation | [optional] 
**queue_time** | **float** | Specifies the queue time for a checklist or item. | [optional] 
**result** | **str** | Overall result of evaluation - only if COMPLETED | [optional] 
**run_status** | **str** | Execution status | [optional] 
**smartlog** | [**HealthcheckEvaluationSmartlog**](HealthcheckEvaluationSmartlog.md) | Relevant information that may be needed for the diagnostics api. This object will be absent in the case where no relevant logs exist. | [optional] 
**start_time** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


