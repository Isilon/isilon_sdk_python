# SettingsKrb5DefaultsKrb5Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_weak_crypto** | **bool** | If true, allow the use of DES encryption | [optional] 
**always_send_preauth** | **bool** | If true, always attempts to preauthenticate to the domain controller. | [optional] 
**default_realm** | **str** | Specifies the realm for unqualified names. | [optional] 
**default_tgs_enctypes** | **list[str]** | Enctypes for ticket granting server | [optional] 
**default_tkt_enctypes** | **list[str]** | Enctypes for tickets | [optional] 
**dns_lookup_kdc** | **bool** | If true, find KDCs through the DNS. | [optional] 
**dns_lookup_realm** | **bool** | If true, find realm names through the DNS. | [optional] 
**permitted_enctypes** | **list[str]** | Enctypes permitted in tickets | [optional] 
**preferred_enctypes** | **list[str]** | Enctypes preferred in tickets | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


