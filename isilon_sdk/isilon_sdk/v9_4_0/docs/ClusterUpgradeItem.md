# ClusterUpgradeItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_timeout** | **int** | The duration in seconds after drain begins that an alert will be raised. An alert timeout must be set to a smaller value than the drain timeout to be used. If not specified, an alert will not be raised (legacy behavior). | [optional] 
**drain_timeout** | **int** | The duration in seconds that upgrade waits for all SMB clients to disconnect from a node before rebooting it. A value of 0 means wait indefinitely. If not specified, upgrade proceeds with reboots regardless of SMB client connections (legacy behavior). | [optional] 
**exclude_device** | **str** | Exclude the specified devices in the firmware upgrade. | [optional] 
**exclude_type** | **str** | Exclude the specified device type in the firmware upgrade. | [optional] 
**fw_pkg** | **str** | The location (path) of the firmware package which must be within /ifs. | [optional] 
**fw_pkg_id** | **str** | The ID of the signed artifact stored in the catalog. | [optional] 
**include_device** | **str** | Include the specified devices in the firmware upgrade. | [optional] 
**include_type** | **str** | Include the specified device type in the firmware upgrade. | [optional] 
**install_image_id** | **str** | The ID of the signed artifact stored in the catalog. | [optional] 
**install_image_path** | **str** | The location (path) of the upgrade image which must be within /ifs. | [optional] 
**no_burn** | **bool** | Do not burn the firmware. | [optional] 
**nodes_to_rolling_upgrade** | **list[int]** | The nodes (to be) scheduled for upgrade ordered by queue position number. Null if the cluster_state is &#39;partially upgraded&#39; or upgrade_type is &#39;simultaneous&#39;. One of the following values: [&lt;lnn-1&gt;, &lt;lnn-2&gt;, ... ], &#39;all&#39;, null | [optional] 
**patch_paths** | **list[str]** | List of additional patches to install during the upgrade. | [optional] 
**skip_optional** | **bool** | Used to indicate that the pre-upgrade check should be skipped. | [optional] 
**upgrade_type** | **str** | The type of upgrade to perform. One of the following values: &#39;rolling&#39;, &#39;simultaneous, parallel&#39; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


