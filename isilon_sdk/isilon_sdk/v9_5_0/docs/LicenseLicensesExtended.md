# LicenseLicensesExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**licenses** | [**list[LicenseLicense]**](LicenseLicense.md) |  | [optional] 
**activation_incomplete_alert** | **bool** | True when we are generating an activation incomplete alert. An activation incomplete alert is generated if we do not have a signed license file 90 days after OneFS is upgraded. | 
**base_only_licenses** | **list[str]** |  | 
**evaluatable** | **list[str]** |  | 
**resume** | **str** | Provide this token as the &#39;resume&#39; query argument to continue listing results. | [optional] 
**swid** | **str** | Software license identifier. SWID will be absent if not yet obtained from a license file. | [optional] 
**total** | **int** | Total number of items available. | [optional] 
**valid_signature** | **bool** | True if license file contains a valid signature. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


