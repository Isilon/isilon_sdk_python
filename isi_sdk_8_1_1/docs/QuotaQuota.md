# QuotaQuota

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container** | **bool** | If true, SMB shares using the quota directory see the quota thresholds as share size. | [optional] 
**enforced** | **bool** | True if the quota provides enforcement, otherwise a accounting quota. | [optional] 
**linked** | **bool** | If false and the quota is linked, attempt to unlink. | [optional] 
**thresholds** | [**QuotaQuotaThresholds**](QuotaQuotaThresholds.md) |  | [optional] 
**thresholds_include_overhead** | **bool** | If true, thresholds apply to data plus filesystem overhead required to store the data (i.e. &#39;physical&#39; usage). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


