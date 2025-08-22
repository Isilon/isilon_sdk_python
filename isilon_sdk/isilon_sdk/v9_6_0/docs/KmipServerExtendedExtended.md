# KmipServerExtendedExtended

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert** | [**KmipServerCaCert**](KmipServerCaCert.md) |  | 
**client_cert** | [**KmipServerClientCert**](KmipServerClientCert.md) |  | 
**connection_timeout** | **int** | KMIP RPC connection timeout in seconds. | 
**host** | **str** | KMIP server hostname. | 
**id** | **str** | Unique KMIP server identifier. | 
**minimum_tls_version** | **str** | Denotes the minimum TLS version supported by the KTP. Default value is set to &#39;1.2&#39;. Supported versions: &#39;1.1&#39; and &#39;1.2&#39;. | 
**port** | **int** | KMIP server port. | 
**retry_timeout** | **int** | KMIP RPC retry timeout in milliseconds. | 
**tls_ciphers** | **str** | TLS cipher suite to use for communication with the KMIP server. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


