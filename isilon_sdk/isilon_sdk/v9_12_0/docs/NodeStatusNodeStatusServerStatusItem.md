# NodeStatusNodeStatusServerStatusItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connections** | **int** | Total number of connections from the cluster node to CAVA servers. | [optional] 
**good_heartbeats** | **int** | Number of good heartbeats exchanges between cluster node and CAVA server. | [optional] 
**heartbeat_rtt** | **int** | Average round trip time (ms) for heartbeat messages between cluster node and CAVA server. | [optional] 
**scan_requests** | **int** | Total number of scan requests received by the CAVA server. | [optional] 
**scan_rtt** | **int** | Average round trip time (ms) for scan request completion. | [optional] 
**server_name** | **str** | Name of the CAVA server as per the configuration. | [optional] 
**server_state** | **str** | State of the CAVA server in string format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


