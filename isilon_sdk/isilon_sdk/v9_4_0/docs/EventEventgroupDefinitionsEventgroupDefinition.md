# EventEventgroupDefinitionsEventgroupDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | ID of eventgroup category: all, 100000000 (SYS_DISK_EVENTS), 200000000 (NODE_STATUS_EVENTS), 300000000 (REBOOT_EVENTS), 400000000 (SW_EVENTS), 500000000 (QUOTA_EVENTS), 600000000 (SNAP_EVENTS), 700000000 (WINNET_EVENTS), 800000000 (FILESYS_EVENTS), 900000000 (HW_EVENTS), 1100000000 (CPOOL_EVENTS). | [optional] 
**channels** | **list[int]** | Channels by which this eventgroup type can be alerted. | [optional] 
**description** | **str** | Human readable description - may contain value placeholders. | [optional] 
**id** | **str** | Unique Identifier. | [optional] 
**name** | **str** | Name for eventgroup. | [optional] 
**no_ignore** | **bool** | True if event should not be ignored. | [optional] 
**node** | **bool** | True if this eventgroup type is node specific, false cluster wide. | [optional] 
**rules** | **list[str]** | Alert rules involving this eventgroup type. | [optional] 
**suppressed** | **bool** | True if alerting is suppressed for this eventgroup type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


