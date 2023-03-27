# StatisticsHistoryStat

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devid** | **int** | Devid of node of statistic or 0 for cluster scoped statistics. | 
**error** | **str** | Key specific error string, if applicable. | [optional] 
**error_code** | **int** | Key specific error number, if applicable. | [optional] 
**key** | **str** | Key name of statistic. | 
**node** | **int** | The LNN of node, if requested. | [optional] 
**resolution** | **int** | The interval for which these results were figured (averaged against.) | 
**values** | [**list[StatisticsHistoryStatValue]**](StatisticsHistoryStatValue.md) | Time-series values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


