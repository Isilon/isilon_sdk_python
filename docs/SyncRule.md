# SyncRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | User-entered description of this performance rule. | [optional] 
**enabled** | **bool** | Whether this performance rule is currently in effect during its specified intervals. | [optional] 
**limit** | **int** | Amount the specified system resource type is limited by this rule.  Units are kb/s for bandwidth, files/s for file-count, or processing percentage used for cpu. | [optional] 
**schedule** | [**SyncRuleSchedule**](SyncRuleSchedule.md) | A schedule defining when during a week this performance rule is in effect.  If unspecified or null, the schedule will always be in effect. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


