# KmipServerCreateParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_cert_path** | **str** | Certification Authority (CA) certificate, used for TLS Mutual Authentication with the KMIP Server. | 
**client_cert_password** | **str** | Cluster identity private key password. | [optional] 
**client_cert_path** | **str** | Cluster identity certificate and private key used for TLS Mutual Authentication with the KMIP Server. | 
**host** | **str** | KMIP server hostname. | 
**minimum_tls_version** | **str** | Denotes the minimum TLS version supported by the KTP. Default value is set to &#39;1.2&#39;. However other supported values are &#39;1.0&#39; and &#39;1.1&#39;. | [optional] 
**port** | **int** | KMIP server port. | [optional] 
**id** | **str** | Unique KMIP server identifier. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


