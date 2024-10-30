# LicenseLicense

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days_since_expiry** | **int** | Number of days since a license expired. | [optional] 
**days_to_expiry** | **int** | Number of days before a license expires. | [optional] 
**expiration** | **str** | Date of license expiry. Format is YYYY-MM-DD. It is not included if there is no expiration. Feature is considered expired at end of this day. The cluster time is used to determine expiry. | [optional] 
**expired_alert** | **bool** | True when we are generating an alert that this feature has expired. | 
**expiring_alert** | **bool** | True when we are generating an alert that this feature is expiring. | 
**id** | **str** | Name of the licensed feature. | 
**name** | **str** | Name of the licensed feature. | 
**status** | **str** | Current status of the license. | 
**tiers** | [**list[LicenseLicenseTier]**](LicenseLicenseTier.md) | Tiered License details. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


