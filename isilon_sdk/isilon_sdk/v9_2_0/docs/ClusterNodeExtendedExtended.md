# ClusterNodeExtendedExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **int** | Unique identifier for the failure domain that thisnode resides in. Within a given domain, nodes are rebooted 1 at a time. The actual value is meaningless, it is merely used to group nodes by failure domain. | [optional] 
**error** | [**ClusterNodesError**](ClusterNodesError.md) | The current OneFS version before upgrade. | [optional] 
**last_action** | **str** | The last action performed to completion/failure on this node.  Null if the node_state is &#39;committed&#39; or &#39;assessing.&#39; One of the following values: &#39;upgrade&#39;, &#39;rollback&#39;. | [optional] 
**last_action_result** | **str** | Did the node pass upgrade or rollback without failing? Null if the node_state is &#39;committed.&#39; One of the following values: &#39;pass&#39;, &#39;fail&#39;, null | [optional] 
**lnn** | **int** | The lnn of the node. | [optional] 
**node_state** | **str** | \\e The state of the node during the upgrade, rollback, or assessment. One of the following values: &#39;committed&#39;, &#39;upgraded&#39;, &#39;upgrading&#39;, &#39;rolling back&#39;, &#39;assessing&#39;, &#39;error&#39; | [optional] 
**onefs_version** | [**ClusterNodesOnefsVersion**](ClusterNodesOnefsVersion.md) | The current OneFS version before upgrade. | [optional] 
**progress** | **int** | What step is the upgrade, assessment, or rollback in? To show via progress indicator. NOTE: the value is an integer between 0 and 100 (percent) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


