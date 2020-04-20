# DatasetWorkloadExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workload. User specified. | [optional] 
**creation_time** | **int** | Timestamp of when the workload was pinned. | [optional] 
**dataset_id** | **int** | Unique identifier of the associated dataset. | [optional] 
**error** | **str** | If this field is present, then there was an error fetching the workload configuration. | [optional] 
**id** | **int** | The workload ID. Unique and automatically assigned. | 
**metric_values** | [**DatasetFilterMetricValues**](DatasetFilterMetricValues.md) | Performance metric values that can be used to pin workloads and apply filters, and performance metric values that are used to display information about the system performance dataset. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


