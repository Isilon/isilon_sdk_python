# CertificateServerCertificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Boolean identifying if a certificate is the default certificate.The default certificate is used as the fallback when no other certificates match a TLS enabled service&#39;s particular criteria. There must always be a configured default certificate. | 
**description** | **str** | Description field associated with a certificate provided for administrative convenience. | 
**dnsnames** | **list[str]** | A list of DNS names/patterns for which this certificate is valid. This list is extracted from the certificates CN (Common Name) and subjectAtlName extension fields. | 
**expired** | **bool** | True if the certificate has expired and is no longer valid. | 
**fingerprints** | [**list[CertificateServerCertificateFingerprint]**](CertificateServerCertificateFingerprint.md) | A list of zero or more certificate fingerprints which can be used for certificate identification. | 
**id** | **str** | Unique server certificate identifier. | 
**issuer** | **str** | Certificate issuer field extracted from the certificate. | 
**name** | **str** | Subject common name extracted from the certificate. | 
**not_after** | **int** | Certificate notAfter field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid after this timestamp. | 
**not_before** | **int** | Certificate notBefore field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid before this timestamp. | 
**subject** | **str** | Certificate subject field extracted from the certificate. | 
**valid** | **bool** | True if the certificate is valid (ie: not_before &lt;&#x3D; now &lt;&#x3D; not_after). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


