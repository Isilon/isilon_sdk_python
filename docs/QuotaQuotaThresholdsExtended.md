# QuotaQuotaThresholdsExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | **int** | Usage bytes at which notifications will be sent but writes will not be denied. | [optional] 
**hard** | **int** | Usage bytes at which further writes will be denied. | [optional] 
**soft** | **int** | Usage bytes at which notifications will be sent and soft grace time will be started. | [optional] 
**soft_grace** | **int** | Time in seconds after which the soft threshold has been hit before writes will be denied. | [optional] 
**advisory_exceeded** | **bool** | True if the advisory threshold has been hit. | [optional] 
**advisory_last_exceeded** | **int** | Time at which advisory threshold was hit. | [optional] 
**hard_exceeded** | **bool** | True if the hard threshold has been hit. | [optional] 
**hard_last_exceeded** | **int** | Time at which hard threshold was hit. | [optional] 
**soft_exceeded** | **bool** | True if the soft threshold has been hit. | [optional] 
**soft_last_exceeded** | **int** | Time at which soft threshold was hit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


