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


class FsaSettingsSettings(object):
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
        'default_template': 'str',
        'disk_usage_depth': 'int',
        'max_age': 'int',
        'max_count': 'int',
        'squash_depth': 'int',
        'top_n_max': 'int',
        'use_snapshot': 'bool'
    }

    attribute_map = {
        'default_template': 'default_template',
        'disk_usage_depth': 'disk_usage_depth',
        'max_age': 'max_age',
        'max_count': 'max_count',
        'squash_depth': 'squash_depth',
        'top_n_max': 'top_n_max',
        'use_snapshot': 'use_snapshot'
    }

    def __init__(self, default_template=None, disk_usage_depth=None, max_age=None, max_count=None, squash_depth=None, top_n_max=None, use_snapshot=None):  # noqa: E501
        """FsaSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._default_template = None
        self._disk_usage_depth = None
        self._max_age = None
        self._max_count = None
        self._squash_depth = None
        self._top_n_max = None
        self._use_snapshot = None
        self.discriminator = None

        if default_template is not None:
            self.default_template = default_template
        if disk_usage_depth is not None:
            self.disk_usage_depth = disk_usage_depth
        if max_age is not None:
            self.max_age = max_age
        if max_count is not None:
            self.max_count = max_count
        if squash_depth is not None:
            self.squash_depth = squash_depth
        if top_n_max is not None:
            self.top_n_max = top_n_max
        if use_snapshot is not None:
            self.use_snapshot = use_snapshot

    @property
    def default_template(self):
        """Gets the default_template of this FsaSettingsSettings.  # noqa: E501

        Name of question template to use for new FSA jobs.  # noqa: E501

        :return: The default_template of this FsaSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_template

    @default_template.setter
    def default_template(self, default_template):
        """Sets the default_template of this FsaSettingsSettings.

        Name of question template to use for new FSA jobs.  # noqa: E501

        :param default_template: The default_template of this FsaSettingsSettings.  # noqa: E501
        :type: str
        """

        self._default_template = default_template

    @property
    def disk_usage_depth(self):
        """Gets the disk_usage_depth of this FsaSettingsSettings.  # noqa: E501

        Maximum directory depth used for disk_usage question if not specified in the question.  # noqa: E501

        :return: The disk_usage_depth of this FsaSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._disk_usage_depth

    @disk_usage_depth.setter
    def disk_usage_depth(self, disk_usage_depth):
        """Sets the disk_usage_depth of this FsaSettingsSettings.

        Maximum directory depth used for disk_usage question if not specified in the question.  # noqa: E501

        :param disk_usage_depth: The disk_usage_depth of this FsaSettingsSettings.  # noqa: E501
        :type: int
        """

        self._disk_usage_depth = disk_usage_depth

    @property
    def max_age(self):
        """Gets the max_age of this FsaSettingsSettings.  # noqa: E501

        Maximum age of non-pinned results in seconds.  # noqa: E501

        :return: The max_age of this FsaSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_age

    @max_age.setter
    def max_age(self, max_age):
        """Sets the max_age of this FsaSettingsSettings.

        Maximum age of non-pinned results in seconds.  # noqa: E501

        :param max_age: The max_age of this FsaSettingsSettings.  # noqa: E501
        :type: int
        """

        self._max_age = max_age

    @property
    def max_count(self):
        """Gets the max_count of this FsaSettingsSettings.  # noqa: E501

        Maximum number of non-pinned result sets to keep.  # noqa: E501

        :return: The max_count of this FsaSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        """Sets the max_count of this FsaSettingsSettings.

        Maximum number of non-pinned result sets to keep.  # noqa: E501

        :param max_count: The max_count of this FsaSettingsSettings.  # noqa: E501
        :type: int
        """

        self._max_count = max_count

    @property
    def squash_depth(self):
        """Gets the squash_depth of this FsaSettingsSettings.  # noqa: E501

        Squash depth to use for squash binning questions if not specified in the question.  # noqa: E501

        :return: The squash_depth of this FsaSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._squash_depth

    @squash_depth.setter
    def squash_depth(self, squash_depth):
        """Sets the squash_depth of this FsaSettingsSettings.

        Squash depth to use for squash binning questions if not specified in the question.  # noqa: E501

        :param squash_depth: The squash_depth of this FsaSettingsSettings.  # noqa: E501
        :type: int
        """

        self._squash_depth = squash_depth

    @property
    def top_n_max(self):
        """Gets the top_n_max of this FsaSettingsSettings.  # noqa: E501

        Maximum number of items in a Top-N question result if not specified in the question.  # noqa: E501

        :return: The top_n_max of this FsaSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._top_n_max

    @top_n_max.setter
    def top_n_max(self, top_n_max):
        """Sets the top_n_max of this FsaSettingsSettings.

        Maximum number of items in a Top-N question result if not specified in the question.  # noqa: E501

        :param top_n_max: The top_n_max of this FsaSettingsSettings.  # noqa: E501
        :type: int
        """

        self._top_n_max = top_n_max

    @property
    def use_snapshot(self):
        """Gets the use_snapshot of this FsaSettingsSettings.  # noqa: E501

        If true, use a snapshot for consistency, otherwise analyze head.  # noqa: E501

        :return: The use_snapshot of this FsaSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_snapshot

    @use_snapshot.setter
    def use_snapshot(self, use_snapshot):
        """Sets the use_snapshot of this FsaSettingsSettings.

        If true, use a snapshot for consistency, otherwise analyze head.  # noqa: E501

        :param use_snapshot: The use_snapshot of this FsaSettingsSettings.  # noqa: E501
        :type: bool
        """

        self._use_snapshot = use_snapshot

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
        if not isinstance(other, FsaSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
