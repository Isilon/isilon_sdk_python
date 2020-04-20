# SyncPolicyExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerated_failback** | **bool** | If set to true, SyncIQ will perform failback configuration tasks during the next job run, rather than waiting to perform those tasks during the failback process. Performing these tasks ahead of time will increase the speed of failback operations. | [optional] 
**action** | **str** | If &#39;copy&#39;, source files will be copied to the target cluster.  If &#39;sync&#39;, the target directory will be made an image of the source directory:  Files and directories that have been deleted on the source, have been moved within the target directory, or no longer match the selection criteria will be deleted from the target directory. | [optional] 
**bandwidth_reservation** | **int** | The desired bandwidth reservation for this policy in kb/s. This feature will not activate unless a SyncIQ bandwidth rule is in effect. | [optional] 
**changelist** | **bool** | If true, retain previous source snapshot and incremental repstate, both of which are required for changelist creation. | [optional] 
**check_integrity** | **bool** | If true, the sync target performs cyclic redundancy checks (CRC) on the data as it is received. | [optional] 
**cloud_deep_copy** | **str** | If set to deny, replicates all CloudPools smartlinks to the target cluster as smartlinks; if the target cluster does not support the smartlinks, the job will fail. If set to force, replicates all smartlinks to the target cluster as regular files. If set to allow, SyncIQ will attempt to replicate smartlinks to the target cluster as smartlinks; if the target cluster does not support the smartlinks, SyncIQ will replicate the smartlinks as regular files. | [optional] 
**conflicted** | **bool** | NOTE: This field should not be changed without the help of Isilon support.  If true, the most recent run of this policy encountered an error and this policy will not start any more scheduled jobs until this field is manually set back to &#39;false&#39;. | [optional] 
**database_mirrored** | **bool** | If true, SyncIQ databases have been mirrored. | [optional] 
**delete_quotas** | **bool** | If true, forcibly remove quotas on the target after they have been removed on the source. | [optional] 
**description** | **str** | User-assigned description of this sync policy. | [optional] 
**disable_file_split** | **bool** | NOTE: This field should not be changed without the help of Isilon support.  If true, the 7.2+ file splitting capability will be disabled. | [optional] 
**disable_fofb** | **bool** | NOTE: This field should not be changed without the help of Isilon support.  Enable/disable sync failover/failback. | [optional] 
**disable_quota_tmp_dir** | **bool** | If set to true, SyncIQ will not create temporary quota directories to aid in replication to target paths which contain quotas. | [optional] 
**disable_stf** | **bool** | NOTE: This field should not be changed without the help of Isilon support.  Enable/disable the 6.5+ STF based data transfer and uses only treewalk. | [optional] 
**enable_hash_tmpdir** | **bool** | If true, syncs will use temporary working directory subdirectories to reduce lock contention. | [optional] 
**enabled** | **bool** | If true, jobs will be automatically run based on this policy, according to its schedule. | 
**encrypted** | **bool** | If true, syncs will be encrypted. | [optional] 
**encryption_cipher_list** | **str** | The cipher list being used with encryption. For SyncIQ targets, this list serves as a list of supported ciphers. For SyncIQ sources, the list of ciphers will be attempted to be used in order. | [optional] 
**expected_dataloss** | **bool** | NOTE: This field should not be changed without the help of Isilon support.  Continue sending files even with the corrupted filesystem. | [optional] 
**file_matching_pattern** | [**SyncJobPolicyFileMatchingPattern**](SyncJobPolicyFileMatchingPattern.md) | A file matching pattern, organized as an OR&#39;ed set of AND&#39;ed file criteria, for example ((a AND b) OR (x AND y)) used to define a set of files with specific properties.  Policies of type &#39;sync&#39; cannot use &#39;path&#39; or time criteria in their matching patterns, but policies of type &#39;copy&#39; can use all listed criteria. | [optional] 
**force_interface** | **bool** | NOTE: This field should not be changed without the help of Isilon support.  Determines whether data is sent only through the subnet and pool specified in the \&quot;source_network\&quot; field. This option can be useful if there are multiple interfaces for the given source subnet.  If you enable this option, the net.inet.ip.choose_ifa_by_ipsrc sysctl should be set. | [optional] 
**has_sync_state** | **bool** | This field is false if the policy is in its initial sync state and true otherwise.  Setting this field to false will reset the policy&#39;s sync state. | [optional] 
**id** | **str** | The system ID given to this sync policy. | 
**job_delay** | **int** | If --schedule is set to When-Source-Modified, the duration to wait after a modification is made before starting a job (default is 0 seconds). | [optional] 
**last_job_state** | **str** | This is the state of the most recent job for this policy. | [optional] 
**last_started** | **int** | The most recent time a job was started for this policy.  Value is null if the policy has never been run. | [optional] 
**last_success** | **int** | Timestamp of last known successfully completed synchronization.  Value is null if the policy has never completed successfully. | [optional] 
**linked_service_policies** | **list[str]** | A list of service replication policies that this data replication policy will be associated with. | [optional] 
**log_level** | **str** | Severity an event must reach before it is logged. | [optional] 
**log_removed_files** | **bool** | If true, the system will log any files or directories that are deleted due to a sync. | [optional] 
**name** | **str** | User-assigned name of this sync policy. | 
**next_run** | **int** | This is the next time a job is scheduled to run for this policy in Unix epoch seconds.  This field is null if the job is not scheduled. | [optional] 
**ocsp_address** | **str** | The address of the OCSP responder to which to connect. | [optional] 
**ocsp_issuer_certificate_id** | **str** | The ID of the certificate authority that issued the certificate whose revocation status is being checked. | [optional] 
**password_set** | **bool** | Indicates if a password is set for accessing the target cluster. Password value is not shown with GET. | [optional] 
**priority** | **int** | Determines the priority level of a policy. Policies with higher priority will have precedence to run over lower priority policies. Valid range is [0, 1]. Default is 0. | [optional] 
**report_max_age** | **int** | Length of time (in seconds) a policy report will be stored. | [optional] 
**report_max_count** | **int** | Maximum number of policy reports that will be stored on the system. | [optional] 
**restrict_target_network** | **bool** | If you specify true, and you specify a SmartConnect zone in the \&quot;target_host\&quot; field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster. | [optional] 
**rpo_alert** | **int** | If --schedule is set to a time/date, an alert is created if the specified RPO for this policy is exceeded. The default value is 0, which will not generate RPO alerts. | [optional] 
**schedule** | **str** | The schedule on which new jobs will be run for this policy. | 
**service_policy** | **bool** | If true, this is a service replication policy. | [optional] 
**skip_lookup** | **bool** | Skip DNS lookup of target IPs. | [optional] 
**skip_when_source_unmodified** | **bool** | If true and --schedule is set to a time/date, the policy will not run if no changes have been made to the contents of the source directory since the last job successfully completed. | [optional] 
**snapshot_sync_existing** | **bool** | If true, snapshot-triggered syncs will include snapshots taken before policy creation time (requires --schedule when-snapshot-taken). | [optional] 
**snapshot_sync_pattern** | **str** | The naming pattern that a snapshot must match to trigger a sync when the schedule is when-snapshot-taken (default is \&quot;*\&quot;). | [optional] 
**source_certificate_id** | **str** | The ID of the source cluster certificate being used for encryption. | [optional] 
**source_domain_marked** | **bool** | If true, the source root path has been domain marked with a SyncIQ domain. | [optional] 
**source_exclude_directories** | **list[str]** | Directories that will be excluded from the sync.  Modifying this field will result in a full synchronization of all data. | [optional] 
**source_include_directories** | **list[str]** | Directories that will be included in the sync.  Modifying this field will result in a full synchronization of all data. | [optional] 
**source_network** | [**SyncPolicySourceNetwork**](SyncPolicySourceNetwork.md) | Restricts replication policies on the local cluster to running on the specified subnet and pool. | [optional] 
**source_root_path** | **str** | The root directory on the source cluster the files will be synced from.  Modifying this field will result in a full synchronization of all data. | 
**source_snapshot_archive** | **bool** | If true, archival snapshots of the source data will be taken on the source cluster before a sync. | [optional] 
**source_snapshot_expiration** | **int** | The length of time in seconds to keep snapshots on the source cluster. | [optional] 
**source_snapshot_pattern** | **str** | The name pattern for snapshots taken on the source cluster before a sync. | [optional] 
**target_certificate_id** | **str** | The ID of the target cluster certificate being used for encryption. | [optional] 
**target_compare_initial_sync** | **bool** | If true, the target creates diffs against the original sync. | [optional] 
**target_detect_modifications** | **bool** | If true, target cluster will detect if files have been changed on the target by legacy tree walk syncs. | [optional] 
**target_host** | **str** | Hostname or IP address of sync target cluster.  Modifying the target cluster host can result in the policy being unrunnable if the new target does not match the current target association. | 
**target_path** | **str** | Absolute filesystem path on the target cluster for the sync destination. | 
**target_snapshot_alias** | **str** | The alias of the snapshot taken on the target cluster after the sync completes. A value of @DEFAULT will reset this field to the default creation value. | [optional] 
**target_snapshot_archive** | **bool** | If true, archival snapshots of the target data will be taken on the target cluster after successful sync completions. | [optional] 
**target_snapshot_expiration** | **int** | The length of time in seconds to keep snapshots on the target cluster. | [optional] 
**target_snapshot_pattern** | **str** | The name pattern for snapshots taken on the target cluster after the sync completes.  A value of @DEFAULT will reset this field to the default creation value. | [optional] 
**workers_per_node** | **int** | The number of worker threads on a node performing a sync. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


