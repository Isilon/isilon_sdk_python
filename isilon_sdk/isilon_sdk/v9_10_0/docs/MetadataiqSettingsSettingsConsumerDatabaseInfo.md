# MetadataiqSettingsSettingsConsumerDatabaseInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | API key to securely connect the database. The default is &#39;&#39;. | [optional] 
**certificate_path** | **str** | Path to the CA certificate to use to ensure the authenticity of the remote database. The path must be under /ifs or empty. Default is &#39;&#39;. | [optional] 
**database_type** | **str** | Type of database to write. The default is &#39;ELK database&#39;. | [optional] 
**host_port** | **int** | Port to the database. The default is 9200. | [optional] 
**hostname** | **str** | Name of the remote ELK database host. The default is &#39;&#39;. | [optional] 
**verify_certificate** | **bool** | Use the certificate under the certificate key from the OneFS certificate store to verify the authenticity of the database. The default is True. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


