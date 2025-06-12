# MetadataiqSettingsSettingsConsumer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_info** | [**MetadataiqSettingsSettingsConsumerDatabaseInfo**](MetadataiqSettingsSettingsConsumerDatabaseInfo.md) | MetadataIQ database information settings for the script that transfers the ChangelistCreate information to the remote database. Note that this includes fake databases or even terminal output. | [optional] 
**excluded_lnns** | **list[int]** | List of LNNs the system should not use to upload data to database. | [optional] 
**fetch_size** | **int** | Minimum number of ChangelistCreate entries the script should fetch at a time. Default is 2048. | [optional] 
**max_threads** | **int** | Maximum number of threads used to upload metadata to the database. The default is 8. | [optional] 
**number_shards** | **int** | The number of primary shards that an index should have. The default is 8. | [optional] 
**work_queue_size** | **int** | Transfer script&#39;s work queue size. Default is 16. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


