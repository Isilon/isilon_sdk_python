# CreateProvidersSamlServicesMetadataExtractItemResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | The SAML entity ID the rest of this object&#39;s properties are within. | [optional] 
**login_endpoints** | [**list[CreateProvidersSamlServicesMetadataExtractItemResponseLoginEndpoint]**](CreateProvidersSamlServicesMetadataExtractItemResponseLoginEndpoint.md) | A list of endpoints from the metadata that can be used as the login URL when creating an IDP on PowerScale. | [optional] 
**logout_endpoints** | [**list[CreateProvidersSamlServicesMetadataExtractItemResponseLogoutEndpoint]**](CreateProvidersSamlServicesMetadataExtractItemResponseLogoutEndpoint.md) | A list of endpoints from the metadata that can be used as the logout URL when creating an IDP on PowerScale. | [optional] 
**signing_certificates** | [**list[CreateProvidersSamlServicesMetadataExtractItemResponseSigningCertificate]**](CreateProvidersSamlServicesMetadataExtractItemResponseSigningCertificate.md) | A list of signing certificates from the metadata&#39;s IDP. Only signing certificates with a status property of valid can be used to create an IDP on PowerScale. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


