# ProvidersKrb5IdParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keytab_entries** | [**list[ProvidersKrb5IdParamsKeytabEntry]**](ProvidersKrb5IdParamsKeytabEntry.md) | Specifies the key information for the Kerberos SPNs. | [optional] 
**keytab_file** | **str** | Specifies the path to a keytab file to import. | [optional] 
**manual_keying** | **bool** | If true, keys are managed manually. If false, keys are managed through kadmin. | [optional] 
**name** | **str** | Specifies the Kerberos provider name. | [optional] 
**password** | **str** | Specifies the Kerberos provider password. | [optional] 
**realm** | **str** | Specifies the name of realm. | [optional] 
**status** | **str** | Specifies the status of the provider. | [optional] 
**user** | **str** | Specifies the name of the user that performs kadmin tasks. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


