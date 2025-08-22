# OauthCertificateCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The certificate content encoded as PEM string (including header, footer and line break). | 
**certificate_format** | **str** | The encoding format of the certificate string. | 
**passphrase** | **str** | Passphrase used to encrypt private key. | [optional] 
**private_key** | **str** | PEM encoded (including header, footer and line break) private key following encrypted PKCS8. | [optional] 
**scope** | **str** | Scope narrows the application of a certificate to a specific instance of a service. | [optional] 
**service** | **str** | The kind of the service for which the certificate is used. | 
**type** | **str** | Whether the certificate is used as client or server certificate, and whether it is a CA certificate. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


