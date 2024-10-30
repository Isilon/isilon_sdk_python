# TargetPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failover_failback_state** | **str** | The condition of this policy with respect to sync failover/failback. | 
**id** | **str** | The system ID given to this sync policy. | 
**last_job_state** | **str** | The state of the last job run for this policy. | 
**last_source_coordinator_ip** | **str** | The IP address from which a SyncIQ coordinator daemon most recently connected to this cluster to update it about the progress of a job for this policy. | 
**last_update_from_source** | **int** | The last time this cluster was updated with sync information from the source cluster for this policy, in unix epoch seconds.  Null if no such update has occurred yet. | [optional] 
**legacy_policy** | **bool** | Was this policy defined by a OneFS version earlier than 6.0? (Pre-6.0 policies did not have the target policy concept and canceling from the target side will not be available.) | 
**name** | **str** | User-assigned name of this sync policy. | 
**source_cluster_guid** | **str** | Unique identifier for the source cluster. | 
**source_host** | **str** | Hostname or IP address of sync source cluster. | 
**target_path** | **str** | Absolute filesystem path on the target cluster for the sync destination. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


