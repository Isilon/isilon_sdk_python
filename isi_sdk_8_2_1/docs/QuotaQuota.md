# QuotaQuota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **bool** | If true, SMB shares using the quota directory see the quota thresholds as share size. | [optional] 
**enforced** | **bool** | True if the quota provides enforcement, otherwise an accounting quota. | [optional] 
**force** | **bool** | Force creation of quotas on the root of /ifs or percent based quotas. | [optional] 
**ignore_limit_checks** | **bool** | If true, skip child quota&#39;s threshold comparison with parent quota path. | [optional] 
**linked** | **bool** | If false and the quota is linked, attempt to unlink. | [optional] 
**thresholds** | [**QuotaQuotaThresholds**](QuotaQuotaThresholds.md) |  | [optional] 
**thresholds_include_overhead** | **bool** | This option is deprecated. Use the option &#39;thresholds_on&#39; to select the usage on which thresholds to apply. | [optional] 
**thresholds_on** | **str** | Thresholds apply on quota accounting metric. | [optional] [default to 'fslogicalsize']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


