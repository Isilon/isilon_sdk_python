# CloudAccountExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_username** | **str** | The username required to authenticate against the cloud service | [optional] 
**enabled** | **bool** | Whether or not this account should be used for cloud storage | [optional] 
**key** | **str** | A valid authentication key for connecting to the cloud | [optional] 
**name** | **str** | A unique name for this account | [optional] 
**uri** | **str** | A valid URI pointing to the location of the cloud storage | [optional] 
**bucket** | **str** | The machine generated name of the account bucket to store data | [optional] 
**id** | **str** | A globally unique name for this account | [optional] 
**metadata_bucket** | **str** | The machine generated name of the account bucket to store metadata | [optional] 
**pool** | **str** | Name of the pool referencing this account.  Empty if none. | [optional] 
**type** | **str** | The type of cloud protocol required (e.g., &#39;ran&#39;, &#39;azure&#39;) | [optional] 
**validity** | **str** | Either &#39;OK&#39; or a message indicating problems with the account (Note* only shown when &#39;validate&#x3D;1&#39; argument is appended to URI) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


