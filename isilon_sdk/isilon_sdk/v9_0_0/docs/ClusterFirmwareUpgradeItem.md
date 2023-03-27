# ClusterFirmwareUpgradeItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_device** | **str** | Exclude the specified devices in the firmware upgrade. | [optional] 
**exclude_type** | **str** | Exclude the specified device type in the firmware upgrade. | [optional] 
**fw_pkg** | **str** | The location (path) of the firmware package which must be within /ifs. | 
**include_device** | **str** | Include the specified devices in the firmware upgrade. | [optional] 
**include_type** | **str** | Include the specified device type in the firmware upgrade. | [optional] 
**no_burn** | **bool** | Do not burn the firmware. | [optional] 
**no_reboot** | **bool** | Do not reboot the node after an upgrade | [optional] 
**nodes_to_upgrade** | **list[int]** | The nodes scheduled for upgrade. Order in array determines queue position number. &#39;all&#39; and null option will upgrade firmware on all nodes in &lt;lnn&gt; order (Note: &#39;all&#39; and null options do not apply to simultaneous firmware upgrade). | [optional] 
**simultaneous** | **bool** | Upgrade Firmware on multiple nodes concurrently | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


