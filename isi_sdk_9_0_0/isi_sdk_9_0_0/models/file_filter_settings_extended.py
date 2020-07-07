# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 10
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class FileFilterSettingsExtended(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'file_filter_extensions': 'list[str]',
        'file_filter_type': 'str',
        'file_filtering_enabled': 'bool'
    }

    attribute_map = {
        'file_filter_extensions': 'file_filter_extensions',
        'file_filter_type': 'file_filter_type',
        'file_filtering_enabled': 'file_filtering_enabled'
    }

    def __init__(self, file_filter_extensions=None, file_filter_type=None, file_filtering_enabled=None):  # noqa: E501
        """FileFilterSettingsExtended - a model defined in Swagger"""  # noqa: E501

        self._file_filter_extensions = None
        self._file_filter_type = None
        self._file_filtering_enabled = None
        self.discriminator = None

        if file_filter_extensions is not None:
            self.file_filter_extensions = file_filter_extensions
        if file_filter_type is not None:
            self.file_filter_type = file_filter_type
        if file_filtering_enabled is not None:
            self.file_filtering_enabled = file_filtering_enabled

    @property
    def file_filter_extensions(self):
        """Gets the file_filter_extensions of this FileFilterSettingsExtended.  # noqa: E501

        List of file extensions to be filtered.  # noqa: E501

        :return: The file_filter_extensions of this FileFilterSettingsExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._file_filter_extensions

    @file_filter_extensions.setter
    def file_filter_extensions(self, file_filter_extensions):
        """Sets the file_filter_extensions of this FileFilterSettingsExtended.

        List of file extensions to be filtered.  # noqa: E501

        :param file_filter_extensions: The file_filter_extensions of this FileFilterSettingsExtended.  # noqa: E501
        :type: list[str]
        """

        self._file_filter_extensions = file_filter_extensions

    @property
    def file_filter_type(self):
        """Gets the file_filter_type of this FileFilterSettingsExtended.  # noqa: E501

        Specifies if filter list is for deny or allow. Default is deny.  # noqa: E501

        :return: The file_filter_type of this FileFilterSettingsExtended.  # noqa: E501
        :rtype: str
        """
        return self._file_filter_type

    @file_filter_type.setter
    def file_filter_type(self, file_filter_type):
        """Sets the file_filter_type of this FileFilterSettingsExtended.

        Specifies if filter list is for deny or allow. Default is deny.  # noqa: E501

        :param file_filter_type: The file_filter_type of this FileFilterSettingsExtended.  # noqa: E501
        :type: str
        """

        self._file_filter_type = file_filter_type

    @property
    def file_filtering_enabled(self):
        """Gets the file_filtering_enabled of this FileFilterSettingsExtended.  # noqa: E501

        Indicates whether file filtering is enabled on this zone.  # noqa: E501

        :return: The file_filtering_enabled of this FileFilterSettingsExtended.  # noqa: E501
        :rtype: bool
        """
        return self._file_filtering_enabled

    @file_filtering_enabled.setter
    def file_filtering_enabled(self, file_filtering_enabled):
        """Sets the file_filtering_enabled of this FileFilterSettingsExtended.

        Indicates whether file filtering is enabled on this zone.  # noqa: E501

        :param file_filtering_enabled: The file_filtering_enabled of this FileFilterSettingsExtended.  # noqa: E501
        :type: bool
        """

        self._file_filtering_enabled = file_filtering_enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, FileFilterSettingsExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
