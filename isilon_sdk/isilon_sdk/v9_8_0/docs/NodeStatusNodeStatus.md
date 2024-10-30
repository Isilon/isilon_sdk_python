# NodeStatusNodeStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**av_vendor** | **str** | Name of antivirus engine for scanning files. | [optional] 
**blocking_events** | **list[str]** | List of blocking event strings if CAVA is FAULTED | [optional] 
**cee_version** | **str** | Remote CEE software version string. | [optional] 
**dtd_version** | **str** | Document type definition version for message exchanges. | [optional] 
**server_status** | [**list[NodeStatusNodeStatusServerStatusItem]**](NodeStatusNodeStatusServerStatusItem.md) | Specifies the list of CAVA servers along with their status. | [optional] 
**signature_timestamp** | **str** | Timestamp of the last antivirus signature update. | [optional] 
**system_stats** | [**NodeStatusNodeStatusSystemStats**](NodeStatusNodeStatusSystemStats.md) | Specifies properties for CAVA system statistics. | [optional] 
**system_status** | **str** | Status of the CAVA antivirus system. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


