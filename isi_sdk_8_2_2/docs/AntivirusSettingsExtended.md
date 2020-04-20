# AntivirusSettingsExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fail_open** | **bool** | Allow access when scanning fails. | [optional] 
**glob_filters** | **list[str]** | Glob patterns for leaf filenames. | [optional] 
**glob_filters_enabled** | **bool** | Enable glob filters. | [optional] 
**glob_filters_include** | **bool** | If true, only scan files matching a glob filter. If false, only scan files that don&#39;t match a glob filter. | [optional] 
**path_prefixes** | **list[str]** | Paths to include in realtime scans. | [optional] 
**quarantine** | **bool** | Try to quarantine files when threats are found. | [optional] 
**repair** | **bool** | Try to repair files when threats are found. | [optional] 
**report_expiry** | **int** | Amount of time in seconds until old reporting data is purged. | [optional] 
**scan_cloudpool_files** | **bool** | Scan files stored in CloudPools. | [optional] 
**scan_on_close** | **bool** | Scan files when apps close them. | [optional] 
**scan_on_open** | **bool** | Scan files on access. | [optional] 
**scan_size_maximum** | **int** | Skip scanning files larger than this. | [optional] 
**service** | **bool** | Whether the antivirus service is enabled. | [optional] 
**truncate** | **bool** | Try to truncate files when threats are found. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


