# DatasetFilterExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the filter. User specified. | [optional] 
**creation_time** | **int** | Timestamp of when the filter was applied. | [optional] 
**dataset_id** | **int** | Unique identifier of the associated dataset. | [optional] 
**error** | **str** | If this field is present, then there was an error fetching the filter configuration. | [optional] 
**id** | **int** | The filter ID. Unique and automatically assigned. | 
**metric_values** | [**DatasetFilterMetricValues**](DatasetFilterMetricValues.md) | Performance metric values that can be used to pin workloads and apply filters, and performance metric values that are used to display information about the system performance dataset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


