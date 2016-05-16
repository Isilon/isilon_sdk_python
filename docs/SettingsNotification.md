# SettingsNotification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_alert** | **bool** | Send alert when rule matches. | 
**action_email_address** | **str** | Email a specific email address when rule matches. | 
**action_email_owner** | **bool** | Email quota domain owner when rule matches. | 
**condition** | **str** | The condition detected. | 
**email_template** | **str** | Path of optional /ifs template file used for email actions. | 
**holdoff** | **int** | Time to wait between detections for rules triggered by user actions. | 
**id** | **str** | The system ID given to the rule. | 
**schedule** | **str** | Schedule for rules that repeatedly notify. | 
**threshold** | **str** | The quota threshold detected. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


