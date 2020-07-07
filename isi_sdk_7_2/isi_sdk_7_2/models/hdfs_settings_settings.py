# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 2
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HdfsSettingsSettings(object):
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
        'default_block_size': 'int',
        'default_checksum_type': 'str',
        'default_sendbuf_size': 'int',
        'server_log_level': 'str',
        'server_threads': 'int'
    }

    attribute_map = {
        'default_block_size': 'default_block_size',
        'default_checksum_type': 'default_checksum_type',
        'default_sendbuf_size': 'default_sendbuf_size',
        'server_log_level': 'server_log_level',
        'server_threads': 'server_threads'
    }

    def __init__(self, default_block_size=None, default_checksum_type=None, default_sendbuf_size=None, server_log_level=None, server_threads=None):  # noqa: E501
        """HdfsSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._default_block_size = None
        self._default_checksum_type = None
        self._default_sendbuf_size = None
        self._server_log_level = None
        self._server_threads = None
        self.discriminator = None

        if default_block_size is not None:
            self.default_block_size = default_block_size
        if default_checksum_type is not None:
            self.default_checksum_type = default_checksum_type
        if default_sendbuf_size is not None:
            self.default_sendbuf_size = default_sendbuf_size
        if server_log_level is not None:
            self.server_log_level = server_log_level
        if server_threads is not None:
            self.server_threads = server_threads

    @property
    def default_block_size(self):
        """Gets the default_block_size of this HdfsSettingsSettings.  # noqa: E501

        Block size (size=2**value) reported by HDFS server.  # noqa: E501

        :return: The default_block_size of this HdfsSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._default_block_size

    @default_block_size.setter
    def default_block_size(self, default_block_size):
        """Sets the default_block_size of this HdfsSettingsSettings.

        Block size (size=2**value) reported by HDFS server.  # noqa: E501

        :param default_block_size: The default_block_size of this HdfsSettingsSettings.  # noqa: E501
        :type: int
        """

        self._default_block_size = default_block_size

    @property
    def default_checksum_type(self):
        """Gets the default_checksum_type of this HdfsSettingsSettings.  # noqa: E501

        Checksum type reported by HDFS server.  # noqa: E501

        :return: The default_checksum_type of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_checksum_type

    @default_checksum_type.setter
    def default_checksum_type(self, default_checksum_type):
        """Sets the default_checksum_type of this HdfsSettingsSettings.

        Checksum type reported by HDFS server.  # noqa: E501

        :param default_checksum_type: The default_checksum_type of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["none", "crc32", "crc32c"]  # noqa: E501
        if default_checksum_type not in allowed_values:
            raise ValueError(
                "Invalid value for `default_checksum_type` ({0}), must be one of {1}"  # noqa: E501
                .format(default_checksum_type, allowed_values)
            )

        self._default_checksum_type = default_checksum_type

    @property
    def default_sendbuf_size(self):
        """Gets the default_sendbuf_size of this HdfsSettingsSettings.  # noqa: E501

        Send Buffer size used by HDFS server.  # noqa: E501

        :return: The default_sendbuf_size of this HdfsSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._default_sendbuf_size

    @default_sendbuf_size.setter
    def default_sendbuf_size(self, default_sendbuf_size):
        """Sets the default_sendbuf_size of this HdfsSettingsSettings.

        Send Buffer size used by HDFS server.  # noqa: E501

        :param default_sendbuf_size: The default_sendbuf_size of this HdfsSettingsSettings.  # noqa: E501
        :type: int
        """

        self._default_sendbuf_size = default_sendbuf_size

    @property
    def server_log_level(self):
        """Gets the server_log_level of this HdfsSettingsSettings.  # noqa: E501

        Log level for HDFS daemon.  # noqa: E501

        :return: The server_log_level of this HdfsSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._server_log_level

    @server_log_level.setter
    def server_log_level(self, server_log_level):
        """Sets the server_log_level of this HdfsSettingsSettings.

        Log level for HDFS daemon.  # noqa: E501

        :param server_log_level: The server_log_level of this HdfsSettingsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["emerg", "alert", "crit", "err", "warning", "notice", "info", "debug"]  # noqa: E501
        if server_log_level not in allowed_values:
            raise ValueError(
                "Invalid value for `server_log_level` ({0}), must be one of {1}"  # noqa: E501
                .format(server_log_level, allowed_values)
            )

        self._server_log_level = server_log_level

    @property
    def server_threads(self):
        """Gets the server_threads of this HdfsSettingsSettings.  # noqa: E501

        Number of worker threads for HDFS daemon.  # noqa: E501

        :return: The server_threads of this HdfsSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._server_threads

    @server_threads.setter
    def server_threads(self, server_threads):
        """Sets the server_threads of this HdfsSettingsSettings.

        Number of worker threads for HDFS daemon.  # noqa: E501

        :param server_threads: The server_threads of this HdfsSettingsSettings.  # noqa: E501
        :type: int
        """

        self._server_threads = server_threads

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
        if not isinstance(other, HdfsSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other