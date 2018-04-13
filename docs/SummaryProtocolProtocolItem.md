# SummaryProtocolProtocolItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_class** | **str** | The class of the operation. | 
**_in** | **float** | Rate of input (in bytes/second) for an operation since the last time isi statistics collected the data. | 
**in_avg** | **float** | Average input (received) bytes for an operation, in bytes. | 
**in_max** | **float** | Maximum input (received) bytes for an operation, in bytes. | 
**in_min** | **float** | Minimum input (received) bytes for an operation, in bytes. | 
**in_standard_dev** | **float** | Standard deviation for input (received) bytes for an operation, in bytes. | 
**node** | **int** | The node on which the operation was performed. | [optional] 
**operation** | **str** | The operation performed. | 
**operation_count** | **int** | The number of times an operation has been performed. | 
**operation_rate** | **float** | The rate (in ops/second) at which an operation has been performed. | 
**out** | **float** | Rate of output (in bytes/second) for an operation since the last time isi statistics collected the data. | 
**out_avg** | **float** | Average output (sent) bytes for an operation, in bytes. | 
**out_max** | **float** | Maximum output (sent) bytes for an operation, in bytes. | 
**out_min** | **float** | Minimum output (sent) bytes for an operation, in bytes. | 
**out_standard_dev** | **float** | Standard deviation for output (received) bytes for an operation, in bytes. | 
**protocol** | **str** | The protocol of the operation. | 
**time** | **int** | Unix Epoch time in seconds of the request. | 
**time_avg** | **float** | The average elapsed time (in microseconds) taken to complete an operation. | 
**time_max** | **float** | The maximum elapsed time (in microseconds) taken to complete an operation. | 
**time_min** | **float** | The minimum elapsed time (in microseconds) taken to complete an operation. | 
**time_standard_dev** | **float** | The standard deviation time (in microseconds) taken to complete an operation. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


