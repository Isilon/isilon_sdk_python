# SupportassistDataItemData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | It has two parts, first part shows status of message second part describes upload status, True-Upload Successful, False-Upload Failed | 
**operation** | **str** | Operation type of transaction. | 
**sent_transaction_id** | **str** | Payload&#39;s sent-transaction-id. It contain the same value as &#x60;transaction-id&#x60; if one was not supplied as part of the request. If one was supplied with the request, the supplied value will be present here. | [optional] 
**status** | **str** | Payload status. | 
**transaction_id** | **str** | Payload&#39;s transaction ID - matches &#x60;x-dell-ese-trans-id&#x60; ofthe response header returned from Product -&gt; ESE /Payload request. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


