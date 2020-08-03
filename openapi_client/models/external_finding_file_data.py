# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ExternalFindingFileData(object):
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
        'findings': 'list[ExternalFindingData]',
        'path': 'str',
        'content': 'str'
    }

    attribute_map = {
        'findings': 'findings',
        'path': 'path',
        'content': 'content'
    }

    def __init__(self, findings=None, path=None, content=None, local_vars_configuration=None):  # noqa: E501
        """ExternalFindingFileData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._findings = None
        self._path = None
        self._content = None
        self.discriminator = None

        if findings is not None:
            self.findings = findings
        if path is not None:
            self.path = path
        if content is not None:
            self.content = content

    @property
    def findings(self):
        """Gets the findings of this ExternalFindingFileData.  # noqa: E501


        :return: The findings of this ExternalFindingFileData.  # noqa: E501
        :rtype: list[ExternalFindingData]
        """
        return self._findings

    @findings.setter
    def findings(self, findings):
        """Sets the findings of this ExternalFindingFileData.


        :param findings: The findings of this ExternalFindingFileData.  # noqa: E501
        :type: list[ExternalFindingData]
        """

        self._findings = findings

    @property
    def path(self):
        """Gets the path of this ExternalFindingFileData.  # noqa: E501


        :return: The path of this ExternalFindingFileData.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ExternalFindingFileData.


        :param path: The path of this ExternalFindingFileData.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def content(self):
        """Gets the content of this ExternalFindingFileData.  # noqa: E501


        :return: The content of this ExternalFindingFileData.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ExternalFindingFileData.


        :param content: The content of this ExternalFindingFileData.  # noqa: E501
        :type: str
        """

        self._content = content

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
        if not isinstance(other, ExternalFindingFileData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExternalFindingFileData):
            return True

        return self.to_dict() != other.to_dict()