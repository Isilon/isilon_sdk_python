# NodeDrivesNodeDrive

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bay_group** | **str** | The name of the bay group this drive belongs to. | [optional] 
**baynum** | **int** | Numerical representation of this drive&#39;s bay. | [optional] 
**blocks** | **int** | Number of blocks on this drive. | [optional] 
**chassis** | **int** | The chassis number which contains this drive. | [optional] 
**devname** | **str** | This drive&#39;s device name. | [optional] 
**firmware** | [**ClusterNodeDriveFirmware**](ClusterNodeDriveFirmware.md) | Drive firmware information. | [optional] 
**format_progress** | **int** | Drive format progress percentage. | [optional] 
**handle** | **int** | Drive_d&#39;s handle representation for this driveIf we fail to retrieve the handle for this drive from drive_d: -1 | [optional] 
**interface_type** | **str** | String representation of this drive&#39;s interface type. | [optional] 
**lnum** | **int** | This drive&#39;s logical drive number in IFS. | [optional] 
**locnstr** | **str** | String representation of this drive&#39;s physical location. | [optional] 
**logical_block_length** | **int** | Size of a logical block on this drive. | [optional] 
**media_type** | **str** | String representation of this drive&#39;s media type. | [optional] 
**model** | **str** | This drive&#39;s manufacturer and model. | [optional] 
**pending_actions** | **list[str]** | This drive&#39;s current outstanding actions. For example, \&quot;add\&quot; or \&quot;firmware_update\&quot;. | [optional] 
**physical_block_length** | **int** | Size of a physical block on this drive. | [optional] 
**present** | **bool** | Indicates whether this drive is physically present in the node. | [optional] 
**purpose** | **str** | This drive&#39;s purpose in the DRV state machine. | [optional] 
**purpose_description** | **str** | Description of this drive&#39;s purpose. | [optional] 
**serial** | **str** | Serial number for this drive. | [optional] 
**ui_state** | **str** | This drive&#39;s state as presented to the UI. | [optional] 
**wwn** | **str** | The drive&#39;s &#39;worldwide name&#39; from its NAA identifiers. | [optional] 
**x_loc** | **int** | This drive&#39;s x-axis grid location. | [optional] 
**y_loc** | **int** | This drive&#39;s y-axis grid location. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


