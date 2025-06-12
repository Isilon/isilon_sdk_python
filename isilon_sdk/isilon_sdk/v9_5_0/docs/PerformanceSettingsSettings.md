# PerformanceSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_impact** | [**PerformanceSettingsSettingsClientImpact**](PerformanceSettingsSettingsClientImpact.md) | This indicates how much this workload can impact clients. The thresholds are added to the latency thresholds for computing the throttling limits. | [optional] 
**cpu_limit_us** | [**PerformanceSettingsSettingsCpuLimitUs**](PerformanceSettingsSettingsCpuLimitUs.md) |  | [optional] 
**disk_read_limit** | [**PerformanceSettingsSettingsCpuLimitUs**](PerformanceSettingsSettingsCpuLimitUs.md) |  | [optional] 
**disk_write_limit** | [**PerformanceSettingsSettingsCpuLimitUs**](PerformanceSettingsSettingsCpuLimitUs.md) |  | [optional] 
**main_loop_timeout_sec** | **int** | Maximum time the main PP Leader&#39;s loop will take to complete, in seconds. | [optional] 
**max_dataset_count** | **int** | The maximum number of datasets that can be configured on the system. | 
**max_filter_count** | **int** | The maximum number of filters that can be applied to a configured performance dataset. | 
**max_stat_size** | **int** | The maximum size in bytes of a single performance dataset sample. | 
**max_top_n_collection_count** | **int** | The maximum valid value for the &#39;top_n_collection_count&#39; setting. | 
**max_workload_count** | **int** | The maximum number of workloads that can be pinned to a configured performance dataset. | 
**protocol_ops_limit_enabled** | **bool** | Limit workload performance by protocol ops. | [optional] 
**protocol_ops_limit_for_zero_curr_protocol_ops** | **int** | Protocol ops limit to set when current protocol ops on a node is zero. | [optional] 
**stats_d_query_interval_sec** | **int** | The number of seconds between consecutive queries to isi_stats_d. | [optional] 
**stats_d_query_timeout_sec** | **int** | The number of seconds before a query to isi_stats_d times out. | [optional] 
**target_disk_time_in_queue_ms** | **float** | The time in disk queue threshold (in milliseconds) beyond which Partitioned Performance considers a node to be degraded. | [optional] 
**target_protocol_read_latency_usec** | **float** | The read latency threshold (in microseconds) beyond which Partitioned Performance considers a node to be degraded. | [optional] 
**target_protocol_write_latency_usec** | **float** | The write latency threshold (in microseconds) beyond which Partitioned Performance considers a node to be degraded. | [optional] 
**top_n_collection_count** | **int** | The number of highest resource-consuming workloads tracked and collected by the system per configured performance dataset. The number of workloads pinned to a configured performance dataset does not count towards this value. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


