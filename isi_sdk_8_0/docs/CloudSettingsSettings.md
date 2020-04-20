# CloudSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_policy_defaults** | [**Empty**](Empty.md) | The default filepool policy values for cloud pools. | [optional] 
**retry_coefficient_archive** | **str** | Coefficients in the quadratic function for determining the rest period between successive archive attempts. | [optional] 
**retry_coefficient_cache_invalidation** | **str** | Coefficients in the quadratic function for determining the rest period between successive cache invalidation attempts. | [optional] 
**retry_coefficient_cloud_garbage_collection** | **str** | Coefficients in the quadratic function for determining the rest period between successive cloud garbage collection attempts. | [optional] 
**retry_coefficient_local_garbage_collection** | **str** | Coefficients in the quadratic function for determining the rest period between successive local garbage collection attempts. | [optional] 
**retry_coefficient_read_ahead** | **str** | Coefficients in the quadratic function for determining the rest period between successive read ahead attempts. | [optional] 
**retry_coefficient_recall** | **str** | Coefficients in the quadratic function for determining the rest period between successive recall attempts. | [optional] 
**retry_coefficient_writeback** | **str** | Coefficients in the quadratic function for determining the rest period between successive writeback attempts. | [optional] 
**sleep_timeout_archive** | [**CloudSettingsSettingsSleepTimeoutCloudGarbageCollection**](CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.md) | Amount of time to wait between successive file archive operations. | [optional] 
**sleep_timeout_cache_invalidation** | [**CloudSettingsSettingsSleepTimeoutCloudGarbageCollection**](CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.md) | Amount of time to wait between successive file cache_invalidation operations. | [optional] 
**sleep_timeout_cloud_garbage_collection** | [**CloudSettingsSettingsSleepTimeoutCloudGarbageCollection**](CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.md) | Amount of time to wait between successive file cloud garbage collection operations. | [optional] 
**sleep_timeout_local_garbage_collection** | [**CloudSettingsSettingsSleepTimeoutCloudGarbageCollection**](CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.md) | Amount of time to wait between successive file local garbage collection operations. | [optional] 
**sleep_timeout_read_ahead** | [**CloudSettingsSettingsSleepTimeoutCloudGarbageCollection**](CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.md) | Amount of time to wait between successive file read ahead operations. | [optional] 
**sleep_timeout_recall** | [**CloudSettingsSettingsSleepTimeoutCloudGarbageCollection**](CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.md) | Amount of time to wait between successive file recall operations. | [optional] 
**sleep_timeout_writeback** | [**CloudSettingsSettingsSleepTimeoutCloudGarbageCollection**](CloudSettingsSettingsSleepTimeoutCloudGarbageCollection.md) | Amount of time to wait between successive file writeback operations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


