# UpgradeClusterFirmwareStatusNodeDevice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The name of the device. | [optional] 
**mismatch** | **bool** | Is the firmware up-to-date for this component. | [optional] 
**target_version** | **str** | The target firmware version. | [optional] 
**type** | **str** | The device type. | [optional] 
**upgrade_status** | **str** | The current state of the firmware upgrade for this component. One of the following values: &#39;queued&#39;, &#39;upgrading&#39;, &#39;upgraded&#39;, &#39;error&#39;. or &#39;null&#39;.&#39;null&#39; indicates that the upgrade status is unknown. | [optional] 
**version** | **str** | The current firmware version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


