# SyncSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth_reservation_reserve_absolute** | **int** | The amount of SyncIQ bandwidth to reserve in kb/s for policies that did not specify a bandwidth reservation. This field takes precedence over bandwidth_reservation_reserve_percentage. | [optional] 
**bandwidth_reservation_reserve_percentage** | **int** | The percentage of SyncIQ bandwidth to reserve for policies that did not specify a bandwidth reservation. | [optional] 
**cluster_certificate_id** | **str** | The ID of this cluster&#39;s certificate being used for encryption. | [optional] 
**encryption_cipher_list** | **str** | The cipher list being used with encryption. For SyncIQ targets, this list serves as a list of supported ciphers. For SyncIQ sources, the list of ciphers will be attempted to be used in order. | [optional] 
**encryption_required** | **bool** | If true, requires all SyncIQ policies to utilize encrypted communications. | [optional] 
**force_interface** | **bool** | NOTE: This field should not be changed without the help of Isilon support.  Default for the \&quot;force_interface\&quot; property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  Determines whether data is sent only through the subnet and pool specified in the \&quot;source_network\&quot; field. This option can be useful if there are multiple interfaces for the given source subnet. | [optional] 
**max_concurrent_jobs** | **int** | The max concurrent jobs that SyncIQ can support. This number is based on the size of the current cluster and the current SyncIQ worker throttle rule. | [optional] 
**ocsp_address** | **str** | The address of the OCSP responder to which to connect. | [optional] 
**ocsp_issuer_certificate_id** | **str** | The ID of the certificate authority that issued the certificate whose revocation status is being checked. | [optional] 
**renegotiation_period** | **int** | If specified, the duration to persist encrypted connection before forcing a renegotiation. | [optional] 
**report_email** | **list[str]** | Email sync reports to these addresses. | [optional] 
**report_max_age** | **int** | The default length of time (in seconds) a policy report will be stored. | [optional] 
**report_max_count** | **int** | The default maximum number of reports to retain for a policy. | [optional] 
**restrict_target_network** | **bool** | Default for the \&quot;restrict_target_network\&quot; property that will be applied to each new sync policy unless otherwise specified at the time of policy creation.  If you specify true, and you specify a SmartConnect zone in the \&quot;target_host\&quot; field, replication policies will connect only to nodes in the specified SmartConnect zone.  If you specify false, replication policies are not restricted to specific nodes on the target cluster. | [optional] 
**rpo_alerts** | **bool** | If disabled, no RPO alerts will be generated. | [optional] 
**service** | **str** | Specifies if the SyncIQ service currently on, paused, or off.  If paused, all sync jobs will be paused.  If turned off, all jobs will be canceled. | [optional] 
**service_history_max_age** | **int** | Maximum age of service information to maintain, in seconds. | [optional] 
**service_history_max_count** | **int** | Maximum number of historical service information records to maintain. | [optional] 
**source_network** | [**SyncPolicySourceNetwork**](SyncPolicySourceNetwork.md) | Restricts replication policies on the local cluster to running on the specified subnet and pool. | [optional] 
**tw_chkpt_interval** | **int** | The interval (in seconds) in which treewalk syncs are forced to checkpoint. | [optional] 
**use_workers_per_node** | **bool** | If enabled, SyncIQ will use the deprecated workers_per_node field with worker pools functionality and limit workers accordingly. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


