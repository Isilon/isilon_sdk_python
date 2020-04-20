# AntivirusPolicyExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description for the policy. | [optional] 
**enabled** | **bool** | Whether the policy is enabled. | [optional] 
**force_run** | **bool** | Forces the scan to run regardless of whether the files were recently scanned. | [optional] 
**impact** | **str** | The priority of the antivirus scan job.  Must be a valid job engine impact policy, or null to use the default impact. | [optional] 
**name** | **str** | The name of the policy. | [optional] 
**paths** | **list[str]** | Paths to include in the scan. | [optional] 
**recursion_depth** | **int** | The depth to recurse in directories.  The default of -1 gives unlimited recursion. | [optional] 
**schedule** | **str** | The schedule for running scans in isi date format.  Examples include: &#39;every Friday&#39; or &#39;every day at 4:00&#39;.  A null value means the policy is manually scheduled. | [optional] 
**id** | **str** | A unique identifier for the policy. | [optional] 
**last_run** | **int** | The epoch time of the last run of this policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


