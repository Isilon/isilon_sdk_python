# QuotaQuotaUsage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applogical** | **int** | Bytes used by governed data apparent to application. | 
**applogical_ready** | **bool** | True if applogical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job. | 
**fslogical** | **int** | Bytes used by governed data apparent to filesystem. | 
**fslogical_ready** | **bool** | True if fslogical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job. | 
**fsphysical** | **int** | Physical data usage adjusted to account for shadow store efficiency | 
**fsphysical_ready** | **bool** | True if fsphysical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job. | 
**inodes** | **int** | Number of inodes (filesystem entities) used by governed data. | 
**inodes_ready** | **bool** | True if inodes resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job. | 
**physical** | **int** | Bytes used for governed data and filesystem overhead. | 
**physical_ready** | **bool** | True if physical resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job. | 
**shadow_refs** | **int** | Number of shadow references (cloned, deduplicated or packed filesystem blocks) used by governed data. | 
**shadow_refs_ready** | **bool** | True if shadow_refs resource accounting is accurate on the quota. If false, this quota is waiting on completion of a QuotaScan job. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


