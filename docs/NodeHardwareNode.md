# NodeHardwareNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis** | **str** | Name of this node&#39;s chassis. | [optional] 
**chassis_code** | **str** | Chassis code of this node (1U, 2U, etc.). | [optional] 
**chassis_count** | **str** | Number of chassis making up this node. | [optional] 
**chassis_depth** | **str** | Chassis depth for this node if applicable (Normal, Deep, Unknown). If not supported: Unknown. If Logic to determine chassis depth fails: Unknown. If PSI_Get fails: Unknown. PSI_Get can fail if PSI not initialized, or key does not exist. | [optional] 
**_class** | **str** | Class of this node (storage, accelerator, etc.). | [optional] 
**code_name** | **str** | Code name of this node if applicable (Minnetonka, MiniHuron, Huron, Union, Tahoe, Superior, Unknown). If not supported: Unknown. If Logic to determine code name fails: Unknown. If PSI_Get fails: Unknown. PSI_Get can fail if PSI not initialized, or key does not exist. | [optional] 
**compute_type** | **str** | Type of compute node if applicable (Low, Medium, High, Turbo, Ultra, Unknown). If not supported: Unknown. If Logic to determine compute type fails: Unknown. If PSI_Get fails: Unknown. PSI_Get can fail if PSI not initialized, or key does not exist. | [optional] 
**configuration_id** | **str** | Node configuration ID. | [optional] 
**cpu** | **str** | Manufacturer and model of this node&#39;s CPU. | [optional] 
**disk_controller** | **str** | Manufacturer and model of this node&#39;s disk controller. | [optional] 
**disk_expander** | **str** | Manufacturer and model of this node&#39;s disk expander. | [optional] 
**family_code** | **str** | Family code of this node (X, S, NL, etc.). | [optional] 
**flash_drive** | **str** | Manufacturer, model, and device id of this node&#39;s flash drive. | [optional] 
**generation_code** | **str** | Generation code of this node. | [optional] 
**hwgen** | **str** | Isilon hardware generation name. | [optional] 
**id** | **int** | Node ID (Device Number) of this node. | [optional] 
**imb_version** | **str** | Version of this node&#39;s Isilon Management Board. | [optional] 
**infiniband** | **str** | Infiniband card type. | [optional] 
**lcd_version** | **str** | Version of the LCD panel. | [optional] 
**lnn** | **int** | Logical Node Number (LNN) of this node. | [optional] 
**model** | **str** | Isilon node model identifier string (S200, X410, Infinity-H500, etc.). | [optional] 
**model_code** | **str** | Isilon node model code string (S200, X410, H500, etc.). | [optional] 
**motherboard** | **str** | Manufacturer and model of this node&#39;s motherboard. | [optional] 
**net_interfaces** | **str** | Description of all this node&#39;s network interfaces. | [optional] 
**node_slot_id** | **int** | Position of node within chassis (e.g., 1-4 for Infinity chassis). -1 for error or not supported. | [optional] 
**nvram** | **str** | Manufacturer and model of this node&#39;s NVRAM board. | [optional] 
**peer_serial_number** | **str** | Serial number of this node&#39;s peer/buddy node.(Infinity Only) | [optional] 
**performance_code** | **str** | Performance code of this node, if applicable (2, 4, 5, etc.). | [optional] 
**powersupplies** | **list[str]** | Description strings for each power supply on this node. | [optional] 
**processor** | **str** | Number of processors and cores on this node. | [optional] 
**product** | **str** | Isilon product name. | [optional] 
**ram** | **int** | Size of RAM in bytes. | [optional] 
**serial_number** | **str** | Serial number of this node. | [optional] 
**series** | **str** | Series of this node (X, I, NL, etc.). | [optional] 
**sled_drive_count** | **int** | Size of drive sleds in node, if applicable. Expected values: 3, 4, 6. 0 if unable to determine sled size. -1 for error or not supported. If PSI_Get fails: -1. PSI_Get can fail if PSI not initialized, or key does not exist. | [optional] 
**storage_class** | **str** | Storage class of this node (storage or diskless). | [optional] 
**tier** | **int** | Platform tier level of this node if applicable (1-4 are defined, 0 for unknown or not supported, -1 for error). If not supported: 0. If Logic to determine tier fails: 0 for unknown. If PSI_Get fails: -1 for error. PSI_Get can fail if PSI not initialized, or key does not exist. | [optional] 
**top_level_assembly_serial_number** | **str** | Serial number of the top level assembly of this node.(Infinity Only) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


