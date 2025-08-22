# AvscanFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_extension_action** | **str** | When a file matches an entry in the list of file extensions, do we include or exclude it?. | [optional] 
**file_extensions** | **list[str]** | Array of file extensions to use in scanning decision. | [optional] 
**filter_enabled** | **bool** | Access zone enabled for AV scanning. | [optional] 
**id** | **str** | A unique identifier for the zone. | [optional] 
**open_on_fail** | **bool** | Allow access to files when scanning fails. | [optional] 
**paths_to_exclude** | **list[str]** | Array of relative paths under zone root not to scan. | [optional] 
**scan_cloudpool_files** | **bool** | Perform real-time scans of cloudpool files? | [optional] 
**scan_if_no_extension** | **bool** | Scan files without extensions? | [optional] 
**scan_on_close** | **bool** | Perform real-time scans of files when the file handle is closed. | [optional] 
**scan_on_read** | **bool** | Perform real-time scans of files on first file read. | [optional] 
**scan_on_rename** | **bool** | Perform real-time scan of file when the file is renamed. | [optional] 
**scan_profile** | **str** | Type of scan profile applicable to the zone. | [optional] 
**zone_name** | **str** | Access zone name containing filter settings. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


