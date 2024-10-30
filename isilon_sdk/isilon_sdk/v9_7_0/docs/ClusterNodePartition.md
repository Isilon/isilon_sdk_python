# ClusterNodePartition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_size** | **int** | The block size used for the reported partition information. | [optional] 
**capacity** | **int** | Total blocks on this file system partition. | [optional] 
**component_devices** | **str** | Comma separated list of devices used for this file system partition. | [optional] 
**mount_point** | **str** | Directory on which this partition is mounted. | [optional] 
**percent_used** | **str** | Used blocks on this file system partition, expressed as a percentage. | [optional] 
**statfs** | [**ClusterNodePartitionStatfs**](ClusterNodePartitionStatfs.md) | System partition details as provided by statfs(2). | [optional] 
**used** | **int** | Used blocks on this file system partition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


