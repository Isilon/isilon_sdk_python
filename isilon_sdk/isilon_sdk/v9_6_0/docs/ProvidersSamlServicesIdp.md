# ProvidersSamlServicesIdp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | Unique identifier of the IDP. | [optional] 
**id** | **str** | Unique identifier of a SAML service resource. | [optional] 
**login** | [**ProvidersSamlServicesIdpLogin**](ProvidersSamlServicesIdpLogin.md) | Login endpoint of the IDP. This specifies the method and location PowerScale will use to send AuthnRequest messages to the IDP. | [optional] 
**logout** | [**ProvidersSamlServicesIdpLogout**](ProvidersSamlServicesIdpLogout.md) |  | [optional] 
**metadata** | **str** | Metadata XML data of the SAML provider. | [optional] 
**metadata_location** | **str** | Metadata location of the SAML provider. | [optional] 
**signing_certificate** | **str** | PEM-encoded certificate used to verify messages from the IDP. | [optional] 
**signing_certificate_path** | **str** | Path to the PEM-encoded certificate used to verify messages from the IDP. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


