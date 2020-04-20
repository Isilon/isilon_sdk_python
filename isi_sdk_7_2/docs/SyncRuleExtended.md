# SyncRuleExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | User-entered description of this performance rule. | 
**enabled** | **bool** | Whether this performance rule is currently in effect during its specified intervals. | 
**limit** | **int** | Amount the specified system resource type is limited by this rule.  Units are kb/s for bandwidth, files/s for file-count, or processing percentage used for cpu. | 
**schedule** | [**SyncRuleSchedule**](SyncRuleSchedule.md) | A schedule defining when during a week this performance rule is in effect.  If unspecified or null, the schedule will always be in effect. | [optional] 
**id** | **str** | The system ID given to this performance rule. | 
**type** | **str** | The type of system resource this rule limits. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


