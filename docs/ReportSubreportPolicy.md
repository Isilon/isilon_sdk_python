# ReportSubreportPolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | If &#39;copy&#39;, source files will be copied to the target cluster.  If &#39;sync&#39;, the target directory will be made an image of the source directory:  Files and directories that have been deleted on the source, have been moved within the target directory, or no longer match the selection criteria will be deleted from the target directory. | [optional] 
**file_matching_pattern** | [**ReportSubreportPolicyFileMatchingPattern**](ReportSubreportPolicyFileMatchingPattern.md) | A file matching pattern, organized as an OR&#39;ed set of AND&#39;ed file criteria, for example ((a AND b) OR (x AND y)) used to define a set of files with specific properties.  Policies of type &#39;sync&#39; cannot use &#39;path&#39; or time criteria in their matching patterns, but policies of type &#39;copy&#39; can use all listed criteria. | [optional] 
**name** | **str** | User-assigned name of this sync policy. | [optional] 
**source_exclude_directories** | **list[str]** | Directories that will be excluded from the sync.  Modifying this field will result in a full synchronization of all data. | [optional] 
**source_include_directories** | **list[str]** | Directories that will be included in the sync.  Modifying this field will result in a full synchronization of all data. | [optional] 
**source_root_path** | **str** | The root directory on the source cluster the files will be synced from.  Modifying this field will result in a full synchronization of all data. | [optional] 
**target_host** | **str** | Hostname or IP address of sync target cluster.  Modifying the target cluster host can result in the policy being unrunnable if the new target does not match the current target association. | [optional] 
**target_path** | **str** | Absolute filesystem path on the target cluster for the sync destination. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


