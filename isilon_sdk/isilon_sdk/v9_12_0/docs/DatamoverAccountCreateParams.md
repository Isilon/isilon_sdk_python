# DatamoverAccountCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type** | **str** | Type of the data storage account | 
**briefcase** | **str** | An opaque container for storing additional data in this object, e.g. key-value pairs | [optional] 
**credentials** | [**DatamoverAccountCredentials**](DatamoverAccountCredentials.md) |  | [optional] 
**enforce_sse** | **bool** | Enforce Server-Side Encryption to make sure that data-at-rest is encrypted in the bucket. Only supported for DM AWS-S3 cloud accounts. SSE-S3, SSE-KMS and DSSE-KMS encryption algorithm types are supported on bucket. Warning: The Data Mover Copy Job will fail unless the target bucket exists and has supported encryption enabled. | [optional] 
**local_network_pool** | **str** | Local platform-specific network restriction | [optional] 
**max_sparks** | **int** | The limit of concurrent running tasks for this account per node | [optional] 
**name** | **str** | Name for this Data Mover account | 
**remote_network_pool** | **str** | Remote platform-specific network restriction | [optional] 
**storage_class** | **str** | The storage class of different cloud accounts. | [optional] 
**uri** | **str** | A valid URI pointing to the data storage | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


