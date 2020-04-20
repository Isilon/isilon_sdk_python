# CloudAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | (S3 only) The user id of the S3 account | [optional] 
**account_username** | **str** | The username required to authenticate against the cloud service | [optional] 
**birth_cluster_id** | **str** | The guid of the cluster where this account was created | [optional] 
**enabled** | **bool** | Whether this account is explicitly enabled or disabled by a user | [optional] 
**key** | **str** | A valid authentication key for connecting to the cloud | [optional] 
**name** | **str** | A unique name for this account | [optional] 
**skip_ssl_validation** | **bool** | Indicates whether to skip SSL certificate validation when connecting to the cloud | [optional] 
**storage_region** | **str** | (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region | [optional] 
**telemetry_bucket** | **str** | (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider | [optional] 
**uri** | **str** | A valid URI pointing to the location of the cloud storage | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


