# ProvidersFileIdParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Enables use of provider for authentication as well as identity. | [optional] 
**cache_entry_expiry** | **int** | Specifies amount of time in seconds to cache a user/group. | [optional] 
**create_home_directory** | **bool** | Automatically create home directory on first login. | [optional] 
**enabled** | **bool** | Enables the file provider. | [optional] 
**enumerate_groups** | **bool** | Enables provider to enumerate groups. | [optional] 
**enumerate_users** | **bool** | Enables provider to enumerate users. | [optional] 
**findable_groups** | **list[str]** | Sets list of groups that can be resolved. | [optional] 
**findable_users** | **list[str]** | Sets list of users that can be resolved. | [optional] 
**group_domain** | **str** | Domain used to qualify groups for this provider. | [optional] 
**group_file** | **str** | Location of the file containing group information. | [optional] 
**home_directory_template** | **str** | Specifies home directory template path. | [optional] 
**listable_groups** | **list[str]** | Specifies groups that can be viewed in the provider. | [optional] 
**listable_users** | **list[str]** | Specifies users that can be viewed in the provider. | [optional] 
**login_shell** | **str** | Sets login shell path. | [optional] 
**modifiable_groups** | **list[str]** | Specifies groups that can be modified in the provider. | [optional] 
**modifiable_users** | **list[str]** | Specifies users that can be modified in the provider. | [optional] 
**name** | **str** | Specifies file provider name. | [optional] 
**netgroup_file** | **str** | Path to a netgroups replacement file. | [optional] 
**normalize_groups** | **bool** | Normalizes group name to lowercase before lookup. | [optional] 
**normalize_users** | **bool** | Normalizes user name to lowercase before lookup. | [optional] 
**ntlm_support** | **str** | For users with NTLM-compatible credentials, specify what NTLM versions to support. | [optional] 
**password_file** | **str** | Location of the file containing user information. | [optional] 
**provider_domain** | **str** | Specifies the provider domain. | [optional] 
**restrict_findable** | **bool** | Check the provider for filtered lists of findable and unfindable users and groups. | [optional] 
**restrict_listable** | **bool** | Check the provider for filtered lists of listable and unlistable users and groups. | [optional] 
**restrict_modifiable** | **bool** | Check the provider for filtered lists of modifiable and unmodifiable users and groups. | [optional] 
**unfindable_groups** | **list[str]** | Specifies a group that cannot be resolved by the provider. | [optional] 
**unfindable_users** | **list[str]** | Specifies a group that cannot be resolved by the provider. | [optional] 
**unlistable_groups** | **list[str]** | Specifies a group that cannot be listed by the provider. | [optional] 
**unlistable_users** | **list[str]** | Specifies a user that cannot be listed by the provider. | [optional] 
**unmodifiable_groups** | **list[str]** | Specifies a group that cannot be modified by the provider. | [optional] 
**unmodifiable_users** | **list[str]** | Specifies a user that cannot be modified by the provider. | [optional] 
**user_domain** | **str** | Domain used to qualify users for this provider. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


