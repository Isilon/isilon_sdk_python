# KmipServer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert_path** | **str** | Certification Authority (CA) certificate, used for TLS Mutual Authentication with the KMIP Server. | [optional] 
**client_cert_password** | **str** | Cluster identity private key password. | [optional] 
**client_cert_path** | **str** | Cluster identity certificate and private key used for TLS Mutual Authentication with the KMIP Server. | [optional] 
**connection_timeout** | **int** | KMIP RPC connection timeout in seconds. | [optional] 
**host** | **str** | KMIP server hostname. | [optional] 
**minimum_tls_version** | **str** | Denotes the minimum TLS version supported by the KTP. Default value is set to &#39;1.2&#39;. However other supported values are &#39;1.0&#39; and &#39;1.1&#39;. | [optional] 
**port** | **int** | KMIP server port. | [optional] 
**retry_timeout** | **int** | KMIP RPC retry timeout in milliseconds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


