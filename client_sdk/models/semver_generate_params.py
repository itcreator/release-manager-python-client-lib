# coding: utf-8

"""
    Release Manager

    This application generates version for your software.  # noqa: E501

    The version of the OpenAPI document: 0.2.0
    Contact: vitalleshchyk@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from client_sdk.configuration import Configuration


class SemverGenerateParams(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'major': 'int',
        'minor': 'int',
        'branch': 'str'
    }

    attribute_map = {
        'major': 'major',
        'minor': 'minor',
        'branch': 'branch'
    }

    def __init__(self, major=None, minor=None, branch=None, local_vars_configuration=None):  # noqa: E501
        """SemverGenerateParams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._major = None
        self._minor = None
        self._branch = None
        self.discriminator = None

        self.major = major
        self.minor = minor
        self.branch = branch

    @property
    def major(self):
        """Gets the major of this SemverGenerateParams.  # noqa: E501

        MAJOR version when you make incompatible API changes  # noqa: E501

        :return: The major of this SemverGenerateParams.  # noqa: E501
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major):
        """Sets the major of this SemverGenerateParams.

        MAJOR version when you make incompatible API changes  # noqa: E501

        :param major: The major of this SemverGenerateParams.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and major is None:  # noqa: E501
            raise ValueError("Invalid value for `major`, must not be `None`")  # noqa: E501

        self._major = major

    @property
    def minor(self):
        """Gets the minor of this SemverGenerateParams.  # noqa: E501

        MAJOR version when you make incompatible API changes  # noqa: E501

        :return: The minor of this SemverGenerateParams.  # noqa: E501
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor):
        """Sets the minor of this SemverGenerateParams.

        MAJOR version when you make incompatible API changes  # noqa: E501

        :param minor: The minor of this SemverGenerateParams.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and minor is None:  # noqa: E501
            raise ValueError("Invalid value for `minor`, must not be `None`")  # noqa: E501

        self._minor = minor

    @property
    def branch(self):
        """Gets the branch of this SemverGenerateParams.  # noqa: E501


        :return: The branch of this SemverGenerateParams.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this SemverGenerateParams.


        :param branch: The branch of this SemverGenerateParams.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and branch is None:  # noqa: E501
            raise ValueError("Invalid value for `branch`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                branch is not None and len(branch) > 150):
            raise ValueError("Invalid value for `branch`, length must be less than or equal to `150`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                branch is not None and len(branch) < 2):
            raise ValueError("Invalid value for `branch`, length must be greater than or equal to `2`")  # noqa: E501

        self._branch = branch

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SemverGenerateParams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SemverGenerateParams):
            return True

        return self.to_dict() != other.to_dict()
