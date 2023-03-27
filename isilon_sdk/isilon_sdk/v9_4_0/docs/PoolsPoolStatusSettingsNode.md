# PoolsPoolStatusSettingsNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devid** | **int** | Node ID (Device Number) of a node. | [optional] 
**interface_status** | [**PoolsPoolStatusSettingsNodeInterfaceStatus**](PoolsPoolStatusSettingsNodeInterfaceStatus.md) |  | [optional] 
**ip_status** | **str** | Summary of the status of the IPs currently configured on this node. usable: The node has IPs allocated that are usable. none_usable: The node has IPs configured, but they are currently not in a usable state. This can occur for a variety of reasons. For static IPs, this can occur if the node is down, or if the interfaces are down. For dynamic IPs, this can occur if all of the IPs are about to move to a different node. none_configured: The node has no IPs from the Network Pool configured currently. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**node_state** | **str** | The node&#39;s current state within the cluster. | [optional] 
**protocols_running** | **bool** | Indicates if the node has the required protocols to be resolvable via DNS. | [optional] 
**sc_dns_resolvable** | **bool** | Indicates if the node can be resolved via SmartConnect DNS or not. | [optional] 
**suspended** | **bool** | Indicates if the node has been suspended within the Network Pool. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


