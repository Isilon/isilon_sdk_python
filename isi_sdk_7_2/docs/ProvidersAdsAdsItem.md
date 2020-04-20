# ProvidersAdsAdsItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocate_gids** | **bool** | Allocate GIDs for unmapped AD groups. | [optional] 
**allocate_uids** | **bool** | Enables allocation of UIDs for unmapped AD users. | [optional] 
**assume_default_domain** | **bool** | Enables lookup of unqualified user names in the primary domain. | [optional] 
**authentication** | **bool** | Enables use of provider for authentication as well as identity. | [optional] 
**cache_entry_expiry** | **int** | Specifies amount of time in seconds to cache a user/group. | [optional] 
**check_online_interval** | **int** | Specifies time in seconds between provider online checks. | [optional] 
**controller_time** | **int** | The domain controllers current time. | [optional] 
**create_home_directory** | **bool** | Automatically create home directory on first login. | [optional] 
**domain_offline_alerts** | **bool** | Send an alert if the domain goes offline. | [optional] 
**forest** | **str** | The active directory forest. | [optional] 
**home_directory_template** | **str** | Specifies home directory template path. | [optional] 
**hostname** | **str** | The fully qualified hostname stored in the machine account. | [optional] 
**id** | **str** | Specifies Active Directory provider ID. | [optional] 
**ignore_all_trusts** | **bool** | Ignores all trusted domains. | [optional] 
**ignored_trusted_domains** | **list[str]** | Includes trusted domains when ignore_all_trusts false. | [optional] 
**include_trusted_domains** | **list[str]** | Includes trusted domains when ignore_all_trusts is true. | [optional] 
**ldap_sign_and_seal** | **bool** | Uses encryption and signing on LDAP requests. | [optional] 
**login_shell** | **str** | Sets login shell path. | [optional] 
**lookup_domains** | **list[str]** | Limits user and group lookups to the specified domains. | [optional] 
**lookup_groups** | **bool** | Looks up AD groups in other providers before allocating a GID. | [optional] 
**lookup_normalize_groups** | **bool** | Normalizes AD group names to lowercase before lookup. | [optional] 
**lookup_normalize_users** | **bool** | Normalize AD user names to lowercase before lookup. | [optional] 
**lookup_users** | **bool** | Looks up AD users in other providers before allocating a UID. | [optional] 
**machine_account** | **str** | The SAM account name of the machine account. | [optional] 
**machine_password_changes** | **bool** | Enables periodic changes of machine password for security. | [optional] 
**machine_password_lifespan** | **int** | Sets maximum age of a password in seconds. | [optional] 
**name** | **str** | Specifies Active Directory provider name. | [optional] 
**netbios_domain** | **str** | NetBIOS domain name associated with the machine account. | [optional] 
**node_dc_affinity** | **str** | Specifies the domain controller to which the node should affinitize | [optional] 
**node_dc_affinity_timeout** | **int** | Specifies the timeout for the local node affinity to a domain controller | [optional] 
**nss_enumeration** | **bool** | Enables the Active Directory provider to respond to getpwent and getgrent requests. | [optional] 
**primary_domain** | **str** | The AD domain to which the provider is joined. | [optional] 
**sfu_support** | **str** | Specifies whether to support RFC 2307 attributes for Windows domain controllers. | [optional] 
**site** | **str** | The active directory site. | [optional] 
**status** | **str** | The status of the provider. | [optional] 
**store_sfu_mappings** | **bool** | Stores SFU mappings permanently in the ID mapper. | [optional] 
**system** | **bool** | If true, this provider instance was created by OneFS and cannot be removed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


