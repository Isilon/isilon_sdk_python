# PoolsPoolInterfacesInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique interface ID. | 
**ip_addrs** | **list[str]** | List of IP addresses | 
**lnn** | **int** | Logical Node Number | 
**name** | **str** | The name of the interface. | 
**nic_name** | **str** | NIC name | 
**owners** | [**list[PoolsPoolInterfacesInterfaceOwner]**](PoolsPoolInterfacesInterfaceOwner.md) | List of owners (membership) | 
**status** | **str** | Status of the interface | 
**type** | **str** | Interface type.  The &#39;*gige&#39; types stand for &#39;gigabit ethernet&#39;.  &#39;gige&#39; itself is occasionally also referred to in other places as &#39;ext&#39; for &#39;external&#39;.  &#39;ib&#39; and &#39;ib_qdr&#39; are internal Infiniband interface types.  &#39;vlan&#39; and &#39;vmxnet3&#39; are virtual interface types that appear on virtual nodes.  &#39;loopback&#39; is an interface for failover addresses and should only appear if failover is configured. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


