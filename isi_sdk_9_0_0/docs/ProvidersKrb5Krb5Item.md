# ProvidersKrb5Krb5Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupnet** | **str** | Groupnet identifier. | [optional] 
**id** | **str** | Specifies the Kerberos provider ID. | [optional] 
**keytab_entries** | [**list[ProvidersKrb5IdParamsKeytabEntry]**](ProvidersKrb5IdParamsKeytabEntry.md) | Specifies the key information for the Kerberos SPNs. | [optional] 
**keytab_file** | **str** | Specifies the path to a keytab file to import. | [optional] 
**manual_keying** | **bool** | If true, keys are managed manually. If false, keys are managed through kadmin. | [optional] 
**name** | **str** | Specifies the Kerberos provider name. | [optional] 
**realm** | **str** | Specifies the name of realm. | [optional] 
**recommended_spns** | **list[str]** | Specifies the recommended SPNs. | [optional] 
**status** | **str** | Specifies the status of the provider. | [optional] 
**system** | **bool** | If true, indicates that this provider instance was created by OneFS and cannot be removed | [optional] 
**user** | **str** | Specifies the name of the user that performs kadmin tasks. | [optional] 
**zone_name** | **str** | Specifies the name of the access zone in which this provider was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


