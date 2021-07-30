# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 11
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_9_1_0.models.result_directories_dir_usage import ResultDirectoriesDirUsage  # noqa: F401,E501
from isi_sdk_9_1_0.models.result_directories_total_usage import ResultDirectoriesTotalUsage  # noqa: F401,E501
from isi_sdk_9_1_0.models.result_directories_usage_data_item import ResultDirectoriesUsageDataItem  # noqa: F401,E501


class ResultDirectories(object):
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
        'attribute_count': 'int',
        'begin_time': 'int',
        'dir_depth': 'int',
        'dir_usage': 'ResultDirectoriesDirUsage',
        'path_parts': 'list[str]',
        'total_usage': 'ResultDirectoriesTotalUsage',
        'usage_data': 'list[ResultDirectoriesUsageDataItem]'
    }

    attribute_map = {
        'attribute_count': 'attribute_count',
        'begin_time': 'begin_time',
        'dir_depth': 'dir_depth',
        'dir_usage': 'dir_usage',
        'path_parts': 'path_parts',
        'total_usage': 'total_usage',
        'usage_data': 'usage_data'
    }

    def __init__(self, attribute_count=None, begin_time=None, dir_depth=None, dir_usage=None, path_parts=None, total_usage=None, usage_data=None):  # noqa: E501
        """ResultDirectories - a model defined in Swagger"""  # noqa: E501

        self._attribute_count = None
        self._begin_time = None
        self._dir_depth = None
        self._dir_usage = None
        self._path_parts = None
        self._total_usage = None
        self._usage_data = None
        self.discriminator = None

        self.attribute_count = attribute_count
        self.begin_time = begin_time
        self.dir_depth = dir_depth
        self.dir_usage = dir_usage
        self.path_parts = path_parts
        self.total_usage = total_usage
        self.usage_data = usage_data

    @property
    def attribute_count(self):
        """Gets the attribute_count of this ResultDirectories.  # noqa: E501

        User attribute count.  # noqa: E501

        :return: The attribute_count of this ResultDirectories.  # noqa: E501
        :rtype: int
        """
        return self._attribute_count

    @attribute_count.setter
    def attribute_count(self, attribute_count):
        """Sets the attribute_count of this ResultDirectories.

        User attribute count.  # noqa: E501

        :param attribute_count: The attribute_count of this ResultDirectories.  # noqa: E501
        :type: int
        """
        if attribute_count is None:
            raise ValueError("Invalid value for `attribute_count`, must not be `None`")  # noqa: E501

        self._attribute_count = attribute_count

    @property
    def begin_time(self):
        """Gets the begin_time of this ResultDirectories.  # noqa: E501

        Unix Epoch time of start of results collection job.  # noqa: E501

        :return: The begin_time of this ResultDirectories.  # noqa: E501
        :rtype: int
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        """Sets the begin_time of this ResultDirectories.

        Unix Epoch time of start of results collection job.  # noqa: E501

        :param begin_time: The begin_time of this ResultDirectories.  # noqa: E501
        :type: int
        """
        if begin_time is None:
            raise ValueError("Invalid value for `begin_time`, must not be `None`")  # noqa: E501
        if begin_time is not None and begin_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `begin_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if begin_time is not None and begin_time < -9223372036854775808:  # noqa: E501
            raise ValueError("Invalid value for `begin_time`, must be a value greater than or equal to `-9223372036854775808`")  # noqa: E501

        self._begin_time = begin_time

    @property
    def dir_depth(self):
        """Gets the dir_depth of this ResultDirectories.  # noqa: E501

        Directory depth.  # noqa: E501

        :return: The dir_depth of this ResultDirectories.  # noqa: E501
        :rtype: int
        """
        return self._dir_depth

    @dir_depth.setter
    def dir_depth(self, dir_depth):
        """Sets the dir_depth of this ResultDirectories.

        Directory depth.  # noqa: E501

        :param dir_depth: The dir_depth of this ResultDirectories.  # noqa: E501
        :type: int
        """
        if dir_depth is None:
            raise ValueError("Invalid value for `dir_depth`, must not be `None`")  # noqa: E501

        self._dir_depth = dir_depth

    @property
    def dir_usage(self):
        """Gets the dir_usage of this ResultDirectories.  # noqa: E501

        Disk usage by the current directory.  # noqa: E501

        :return: The dir_usage of this ResultDirectories.  # noqa: E501
        :rtype: ResultDirectoriesDirUsage
        """
        return self._dir_usage

    @dir_usage.setter
    def dir_usage(self, dir_usage):
        """Sets the dir_usage of this ResultDirectories.

        Disk usage by the current directory.  # noqa: E501

        :param dir_usage: The dir_usage of this ResultDirectories.  # noqa: E501
        :type: ResultDirectoriesDirUsage
        """
        if dir_usage is None:
            raise ValueError("Invalid value for `dir_usage`, must not be `None`")  # noqa: E501

        self._dir_usage = dir_usage

    @property
    def path_parts(self):
        """Gets the path_parts of this ResultDirectories.  # noqa: E501

        Directory path information from root to current directory.  # noqa: E501

        :return: The path_parts of this ResultDirectories.  # noqa: E501
        :rtype: list[str]
        """
        return self._path_parts

    @path_parts.setter
    def path_parts(self, path_parts):
        """Sets the path_parts of this ResultDirectories.

        Directory path information from root to current directory.  # noqa: E501

        :param path_parts: The path_parts of this ResultDirectories.  # noqa: E501
        :type: list[str]
        """
        if path_parts is None:
            raise ValueError("Invalid value for `path_parts`, must not be `None`")  # noqa: E501

        self._path_parts = path_parts

    @property
    def total_usage(self):
        """Gets the total_usage of this ResultDirectories.  # noqa: E501

        Disk usage from root.  # noqa: E501

        :return: The total_usage of this ResultDirectories.  # noqa: E501
        :rtype: ResultDirectoriesTotalUsage
        """
        return self._total_usage

    @total_usage.setter
    def total_usage(self, total_usage):
        """Sets the total_usage of this ResultDirectories.

        Disk usage from root.  # noqa: E501

        :param total_usage: The total_usage of this ResultDirectories.  # noqa: E501
        :type: ResultDirectoriesTotalUsage
        """
        if total_usage is None:
            raise ValueError("Invalid value for `total_usage`, must not be `None`")  # noqa: E501

        self._total_usage = total_usage

    @property
    def usage_data(self):
        """Gets the usage_data of this ResultDirectories.  # noqa: E501

        Disk usage for all of immediate children of the current directory.  # noqa: E501

        :return: The usage_data of this ResultDirectories.  # noqa: E501
        :rtype: list[ResultDirectoriesUsageDataItem]
        """
        return self._usage_data

    @usage_data.setter
    def usage_data(self, usage_data):
        """Sets the usage_data of this ResultDirectories.

        Disk usage for all of immediate children of the current directory.  # noqa: E501

        :param usage_data: The usage_data of this ResultDirectories.  # noqa: E501
        :type: list[ResultDirectoriesUsageDataItem]
        """
        if usage_data is None:
            raise ValueError("Invalid value for `usage_data`, must not be `None`")  # noqa: E501

        self._usage_data = usage_data

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
        if not isinstance(other, ResultDirectories):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
