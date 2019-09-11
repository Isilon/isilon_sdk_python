# QuotaQuotaCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **bool** | If true, SMB shares using the quota directory see the quota thresholds as share size. | [optional] 
**enforced** | **bool** | True if the quota provides enforcement, otherwise an accounting quota. | [optional] 
**force** | **bool** | Force creation of quotas on the root of /ifs or percent based quotas. | [optional] 
**ignore_limit_checks** | **bool** | If true, skip child quota&#39;s threshold comparison with parent quota path. | [optional] 
**include_snapshots** | **bool** | If true, quota governs snapshot data as well as head data. | 
**path** | **str** |  | 
**persona** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**thresholds** | [**QuotaQuotaThresholds**](QuotaQuotaThresholds.md) |  | [optional] 
**thresholds_include_overhead** | **bool** | This option is deprecated. Use the option &#39;thresholds_on&#39; to select the usage on which thresholds to apply. | [optional] 
**thresholds_on** | **str** | Thresholds apply on quota accounting metric. | [optional] [default to 'fslogicalsize']
**type** | **str** | The type of quota. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


