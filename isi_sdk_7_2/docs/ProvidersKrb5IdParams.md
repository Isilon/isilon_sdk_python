# ProvidersKrb5IdParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keytab_entries** | [**list[ProvidersKrb5IdParamsKeytabEntry]**](ProvidersKrb5IdParamsKeytabEntry.md) | Service principal names to register | [optional] 
**keytab_file** | **str** | Path to a keytab file to import | [optional] 
**manual_keying** | **bool** | Indicates keys are managed manually rather than with kadmin | [optional] 
**name** | **str** | Specifies Kerberos provider name. | [optional] 
**password** | **str** |  | [optional] 
**realm** | **str** | Name of realm we are joined to | [optional] 
**status** | **str** | The status of the provider. | [optional] 
**user** | **str** | Name of the user to use for kadmin tasks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


