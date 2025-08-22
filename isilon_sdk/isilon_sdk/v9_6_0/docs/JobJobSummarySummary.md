# JobJobSummarySummary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_is_degraded** | **bool** | Whether the cluster is in a degraded state.  Note this is from the perspective of the node handling the query, which might be different from another node. | 
**connected** | **bool** | Whether isi_job_d instances on all up nodes in the cluster are connected to the coordinator. | 
**coordinator** | **int** | The devid of the job engine coordinator. | 
**coordinator_lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**disconnected_nodes** | **list[int]** | If connected&#x3D;false, this is the set of devids that are not connected to the coordinator. | [optional] 
**down_or_read_only_nodes** | **bool** | Whether the cluster has any down or read-only nodes.  These nodes are not considered in the connected property. | 
**job_d_enabled** | **bool** | Whether the isi_job_d is enabled. | 
**next_jid** | **int** | The job ID to be assigned to the next job. | 
**non_responding_nodes** | **list[int]** | Shows which nodes have not acknowledged the coordinator. | [optional] 
**pp_enabled** | **bool** | Whether Job Engine uses partitioned performance for throttling. | 
**run_degraded** | **bool** | Whether the job engine would allow most jobs to run even when the cluster is in a degraded state. | 
**stats_ready** | **bool** | Whether the coordinator has recently gathered statistics for all nodes in the cluster. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


