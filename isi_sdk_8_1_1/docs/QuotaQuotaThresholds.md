# QuotaQuotaThresholds

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | **int** | Usage bytes at which notifications will be sent but writes will not be denied. | [optional] 
**hard** | **int** | Usage bytes at which further writes will be denied. | [optional] 
**soft** | **int** | Usage bytes at which notifications will be sent and soft grace time will be started. | [optional] 
**soft_grace** | **int** | Time in seconds after which the soft threshold has been hit before writes will be denied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


