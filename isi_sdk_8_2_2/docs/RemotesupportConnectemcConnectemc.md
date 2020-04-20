# RemotesupportConnectemcConnectemc

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_customer_on_failure** | **bool** | Email the customer if all transmission methods fail. | [optional] 
**enabled** | **bool** | Enable ConnectEMC. | [optional] 
**gateway_access_pools** | **list[str]** | List of network pools that are able to connect to the ESRS gateway.  Necessary to enable ConnectEMC. | [optional] 
**primary_esrs_gateway** | **str** | Primary ESRS Gateway. Necessary to enable ConnectEMC. | [optional] 
**secondary_esrs_gateway** | **str** | Secondary ESRS Gateway. Used if Primary is unavailable. | [optional] 
**use_smtp_failover** | **bool** | Use SMPT if primary and secondary gateways are unavailable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


