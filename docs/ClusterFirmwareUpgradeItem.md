# ClusterFirmwareUpgradeItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_device** | **str** | Exclude the specified devices in the firmware upgrade. | [optional] 
**exclude_type** | **str** | Include the specified device type in the firmware upgrade. | [optional] 
**include_device** | **str** | Include the specified devices in the firmware upgrade. | [optional] 
**include_type** | **str** | Include the specified device type in the firmware upgrade. | [optional] 
**no_burn** | **bool** | Do not burn the firmware. | [optional] 
**no_reboot** | **bool** | Do not reboot the node after an upgrade | [optional] 
**no_verify** | **bool** | Do not verify the firmware upgrade after an upgrade. | [optional] 
**nodes_to_upgrade** | **list[int]** | The nodes scheduled for upgrade. Order in array determines queue position number. &#39;All&#39; and null option will upgrade all nodes in &lt;lnn&gt; order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


