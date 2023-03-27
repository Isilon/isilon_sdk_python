# NdmpSettingsGlobalGlobal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bre_max_num_contexts** | **int** | Maximum number of BRE contexts. | [optional] 
**dma** | **str** | A unique identifier for the dma vendor. | [optional] 
**enable_redirector** | **bool** | Enable/Disable NDMP Redirector feature to distribute NDMP backup and restore operations among multiple nodes. | [optional] 
**enable_throttler** | **bool** | Enable/Disable NDMP throttler feature to limit CPU usage for NDMP backup or restore operations on each node. | [optional] 
**msb_context_retention_duration** | **int** | Multi-Stream Backup context retention duration, expressed in seconds. | [optional] 
**msr_context_retention_duration** | **int** | Multi-Stream Restore context retention duration, expressed in seconds. | [optional] 
**port** | **int** | The port to listen on. | [optional] 
**service** | **bool** | Property to enable/disable the NDMP service. | [optional] 
**stub_file_open_timeout** | **int** | Stub file open timeout during a backup or restore, expressed in seconds. | [optional] 
**throttler_cpu_threshold** | **int** | NDMP Throttler CPU threshold in percentage. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


