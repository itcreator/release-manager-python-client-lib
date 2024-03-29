# reelase-manager-api
This application generates version for your software.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.2.0
- Package version: 0.2.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/itcreator/release-manager-micro](https://github.com/itcreator/release-manager-micro)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import client_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import client_sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import client_sdk
from client_sdk.rest import ApiException
from pprint import pprint


# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = client_sdk.ProjectApi(client_sdk.ApiClient(configuration))
body = client_sdk.Project() # Project |  (optional)

try:
    # Create new projects
    api_response = api_instance.create_project(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ProjectApi* | [**create_project**](docs/ProjectApi.md#create_project) | **POST** /projects | Create new projects
*ProjectApi* | [**list_projects**](docs/ProjectApi.md#list_projects) | **GET** /projects | List the projects
*ProjectApi* | [**read_project**](docs/ProjectApi.md#read_project) | **GET** /projects/{uuid} | Read the projects
*ProjectApi* | [**update_project**](docs/ProjectApi.md#update_project) | **PUT** /projects/{uuid} | 
*VersionSemanticApi* | [**semver_generate**](docs/VersionSemanticApi.md#semver_generate) | **POST** /projects/{projectUuid}/version/semantic | Generate new semantic version number (based on gitflow)


## Documentation For Models

 - [Error](docs/Error.md)
 - [Project](docs/Project.md)
 - [SemverGenerateParams](docs/SemverGenerateParams.md)
 - [SemverTagSet](docs/SemverTagSet.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author

vitalleshchyk@gmail.com


