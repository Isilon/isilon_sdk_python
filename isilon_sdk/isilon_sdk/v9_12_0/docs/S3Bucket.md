# S3Bucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_logging** | **bool** | Enable S3 access logging. | [optional] 
**acl** | [**list[S3BucketAclItem]**](S3BucketAclItem.md) | Specifies an ordered list of S3 permissions. | [optional] 
**default_retention** | [**S3BucketDefaultRetention**](S3BucketDefaultRetention.md) | Specifies properties for an S3 bucket&#39;s retention | [optional] 
**description** | **str** | Description for this S3 bucket. | [optional] 
**lock_protection_mode** | **str** | Lock protection mode for S3 bucket | [optional] 
**log_prefix** | **str** | Log prefix for access logging. | [optional] 
**lower_retention** | **bool** | lower_retention must be set to true to lower object lock retention on an object. | [optional] 
**object_acl_policy** | **str** | Set behavior of modifying object acls | [optional] 
**object_lock_enabled** | **bool** | Enable object lock | [optional] 
**target_bucket** | **str** | Target bucket name for access logging. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


