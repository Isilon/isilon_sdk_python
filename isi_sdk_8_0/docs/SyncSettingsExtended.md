# SyncSettingsExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**burst_memory_constraint** | **int** | The per-worker burst socket memory constraint, in bytes. | [optional] 
**burst_socket_buffer_size** | **int** | The per-worker burst socket buffer coalesced data, in bytes. | [optional] 
**force_interface** | **bool** | NOTE: This field should not be changed without the help of Isilon support.  Default for the \&quot;force_interface\&quot; property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \&quot;source_network\&quot; field. This option can be useful if there are multiple interfaces for the given source subnet. | [optional] 
**report_email** | **list[str]** | Email sync reports to these addresses. | [optional] 
**report_max_age** | **int** | The default length of time (in seconds) a policy report will be stored. | [optional] 
**report_max_count** | **int** | The default maximum number of reports to retain for a policy. | [optional] 
**restrict_target_network** | **bool** | Default for the \&quot;restrict_target_network\&quot; property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \&quot;target_host\&quot; field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster. | [optional] 
**rpo_alerts** | **bool** | If disabled, no RPO alerts will be generated. | [optional] 
**service** | **str** | Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled. | [optional] 
**source_network** | [**SyncPolicySourceNetwork**](SyncPolicySourceNetwork.md) | Restricts replication policies on the local cluster to running on the specified subnet and pool. | [optional] 
**tw_chkpt_interval** | **int** | The interval (in seconds) in which treewalk syncs are forced to checkpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


