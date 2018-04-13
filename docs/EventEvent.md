# EventEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged_time** | **int** | The time in epoch seconds at which the event was acknowledged. Set to null when event has not been acknowledged. | [optional] 
**coalesced_by_id** | **str** | The ID of the parent event that coalesced this event. Set to null when event has not been coalesced. | [optional] 
**devid** | **int** | The ID of the device the event refers to. When set to 0, indicates a cluster event. | 
**end** | **int** | The time in epoch seconds at which the event&#39;s lifetime ended. Set to null when the event is still alive. | [optional] 
**event_type** | **int** | A number indicating the class or type of the event. | 
**extreme_severity** | **str** | A severity assigned to events that can change severity during their lifetime. | 
**extreme_value** | **float** | A value corresponding to extreme_severity assignment. | 
**id** | **str** | A unique (across all event_types and instances) identifier for an event. | 
**is_coalescing** | **int** | If non-zero this field represents the coalescer type. | 
**message** | **str** | A message containing information about the event. | 
**severity** | **str** | The current severity of the event. | 
**specifiers** | [**Empty**](Empty.md) | Key-value pairs containing information specific to this event. | 
**start** | **int** | The time in epoch seconds at which the event&#39;s lifetime begins. | 
**update_count** | **int** | The number of times (some parameter of) the event was updated during its lifetime. | [optional] 
**value** | **float** | A value associated with the event. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


