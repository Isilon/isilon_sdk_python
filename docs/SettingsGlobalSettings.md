# SettingsGlobalSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audited_zones** | **list[str]** | Specifies zones that are audited when the protocol_auditing_enabled property is enabled. | [optional] 
**cee_log_time** | **str** | Specifies that events past a certain date are forwarded by the audit CEE forwarder. Format these events as follows: &#39;Topic@YYYY-MM-DD HH:MM:SS&#39;. | [optional] 
**cee_server_uris** | **list[str]** | Specifies a list of Common Event Enabler (CEE) server URIs. Protocol audit logs are sent to these URIs for external processing. | [optional] 
**config_auditing_enabled** | **bool** | Specifies whether logging for API configuration changes are enabled. | [optional] 
**config_syslog_enabled** | **bool** | Specifies whether configuration audit syslog messages are forwarded. | [optional] 
**config_syslog_servers** | **list[str]** | Specifies a list of remote servers for audit logging of configuration changes. Audit logs are sent to syslog of these remote servers. | [optional] 
**hostname** | **str** | Specifies the hostname that is reported in protocol events from this cluster. | [optional] 
**protocol_auditing_enabled** | **bool** | Specifies if logging for the I/O stream is enabled. | [optional] 
**protocol_syslog_servers** | **list[str]** | Specifies a list of remote servers for protocol audit logging. Protocol audit logs are sent to syslog of these remote servers. | [optional] 
**syslog_log_time** | **str** | Specifies that events past a specified date are forwarded by the audit syslog forwarder. Format these events as follows: &#39;Topic@YYYY-MM-DD HH:MM:SS&#39; format | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


