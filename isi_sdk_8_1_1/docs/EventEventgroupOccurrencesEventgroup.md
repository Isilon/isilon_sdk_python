# EventEventgroupOccurrencesEventgroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**causes** | **list[list[str]]** | List of eventgroup IDs that may be causes of this occurrence. | [optional] 
**channels** | **list[str]** | List of channels to which alerts are configured for this eventgroup | [optional] 
**event_count** | **int** | Number of events linked to this eventgroup. | [optional] 
**eventgroup_instance** | **str** | Unique identifier of eventgroup instance. | [optional] 
**id** | **str** | Same as eventgroup_instance. | [optional] 
**ignore** | **bool** | True if eventgroup is marked as &#39;ignore&#39;. | [optional] 
**ignore_time** | **int** | Time eventgroup was marked as &#39;ignore&#39;. | [optional] 
**last_event** | **int** | Time the most recent event was added to this eventgroup. | [optional] 
**resolve_time** | **int** | When the eventgroup became resolved. | [optional] 
**resolved** | **bool** | True if eventgroup is resolved. | [optional] 
**resolver** | **str** | &#39;USER&#39; if the eventgroup was marked resolved via PAPI &lt;event_instance&gt; if eventgroup was marked resolved as a result of an event. | [optional] 
**sequence** | **int** | XXX description needed. | [optional] 
**severity** | **str** | Event Group severity. | [optional] 
**specifier** | [**Empty**](Empty.md) | A collection of parameters defined per eventgroup_id. | [optional] 
**time_noticed** | **int** | Time of first event linked to this eventgroup. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


