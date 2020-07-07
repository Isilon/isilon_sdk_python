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


class SmbLogLevelFiltersFilter(object):
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
        'id': 'int',
        'ip_addrs': 'list[str]',
        'level': 'str',
        'ops': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'ip_addrs': 'ip_addrs',
        'level': 'level',
        'ops': 'ops'
    }

    def __init__(self, id=None, ip_addrs=None, level=None, ops=None):  # noqa: E501
        """SmbLogLevelFiltersFilter - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._ip_addrs = None
        self._level = None
        self._ops = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if ip_addrs is not None:
            self.ip_addrs = ip_addrs
        self.level = level
        if ops is not None:
            self.ops = ops

    @property
    def id(self):
        """Gets the id of this SmbLogLevelFiltersFilter.  # noqa: E501

        Unique ID of the log filter.  # noqa: E501

        :return: The id of this SmbLogLevelFiltersFilter.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmbLogLevelFiltersFilter.

        Unique ID of the log filter.  # noqa: E501

        :param id: The id of this SmbLogLevelFiltersFilter.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ip_addrs(self):
        """Gets the ip_addrs of this SmbLogLevelFiltersFilter.  # noqa: E501

        Array of client IP addresses to filter against.  # noqa: E501

        :return: The ip_addrs of this SmbLogLevelFiltersFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addrs

    @ip_addrs.setter
    def ip_addrs(self, ip_addrs):
        """Sets the ip_addrs of this SmbLogLevelFiltersFilter.

        Array of client IP addresses to filter against.  # noqa: E501

        :param ip_addrs: The ip_addrs of this SmbLogLevelFiltersFilter.  # noqa: E501
        :type: list[str]
        """

        self._ip_addrs = ip_addrs

    @property
    def level(self):
        """Gets the level of this SmbLogLevelFiltersFilter.  # noqa: E501

        Logging level of the filter.  # noqa: E501

        :return: The level of this SmbLogLevelFiltersFilter.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this SmbLogLevelFiltersFilter.

        Logging level of the filter.  # noqa: E501

        :param level: The level of this SmbLogLevelFiltersFilter.  # noqa: E501
        :type: str
        """
        if level is None:
            raise ValueError("Invalid value for `level`, must not be `None`")  # noqa: E501

        self._level = level

    @property
    def ops(self):
        """Gets the ops of this SmbLogLevelFiltersFilter.  # noqa: E501

        Array of SMB operations to filter against.  # noqa: E501

        :return: The ops of this SmbLogLevelFiltersFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._ops

    @ops.setter
    def ops(self, ops):
        """Sets the ops of this SmbLogLevelFiltersFilter.

        Array of SMB operations to filter against.  # noqa: E501

        :param ops: The ops of this SmbLogLevelFiltersFilter.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["read", "write", "session-setup", "logoff", "flush", "notify", "tree-connect", "tree-disconnect", "create", "delete", "oplock", "locking", "set-info", "query", "close", "create-directory", "delete-directory"]  # noqa: E501
        if not set(ops).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `ops` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(ops) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._ops = ops

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
        if not isinstance(other, SmbLogLevelFiltersFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
