# release-manager-client.VersionSemanticApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**semver_generate**](VersionSemanticApi.md#semver_generate) | **POST** /projects/{projectUuid}/version/semantic | Generate new semantic version number (based on gitflow)


# **semver_generate**
> SemverTagSet semver_generate(project_uuid, body=body)

Generate new semantic version number (based on gitflow)

Semantic Versioning 2.0.0 See also http://semver.org/spec/v2.0.0.html Based on branching model [GitFlow](http://nvie.com/posts/a-successful-git-branching-model/) 

### Example

```python
from __future__ import print_function
import time
import release-manager-client
from release-manager-client.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = release-manager-client.VersionSemanticApi()
project_uuid = 'project_uuid_example' # str | Project ID in UUID format
body = release-manager-client.SemverGenerateParams() # SemverGenerateParams |  (optional)

try:
    # Generate new semantic version number (based on gitflow)
    api_response = api_instance.semver_generate(project_uuid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionSemanticApi->semver_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_uuid** | [**str**](.md)| Project ID in UUID format | 
 **body** | [**SemverGenerateParams**](SemverGenerateParams.md)|  | [optional] 

### Return type

[**SemverTagSet**](SemverTagSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/release-manager.v1+json
 - **Accept**: application/release-manager.v1+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Generate semantic version response |  -  |
**404** | Semver: project not found response |  -  |
**500** | Error response |  * X-Error-Code -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

