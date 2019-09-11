# ProvidersFileFileItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Enables authentication and identity mapping through the authentication provider. | [optional] 
**create_home_directory** | **bool** | Automatically creates a home directory on the first login. | [optional] 
**enabled** | **bool** | Enables the file provider. | [optional] 
**enumerate_groups** | **bool** | Enables the provider to enumerate groups. | [optional] 
**enumerate_users** | **bool** | Enables the provider to enumerate users. | [optional] 
**findable_groups** | **list[str]** | Specifies the list of groups that can be resolved. | [optional] 
**findable_users** | **list[str]** | Specifies the list of users that can be resolved. | [optional] 
**group_domain** | **str** | Specifies the domain for this provider through which domains are qualified. | [optional] 
**group_file** | **str** | Specifies the location of the file that contains information about the group. | [optional] 
**home_directory_template** | **str** | Specifies the path to the home directory template. | [optional] 
**id** | **str** | Specifies the file provider ID. | [optional] 
**listable_groups** | **list[str]** | Specifies the groups that can be viewed in the provider. | [optional] 
**listable_users** | **list[str]** | Specifies the users that can be viewed in the provider. | [optional] 
**login_shell** | **str** | Specifies the login shell path. | [optional] 
**modifiable_groups** | **list[str]** | Specifies the groups that can be modified in the provider. | [optional] 
**modifiable_users** | **list[str]** | Specifies the users that can be modified in the provider. | [optional] 
**name** | **str** | Specifies the name of the file provider. | [optional] 
**netgroup_file** | **str** | Specifies the path to a netgroups replacement file. | [optional] 
**normalize_groups** | **bool** | Normalizes group names to lowercase before look up. | [optional] 
**normalize_users** | **bool** | Normalizes user names to lowercase before look up. | [optional] 
**ntlm_support** | **str** | Specifies which NTLM versions to support for users with NTLM-compatible credentials. | [optional] 
**password_file** | **str** | Specifies the location of the file containing information about users. | [optional] 
**provider_domain** | **str** | Specifies the domain for the provider. | [optional] 
**restrict_findable** | **bool** | If true, checks the provider for filtered lists of findable and unfindable users and groups. | [optional] 
**restrict_listable** | **bool** | If true, checks the provider for filtered lists of listable and unlistable users and groups. | [optional] 
**restrict_modifiable** | **bool** | If true, checks the provider for filtered lists of modifiable and unmodifiable users and groups. | [optional] 
**status** | **str** | Specifies the status of the provider. | [optional] 
**system** | **bool** | If true, indicates that this provider instance was created by OneFS and cannot be removed. | [optional] 
**unfindable_groups** | **list[str]** | Specifies groups that cannot be resolved by the provider. | [optional] 
**unfindable_users** | **list[str]** | Specifies users that cannot be resolved by the provider. | [optional] 
**unlistable_groups** | **list[str]** | Specifies a group that cannot be listed by the provider. | [optional] 
**unlistable_users** | **list[str]** | Specifies a user that cannot be listed by the provider. | [optional] 
**unmodifiable_groups** | **list[str]** | Specifies a group that cannot be modified by the provider. | [optional] 
**unmodifiable_users** | **list[str]** | Specifies a user that cannot be modified by the provider. | [optional] 
**user_domain** | **str** | Specifies the domain for this provider through which users are qualified. | [optional] 
**zone_name** | **str** | Specifies the name of the access zone in which this provider was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


