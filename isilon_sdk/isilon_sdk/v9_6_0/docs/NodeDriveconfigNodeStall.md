# NodeDriveconfigNodeStall

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clear_time** | **int** | The amount of time in seconds with no stalls before ignoring previous stalls. | [optional] 
**diskscrub_stripes** | **int** | Number of stripes to read during a diskscrub. | [optional] 
**max_error_frequency** | **int** | The number of errors during stalled drive disk exercises to cause the drive to be softfailed. | [optional] 
**max_slow_access** | **int** | The number of slow accesses during stalled drive disk exercises to cause the drive to be softfailed. | [optional] 
**max_slow_frequency** | **int** | The number of slow frequency triggers during stalled drive disk exercises to cause the drive to be softfailed. | [optional] 
**max_total_stall_time** | **int** | The maximum amount of time, in seconds, to remain stalled before softfailing the drive. | [optional] 
**max_total_stall_time_without_error** | **int** | Max amount of time to spend in stalled before softfailing the drive even without new errors. | [optional] 
**scan_max_ecc_delay** | **int** | Maximum delay in seconds after an ECC correction during a scan. | [optional] 
**scan_size** | **int** | Total bytes of error-free reads to complete a scan. | [optional] 
**sleep** | **int** | Delay in seconds between evaluations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


