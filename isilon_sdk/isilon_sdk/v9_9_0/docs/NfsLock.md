# NfsLock

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | **str** | The client host name, FQDN, or IP. | [optional] 
**client_id** | **int** | The client ID. | [optional] 
**created** | **int** | Specifies the UNIX Epoch time that the lock was created. | [optional] 
**id** | **str** | The lock ID. | [optional] 
**lin** | **int** | The logical inode number (LIN) of the locked resource. | [optional] 
**lock_type** | **str** | The type of lock. | [optional] 
**path** | **str** |  | [optional] 
**range** | **list[int]** | The byte range within the file that is locked. | [optional] 
**version** | **str** | NFS major version: v3 or v4 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


