# ClusterConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Customer configurable description. | 
**devices** | [**list[ClusterConfigDevice]**](ClusterConfigDevice.md) |  | 
**encoding** | **str** | Default encoding. | 
**guid** | **str** | Cluster GUID. | 
**has_quorum** | **bool** | If true, the local node is in a group with quorum: It is communicating, storing, and protecting data normally with other nodes in its group.  Under normal circumstances, every node in the cluster is part of one group. | 
**is_compliance** | **bool** | If true, the cluster is in compliance mode.  Compliance mode clusters do not allow root access and have stricter WORM (Write Once Read Many) features for retaining data in compliance with U.S. Securities and Exchange Commission rule 17a-4. | 
**is_virtual** | **bool** | true if the cluster is deployed on a desktop VMWorkstation | 
**is_vonefs** | **bool** | true if this is a vOneFS cluster on an ESXi | 
**join_mode** | **str** | Node join mode: &#39;manual&#39; or &#39;secure&#39;. | 
**local_devid** | **int** | Device ID of the queried node. | 
**local_lnn** | **int** | Device logical node number of the queried node. | 
**local_serial** | **str** | Device serial number of the queried node. | 
**name** | **str** | Cluster name. | 
**onefs_version** | [**ClusterConfigOnefsVersion**](ClusterConfigOnefsVersion.md) |  | [optional] 
**timezone** | [**ClusterConfigTimezone**](ClusterConfigTimezone.md) | The cluster timezone settings. | [optional] 
**upgrade_type** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


