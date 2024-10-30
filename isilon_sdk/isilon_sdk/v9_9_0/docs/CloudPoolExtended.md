# CloudPoolExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | **list[str]** | A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool. | [optional] 
**birth_cluster_id** | **str** | The guid of the cluster where this pool was created | [optional] 
**description** | **str** | A brief description of this pool | [optional] 
**name** | **str** | A unique name for this pool | [optional] 
**vendor** | **str** | A string identifier of the cloud services vendor | [optional] 
**id** | **str** | A unique name for this pool | [optional] 
**state** | **str** | Indicates whether this pool is in a good state (\&quot;OK\&quot;) or disabled (\&quot;disabled\&quot;) | [optional] 
**state_details** | **str** | Gives further information to describe the state of this pool | [optional] 
**type** | **str** | The type of cloud protocol required.  E.g., \&quot;isilon\&quot; for Dell EMC PowerScale, \&quot;ecs\&quot; for Dell EMC ECS Appliance, \&quot;virtustream\&quot; for Virtustream Storage Cloud, \&quot;azure\&quot; for Microsoft Azure, \&quot;s3\&quot; for Amazon S3, \&quot;c2s-s3\&quot; for Amazon Commercial Cloud Services S3 and \&quot;google\&quot; for Google Cloud Platform and \&quot;alibaba-cloud\&quot; for Alibaba Cloud | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


