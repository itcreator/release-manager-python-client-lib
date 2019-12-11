# release-manager-client.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /projects | Create new projects
[**list_projects**](ProjectApi.md#list_projects) | **GET** /projects | List the projects
[**read_project**](ProjectApi.md#read_project) | **GET** /projects/{uuid} | Read the projects
[**update_project**](ProjectApi.md#update_project) | **PUT** /projects/{uuid} | 


# **create_project**
> Project create_project(body=body)

Create new projects

### Example

```python
from __future__ import print_function
import time
import release-manager-client
from release-manager-client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = release-manager-client.ProjectApi()
body = release-manager-client.Project() # Project |  (optional)

try:
    # Create new projects
    api_response = api_instance.create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Project**](Project.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/release-manager.v1+json
 - **Accept**: application/release-manager.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Project response |  * X-Error-Code -  <br>  |
**500** | Error response |  * X-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> list[Project] list_projects()

List the projects

Get all projects list. 

### Example

```python
from __future__ import print_function
import time
import release-manager-client
from release-manager-client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = release-manager-client.ProjectApi()

try:
    # List the projects
    api_response = api_instance.list_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Project]**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/release-manager.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**500** | Error response |  * X-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project**
> Project read_project(uuid)

Read the projects

Get all projects list 

### Example

```python
from __future__ import print_function
import time
import release-manager-client
from release-manager-client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = release-manager-client.ProjectApi()
uuid = 'uuid_example' # str | Project ID in UUID format

try:
    # Read the projects
    api_response = api_instance.read_project(uuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->read_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Project ID in UUID format | 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/release-manager.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project response |  * X-Error-Code -  <br>  |
**404** | Project response |  * X-Error-Code -  <br>  |
**500** | Error response |  * X-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> Project update_project(uuid, body=body)



### Example

```python
from __future__ import print_function
import time
import release-manager-client
from release-manager-client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = release-manager-client.ProjectApi()
uuid = 'uuid_example' # str | Project ID in UUID format
body = release-manager-client.Project() # Project |  (optional)

try:
    api_response = api_instance.update_project(uuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | [**str**](.md)| Project ID in UUID format | 
 **body** | [**Project**](Project.md)|  | [optional] 

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/release-manager.v1+json
 - **Accept**: application/release-manager.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Project response |  * X-Error-Code -  <br>  |
**404** | Project response |  * X-Error-Code -  <br>  |
**500** | Error response |  * X-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

