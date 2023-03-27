# NodeStatusNodeStatusSystemStats

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_scan_requests** | **int** | Total number of scan requests received by the CAVA antivirus system. | [optional] 
**avg_scan_block_time** | **int** | Average time spent during which the scan requests are blocked. | [optional] 
**avg_scan_duration** | **int** | Average time to scan a file (in milliseconds). | [optional] 
**batch_file_queue_max_size** | **int** | Maximum number of files that can be queued in the batch file queue. | [optional] 
**batch_file_queue_size** | **int** | Number of scan requests queued for scanning in the batch file queue. | [optional] 
**cee_failure_count** | **int** | Number of scan failure responses received from CEE server. | [optional] 
**cee_infected_count** | **int** | Number of scan infected responses received from CEE server. | [optional] 
**cee_success_count** | **int** | Number of scan success responses received from CEE server. | [optional] 
**fast_file_queue_max_size** | **int** | Maximum number of files that can be queued in the fast file queue. | [optional] 
**fast_file_queue_size** | **int** | Number of scan requests queued for scanning in the fast file queue. | [optional] 
**files_processed** | **int** | Total number of files processed by the CAVA antivirus system. | [optional] 
**files_skipped_per_filter** | **int** | Total number of files skipped per filter settings. | [optional] 
**files_skipped_per_size** | **int** | Total number of files skipped per maximum size setting. | [optional] 
**job_scan_requests** | **int** | Total number of scan requests received from the job engine. | [optional] 
**manual_scan_requests** | **int** | Total number of scan requests initiated through PAPI. | [optional] 
**on_demand_scan_requests** | **int** | Total number of on-demand (protocol) scan requests received. | [optional] 
**scan_fails** | **int** | Number of scan failures occurred while scanning. | [optional] 
**scan_timeouts** | **int** | Number of scan timeouts occurred while scanning. | [optional] 
**slow_file_queue_max_size** | **int** | Maximum number of files that can be queued in the slow (large/cloudpool) file queue. | [optional] 
**slow_file_queue_size** | **int** | Number of scan requests queued for scanning in the slow (large/cloudpool) file queue. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


