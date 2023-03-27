# SedStatusNodeExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_msg** | **str** | information of the error if there is an error status. Empty if no error occurred. | 
**id** | **int** | Node ID (Device Number) of a node. | 
**lnn** | **int** | Logical Node Number (LNN) of a node. | 
**location** | **str** | Current location of the key. | 
**remote_key_id** | **str** | Key ID in the remote KMIP server. | 
**status** | **str** | Current key migration status. If no SEDs are avaiable and KMIP is not supported, it will show OFFLINE status. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


