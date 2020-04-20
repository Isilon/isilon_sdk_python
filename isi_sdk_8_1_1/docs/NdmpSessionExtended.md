# NdmpSessionExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_bytes_transferred** | **int** | Bytes transferred to/from the filesystem | 
**data_state** | **str** | State of the NDMP Data Service | 
**dest_path** | **str** | The path being recovered to | 
**dma_ip_addr** | **str** | IP address of the DMA | 
**elapsed_time** | **int** | Number of seconds elapsed since the backup was started | 
**id** | **str** | Unique display ID. | 
**mover_bytes_transferred** | **int** | Bytes transferred to/from tape or remote writer | 
**mover_state** | **str** | State of the NDMP Mover Service | 
**operation** | **str** | The type of backup session | 
**remote_ip_addr** | **str** | IP address of the remote NDMP participant | 
**scsi_device** | **str** | Name of the media changer device used if any | 
**session** | **str** | Session ID in form &lt;lnn&gt;.&lt;pid&gt;. | 
**source_path** | **str** | The path being backed up | 
**start_time** | **int** | Time backup was started in seconds since epoch | 
**tape_device** | **str** | Name of the tape device used if any | 
**tape_open_mode** | **str** | Describes the mode in which the tape is opened | 
**throughput** | **int** | The throughput in MB/s | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


