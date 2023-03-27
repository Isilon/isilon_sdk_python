# UpgradeCluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_overview** | [**UpgradeClusterClusterOverview**](UpgradeClusterClusterOverview.md) | The cluster overview of an upgrade process. | [optional] 
**cluster_state** | **str** | The different states of an upgrade, rollback, or assessment. One of the following values: &#39;committed&#39;, &#39;upgraded&#39;, &#39;partially upgraded&#39;, &#39;upgrading&#39;, &#39;rolling back&#39;, &#39;assessing&#39;, &#39;error&#39; | [optional] 
**committed_features** | [**UpgradeClusterCommittedFeatures**](UpgradeClusterCommittedFeatures.md) | The feature set supported as of the most recent upgrade commit. | [optional] 
**current_process** | **str** | The current upgrade activity. | [optional] 
**finish_time** | **str** | The time when a rollback, assessment or upgrade has finished completely. Use ISO 8601 standard. Null if the cluster_state is not &#39;upgraded&#39;. | [optional] 
**fw_pkg** | **str** | The location (path) of the firmware package which must be within /ifs. | [optional] 
**fw_pkg_id** | **str** | The ID of the signed artifact stored in the catalog. | [optional] 
**install_image_path** | **str** | The location (path) of the upgrade image which must be within /ifs. Null if the cluster_state is &#39;committed&#39; or &#39;upgraded.&#39; | [optional] 
**node_median_time** | **int** | The median time (seconds) to complete each node so far during this upgrade. Before the first node in an upgrade has completed this key will have an associated null value. | [optional] 
**onefs_version_current** | [**ClusterNodesOnefsVersion**](ClusterNodesOnefsVersion.md) | The current OneFS version before upgrade. | [optional] 
**onefs_version_upgrade** | [**ClusterNodesOnefsVersion**](ClusterNodesOnefsVersion.md) | The OneFS version the user is attempting to upgrade to. Null if the cluster_state is &#39;committed&#39; or &#39;assessing.&#39; | [optional] 
**patch_action** | **str** | The most recent patch action performed. | [optional] 
**patch_name** | **str** | The patch with the most recent patch action. | [optional] 
**start_time** | **str** | The time when an upgrade, rollback, or assessment was started. Use ISO 8601 standard. Null if the cluster_state is &#39;committed&#39; or &#39;partially upgraded.&#39; | [optional] 
**upgrade_is_committed** | **bool** | True if upgrade is committed. | [optional] 
**upgrade_process_state** | **str** | The different states of upgrade process. One of the following values: &#39;Not started&#39;, &#39;Running&#39;, &#39;Pausing&#39;, &#39;Paused&#39;.  | [optional] 
**upgrade_settings** | [**UpgradeClusterUpgradeSettings**](UpgradeClusterUpgradeSettings.md) | The settings necessary when starting an upgrade. Null if the cluster_state is not &#39;upgrading&#39; or &#39;partially upgraded.&#39; or &#39;error&#39;. | [optional] 
**upgrade_triggered_time** | **str** | Time at which upgrade was originally requested. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


