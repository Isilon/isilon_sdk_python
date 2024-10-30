# PerformanceDatasetExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the performance dataset. If a name is not specified then a default name is assigned. The default name will be an underscore separated list of the performance metrics and filters used to configure the dataset. | 
**creation_time** | **int** | Timestamp of when the dataset was created. | 
**filter_count** | **int** | Number of filters applied to this dataset. | 
**filters** | **list[str]** | Filtered metrics for configuring this dataset. | 
**id** | **int** | Unique identifier for the configured dataset. | 
**metrics** | **list[str]** | Performance metrics defining the dataset. | 
**note** | **str** | Additional information about this dataset | [optional] 
**statkey** | **str** | Key for use in viewing associated raw statistics under the endpoints /statistics/history and /statistics/current. | 
**workload_count** | **int** | Number of workloads pinned to this dataset. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


