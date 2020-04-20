# CloudSettingsSettingsCloudPolicyDefaults

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archive_snapshot_files** | **bool** | Specifies if files with snapshots should be archived. | [optional] 
**cache** | [**CloudSettingsSettingsCloudPolicyDefaultsCache**](CloudSettingsSettingsCloudPolicyDefaultsCache.md) | Specifies default cloudpool cache settings for new filepool policies. | [optional] 
**compression** | **bool** | Specifies if files should be compressed. | [optional] 
**data_retention** | **int** | Specifies the minimum amount of time archived data will be retained in the cloud after deletion. | [optional] 
**encryption** | **bool** | Specifies if files should be encrypted. | [optional] 
**full_backup_retention** | **int** | (Used with NDMP backups only.  Not applicable to SyncIQ.)  The minimum amount of time cloud files will be retained after the creation of a full NDMP backup. | [optional] 
**incremental_backup_retention** | **int** | (Used with SyncIQ and NDMP backups.)  The minimum amount of time cloud files will be retained after the creation of a SyncIQ backup or an incremental NDMP backup. | [optional] 
**writeback_frequency** | **int** | The minimum amount of time to wait before updating cloud data with local changes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


