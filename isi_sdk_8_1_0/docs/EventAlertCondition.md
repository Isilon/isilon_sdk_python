# EventAlertCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **list[str]** | Event Group categories to be alerted: all, 100000000 (SYS_DISK_EVENTS), 200000000 (NODE_STATUS_EVENTS), 300000000 (REBOOT_EVENTS), 400000000 (SW_EVENTS), 500000000 (QUOTA_EVENTS), 600000000 (SNAP_EVENTS), 700000000 (WINNET_EVENTS), 800000000 (FILESYS_EVENTS), 900000000 (HW_EVENTS), 1100000000 (CPOOL_EVENTS) | [optional] 
**channels** | **list[str]** | Channels for alert | [optional] 
**condition** | **str** | Trigger condition for alert | [optional] 
**eventgroup_ids** | **list[str]** | Event Group IDs to be alerted | [optional] 
**interval** | **int** | Required with ONGOING condition only, period in seconds between alerts of ongoing conditions | [optional] 
**limit** | **int** | Required with NEW EVENTS condition only, limits the number of alerts sent as events are added | [optional] 
**severities** | **list[str]** | Severities to be alerted | [optional] 
**transient** | **int** | Any eventgroup lasting less than this many seconds is deemed transient and will not generate alerts under this condition. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


