# QuotaQuotaCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **bool** | If true, SMB shares using the quota directory see the quota thresholds as share size. | [optional] 
**enforced** | **bool** | True if the quota provides enforcement, otherwise a accounting quota. | 
**force** | **bool** | Force creation of quotas on the root of /ifs. | [optional] 
**include_snapshots** | **bool** | If true, quota governs snapshot data as well as head data. | 
**path** | **str** | The /ifs path governed. | 
**persona** | [**GroupMember**](GroupMember.md) | A persona consists of either a &#39;type&#39; and &#39;name&#39; or a &#39;ID&#39;. | [optional] 
**thresholds** | [**QuotaQuotaThresholds**](QuotaQuotaThresholds.md) |  | [optional] 
**thresholds_include_overhead** | **bool** | If true, thresholds apply to data plus filesystem overhead required to store the data (i.e. &#39;physical&#39; usage). | 
**type** | **str** | The type of quota. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


