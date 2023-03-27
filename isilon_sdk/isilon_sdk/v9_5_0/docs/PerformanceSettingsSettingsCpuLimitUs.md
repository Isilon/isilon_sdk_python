# PerformanceSettingsSettingsCpuLimitUs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_limit** | **int** | Base value for the resource limit. This value will be used to compute final workload&#39;s limits. | [optional] 
**health_modifier** | [**PerformanceSettingsSettingsCpuLimitUsHealthModifier**](PerformanceSettingsSettingsCpuLimitUsHealthModifier.md) |  | [optional] 
**impact_multiplier** | [**PerformanceSettingsSettingsCpuLimitUsImpactMultiplier**](PerformanceSettingsSettingsCpuLimitUsImpactMultiplier.md) |  | [optional] 
**max_health_multiplier_unhealthy** | **float** | Maximum multiplier computed from cluster&#39;s health when the cluster is not healthy | [optional] 
**min_health_multiplier** | **float** | Minimum multiplier computed from cluster&#39;s health. | [optional] 
**starting_health_multiplier** | **float** | Starting health multiplier when the workload is created | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


