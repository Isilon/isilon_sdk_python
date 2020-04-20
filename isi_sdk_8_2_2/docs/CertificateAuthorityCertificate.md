# CertificateAuthorityCertificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description field associated with a certificate provided for administrative convenience. | 
**fingerprints** | [**list[CertificateServerCertificateFingerprint]**](CertificateServerCertificateFingerprint.md) | A list of zero or more certificate fingerprints which can be used for certificate identification. | 
**id** | **str** | Unique server certificate identifier. | 
**issuer** | **str** | Certificate issuer field extracted from the certificate. | 
**name** | **str** | Administrator specified name identifier. | 
**not_after** | **int** | Certificate notAfter field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid after this timestamp. | 
**not_before** | **int** | Certificate notBefore field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid before this timestamp. | 
**status** | **str** | Certificate validity status | 
**subject** | **str** | Certificate subject field extracted from the certificate. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


