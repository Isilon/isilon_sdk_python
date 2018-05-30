# NamespaceObject

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_time** | **str** | Specifies the date when the object was last accessed in HTTP date/time format. | [optional] 
**atime_val** | **int** | Specifies the time when the object was last accessed in UNIX Epoch format. | [optional] 
**block_size** | **int** | Specifies the block size of the object. | [optional] 
**blocks** | **int** | Specifies the number of blocks that compose the object. | [optional] 
**btime_val** | **int** | Specifies the time when the object data was created in UNIX Epoch format. | [optional] 
**change_time** | **str** | Specifies the date when the object was last changed (including data and metadata changes) in HTTP date/time format. | [optional] 
**create_time** | **str** | Specifies the date when the object data was created in HTTP date/time format. | [optional] 
**ctime_val** | **int** | Specifies the time when the object was last changed (including data and metadata changes) in UNIX Epoch format. | [optional] 
**gid** | **int** | Specifies the GID for the owner. | [optional] 
**group** | **str** | Specifies the group name for the owner of the object. | [optional] 
**id** | **int** | Specifies the object ID, which is also the INODE number. | [optional] 
**is_hidden** | **bool** | Specifies whether the file is hidden or not. | [optional] 
**last_modified** | **str** | Specifies the time when the object data was last modified in HTTP date/time format. | [optional] 
**mode** | **str** | Specifies the UNIX mode octal number. | [optional] 
**mtime_val** | **int** | Specifies the time when the object data was last modified in UNIX Epoch format. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**nlink** | **int** | Specifies the number of hard links to the object. | [optional] 
**owner** | **str** | Specifies the user name for the owner of the object. | [optional] 
**size** | **int** | Specifies the size of the object in bytes. | [optional] 
**stub** | **bool** |  | [optional] 
**type** | **str** | Specifies the object type, which can be one of the following values: container, object, pipe, character_device, block_device, symbolic_link, socket, or whiteout_file. | [optional] 
**uid** | **int** | Specifies the UID for the owner. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


