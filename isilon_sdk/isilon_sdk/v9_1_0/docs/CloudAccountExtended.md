# CloudAccountExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | (S3 only) The user id of the S3 account | [optional] 
**account_username** | **str** | The username required to authenticate against the cloud service | [optional] 
**birth_cluster_id** | **str** | The guid of the cluster where this account was created | [optional] 
**credential_provider** | [**CloudAccountCredentialProvider**](CloudAccountCredentialProvider.md) |  | [optional] 
**enable_ocsp** | **bool** | (C2S-S3 only) Indicates whether to use OCSP to check the revocation status of the authentication certificate | [optional] 
**enabled** | **bool** | Whether this account is explicitly enabled or disabled by a user | [optional] 
**key** | **str** | A valid authentication key for connecting to the cloud | [optional] 
**name** | **str** | A unique name for this account | [optional] 
**ocsp_responder_url_required** | **bool** | (C2S-S3 only) Determines whether a certificate without an OCSP responder URL is considered valid or not | [optional] 
**proxy** | **str** | The id or name of a proxy to be used by this account | [optional] 
**skip_account_check** | **bool** | (Not recommended) Indicates whether to skip validation that the cloud account is still accessible | [optional] 
**skip_ssl_validation** | **bool** | Indicates whether to skip peer verification of SSL certificates when connecting to the cloud | [optional] 
**storage_region** | **str** | An appropriate region for the account as defined by the cloud service provider.  For example, faster access times may be gained by referencing a nearby region | [optional] 
**telemetry_bucket** | **str** | (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider | [optional] 
**uri** | **str** | A valid URI pointing to the location of the cloud storage | [optional] 
**bucket** | **str** | The machine generated name of the account bucket to store data | [optional] 
**id** | **str** | A globally unique name for this account | [optional] 
**metadata_bucket** | **str** | The machine generated name of the account bucket to store metadata | [optional] 
**pool** | **str** | Name of the pool referencing this account.  Empty if none. | [optional] 
**state** | **str** | Indicates whether this account is in a good state (\&quot;OK\&quot;), disabled (\&quot;disabled\&quot;) or inaccessible via the network (\&quot;unreachable\&quot;) | [optional] 
**state_details** | **str** | Gives further information to describe the state of this account | [optional] 
**type** | **str** | The type of cloud protocol required.  E.g., \&quot;isilon\&quot; for Dell EMC PowerScale, \&quot;ecs\&quot; for Dell EMC ECS Appliance, \&quot;virtustream\&quot; for Virtustream Storage Cloud, \&quot;azure\&quot; for Microsoft Azure, \&quot;s3\&quot; for Amazon S3, \&quot;c2s-s3\&quot; for Amazon Commercial Cloud Services S3 and \&quot;google\&quot; for Google Cloud Platform and \&quot;alibaba-cloud\&quot; for Alibaba Cloud | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


