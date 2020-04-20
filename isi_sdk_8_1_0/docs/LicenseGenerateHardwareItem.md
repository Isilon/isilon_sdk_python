# LicenseGenerateHardwareItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drive_capacity** | **int** | Licensed terabyte (TB, 10^12 bytes) drive capacity allocated as storage associated with tier. Included if tier is not NONINF and license is not a base only license. | [optional] 
**node_count** | **int** | Licensed number of nodes in this tier. | [optional] 
**nodes_with_seds_count** | **int** | Licensed number of nodes of this tier that contain self-encrypting drives. Included only if license is ONEFS and tier is not NONINF. | [optional] 
**tier** | **str** | OneFS hardware tier. Tier is a number, NONINF, or NO_TIER. NONINF indicates a non infinity tier. NO_TIER indicates a license that is not tier based. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


