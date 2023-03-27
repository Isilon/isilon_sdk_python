# AvscanJobExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Free-form customer description of job. | [optional] 
**enabled** | **bool** | Whether the job is enabled. | [optional] 
**file_extension_action** | **str** | When a file matches an entry in the list of file extensions, do we include or exclude it?. | [optional] 
**file_extensions** | **list[str]** | Array of file extensions to use in scanning decision. | [optional] 
**id** | **str** | A unique identifier for the job. | [optional] 
**ignore_previous_scan_status** | **bool** | If True, force a scan of a previously scanned file. | [optional] 
**impact** | **str** | Specifies an impact policy for the antivirus scan jobs. | [optional] 
**job_name** | **str** | Unique short name for job. | [optional] 
**last_scheduled_run** | **int** | Status field indicating when the job was last run. | [optional] 
**paths_to_exclude** | **list[str]** | Array of relative paths under paths_to_include not to scan. | [optional] 
**paths_to_include** | **list[str]** | Array of absolute paths under /ifs to scan. | [optional] 
**scan_cloudpool_files** | **bool** | Perform real-time scans of cloudpool files? | [optional] 
**scan_if_no_extension** | **bool** | Scan files without extensions? | [optional] 
**schedule** | **str** | The ever-unfortunate &#39;schedule&#39; string type, e.g. &#39;every Thursday at 01:00&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


