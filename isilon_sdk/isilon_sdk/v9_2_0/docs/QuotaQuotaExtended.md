# QuotaQuotaExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **bool** | If true, SMB shares using the quota directory see the quota thresholds as share size. | 
**efficiency_ratio** | **float** | Represents the ratio of logical space provided to physical space used. This accounts for protection overhead, metadata, and compression ratios for the data. | [optional] 
**enforced** | **bool** | True if the quota provides enforcement, otherwise a accounting quota. | 
**id** | **str** | The system ID given to the quota. | 
**include_snapshots** | **bool** | If true, quota governs snapshot data as well as head data. | 
**linked** | **bool** | For user, group and directory quotas, true if the quota is linked and controlled by a parent default-* quota. Linked quotas cannot be modified until they are unlinked. | [optional] 
**notifications** | **str** | Summary of notifications: &#39;custom&#39; indicates one or more notification rules available from the notifications sub-resource; &#39;default&#39; indicates system default rules are used; &#39;disabled&#39; indicates that no notifications will be used for this quota.; &#39;badmap&#39; indicates that notification rule has problem in rule map. | 
**path** | **str** |  | [optional] 
**persona** | [**AuthAccessAccessItemFileGroup**](AuthAccessAccessItemFileGroup.md) | Specifies properties for a persona, which consists of either a &#39;type&#39; and a &#39;name&#39; or an &#39;ID&#39;. | [optional] 
**ready** | **bool** | True if the default resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job. | 
**reduction_ratio** | **float** | Represents the ratio of logical space provided to physical data space used. This accounts for compression and data deduplication effects. | [optional] 
**thresholds** | [**QuotaQuotaThresholdsExtended**](QuotaQuotaThresholdsExtended.md) |  | 
**thresholds_on** | **str** | Thresholds apply on quota accounting metric. | [optional] 
**type** | **str** | The type of quota. | 
**usage** | [**QuotaQuotaUsage**](QuotaQuotaUsage.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


