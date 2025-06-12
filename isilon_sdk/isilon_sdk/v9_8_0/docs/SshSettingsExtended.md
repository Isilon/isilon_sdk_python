# SshSettingsExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_settings_template** | **str** | Specifies the configuration template for the supported method by which a user is authenticated. | [optional] 
**authentication_methods** | **str** | Specifies the authentication methods that must be successfully completed for a user to be granted access. | [optional] 
**banner** | **str** | Specifies file name to be used as SSH warning banner that is shown before the password prompt | [optional] 
**ca_signature_algorithms** | **str** | Specifies which algorithms are allowed for signing of certificates by certificate authorities (CAs). | [optional] 
**challenge_response_authentication** | **bool** | Specifies whether challenge-response authentication is allowed. | [optional] 
**ciphers** | **str** | Specifies the ciphers allowed for protocol version 2. | [optional] 
**host_key_algorithms** | **str** | Specifies the protocol version 2 host key algorithms the server offers. | [optional] 
**ignore_rhosts** | **bool** | If true, ignores .rhosts and .shosts files. | [optional] 
**kex_algorithms** | **str** | Specifies the available KEX algorithms. | [optional] 
**keyboard_interactive_authentication** | **bool** | Specifies whether to allow keyboard-interactive authentication. | [optional] 
**log_level** | **str** | Specifies the log level when logging messages from sshd(8). | [optional] 
**login_grace_time** | **int** | Specifies the length of time in seconds before idle log in fails.  If the value is 0, there is no time limit. | [optional] 
**macs** | **str** | Specifies the available MAC algorithms. | [optional] 
**match** | **str** | Specifies match blocks. | [optional] 
**max_auth_tries** | **int** | Specifies the maximum number of authentication attempts per connection. | [optional] 
**max_sessions** | **int** | Specifies the maximum number of open sessions permitted per network connection. | [optional] 
**max_startups** | **str** | Specifies maximum number of unauthenticated connections. | [optional] 
**password_authentication** | **bool** | Specifies whether password authentication is allowed. | [optional] 
**permit_empty_passwords** | **bool** | Enable empty passwords if password authentication is allowed. | [optional] 
**permit_root_login** | **bool** | Enable root SSH login. | [optional] 
**port** | **int** | Specifies the port sshd(8) should listen on | [optional] 
**print_motd** | **bool** | Enable printing /etc/motd when a user logs in. | [optional] 
**pubkey_accepted_key_types** | **str** | Specifies the accepted public key types. | [optional] 
**pubkey_authentication** | **bool** | Specifies whether public key authentication is allowed. | [optional] 
**strict_modes** | **bool** | Specifies if sshd(8) should check home directory permissions before accepting login. | [optional] 
**subsystem** | **str** | Specifies an external subsystem. | [optional] 
**syslog_facility** | **str** | Specifies the facility code when logging messages from sshd(8). | [optional] 
**tcp_keep_alive** | **bool** | Enable sending TCP keep alive messages. | [optional] 
**use_dns** | **bool** | Specifies whether sshd should look up the remote host name. | [optional] 
**use_pam** | **bool** | Enables the Pluggable Authentication Module interface. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


