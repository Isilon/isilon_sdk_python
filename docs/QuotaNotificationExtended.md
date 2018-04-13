# QuotaNotificationExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_alert** | **bool** | Send alert when rule matches. | 
**action_email_address** | **str** | Email a specific email address when rule matches. | [optional] 
**action_email_owner** | **bool** | Email quota domain owner when rule matches. | 
**email_template** | **str** | Path of optional /ifs template file used for email actions. | [optional] 
**holdoff** | **int** | Time to wait between detections for rules triggered by user actions. | [optional] 
**schedule** | **str** | Schedule for rules that repeatedly notify. | [optional] 
**condition** | **str** | The condition detected. | 
**id** | **str** | The system ID given to the rule. | 
**threshold** | **str** | The quota threshold detected. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


