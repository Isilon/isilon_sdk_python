# SummaryWorkloadWorkloadItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_in** | **float** | Count of bytes-in per second. | 
**bytes_out** | **float** | Count of bytes-out per second. | 
**cpu** | **float** | The number (across all cores) of micro-seconds per second. | 
**domain_id** | **str** | The IFS domain of the path which the operation was requested on. | [optional] 
**error** | **str** | Report any errors during id resolution. | [optional] 
**export_id** | **float** | The ID of the NFS export through which the operation was requested. | [optional] 
**group_id** | **float** | Group ID of the group that initiated the operation. | [optional] 
**group_sid** | **str** | Group SID of the group that initiated the operation. | [optional] 
**groupname** | **str** | The resolved text name of the group that initiated the operation. | [optional] 
**job_type** | **str** | The canonical name for the job followed by phase in brackets, ie. &#39;AVscan[1]&#39;, etc... | [optional] 
**l2** | **float** | L2 cache hits per second. | 
**l3** | **float** | L3 cache hits per second. | 
**local_address** | **str** | The IP address of the host receiving the operation request. | [optional] 
**local_name** | **str** | The resolved text name of the LocalAddr, if resolution can be performed. | [optional] 
**node** | **float** | The node on which the operation was performed or 0 for cluster scoped statistics. | 
**ops** | **float** | Operations per second. | 
**path** | **str** | The path which the operation was requestion on. | [optional] 
**protocol** | **str** | The protocol of the operation. | [optional] 
**reads** | **float** | Disk read operations per second. | 
**remote_address** | **str** | The IP address of the host sending the operation request. | [optional] 
**remote_name** | **str** | The resolved text name of the RemoteAddr, if resolution can be performed. | [optional] 
**share_name** | **str** | The name of the SMB share through which the operation was requested. | [optional] 
**system_name** | **str** | The process name, job ID, etc... | [optional] 
**time** | **int** | Unix Epoch time in seconds that statistic was collected. | 
**user_id** | **float** | User ID of the user who initiated the operation. | [optional] 
**user_sid** | **str** | User SID of the user who initiated the operation. | [optional] 
**username** | **str** | The resolved text name of the user who initiated the operation. | [optional] 
**workload_id** | **int** | ID of the workload (Pinned workloads only). | [optional] 
**workload_type** | **str** | The type of workload output. | [optional] 
**writes** | **float** | Disk write operations per second. | 
**zone_id** | **float** | Zone ID | [optional] 
**zone_name** | **str** | The resolved text zone name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


