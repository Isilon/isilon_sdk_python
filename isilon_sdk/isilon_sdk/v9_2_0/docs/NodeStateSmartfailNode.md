# NodeStateSmartfailNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dead** | **bool** | This node is dead (dead_devs). | [optional] 
**down** | **bool** | This node is down (down_devs). | [optional] 
**error** | **str** | Error message, if the HTTP status returned from this node was not 200. | [optional] 
**id** | **int** | Node ID (Device Number) of a node. | [optional] 
**in_cluster** | **bool** | This node is in the cluster (all_devs). | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of a node. | [optional] 
**readonly** | **bool** | This node is readonly (ro_devs). | [optional] 
**shutdown_readonly** | **bool** | This node is shutdown readonly (down_devs). | [optional] 
**smartfailed** | **bool** | This node is smartfailed (soft_devs). | [optional] 
**status** | **int** | Status of the HTTP response from this node if not 200.  If 200, this field does not appear. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


