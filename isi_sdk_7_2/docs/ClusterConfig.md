# ClusterConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Customer configurable description. | 
**devices** | [**list[ClusterConfigDevice]**](ClusterConfigDevice.md) |  | 
**encoding** | **str** | Default encoding. | 
**guid** | **str** | Cluster GUID. | 
**is_compliance** | **bool** | If true, the cluster is in compliance mode.  Compliance mode clusters do not allow root access and have stricter WORM (Write Once Read Many) features for retaining data in compliance with U.S. Securities and Exchange Commission rule 17a-4. | 
**is_rolling_upgrade** | **bool** | If true, the cluster is currently performing a rolling upgrade. | 
**join_mode** | **str** | Node join mode: &#39;manual&#39;, &#39;automatic&#39;, or &#39;secure&#39;. | 
**local_devid** | **int** | Device ID of the queried node. | 
**local_lnn** | **int** | Device logical node number of the queried node. | 
**local_serial** | **str** | Device serial number of the queried node. | 
**name** | **str** | Cluster name. | 
**onefs_version** | [**ClusterConfigOnefsVersion**](ClusterConfigOnefsVersion.md) |  | 
**timezone** | [**ClusterConfigTimezone**](ClusterConfigTimezone.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


