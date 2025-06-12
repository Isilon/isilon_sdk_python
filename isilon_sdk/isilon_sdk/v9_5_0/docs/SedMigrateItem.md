# SedMigrateItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retry** | **bool** | Set to true to retry KMIP migration in the previous direction for errored nodes. e.g. if error occurred after migrate with &#39;to_server&#x3D;true&#39;, using &#39;sed/migrate&#39; handler with &#39;retry&#x3D;true&#39; will retry migration to server. Similarly, if previous migration was &#39;to_server&#x3D;false&#39;, retry will try to restore back to local. Also note that, whenever a &#39;retry&#39; arg is provided to the handler, regardless of true or false, &#39;to_server&#39; arg will be ignored. i.e. if using the handler with (&#39;retry&#39;:true(or false), &#39;to_server&#39;: true), the &#39;to_server&#39; arg will be ignored and have no effects. | [optional] 
**to_server** | **bool** | Set to true to indicate migrating all keys to server. Set to false to indicate restoring all keys back to local. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


