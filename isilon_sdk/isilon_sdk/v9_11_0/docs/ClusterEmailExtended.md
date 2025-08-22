# ClusterEmailExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_mode** | **str** | This setting determines how notifications will be batched together to be sent by email. &#39;none&#39; means each notification will be sent separately. &#39;severity&#39; means notifications of the same severity will be sent together. &#39;category&#39; means notifications of the same category will be sent together. &#39;all&#39; means all notifications will be batched together and sent in a single email. | [optional] 
**mail_relay** | **str** | The address of the SMTP server to be used for relaying the notification messages.  An SMTP server is required in order to send notifications.  If this string is empty, no emails will be sent. | [optional] 
**mail_sender** | **str** | The full email address that will appear as the sender of notification messages. | [optional] 
**mail_subject** | **str** | The subject line for notification messages from this cluster. | [optional] 
**smtp_auth_passwd** | **str** | Password to authenticate with if SMTP authentication is being used. | [optional] 
**smtp_auth_security** | **str** | The type of secure communication protocol to use if SMTP is being used.  If &#39;none&#39;, cleartext will be used for the full SMTP transaction. If &#39;starttls&#39;, Secure SMTP will be used, a connection is begun in cleartext and then upgraded to encryption. If &#39;smtps&#39;, Implicit TLS will be used, TLS encryption is negotiated immediately at connection start. | [optional] 
**smtp_auth_username** | **str** | Username to authenticate with if SMTP authentication is being used. | [optional] 
**smtp_port** | **int** | The port on the SMTP server to be used for relaying the notification messages. | [optional] 
**use_smtp_auth** | **bool** | If true, this cluster will send SMTP authentication credentials to the SMTP relay server in order to send its notification emails. If false, the cluster will attempt to send its notification emails without authentication. | [optional] 
**user_template** | **str** | Location of a custom template file that can be used to specify the layout of the notification emails. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


