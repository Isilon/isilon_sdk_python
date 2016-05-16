# StoragepoolSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatically_manage_io_optimization** | **str** | Automatically manage IO optimization settings on files. | 
**automatically_manage_protection** | **str** | Automatically manage protection settings on files. | 
**global_namespace_acceleration_enabled** | **bool** | Optimize namespace operations by storing metadata on SSDs. | 
**global_namespace_acceleration_state** | **str** | Whether or not namespace operation optimizations are currently in effect. | 
**protect_directories_one_level_higher** | **bool** | Automatically add additional protection level to all directories. | 
**spillover_enabled** | **bool** | Spill writes into other pools as needed. | 
**spillover_target** | [**StoragepoolSettingsSettingsSpilloverTarget**](StoragepoolSettingsSettingsSpilloverTarget.md) | Target pool for spilled writes. | 
**ssd_l3_cache_default_enabled** | **bool** | The L3 Cache default enabled state. This specifies whether L3 Cache should be enabled on new node pools. | 
**virtual_hot_spare_deny_writes** | **bool** | Deny writes into reserved virtual hot spare space. | 
**virtual_hot_spare_hide_spare** | **bool** | Hide reserved virtual hot spare space from free space counts. | 
**virtual_hot_spare_limit_drives** | **int** | The number of drives to reserve for the virtual hot spare, from 0-4. | 
**virtual_hot_spare_limit_percent** | **int** | The percent space to reserve for the virtual hot spare, from 0-20. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


