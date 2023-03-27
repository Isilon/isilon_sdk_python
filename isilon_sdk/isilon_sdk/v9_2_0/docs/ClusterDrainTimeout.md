# ClusterDrainTimeout

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_timeout** | **int** | The duration in seconds after drain begins that an alert will be raised. An alert timeout must be set to a smaller value than the drain timeout to be used. If not specified, an alert will not be raised (legacy behavior). | [optional] 
**drain_timeout** | **int** | The duration in seconds that upgrade waits for all SMB clients to disconnect from a node before rebooting it. A value of 0 means wait indefinitely. If not specified, upgrade proceeds with reboots regardless of SMB client connections (legacy behavior). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


