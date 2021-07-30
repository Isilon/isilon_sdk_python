# LicenseLicenseTier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entitlements_exceeded_alerts** | [**list[LicenseLicenseTierEntitlementsExceededAlert]**](LicenseLicenseTierEntitlementsExceededAlert.md) | List of alerts about exceeded entitlements: The following alerts appear when usage of a resource such as a node, an encryption node, or storage capacity exceeds the quantity licensed for that resource. | [optional] 
**licensed_drive_capacity** | **int** | Licensed terabyte (TB, 10^12 bytes) drive capacity allocated as storage associated with tier. Included if tier is not NONINF and license is not a base only license. | [optional] 
**licensed_node_count** | **int** | Licensed number of nodes in this tier. | [optional] 
**licensed_nodes_with_seds_count** | **int** | Licensed number of nodes of this tier that contain self-encrypting drives. Included only if license is ONEFS and tier is not NONINF. | [optional] 
**tier** | **str** | OneFS hardware tier. Tier is a number, NONINF, or NO_TIER. NONINF indicates a non infinity tier. NO_TIER indicates a license that is not tier based. | [optional] 
**used_drive_capacity** | **int** | Actual terabyte (TB, 10^12 bytes) drive capacity allocated as storage space associated with tier. Included if tier is not NONINF and license is not a base only license. | [optional] 
**used_node_count** | **int** | Actual number of nodes in this tier. | [optional] 
**used_nodes_with_seds_count** | **int** | Actual number of nodes of this tier that contain self-encrypting drives. Included only if license is ONEFS and if tier is not NONINF. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


