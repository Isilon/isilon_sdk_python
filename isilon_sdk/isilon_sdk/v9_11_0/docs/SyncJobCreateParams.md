# SyncJobCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be taken by this job. | [optional] 
**id** | **str** | The ID or Name of the policy | 
**log_level** | **str** | Only valid for allow_write, and allow_write_revert; specify the desired logging level, will be stored in the logs for isi_migrate, defaults to &#39;info&#39;. | [optional] 
**source_snapshot** | **str** | An optional snapshot to copy/sync from. | [optional] 
**workers_per_node** | **int** | Only valid for allow_write, and allow_write_revert; specify the desired workers per node, defaults to 3. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


