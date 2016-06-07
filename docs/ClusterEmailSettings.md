# ClusterEmailSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_mode** | **str** | This setting determines how notifications will be batched together to be sent by email.  &#39;none&#39; means each notification will be sent separately.  &#39;severity&#39; means notifications of the same severity will be sent together.  &#39;category&#39; means notifications of the same category will be sent together.  &#39;all&#39; means all notifications will be batched together and sent in a single email. | 
**mail_relay** | **str** | The address of the SMTP server to be used for relaying the notification messages.  An SMTP server is required in order to send notifications.  If this string is empty, no emails will be sent. | 
**mail_sender** | **str** | The full email address that will appear as the sender of notification messages. | 
**mail_subject** | **str** | The subject line for notification messages from this cluster. | 
**smtp_auth_passwd_set** | **bool** | Indicates if an SMTP authentication password is set. | 
**smtp_auth_security** | **str** | The type of secure communication protocol to use if SMTP is being used.  If &#39;none&#39;, plain text will be used, if &#39;starttls&#39;, the encrypted STARTTLS protocol will be used. | 
**smtp_auth_username** | **str** | Username to authenticate with if SMTP authentication is being used. | 
**smtp_port** | **int** | The port on the SMTP server to be used for relaying the notification messages.   | 
**use_smtp_auth** | **bool** | If true, this cluster will send SMTP authentication credentials to the SMTP relay server in order to send its notification emails.  If false, the cluster will attempt to send its notification emails without authentication. | 
**user_template** | **str** | Location of a custom template file that can be used to specify the layout of the notification emails. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


