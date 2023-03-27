# ProvidersAdsIdParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocate_gids** | **bool** | Allocates an ID for an unmapped Active Directory (ADS) group. ADS groups without GIDs can be proactively assigned a GID by the ID mapper. If the ID mapper option is disabled, GIDs are not proactively assigned, and when a primary group for a user does not include a GID, the system may allocate one.  | [optional] 
**allocate_uids** | **bool** | Allocates a user ID for an unmapped Active Directory (ADS) user. ADS users without UIDs can be proactively assigned a UID by the ID mapper. IF the ID mapper option is disabled, UIDs are not proactively assigned, and when an identify for a user does not include a UID, the system may allocate one. | [optional] 
**assume_default_domain** | **bool** | Enables lookup of unqualified user names in the primary domain. | [optional] 
**authentication** | **bool** | Enables authentication and identity management through the authentication provider. | [optional] 
**check_online_interval** | **int** | Specifies the time in seconds between provider online checks. | [optional] 
**controller_time** | **int** | Specifies the current time for the domain controllers. | [optional] 
**create_home_directory** | **bool** | Automatically creates a home directory on the first login. | [optional] 
**domain_controller** | **str** | Specifies the domain controller to which the authentication service should send requests | [optional] 
**domain_offline_alerts** | **bool** | Sends an alert if the domain goes offline. | [optional] 
**extra_expected_spns** | **list[str]** | List of additional SPNs to expect beyond what automatic checking routines might find | [optional] 
**findable_groups** | **list[str]** | Sets list of groups that can be resolved. | [optional] 
**findable_users** | **list[str]** | Sets list of users that can be resolved. | [optional] 
**home_directory_template** | **str** | Specifies the path to the home directory template. | [optional] 
**ignore_all_trusts** | **bool** | If set to true, ignores all trusted domains. | [optional] 
**ignored_trusted_domains** | **list[str]** | Includes trusted domains when &#39;ignore_all_trusts&#39; is set to false. | [optional] 
**include_trusted_domains** | **list[str]** | Includes trusted domains when &#39;ignore_all_trusts&#39; is set to true. | [optional] 
**ldap_sign_and_seal** | **bool** | Enables encryption and signing on LDAP requests. | [optional] 
**login_shell** | **str** | Specifies the login shell path. | [optional] 
**lookup_domains** | **list[str]** | Limits user and group lookups to the specified domains. | [optional] 
**lookup_groups** | **bool** | Looks up AD groups in other providers before allocating a group ID. | [optional] 
**lookup_normalize_groups** | **bool** | Normalizes AD group names to lowercase before look up. | [optional] 
**lookup_normalize_users** | **bool** | Normalize AD user names to lowercase before look up. | [optional] 
**lookup_users** | **bool** | Looks up AD users in other providers before allocating a user ID. | [optional] 
**machine_password_changes** | **bool** | Enables periodic changes of the machine password for security. | [optional] 
**machine_password_lifespan** | **int** | Sets maximum age of a password in seconds. | [optional] 
**node_dc_affinity** | **str** | Specifies the domain controller for which the node has affinity. | [optional] 
**node_dc_affinity_timeout** | **int** | Specifies the timeout for the domain controller for which the local node has affinity. | [optional] 
**nss_enumeration** | **bool** | Enables the Active Directory provider to respond to &#39;getpwent&#39; and &#39;getgrent&#39; requests. | [optional] 
**password** | **str** | Specifies the password used during domain join. | [optional] 
**reset_schannel** | **bool** | Resets the secure channel to the primary domain. | [optional] 
**restrict_findable** | **bool** | Check the provider for filtered lists of findable and unfindable users and groups. | [optional] 
**rpc_call_timeout** | **int** | The maximum amount of time (in seconds) an RPC call to Active Directory is allowed to take. | [optional] 
**server_retry_limit** | **int** | The number of retries attempted when a call to Active Directory fails due to network error. | [optional] 
**sfu_support** | **str** | Specifies whether to support RFC 2307 attributes on ADS domain controllers. | [optional] 
**spns** | **list[str]** |  | [optional] 
**store_sfu_mappings** | **bool** | Stores SFU mappings permanently in the ID mapper. | [optional] 
**unfindable_groups** | **list[str]** | Specifies groups that cannot be resolved by the provider. | [optional] 
**unfindable_users** | **list[str]** | Specifies users that cannot be resolved by the provider. | [optional] 
**user** | **str** | Specifies the user name that has permission to join a machine to the given domain. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


