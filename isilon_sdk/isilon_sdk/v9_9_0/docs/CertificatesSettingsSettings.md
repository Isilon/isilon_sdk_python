# CertificatesSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_encryption** | **bool** | Enables encryption. If disabled, TLS handshakes still must succeed, but once successful, traffic is left unencrypted. | [optional] 
**ocsp_uri** | **str** | The URI of the server to check revocation status against if the received certificate does not contain an AIA extension. | [optional] 
**revocation_setting** | **str** | The strictness of revocation checking to use.NONE:  Don&#39;t check for revoked certificates.STRICT: Check for revoked certificates and fail the handshake if any certificate in the chain is revoked, or if revocation status data cannot be obtained.ALLOW_NO_REVOKE_SRC: Allow handshakes to proceed if a certificate does not contain information on where to check for revocation (e.g. no OCSP responder field).ALLOW_REVOKE_DATA_UNAVAILABLE: Attempt to check each certificate for revocation status, but proceed if revocation status information is unavailable. | [optional] 
**strict_hostname_check** | **bool** | If enabled, the CN in the certificate presented by the remote host must match the CN used to connect to that host for the handshake to succeed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


