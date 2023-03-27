# ClusterFirmwareUpgradeItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_timeout** | **int** | The duration in seconds after drain begins that an alert will be raised. An alert timeout must be set to a smaller value than the drain timeout to be used. If not specified, an alert will not be raised (legacy behavior). | [optional] 
**drain_timeout** | **int** | The duration in seconds that upgrade waits for all SMB clients to disconnect from a node before rebooting it. A value of 0 means wait indefinitely. If not specified, upgrade proceeds with reboots regardless of SMB client connections (legacy behavior). | [optional] 
**exclude_device** | **str** | Exclude the specified devices in the firmware upgrade. | [optional] 
**exclude_type** | **str** | Exclude the specified device type in the firmware upgrade. | [optional] 
**fw_pkg** | **str** | The location (path) of the firmware package which must be within /ifs. | [optional] 
**include_device** | **str** | Include the specified devices in the firmware upgrade. | [optional] 
**include_type** | **str** | Include the specified device type in the firmware upgrade. | [optional] 
**no_burn** | **bool** | Do not burn the firmware. | [optional] 
**no_reboot** | **bool** | Do not reboot the node after an upgrade | [optional] 
**nodes_to_upgrade** | **list[int]** | The nodes scheduled for upgrade. Order in array determines queue position number. &#39;all&#39; and null option will upgrade firmware on all nodes in &lt;lnn&gt; order (Note: &#39;all&#39; and null options do not apply to simultaneous firmware upgrade). | [optional] 
**upgrade_type** | **str** | The type of upgrade to perform. One of the following values: &#39;rolling&#39;, &#39;simultaneous, parallel&#39; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


