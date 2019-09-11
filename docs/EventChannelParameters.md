# EventChannelParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **list[str]** | Email addresses to send to. | [optional] 
**batch** | **str** | Batching criterion. | [optional] 
**batch_period** | **int** | Period over which batching is to be performed. | [optional] 
**custom_template** | **str** | Path to custom notification template. | [optional] 
**send_as** | **str** | Email address to use as from. | [optional] 
**smtp_host** | **str** | SMTP relay host. | [optional] 
**smtp_password** | **str** | Password for SMTP authentication - only if smtp_use_auth true. | [optional] 
**smtp_port** | **int** | SMTP relay port - optional defaults to 25. | [optional] 
**smtp_security** | **str** | Encryption protocol to use for SMTP. | [optional] 
**smtp_use_auth** | **bool** | Use SMTP authentication - optional defaults to false. | [optional] 
**smtp_username** | **str** | Username for SMTP authentication - only if smtp_use_auth true. | [optional] 
**subject** | **str** | Subject for emails. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


