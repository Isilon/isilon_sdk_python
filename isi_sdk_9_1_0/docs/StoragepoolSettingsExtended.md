# StoragepoolSettingsExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatically_manage_io_optimization** | **str** | Automatically manage IO optimization settings on files. | [optional] 
**automatically_manage_protection** | **str** | Automatically manage protection settings on files. | [optional] 
**global_namespace_acceleration_enabled** | **bool** | Optimize namespace operations by storing metadata on SSDs. | [optional] 
**protect_directories_one_level_higher** | **bool** | Automatically add additional protection level to all directories. | [optional] 
**spillover_enabled** | **bool** | Spill writes into other pools as needed. | [optional] 
**spillover_target** | [**StoragepoolSettingsSpilloverTarget**](StoragepoolSettingsSpilloverTarget.md) | Target pool for spilled writes. | [optional] 
**ssd_l3_cache_default_enabled** | **bool** | The L3 Cache default enabled state. This specifies whether L3 Cache should be enabled on new node pools | [optional] 
**ssd_qab_mirrors** | **str** | Controls number of mirrors of QAB blocks to place on SSDs. | [optional] 
**ssd_system_btree_mirrors** | **str** | Controls number of mirrors of system B-tree blocks to place on SSDs. | [optional] 
**ssd_system_delta_mirrors** | **str** | Controls number of mirrors of system delta blocks to place on SSDs. | [optional] 
**virtual_hot_spare_deny_writes** | **bool** | Deny writes into reserved virtual hot spare space. | [optional] 
**virtual_hot_spare_hide_spare** | **bool** | Hide reserved virtual hot spare space from free space counts. | [optional] 
**virtual_hot_spare_limit_drives** | **int** | The number of drives to reserve for the virtual hot spare, from 0-4. | [optional] 
**virtual_hot_spare_limit_percent** | **int** | The percent space to reserve for the virtual hot spare, from 0-20. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


