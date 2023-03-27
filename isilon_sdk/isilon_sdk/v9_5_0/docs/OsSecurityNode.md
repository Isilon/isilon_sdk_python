# OsSecurityNode

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Sequence ID. | [optional] 
**kern_elf32_allow_wx** | **bool** | [ELF32] Allow pages to be mapped simultaneously writable and executable. | [optional] 
**kern_elf32_aslr_enable** | **bool** | [ELF32] Enable address map randomization. | [optional] 
**kern_elf32_aslr_pie_enable** | **bool** | [ELF32] Enable address map randomization for PIE binaries. | [optional] 
**kern_elf32_aslr_stack_gap** | **int** | [ELF32] Maximum percentage of main stack to waste on a random gap. | [optional] 
**kern_elf32_nxstack** | **bool** | [ELF32] Enable non-executable stack. | [optional] 
**kern_elf64_allow_wx** | **bool** | [ELF64] Allow pages to be mapped simultaneously writable and executable. | [optional] 
**kern_elf64_aslr_enable** | **bool** | [ELF64] Enable address map randomization. | [optional] 
**kern_elf64_aslr_pie_enable** | **bool** | [ELF64] Enable address map randomization for PIE binaries. | [optional] 
**kern_elf64_aslr_stack_gap** | **int** | [ELF32] Maximum percentage of main stack to waste on a random gap. | [optional] 
**kern_elf64_nxstack** | **bool** | [ELF64] Enable non-executable stack. | [optional] 
**lnn** | **int** | Logical Node Number. | [optional] 
**vm_aslr_restarts** | **int** | Number of aslr failures. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


