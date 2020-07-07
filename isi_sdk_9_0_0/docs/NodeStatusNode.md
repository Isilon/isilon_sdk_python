# NodeStatusNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batterystatus** | [**ClusterNodeStatusBatterystatus**](ClusterNodeStatusBatterystatus.md) | Battery status information. | [optional] 
**capacity** | [**list[ClusterNodeStatusCapacityItem]**](ClusterNodeStatusCapacityItem.md) | Storage capacity of this node. | [optional] 
**cpu** | [**ClusterNodeStatusCpu**](ClusterNodeStatusCpu.md) | CPU status information for this node. | [optional] 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**nvram** | [**ClusterNodeStatusNvram**](ClusterNodeStatusNvram.md) | Node NVRAM information. | [optional] 
**powersupplies** | [**ClusterNodeStatusPowersupplies**](ClusterNodeStatusPowersupplies.md) | Information about this node&#39;s power supplies. | [optional] 
**release** | **str** | OneFS release. | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 
**uptime** | **int** | Seconds this node has been online. | [optional] 
**version** | **str** | OneFS version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


