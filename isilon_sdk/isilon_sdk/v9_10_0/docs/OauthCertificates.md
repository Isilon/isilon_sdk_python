# OauthCertificates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_fingerprint** | **str** | The hexadecimal representation of the certificate hash, using SHA-256 hash algorithm. | [optional] 
**certificate** | **str** | The certificate content encoded as PEM string (including header, footer and line break). | [optional] 
**common_name** | **str** | The fully qualified domain name of the certificate. | [optional] 
**id** | **str** | Unique identifier of certificate. | [optional] 
**is_current** | **bool** | Indicates whether this is the current certificate to be used by the service. When is_current is false for a certificate, that certificate will not be used by the service. | [optional] 
**is_valid** | **bool** | Indicates whether this is a valid certificate. | [optional] 
**issuer** | **str** | Distinguished name of the certificate issuer. | [optional] 
**scope** | **str** | Scope narrows the application of a certificate to a specific instance of a service. | [optional] 
**service** | **str** | The kind of the service for which the certificate is used. | [optional] 
**signature_algorithm** | **str** | The kind of signature algorithm used for the certificate. | [optional] 
**signature_hash_algorithm** | **str** | The kind of signature hash algorithm used for the certificate. | [optional] 
**subject** | **str** | Certificate subject field extracted from the certificate. | [optional] 
**subject_alternative_names** | **list[str]** | Array of host names of the component to secure, as defined by the RFC5280 subjectAltName attribute. | [optional] 
**type** | **str** | Whether the certificate is used as client or server certificate, and whether it is a CA certificate. | [optional] 
**valid_from_timestamp** | **str** | The date in &#39;%Y-%m-%dT%H:%M:%SZ&#39; format when the certificate becomes valid. | [optional] 
**valid_to_timestamp** | **str** | The date in &#39;%Y-%m-%dT%H:%M:%SZ&#39; format when the certificate is no longer valid. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


