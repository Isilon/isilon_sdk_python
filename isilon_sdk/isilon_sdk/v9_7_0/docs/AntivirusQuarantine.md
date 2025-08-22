# AntivirusQuarantine

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | Path of this file, starting with /ifs. | 
**last_istag** | **str** |  | [optional] 
**last_scan** | **int** |  | [optional] 
**quarantined** | **bool** | If true, this file is quarantined.  If false, the file is not quarantined. | 
**scan_result** | **str** | The result of the last scan on this file.  This string is usually one of: never_scanned, clean, quarantined, repaired, truncated, infected_no_action_taken, skipped_per_settings.  However, a longer string starting with &#39;unknown_status&#39; and describing the details can also appear in uncommon edge cases. | 
**scan_status** | **str** | The scanning status of this file.  If &#39;current&#39;, the file was scanned with the most up-to-date virus definitions.  If &#39;not_current&#39;, it has either not been scanned, been modified since the last scan, or the virus definitions are not current. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


