# NfsSettingsZoneSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfsv4_allow_numeric_ids** | **bool** | Send owners/groups as UIDs/GIDs when lookups fail or if no_names&#x3D;1 (v4) | [optional] 
**nfsv4_domain** | **str** | The domain or realm used to associate users and groups. | [optional] 
**nfsv4_no_domain** | **bool** | Send owners/groups without domainname (v4) | [optional] 
**nfsv4_no_domain_uids** | **bool** | Send UIDs/GIDs without domainname (v4) | [optional] 
**nfsv4_no_names** | **bool** | Always send owners/groups as UIDs/GIDs (v4) | [optional] 
**nfsv4_replace_domain** | **bool** | Replace owner/group domain with nfs domainname. (v4) | [optional] 
**zone** | **str** | The zone in which these settings apply | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


