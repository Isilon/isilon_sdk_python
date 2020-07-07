# ClusterNodeHardware

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chassis** | **str** | Name of this node&#39;s chassis. | [optional] 
**chassis_code** | **str** | Chassis code of this node (1U, 2U, etc.). | [optional] 
**chassis_count** | **str** | Number of chassis making up this node. | [optional] 
**_class** | **str** | Class of this node (storage, accelerator, etc.). | [optional] 
**configuration_id** | **str** | Node configuration ID. | [optional] 
**cpu** | **str** | Manufacturer and model of this node&#39;s CPU. | [optional] 
**disk_controller** | **str** | Manufacturer and model of this node&#39;s disk controller. | [optional] 
**disk_expander** | **str** | Manufacturer and model of this node&#39;s disk expander. | [optional] 
**family_code** | **str** | Family code of this node (X, S, NL, etc.). | [optional] 
**flash_drive** | **str** | Manufacturer, model, and device id of this node&#39;s flash drive. | [optional] 
**generation_code** | **str** | Generation code of this node. | [optional] 
**hwgen** | **str** | PowerScale hardware generation name. | [optional] 
**imb_version** | **str** | Version of this node&#39;s PowerScale Management Board. | [optional] 
**infiniband** | **str** | Infiniband card type. | [optional] 
**lcd_version** | **str** | Version of the LCD panel. | [optional] 
**motherboard** | **str** | Manufacturer and model of this node&#39;s motherboard. | [optional] 
**net_interfaces** | **str** | Description of all this node&#39;s network interfaces. | [optional] 
**nvram** | **str** | Manufacturer and model of this node&#39;s NVRAM board. | [optional] 
**powersupplies** | **list[str]** | Description strings for each power supply on this node. | [optional] 
**processor** | **str** | Number of processors and cores on this node. | [optional] 
**product** | **str** | PowerScale product name. | [optional] 
**ram** | **int** | Size of RAM in bytes. | [optional] 
**serial_number** | **str** | Serial number of this node. | [optional] 
**series** | **str** | Series of this node (X, I, NL, etc.). | [optional] 
**storage_class** | **str** | Storage class of this node (storage or diskless). | [optional] 
**tier** | **int** | Platform tier level of this node if applicable (1-6 are defined, 0 for unknown or not supported, -1 for error). If not supported: 0. If Logic to determine tier fails: 0 for unknown. If PSI_Get fails: -1 for error. PSI_Get can fail if PSI not initialized, or key does not exist. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


