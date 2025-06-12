# SyncJobCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be taken by this job. | [optional] 
**id** | **str** | The ID or Name of the policy | 
**log_level** | **str** | Only valid for allow_write, and allow_write_revert; specify the desired logging level, will be stored in the logs for isi_migrate, defaults to &#39;info&#39;. | [optional] 
**service_policy** | **bool** | If true, this is a service replication policy. | [optional] 
**skip_copy** | **bool** | Skips the copy phase of the service replication allow-write operation. | [optional] 
**skip_failover** | **bool** | Skips the data failover phase of the service replication allow-write operation. | [optional] 
**skip_map** | **bool** | Skips the mapping phase of the service replication allow-write operation. | [optional] 
**source_snapshot** | **str** | An optional snapshot to copy/sync from. | [optional] 
**tgt_path** | **str** | Specifies the directory to output the service replication files for restoration. | [optional] 
**timestamp** | **int** | Specifies the timestamp of a service replication policy backup to restore from. | [optional] 
**workers_per_node** | **int** | Only valid for allow_write, and allow_write_revert; specify the desired workers per node, defaults to 3. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


