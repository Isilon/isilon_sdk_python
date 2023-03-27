# CreateProvidersSamlServicesMetadataExtractItemResponseSigningCertificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fingerprints** | [**list[CertificatesCaCertificateFingerprint]**](CertificatesCaCertificateFingerprint.md) | A list of zero or more certificate fingerprints which can be used for certificate identification. | [optional] 
**issuer** | **str** | Certificate issuer field extracted from the certificate. | [optional] 
**not_after** | **int** | Certificate notAfter field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid after this timestamp. | [optional] 
**not_before** | **int** | Certificate notBefore field extracted from the certificate encoded as a UNIX epoch timestamp.  The certificate is not valid before this timestamp. | [optional] 
**status** | **str** | Certificate validity status | [optional] 
**subject** | **str** | Certificate subject field extracted from the certificate. | [optional] 
**value** | [**ProvidersSamlServicesCertExtractSettingsCertificateInfoValue**](ProvidersSamlServicesCertExtractSettingsCertificateInfoValue.md) | Certificate data. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


