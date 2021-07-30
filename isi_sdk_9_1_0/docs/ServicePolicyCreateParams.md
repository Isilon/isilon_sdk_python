# ServicePolicyCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accelerated_failback** | **bool** | If set to true, SyncIQ will perform failback configuration tasks during the next job run, rather than waiting to perform those tasks during the failback process. Performing these tasks ahead of time will increase the speed of failback operations. | [optional] 
**bandwidth_reservation** | **int** | The desired bandwidth reservation for this policy in kb/s. This feature will not activate unless a SyncIQ bandwidth rule is in effect. | [optional] 
**check_integrity** | **bool** | If true, the sync target performs cyclic redundancy checks (CRC) on the data as it is received. | [optional] 
**description** | **str** | User-assigned description of this sync policy. | [optional] 
**disable_file_split** | **bool** | NOTE: This field should not be changed without the help of PowerScale support.  If true, the 7.2+ file splitting capability will be disabled. | [optional] 
**disable_fofb** | **bool** | NOTE: This field should not be changed without the help of PowerScale support.  Enable/disable sync failover/failback. | [optional] 
**disable_quota_tmp_dir** | **bool** | If set to true, SyncIQ will not create temporary quota directories to aid in replication to target paths which contain quotas. | [optional] 
**enabled** | **bool** | If true, jobs will be automatically run based on this policy, according to its schedule. | [optional] 
**encryption_cipher_list** | **str** | The cipher list being used with encryption. For SyncIQ targets, this list serves as a list of supported ciphers. For SyncIQ sources, the list of ciphers will be attempted to be used in order. | [optional] 
**expected_dataloss** | **bool** | NOTE: This field should not be changed without the help of PowerScale support.  Continue sending files even with the corrupted filesystem. | [optional] 
**force_interface** | **bool** | NOTE: This field should not be changed without the help of PowerScale support.  Determines whether data is sent only through the subnet and pool specified in the \&quot;source_network\&quot; field. This option can be useful if there are multiple interfaces for the given source subnet.  If you enable this option, the net.inet.ip.choose_ifa_by_ipsrc sysctl should be set. | [optional] 
**linked_data_policies** | **list[str]** | A list of SyncIQ policy names/IDs whose source root directories will be used to filter service replication. | [optional] 
**log_level** | **str** | Severity an event must reach before it is logged. | [optional] 
**name** | **str** | User-assigned name of this sync policy. | 
**ocsp_address** | **str** | The address of the OCSP responder to which to connect. | [optional] 
**ocsp_issuer_certificate_id** | **str** | The ID of the certificate authority that issued the certificate whose revocation status is being checked. | [optional] 
**password** | **str** | The password for the target cluster.  This field is not readable. | [optional] 
**priority** | **int** | Determines the priority level of a policy. Policies with higher priority will have precedence to run over lower priority policies. Valid range is [0, 1]. Default is 0. | [optional] 
**replicated_services** | **list[str]** | A list of services to replicate. | [optional] 
**report_max_age** | **int** | Length of time (in seconds) a policy report will be stored. | [optional] 
**report_max_count** | **int** | Maximum number of policy reports that will be stored on the system. | [optional] 
**restrict_target_network** | **bool** | If you specify true, and you specify a SmartConnect zone in the \&quot;target_host\&quot; field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster. | [optional] 
**rpo_alert** | **int** | If --schedule is set to a time/date, an alert is created if the specified RPO for this policy is exceeded. The default value is 0, which will not generate RPO alerts. | [optional] 
**schedule** | **str** | The schedule on which new jobs will be run for this policy. | [optional] 
**service_history_max_age** | **int** | Maximum age of service information to maintain, in seconds. | [optional] 
**service_history_max_count** | **int** | Maximum number of historical service information records to maintain. | [optional] 
**skip_lookup** | **bool** | Skip DNS lookup of target IPs. | [optional] 
**snapshot_sync_existing** | **bool** | If true, snapshot-triggered syncs will include snapshots taken before policy creation time (requires --schedule when-snapshot-taken). | [optional] 
**snapshot_sync_pattern** | **str** | The naming pattern that a snapshot must match to trigger a sync when the schedule is when-snapshot-taken (default is \&quot;*\&quot;). | [optional] 
**source_network** | [**SyncPolicySourceNetwork**](SyncPolicySourceNetwork.md) | Restricts replication policies on the local cluster to running on the specified subnet and pool. | [optional] 
**source_snapshot_expiration** | **int** | The length of time in seconds to keep snapshots on the source cluster. | [optional] 
**source_snapshot_pattern** | **str** | The name pattern for snapshots taken on the source cluster before a sync. | [optional] 
**target_certificate_id** | **str** | The ID of the target cluster certificate being used for encryption. | [optional] 
**target_host** | **str** | Hostname or IP address of sync target cluster.  Modifying the target cluster host can result in the policy being unrunnable if the new target does not match the current target association. | 
**target_snapshot_alias** | **str** | The alias of the snapshot taken on the target cluster after the sync completes. A value of @DEFAULT will reset this field to the default creation value. | [optional] 
**target_snapshot_expiration** | **int** | The length of time in seconds to keep snapshots on the target cluster. | [optional] 
**target_snapshot_pattern** | **str** | The name pattern for snapshots taken on the target cluster after the sync completes.  A value of @DEFAULT will reset this field to the default creation value. | [optional] 
**workers_per_node** | **int** | The number of worker threads on a node performing a sync. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


