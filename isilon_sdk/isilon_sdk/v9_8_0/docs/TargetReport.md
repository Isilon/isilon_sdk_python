# TargetReport

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be taken by this job. | 
**ads_streams_replicated** | **int** | The number of ads streams replicated by this job. | 
**block_specs_replicated** | **int** | The number of block specs replicated by this job. | 
**bytes_recoverable** | **int** | The number of bytes recoverable by this job. | 
**bytes_transferred** | **int** | The number of bytes that have been transferred by this job. | 
**char_specs_replicated** | **int** | The number of char specs replicated by this job. | 
**committed_files** | **int** | The number of WORM committed files. | 
**corrected_lins** | **int** | The number of LINs corrected by this job. | 
**dead_node** | **bool** | This field is true if the node running this job is dead. | 
**directories_replicated** | **int** | The number of directories replicated. | 
**dirs_changed** | **int** | The number of directories changed by this job. | 
**dirs_deleted** | **int** | The number of directories deleted by this job. | 
**dirs_moved** | **int** | The number of directories moved by this job. | 
**dirs_new** | **int** | The number of directories created by this job. | 
**duration** | **int** | The amount of time in seconds between when the job was started and when it ended.  If the job has not yet ended, this is the amount of time since the job started.  This field is null if the job has not yet started. | [optional] 
**encrypted** | **bool** | If true, syncs will be encrypted. | 
**end_time** | **int** | The time the job ended in unix epoch seconds. The field is null if the job hasn&#39;t ended. | [optional] 
**error** | **str** | The primary error message for this job. | 
**error_checksum_files_skipped** | **int** | The number of files with checksum errors skipped by this job. | 
**error_io_files_skipped** | **int** | The number of files with io errors skipped by this job. | 
**error_net_files_skipped** | **int** | The number of files with network errors skipped by this job. | 
**errors** | **list[str]** | A list of error messages for this job. | 
**failed_chunks** | **int** | Tyhe number of data chunks that failed transmission. | 
**fifos_replicated** | **int** | The number of fifos replicated by this job. | 
**file_data_bytes** | **int** | The number of bytes transferred that belong to files. | 
**files_changed** | **int** | The number of files changed by this job. | 
**files_linked** | **int** | The number of files linked by this job. | 
**files_new** | **int** | The number of files created by this job. | 
**files_selected** | **int** | The number of files selected by this job. | 
**files_transferred** | **int** | The number of files transferred by this job. | 
**files_unlinked** | **int** | The number of files unlinked by this job. | 
**files_with_ads_replicated** | **int** | The number of files with ads replicated by this job. | 
**flipped_lins** | **int** | The number of LINs flipped by this job. | 
**hard_links_replicated** | **int** | The number of hard links replicated by this job. | 
**hash_exceptions_fixed** | **int** | The number of hash exceptions fixed by this job. | 
**hash_exceptions_found** | **int** | The number of hash exceptions found by this job. | 
**id** | **str** | A unique identifier for this object. | 
**job_id** | **int** | The ID of the job. | [optional] 
**lins_total** | **int** | The number of LINs transferred by this job. | 
**network_bytes_to_source** | **int** | The total number of bytes sent to the source by this job. | 
**network_bytes_to_target** | **int** | The total number of bytes sent to the target by this job. | 
**new_files_replicated** | **int** | The number of new files replicated by this job. | 
**num_retransmitted_files** | **int** | The number of files that have been retransmitted by this job. | 
**phases** | [**list[SyncJobPhase]**](SyncJobPhase.md) | Data for each phase of this job. | 
**policy_id** | **str** | The ID of the policy. | 
**policy_name** | **str** | The name of the policy. | 
**quotas_deleted** | **int** | The number of quotas removed from the target. | 
**regular_files_replicated** | **int** | The number of regular files replicated by this job. | 
**resynced_lins** | **int** | The number of LINs resynched by this job. | 
**retransmitted_files** | **list[str]** | The files that have been retransmitted by this job. | 
**retry** | **int** | The number of times the job has been retried. | 
**running_chunks** | **int** | The number of data chunks currently being transmitted. | 
**service_report** | [**list[SyncJobServiceReportItem]**](SyncJobServiceReportItem.md) | Data for each component exported as part of service replication. | [optional] 
**sockets_replicated** | **int** | The number of sockets replicated by this job. | 
**source_bytes_recovered** | **int** | The number of bytes recovered on the source. | 
**source_directories_created** | **int** | The number of directories created on the source. | 
**source_directories_deleted** | **int** | The number of directories deleted on the source. | 
**source_directories_linked** | **int** | The number of directories linked on the source. | 
**source_directories_unlinked** | **int** | The number of directories unlinked on the source. | 
**source_directories_visited** | **int** | The number of directories visited on the source. | 
**source_files_deleted** | **int** | The number of files deleted on the source. | 
**source_files_linked** | **int** | The number of files linked on the source. | 
**source_files_unlinked** | **int** | The number of files unlinked on the source. | 
**source_host** | **str** | Hostname or IP address of sync source cluster. | 
**sparse_data_bytes** | **int** | The number of sparse data bytes transferred by this job. | 
**start_time** | **int** | The time the job started in unix epoch seconds. The field is null if the job hasn&#39;t started. | [optional] 
**state** | **str** | The state of the job. | 
**subreport_count** | **int** | The number of subreports that are available for this job report. | 
**succeeded_chunks** | **int** | The number of data chunks that have been transmitted successfully. | 
**symlinks_replicated** | **int** | The number of symlinks replicated by this job. | 
**sync_type** | **str** | The type of sync being performed by this job. | 
**target_bytes_recovered** | **int** | The number of bytes recovered on the target. | 
**target_directories_created** | **int** | The number of directories created on the target. | 
**target_directories_deleted** | **int** | The number of directories deleted on the target. | 
**target_directories_linked** | **int** | The number of directories linked on the target. | 
**target_directories_unlinked** | **int** | The number of directories unlinked on the target. | 
**target_files_deleted** | **int** | The number of files deleted on the target. | 
**target_files_linked** | **int** | The number of files linked on the target. | 
**target_files_unlinked** | **int** | The number of files unlinked on the target. | 
**target_path** | **str** | Absolute filesystem path on the target cluster for the sync destination. | 
**target_snapshots** | **list[str]** | The target snapshots created by this job. | 
**throughput** | **str** | Throughput of a job | [optional] 
**total_chunks** | **int** | The total number of data chunks transmitted by this job. | 
**total_data_bytes** | **int** | The total number of bytes transferred by this job. | 
**total_exported_services** | **int** | The total number of components exported as part of service replication. | [optional] 
**total_files** | **int** | The number of files affected by this job. | 
**total_network_bytes** | **int** | The total number of bytes sent over the network by this job. | 
**total_phases** | **int** | The total number of phases for this job. | 
**unchanged_data_bytes** | **int** | The number of bytes unchanged by this job. | 
**up_to_date_files_skipped** | **int** | The number of up-to-date files skipped by this job. | 
**updated_files_replicated** | **int** | The number of updated files replicated by this job. | 
**user_conflict_files_skipped** | **int** | The number of files with user conflicts skipped by this job. | 
**warnings** | **list[str]** | A list of warning messages for this job. | 
**worm_committed_file_conflicts** | **int** | The number of WORM committed files which needed to be reverted. Since WORM committed files cannot be reverted, this is the number of files that were preserved in the compliance store. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


