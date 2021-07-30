# FtpSettingsSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accept_timeout** | **int** | The timeout, in seconds, for a remote client to establish a PASV style data connection. | [optional] 
**allow_anon_access** | **bool** | Controls whether anonymous logins are permitted or not. | [optional] 
**allow_anon_upload** | **bool** | Controls whether anonymous users will be permitted to upload files. | [optional] 
**allow_dirlists** | **bool** | If set to false, all directory list commands will return a permission denied error. | [optional] 
**allow_downloads** | **bool** | If set to false, all downloads requests will return a permission denied error. | [optional] 
**allow_local_access** | **bool** | Controls whether local logins are permitted or not. | [optional] 
**allow_writes** | **bool** | This controls whether any FTP commands which change the filesystem are allowed or not. | [optional] 
**always_chdir_homedir** | **bool** | This controls whether FTP will always initially change directories to the home directory of the user, regardless of whether it is chroot-ing. | [optional] 
**anon_chown_username** | **str** | This is the name of the user who is given ownership of anonymously uploaded files. | [optional] 
**anon_password_list** | **list[str]** | A list of passwords for anonymous users. | [optional] 
**anon_root_path** | **str** | This option represents a directory in /ifs which vsftpd will try to change into after an anonymous login. | [optional] 
**anon_umask** | **int** | The value that the umask for file creation is set to for anonymous users. | [optional] 
**ascii_mode** | **str** | Controls whether ascii mode data transfers are honored for various types of requests. | [optional] 
**chroot_exception_list** | **list[str]** | A list of users that are not chrooted when logging in. | [optional] 
**chroot_local_mode** | **str** | If set to &#39;all&#39;, all local users will be (by default) placed in a chroot() jail in their home directory after login. If set to &#39;all-with-exceptions&#39;, all local users except those listed in the chroot exception list (isi ftp chroot-exception-list) will be placed in a chroot() jail in their home directory after login. If set to &#39;none&#39;, no local users will be chrooted by default. If set to &#39;none-with-exceptions&#39;, only the local users listed in the chroot exception list (isi ftp chroot-exception-list) will be place in a chroot() jail in their home directory after login. | [optional] 
**connect_timeout** | **int** | The timeout, in seconds, for a remote client to respond to our PORT style data connection. | [optional] 
**data_timeout** | **int** | The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off. | [optional] 
**denied_user_list** | **list[str]** | A list of uses that will be denied access. | [optional] 
**dirlist_localtime** | **bool** | If enabled, display directory listings with the time in your local time zone. The default is to display GMT. The times returned by the MDTM FTP command are also affected by this option. | [optional] 
**dirlist_names** | **str** | When set to &#39;hide&#39;,  all user and group information in directory listings will be displayed as &#39;ftp&#39;. When set to &#39;textual&#39;, textual names are shown in the user and group fields of directory listings. When set to &#39;numeric&#39;, numeric IDs are show in the user and group fields of directory listings. | [optional] 
**file_create_perm** | **int** | The permissions with which uploaded files are created. Umasks are applied on top of this value. | [optional] 
**limit_anon_passwords** | **bool** | This field determines whether the anon_password_list is used. | [optional] 
**local_root_path** | **str** | This option represents a directory in /ifs which vsftpd will try to change into after a local login. | [optional] 
**local_umask** | **int** | The value that the umask for file creation is set to for local users. | [optional] 
**server_to_server** | **bool** | If enabled, allow server-to-server (FXP) transfers. | [optional] 
**service** | **bool** | This field controls whether the FTP daemon is running. | [optional] 
**session_support** | **bool** | If enabled, maintain login sessions for each user through Pluggable Authentication Modules (PAM). Disabling this option prevents the ability to do automatic home directory creation if that functionality were otherwise available. | [optional] 
**session_timeout** | **int** | The timeout, in seconds, which is roughly the maximum time we permit data transfers to stall for with no progress. If the timeout triggers, the remote client is kicked off. | [optional] 
**user_config_dir** | **str** | Specifies the directory where per-user config overrides can be found. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


