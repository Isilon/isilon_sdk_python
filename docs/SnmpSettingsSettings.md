# SnmpSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_only_community** | **str** | The read-only community name.  @DEFAULT reverts this field to its default value. | [optional] 
**service** | **bool** | Whether the SNMP service is enabled. | [optional] 
**snmp_v1_v2c_access** | **bool** | Whether SNMP v1 and v2c protocols are enabled.  @DEFAULT reverts this field to its default value. | [optional] 
**snmp_v3_access** | **bool** | Whether SNMP v3 is enabled.  @DEFAULT reverts this field to its default value. | [optional] 
**snmp_v3_auth_protocol** | **str** | SNMPv3 authentication protocol. May only be SHA or MD5.  @DEFAULT reverts this field to its default value. | [optional] 
**snmp_v3_priv_protocol** | **str** | SNMPv3 privacy protocol. May only be AES or DES. @DEFAULT reverts this field to its default value. | [optional] 
**snmp_v3_read_only_user** | **str** | The read-only user for SNMP v3 read requests.  @DEFAULT reverts this field to its default value. | [optional] 
**snmp_v3_security_level** | **str** | SNMPv3 privacy protocol. May only be AES or DES. @DEFAULT reverts this field to its default value. | [optional] 
**system_contact** | **str** | Contact information for the system owner.  This must be a valid email address.  @DEFAULT reverts this field to its default value. | [optional] 
**system_location** | **str** | A location name for the SNMP system.  @DEFAULT reverts this field to its default value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


