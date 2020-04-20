# ProvidersNisIdParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Enables use of provider for authentication as well as identity. | [optional] 
**balance_servers** | **bool** | Makes provider connect to a random server. | [optional] 
**cache_entry_expiry** | **int** | Specifies amount of time in seconds to cache a user/group. | [optional] 
**check_online_interval** | **int** | Specifies time in seconds between provider online checks. | [optional] 
**create_home_directory** | **bool** | Automatically create home directory on first login. | [optional] 
**enabled** | **bool** | Enables NIS provider. | [optional] 
**enumerate_groups** | **bool** | Enables provider to enumerate groups. | [optional] 
**enumerate_users** | **bool** | Enables provider to enumerate users. | [optional] 
**findable_groups** | **list[str]** | Sets list of groups that can be resolved. | [optional] 
**findable_users** | **list[str]** | Sets list of users that can be resolved. | [optional] 
**group_domain** | **str** | Domain used to qualify groups for this provider. | [optional] 
**home_directory_template** | **str** | Specifies home directory template path. | [optional] 
**hostname_lookup** | **bool** | Enables host name lookups. | [optional] 
**listable_groups** | **list[str]** | Specifies groups that can be viewed in the provider. | [optional] 
**listable_users** | **list[str]** | Specifies users that can be viewed in the provider. | [optional] 
**login_shell** | **str** | Sets login shell path. | [optional] 
**name** | **str** | Specifies NIS provider name. | [optional] 
**nis_domain** | **str** | Specifies NIS domain name. | [optional] 
**normalize_groups** | **bool** | Normalizes group name to lowercase before lookup. | [optional] 
**normalize_users** | **bool** | Normalizes user name to lowercase before lookup. | [optional] 
**ntlm_support** | **str** | For users with NTLM-compatible credentials, specify what NTLM versions to support. | [optional] 
**provider_domain** | **str** | Specifies the provider domain. | [optional] 
**request_timeout** | **int** | Specifies the request timeout interval in seconds. | [optional] 
**restrict_findable** | **bool** | Check the provider for filtered lists of findable and unfindable users and groups. | [optional] 
**restrict_listable** | **bool** | Check the provider for filtered lists of listable and unlistable users and groups. | [optional] 
**retry_time** | **int** | Sets timeout period in seconds after which a request will be retried. | [optional] 
**servers** | **list[str]** | Adds a NIS server to be used by this provider. | [optional] 
**unfindable_groups** | **list[str]** | Specifies a group that cannot be resolved by the provider. | [optional] 
**unfindable_users** | **list[str]** | Specifies a group that cannot be resolved by the provider. | [optional] 
**unlistable_groups** | **list[str]** | Specifies a group that cannot be listed by the provider. | [optional] 
**unlistable_users** | **list[str]** | Specifies a user that cannot be listed by the provider. | [optional] 
**user_domain** | **str** | Domain used to qualify users for this provider. | [optional] 
**ypmatch_using_tcp** | **bool** | Uses TCP for YP Match operations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


