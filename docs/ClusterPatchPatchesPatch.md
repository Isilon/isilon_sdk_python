# ClusterPatchPatchesPatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | A long comment about the patch. | [optional] 
**conflicts** | **list[str]** | Other patches that this patch conflicts with. | [optional] 
**dependencies** | **list[str]** | Other patches that this patch depends on. | [optional] 
**description** | **str** | A short description of the patch. | [optional] 
**files** | [**list[ClusterPatchPatchesPatchFile]**](ClusterPatchPatchesPatchFile.md) | The files contained in this patch. | [optional] 
**id** | **str** | A unique identifier for the patch. | [optional] 
**name** | **str** | The name of the patch. | [optional] 
**nodes** | **list[int]** | The nodes that this patch is installed on. | [optional] 
**reboot** | **str** | Describes the reboot requirements | [optional] 
**services** | [**list[ClusterPatchPatchesPatchService]**](ClusterPatchPatchesPatchService.md) | The services affected during the patch deployment | [optional] 
**status** | **str** | The installation status of this patch on the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


