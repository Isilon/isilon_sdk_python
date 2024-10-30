# ProvidersSamlServicesIdpsIdp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Unique identifier of the IDP. | [optional] 
**id** | **str** | Unique identifier of a SAML service resource. | [optional] 
**login** | [**ProvidersSamlServicesIdpLogin**](ProvidersSamlServicesIdpLogin.md) | Login endpoint of the IDP. This specifies the method and location PowerScale will use to send AuthnRequest messages to the IDP. | [optional] 
**logout** | [**ProvidersSamlServicesIdpLogout**](ProvidersSamlServicesIdpLogout.md) |  | [optional] 
**metadata_location** | **str** | Metadata location of the SAML provider. | [optional] 
**signing_certificate** | [**ProvidersSamlServicesCertExtractSettingsCertificateInfo**](ProvidersSamlServicesCertExtractSettingsCertificateInfo.md) | Certificate with information about it. | [optional] 
**type** | **str** | How the IDP was configured and how it can be updated. When set to \&quot;metadata\&quot; metadata XML was used to configure the IDP and can be used to update it. When set to \&quot;manual\&quot; the IDP was manually configured and can be manually updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


