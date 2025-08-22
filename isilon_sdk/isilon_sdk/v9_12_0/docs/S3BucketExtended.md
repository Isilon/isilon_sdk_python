# S3BucketExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_logging** | **bool** | Enable S3 access logging. | [optional] 
**acl** | [**list[S3BucketAclItem]**](S3BucketAclItem.md) | Specifies an ordered list of S3 permissions. | [optional] 
**default_retention** | [**S3BucketDefaultRetention**](S3BucketDefaultRetention.md) | Specifies properties for an S3 bucket&#39;s retention | [optional] 
**description** | **str** | Description for this S3 bucket. | 
**id** | **str** | Bucket ID. | 
**lock_protection_mode** | **str** | Lock protection mode for S3 bucket | [optional] 
**log_prefix** | **str** | Log prefix for access logging. | [optional] 
**name** | **str** | Bucket name. | 
**object_acl_policy** | **str** | Set behavior of modifying object acls | 
**object_lock_enabled** | **bool** | Enable object lock | [optional] 
**owner** | **str** | Specifies the name of the owner. | 
**path** | **str** | Path of bucket within /ifs. | 
**target_bucket** | **str** | Target bucket name for access logging. | [optional] 
**zid** | **int** | Zone ID | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


