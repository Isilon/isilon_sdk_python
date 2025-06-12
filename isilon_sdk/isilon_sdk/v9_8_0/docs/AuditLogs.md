# AuditLogs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before** | **str** | The date which the current purging process will delete logs before. | [optional] 
**blocker** | [**list[AuditLogsBlockerItem]**](AuditLogsBlockerItem.md) | The status ot the consumers that blocked the deletion. | [optional] 
**deletion** | [**list[AuditLogsDeletionItem]**](AuditLogsDeletionItem.md) | Deleted result on each node. | [optional] 
**status** | **str** | Status of current manual purging. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


