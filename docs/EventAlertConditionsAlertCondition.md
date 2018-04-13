# EventAlertConditionsAlertCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **list[str]** | Event Group categories to be alerted | [optional] 
**channel_ids** | **list[int]** | Channels for alert | [optional] 
**condition** | **str** | Trigger condition for alert | [optional] 
**eventgroup_ids** | **list[str]** | Event Group IDs to be alerted | [optional] 
**id** | **str** | Unique identifier. | [optional] 
**interval** | **int** | Required with ONGOING condition only, period in seconds between alerts of ongoing conditions | [optional] 
**limit** | **int** | Required with NEW EVENTS condition only, limits the number of alerts sent as events are added | [optional] 
**name** | **str** | Unique identifier. | [optional] 
**severities** | **list[str]** | Severities to be alerted | [optional] 
**transient** | **int** | Any eventgroup lasting less than this many seconds is deemed transient and will not generate alerts under this condition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


