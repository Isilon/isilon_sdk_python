# isi_sdk_8_2_1.HealthcheckApi

All URIs are relative to *https://YOUR_CLUSTER_HOSTNAME_OR_NODE_IP:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_healthcheck_evaluation**](HealthcheckApi.md#create_healthcheck_evaluation) | **POST** /platform/3/healthcheck/evaluations | 
[**create_healthcheck_parameter**](HealthcheckApi.md#create_healthcheck_parameter) | **POST** /platform/3/healthcheck/parameters | 
[**delete_healthcheck_evaluation**](HealthcheckApi.md#delete_healthcheck_evaluation) | **DELETE** /platform/3/healthcheck/evaluations/{HealthcheckEvaluationId} | 
[**delete_healthcheck_parameter**](HealthcheckApi.md#delete_healthcheck_parameter) | **DELETE** /platform/3/healthcheck/parameters/{HealthcheckParameterId} | 
[**get_healthcheck_checklist**](HealthcheckApi.md#get_healthcheck_checklist) | **GET** /platform/3/healthcheck/checklists/{HealthcheckChecklistId} | 
[**get_healthcheck_checklists**](HealthcheckApi.md#get_healthcheck_checklists) | **GET** /platform/3/healthcheck/checklists | 
[**get_healthcheck_evaluation**](HealthcheckApi.md#get_healthcheck_evaluation) | **GET** /platform/3/healthcheck/evaluations/{HealthcheckEvaluationId} | 
[**get_healthcheck_item**](HealthcheckApi.md#get_healthcheck_item) | **GET** /platform/3/healthcheck/items/{HealthcheckItemId} | 
[**get_healthcheck_items**](HealthcheckApi.md#get_healthcheck_items) | **GET** /platform/3/healthcheck/items | 
[**get_healthcheck_parameter**](HealthcheckApi.md#get_healthcheck_parameter) | **GET** /platform/3/healthcheck/parameters/{HealthcheckParameterId} | 
[**list_healthcheck_evaluations**](HealthcheckApi.md#list_healthcheck_evaluations) | **GET** /platform/3/healthcheck/evaluations | 
[**list_healthcheck_parameters**](HealthcheckApi.md#list_healthcheck_parameters) | **GET** /platform/3/healthcheck/parameters | 
[**update_healthcheck_evaluation**](HealthcheckApi.md#update_healthcheck_evaluation) | **PUT** /platform/3/healthcheck/evaluations/{HealthcheckEvaluationId} | 
[**update_healthcheck_parameter**](HealthcheckApi.md#update_healthcheck_parameter) | **PUT** /platform/3/healthcheck/parameters/{HealthcheckParameterId} | 


# **create_healthcheck_evaluation**
> CreateResponse create_healthcheck_evaluation(healthcheck_evaluation)



Request an evaluation.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_evaluation = isi_sdk_8_2_1.HealthcheckEvaluationCreateParams() # HealthcheckEvaluationCreateParams | 

try:
    api_response = api_instance.create_healthcheck_evaluation(healthcheck_evaluation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->create_healthcheck_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_evaluation** | [**HealthcheckEvaluationCreateParams**](HealthcheckEvaluationCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_healthcheck_parameter**
> CreateResponse create_healthcheck_parameter(healthcheck_parameter)



Create a parameter.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_parameter = isi_sdk_8_2_1.HealthcheckParameterCreateParams() # HealthcheckParameterCreateParams | 

try:
    api_response = api_instance.create_healthcheck_parameter(healthcheck_parameter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->create_healthcheck_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_parameter** | [**HealthcheckParameterCreateParams**](HealthcheckParameterCreateParams.md)|  | 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthcheck_evaluation**
> delete_healthcheck_evaluation(healthcheck_evaluation_id)



Cancel an evaluation.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_evaluation_id = 'healthcheck_evaluation_id_example' # str | Cancel an evaluation.

try:
    api_instance.delete_healthcheck_evaluation(healthcheck_evaluation_id)
except ApiException as e:
    print("Exception when calling HealthcheckApi->delete_healthcheck_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_evaluation_id** | **str**| Cancel an evaluation. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_healthcheck_parameter**
> delete_healthcheck_parameter(healthcheck_parameter_id)



Delete a parameter.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_parameter_id = 'healthcheck_parameter_id_example' # str | Delete a parameter.

try:
    api_instance.delete_healthcheck_parameter(healthcheck_parameter_id)
except ApiException as e:
    print("Exception when calling HealthcheckApi->delete_healthcheck_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_parameter_id** | **str**| Delete a parameter. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_healthcheck_checklist**
> HealthcheckChecklists get_healthcheck_checklist(healthcheck_checklist_id)



Retrieve a checklist definition.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_checklist_id = 'healthcheck_checklist_id_example' # str | Retrieve a checklist definition.

try:
    api_response = api_instance.get_healthcheck_checklist(healthcheck_checklist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->get_healthcheck_checklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_checklist_id** | **str**| Retrieve a checklist definition. | 

### Return type

[**HealthcheckChecklists**](HealthcheckChecklists.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_healthcheck_checklists**
> HealthcheckChecklistsExtended get_healthcheck_checklists(limit=limit, resume=resume)



List checklists.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_healthcheck_checklists(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->get_healthcheck_checklists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**HealthcheckChecklistsExtended**](HealthcheckChecklistsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_healthcheck_evaluation**
> HealthcheckEvaluations get_healthcheck_evaluation(healthcheck_evaluation_id, detailed=detailed)



Retrieve individual evaluation.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_evaluation_id = 'healthcheck_evaluation_id_example' # str | Retrieve individual evaluation.
detailed = true # bool | Also return details for items that pass (optional)

try:
    api_response = api_instance.get_healthcheck_evaluation(healthcheck_evaluation_id, detailed=detailed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->get_healthcheck_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_evaluation_id** | **str**| Retrieve individual evaluation. | 
 **detailed** | **bool**| Also return details for items that pass | [optional] 

### Return type

[**HealthcheckEvaluations**](HealthcheckEvaluations.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_healthcheck_item**
> HealthcheckItems get_healthcheck_item(healthcheck_item_id)



Retrieve an item definition.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_item_id = 'healthcheck_item_id_example' # str | Retrieve an item definition.

try:
    api_response = api_instance.get_healthcheck_item(healthcheck_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->get_healthcheck_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_item_id** | **str**| Retrieve an item definition. | 

### Return type

[**HealthcheckItems**](HealthcheckItems.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_healthcheck_items**
> HealthcheckItemsExtended get_healthcheck_items(limit=limit, resume=resume)



List items.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.get_healthcheck_items(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->get_healthcheck_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**HealthcheckItemsExtended**](HealthcheckItemsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_healthcheck_parameter**
> HealthcheckParameters get_healthcheck_parameter(healthcheck_parameter_id)



Retrieve individual parameter.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_parameter_id = 'healthcheck_parameter_id_example' # str | Retrieve individual parameter.

try:
    api_response = api_instance.get_healthcheck_parameter(healthcheck_parameter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->get_healthcheck_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_parameter_id** | **str**| Retrieve individual parameter. | 

### Return type

[**HealthcheckParameters**](HealthcheckParameters.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_healthcheck_evaluations**
> HealthcheckEvaluationsExtended list_healthcheck_evaluations(detailed=detailed, limit=limit, resume=resume)



List evaluations.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
detailed = true # bool | Also return details for items that pass (optional)
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_healthcheck_evaluations(detailed=detailed, limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->list_healthcheck_evaluations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detailed** | **bool**| Also return details for items that pass | [optional] 
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**HealthcheckEvaluationsExtended**](HealthcheckEvaluationsExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_healthcheck_parameters**
> HealthcheckParametersExtended list_healthcheck_parameters(limit=limit, resume=resume)



List parameters.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
limit = 56 # int | Return no more than this many results at once (see resume). (optional)
resume = 'resume_example' # str | Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). (optional)

try:
    api_response = api_instance.list_healthcheck_parameters(limit=limit, resume=resume)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckApi->list_healthcheck_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Return no more than this many results at once (see resume). | [optional] 
 **resume** | **str**| Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options). | [optional] 

### Return type

[**HealthcheckParametersExtended**](HealthcheckParametersExtended.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthcheck_evaluation**
> update_healthcheck_evaluation(healthcheck_evaluation, healthcheck_evaluation_id)



Pause or resume an evaluation.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_evaluation = isi_sdk_8_2_1.HealthcheckEvaluation() # HealthcheckEvaluation | 
healthcheck_evaluation_id = 'healthcheck_evaluation_id_example' # str | Pause or resume an evaluation.

try:
    api_instance.update_healthcheck_evaluation(healthcheck_evaluation, healthcheck_evaluation_id)
except ApiException as e:
    print("Exception when calling HealthcheckApi->update_healthcheck_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_evaluation** | [**HealthcheckEvaluation**](HealthcheckEvaluation.md)|  | 
 **healthcheck_evaluation_id** | **str**| Pause or resume an evaluation. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_healthcheck_parameter**
> update_healthcheck_parameter(healthcheck_parameter, healthcheck_parameter_id)



Modify a parameter value.

### Example
```python
from __future__ import print_function
import time
import isi_sdk_8_2_1
from isi_sdk_8_2_1.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = isi_sdk_8_2_1.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = isi_sdk_8_2_1.HealthcheckApi(isi_sdk_8_2_1.ApiClient(configuration))
healthcheck_parameter = isi_sdk_8_2_1.HealthcheckParameter() # HealthcheckParameter | 
healthcheck_parameter_id = 'healthcheck_parameter_id_example' # str | Modify a parameter value.

try:
    api_instance.update_healthcheck_parameter(healthcheck_parameter, healthcheck_parameter_id)
except ApiException as e:
    print("Exception when calling HealthcheckApi->update_healthcheck_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **healthcheck_parameter** | [**HealthcheckParameter**](HealthcheckParameter.md)|  | 
 **healthcheck_parameter_id** | **str**| Modify a parameter value. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

