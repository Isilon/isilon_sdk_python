# AntivirusSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fail_open** | **bool** | Allow access when scanning fails. | 
**glob_filters** | **list[str]** | Glob patterns for leaf filenames. | 
**glob_filters_enabled** | **bool** | Enable glob filters. | 
**glob_filters_include** | **bool** | If true, only scan files matching a glob filter. If false, only scan files that don&#39;t match a glob filter. | 
**path_prefixes** | **list[str]** | Paths to include in realtime scans. | 
**quarantine** | **bool** | Try to quarantine files when threats are found. | 
**repair** | **bool** | Try to repair files when threats are found. | 
**report_expiry** | **int** | Amount of time in seconds until old reporting data is purged. | 
**scan_cloudpool_files** | **bool** | Scan files stored in CloudPools. | 
**scan_on_close** | **bool** | Scan files when apps close them. | 
**scan_on_open** | **bool** | Scan files on access. | 
**scan_size_maximum** | **int** | Skip scanning files larger than this. | 
**service** | **bool** | Whether the antivirus service is enabled. | 
**truncate** | **bool** | Try to truncate files when threats are found. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


