# ProvidersAdsItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **str** | Machine account name to use in AD. Default is the cluster name. | [optional] 
**allocate_gids** | **bool** | Allocate GIDs for unmapped AD groups. | [optional] 
**allocate_uids** | **bool** | Enables allocation of UIDs for unmapped AD users. | [optional] 
**assume_default_domain** | **bool** | Enables lookup of unqualified user names in the primary domain. | [optional] 
**authentication** | **bool** | Enables use of provider for authentication as well as identity. | [optional] 
**cache_entry_expiry** | **int** | Specifies amount of time in seconds to cache a user/group. | [optional] 
**check_online_interval** | **int** | Specifies time in seconds between provider online checks. | [optional] 
**controller_time** | **int** | The domain controllers current time. | [optional] 
**create_home_directory** | **bool** | Automatically create home directory on first login. | [optional] 
**dns_domain** | **str** | The DNS search domain.  Set if DNS search domain differs. | [optional] 
**domain_offline_alerts** | **bool** | Send an alert if the domain goes offline. | [optional] 
**home_directory_template** | **str** | Specifies home directory template path. | [optional] 
**ignore_all_trusts** | **bool** | Ignores all trusted domains. | [optional] 
**ignored_trusted_domains** | **list[str]** | Includes trusted domains when ignore_all_trusts false. | [optional] 
**include_trusted_domains** | **list[str]** | Includes trusted domains when ignore_all_trusts is true. | [optional] 
**kerberos_hdfs_spn** | **bool** | SPN for using Kerberized HDFS. | [optional] 
**kerberos_nfs_spn** | **bool** | SPN for using Kerberized NFS. | [optional] 
**ldap_sign_and_seal** | **bool** | Uses encryption and signing on LDAP requests. | [optional] 
**login_shell** | **str** | Sets login shell path. | [optional] 
**lookup_domains** | **list[str]** | Limits user and group lookups to the specified domains. | [optional] 
**lookup_groups** | **bool** | Looks up AD groups in other providers before allocating a GID. | [optional] 
**lookup_normalize_groups** | **bool** | Normalizes AD group names to lowercase before lookup. | [optional] 
**lookup_normalize_users** | **bool** | Normalize AD user names to lowercase before lookup. | [optional] 
**lookup_users** | **bool** | Looks up AD users in other providers before allocating a UID. | [optional] 
**machine_password_changes** | **bool** | Enables periodic changes of machine password for security. | [optional] 
**machine_password_lifespan** | **int** | Sets maximum age of a password in seconds. | [optional] 
**name** | **str** | Specifies Active Directory provider name. | 
**node_dc_affinity** | **str** | Specifies the domain controller to which the node should affinitize | [optional] 
**node_dc_affinity_timeout** | **int** | Specifies the timeout for the local node affinity to a domain controller | [optional] 
**nss_enumeration** | **bool** | Enables the Active Directory provider to respond to getpwent and getgrent requests. | [optional] 
**organizational_unit** | **str** | The organizational unit. | [optional] 
**password** | **str** | Password used during domain join. | 
**sfu_support** | **str** | Specifies whether to support RFC 2307 attributes for Windows domain controllers. | [optional] 
**store_sfu_mappings** | **bool** | Stores SFU mappings permanently in the ID mapper. | [optional] 
**user** | **str** | User name with permission to join machine to the given domain. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


