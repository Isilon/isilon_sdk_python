# AuditSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audited_zones** | **list[str]** | Zones that are audited when protocol auditing is enabled. | [optional] 
**cee_log_time** | **str** | Sets audit CEE forwarder to forward events past a specified date in &#39;Topic@YYYY-MM-DD HH:MM:SS&#39; format | [optional] 
**cee_server_uris** | **list[str]** | URIs of backend CEE servers to which to send audit logs | [optional] 
**config_auditing_enabled** | **bool** | Enables/disables PAPI configuration audit | [optional] 
**config_syslog_enabled** | **bool** | Enables/disables config audit syslog forwarding. | [optional] 
**hostname** | **str** | Hostname reported in protocol events from this cluster | [optional] 
**protocol_auditing_enabled** | **bool** | Enables/disables auditing of I/O requests | [optional] 
**syslog_log_time** | **str** | Sets audit syslog forwarder to forward events past a specified date in &#39;Topic@YYYY-MM-DD HH:MM:SS&#39; format | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


