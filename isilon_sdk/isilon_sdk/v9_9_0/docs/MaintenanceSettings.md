# MaintenanceSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates whether maintenance mode is active. | 
**auto_enable** | **bool** | Indicates whether auto maintenance mode is enabled. | 
**components** | [**list[MaintenanceSettingsComponent]**](MaintenanceSettingsComponent.md) | Maintenance mode status of individual components. | [optional] 
**history** | [**list[MaintenanceSettingsHistoryItem]**](MaintenanceSettingsHistoryItem.md) | History list of maintenance mode windows. | [optional] 
**manual_window_enabled** | **bool** | Indicates whether the manual maintenance window enabled. | 
**manual_window_hours** | **int** | When the manual maintenance window is enabled, the duration of the window in hours. | 
**manual_window_start** | **int** | When the manual maintenance window is enabled, the time when the maintenance window will start. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


