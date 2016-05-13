# ProvidersNisNisItemExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | If true, enables authentication and identity management through the authentication provider. | [optional] 
**balance_servers** | **bool** | If true, connects the provider to a random server. | [optional] 
**check_online_interval** | **int** | Specifies the time in seconds between provider online checks. | [optional] 
**create_home_directory** | **bool** | Automatically creates the home directory on the first login. | [optional] 
**enabled** | **bool** | If true, enables the NIS provider. | [optional] 
**enumerate_groups** | **bool** | If true, allows the provider to enumerate groups. | [optional] 
**enumerate_users** | **bool** | If true, allows the provider to enumerate users. | [optional] 
**findable_groups** | **list[str]** | Specifies the list of groups that can be resolved. | [optional] 
**findable_users** | **list[str]** | Specifies the list of users that can be resolved. | [optional] 
**group_domain** | **str** | Specifies the domain for this provider through which groups are qualified. | [optional] 
**home_directory_template** | **str** | Specifies the path to the home directory template. | [optional] 
**hostname_lookup** | **bool** | If true, enables host name look ups. | [optional] 
**id** | **str** | Specifies the NIS provider ID. | [optional] 
**listable_groups** | **list[str]** | Specifies the groups that can be viewed in the provider. | [optional] 
**listable_users** | **list[str]** | Specifies the users that can be viewed in the provider. | [optional] 
**login_shell** | **str** | Specifies the login shell path. | [optional] 
**name** | **str** | Specifies the NIS provider name. | [optional] 
**nis_domain** | **str** | Specifies the NIS domain name. | [optional] 
**normalize_groups** | **bool** | Normalizes group names to lowercase before look up. | [optional] 
**normalize_users** | **bool** | Normalizes user names to lowercase before look up. | [optional] 
**ntlm_support** | **str** | Specifies which NTLM versions to support for users with NTLM-compatible credentials. | [optional] 
**provider_domain** | **str** | Specifies the domain for the provider. | [optional] 
**request_timeout** | **int** | Specifies the request timeout interval in seconds. | [optional] 
**restrict_findable** | **bool** | If true, checks the provider for filtered lists of findable and unfindable users and groups. | [optional] 
**restrict_listable** | **bool** | If true, checks the provider for filtered lists of listable and unlistable users and groups. | [optional] 
**retry_time** | **int** | Specifies the timeout period in seconds after which a request will be retried. | [optional] 
**servers** | **list[str]** | Adds an NIS server for this provider. | [optional] 
**status** | **str** | Specifies the status of the provider. | [optional] 
**system** | **bool** | If true, indicates that this provider instance was created by OneFS and cannot be removed. | [optional] 
**unfindable_groups** | **list[str]** | Specifies groups that cannot be resolved by the provider. | [optional] 
**unfindable_users** | **list[str]** | Specifies users that cannot be resolved by the provider. | [optional] 
**unlistable_groups** | **list[str]** | Specifies a group that cannot be listed by the provider. | [optional] 
**unlistable_users** | **list[str]** | Specifies a user that cannot be listed by the provider. | [optional] 
**user_domain** | **str** | Specifies the domain for this provider through which users are qualified. | [optional] 
**ypmatch_using_tcp** | **bool** | If true, specifies TCP for YP Match operations. | [optional] 
**groupnet** | **str** | Groupnet identifier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


