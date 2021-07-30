# NfsNlmLocksLock

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client** | **str** | Specifies the client host name and IP address. | [optional] 
**client_id** | **str** | Specifies the client ID. | [optional] 
**created** | **int** | Specifies the UNIX EPoch time that the lock was created. | [optional] 
**id** | **str** | Specifies the system-assigned ID given to the lock. This value is returned when the lock is created with the POST method. | [optional] 
**lin** | **str** | Specifies the LIN in /ifs that is locked. | [optional] 
**lock_type** | **str** | Specifies the lock type. | [optional] 
**path** | **str** | Specifies the path under /ifs that is locked. | [optional] 
**range** | **list[int]** | Specifies the byte range within the locked file. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


