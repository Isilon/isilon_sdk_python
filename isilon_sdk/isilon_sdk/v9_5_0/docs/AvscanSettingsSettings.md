# AvscanSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_pool** | **str** | The IP Pool to be used by the CAVA server. | [optional] 
**report_expiry** | **int** | How many seconds a scan report will be kept. | [optional] 
**scan_cloudpool_timeout** | **int** | How many seconds SMB will wait for an AV scan of a cloudpool to complete. | [optional] 
**scan_size_maximum** | **int** | Maximum size file that will be scanned (in kBs). 0 means no limit. | [optional] 
**scan_timeout** | **int** | How many seconds SMB will wait for an AV scan to complete. | [optional] 
**scan_zones** | **list[str]** | Array of access zones that are enabled for antivirus scanning. | [optional] 
**service_enabled** | **bool** | CAVA antivirus service is on/off. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


