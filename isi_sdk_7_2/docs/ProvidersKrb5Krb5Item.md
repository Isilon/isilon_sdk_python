# ProvidersKrb5Krb5Item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies Kerberos provider ID. | [optional] 
**keytab_entries** | [**list[ProvidersKrb5IdParamsKeytabEntry]**](ProvidersKrb5IdParamsKeytabEntry.md) | Service principal names to register | [optional] 
**keytab_file** | **str** | Path to a keytab file to import | [optional] 
**manual_keying** | **bool** | Indicates keys are managed manually rather than with kadmin | [optional] 
**name** | **str** | Specifies Kerberos provider name. | [optional] 
**realm** | **str** | Name of realm we are joined to | [optional] 
**recommended_spns** | **list[str]** | Service principal names advised to be populated | [optional] 
**status** | **str** | The status of the provider. | [optional] 
**system** | **bool** | If true, this provider instance was created by OneFS and cannot be removed | [optional] 
**user** | **str** | Name of the user to use for kadmin tasks | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


