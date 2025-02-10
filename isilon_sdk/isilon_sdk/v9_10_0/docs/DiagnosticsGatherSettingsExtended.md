# DiagnosticsGatherSettingsExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectivity** | **bool** | Use Dell Technologies connectivity services for upload of gather. | [optional] 
**esrs** | **bool** | Use ESRS for upload of gather. | [optional] 
**ftp_upload** | **bool** | Use FTP to upload logs from the isi gather command | [optional] 
**ftp_upload_host** | **str** | Alternate FTP host to use for FTP upload. | [optional] 
**ftp_upload_insecure** | **bool** | Whether to attempt a plain text FTP upload. | [optional] 
**ftp_upload_mode** | **str** | FTP upload mode. | [optional] 
**ftp_upload_pass** | **str** | FTP password to use for FTP upload. | [optional] 
**ftp_upload_path** | **str** | Alternate FTP path to use for FTP upload. | [optional] 
**ftp_upload_proxy** | **str** | Proxy server to use for FTP upload. | [optional] 
**ftp_upload_proxy_port** | **int** | Proxy server port to use for FTP upload. | [optional] 
**ftp_upload_ssl_cert** | **str** | Path to certificate. Leave it blank to use root signed-CA | [optional] 
**ftp_upload_user** | **str** | FTP user to use for FTP upload. | [optional] 
**ftp_upload_webui_default** | **bool** | Hidden key to save default checkbox in WebUI | [optional] 
**gather_begin** | **str** | Sets the starting time of files to be gathered using datetime format. The accepted datetime format should be in the form &#39;YYYY-MM-DD HH:MM&#39; where time is optional. This will gather all files modified past that date. | [optional] 
**gather_mode** | **str** | Set gather to full, incremental, or partial. | [optional] 
**gather_past** | **str** | Gather logs modified within this time frame. Enter a number followed by a letter for the starting range of files to be gathered, eg. 1h for files last modified in the past hour. Other supported times include d and w for days and weeks respectively. | [optional] 
**group** | **str** | Only gathers component groups specified by the group field.  | [optional] 
**http_insecure_upload** | **bool** | Use insecure HTTP to upload logs from the isi gather command | [optional] 
**http_upload** | **bool** | This option is deprecated. Use the option http_insecure_upload to upload logs via insecure HTTP from the isi gather command | [optional] 
**http_upload_host** | **str** | Address of an alternate HTTP host used to upload logs | [optional] 
**http_upload_path** | **str** | Alternate path on HTTP server to use for HTTP upload. | [optional] 
**http_upload_proxy** | **str** | Proxy server to use for HTTP upload. | [optional] 
**http_upload_proxy_port** | **int** | Proxy server port to use for HTTP upload. | [optional] 
**upload** | **bool** | Upload gather to Dell EMC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


