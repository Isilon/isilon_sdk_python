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

from isi_sdk_9_0_0.models.cloud_proxy import CloudProxy  # noqa: F401,E501


class CloudProxyCreateParams(object):
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
        'host': 'str',
        'name': 'str',
        'password': 'str',
        'port': 'int',
        'type': 'str',
        'username': 'str'
    }

    attribute_map = {
        'host': 'host',
        'name': 'name',
        'password': 'password',
        'port': 'port',
        'type': 'type',
        'username': 'username'
    }

    def __init__(self, host=None, name=None, password=None, port=None, type=None, username=None):  # noqa: E501
        """CloudProxyCreateParams - a model defined in Swagger"""  # noqa: E501

        self._host = None
        self._name = None
        self._password = None
        self._port = None
        self._type = None
        self._username = None
        self.discriminator = None

        self.host = host
        self.name = name
        if password is not None:
            self.password = password
        self.port = port
        self.type = type
        if username is not None:
            self.username = username

    @property
    def host(self):
        """Gets the host of this CloudProxyCreateParams.  # noqa: E501

        A host name or network address for connecting to this proxy  # noqa: E501

        :return: The host of this CloudProxyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this CloudProxyCreateParams.

        A host name or network address for connecting to this proxy  # noqa: E501

        :param host: The host of this CloudProxyCreateParams.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def name(self):
        """Gets the name of this CloudProxyCreateParams.  # noqa: E501

        A unique friendly name for this proxy configuration  # noqa: E501

        :return: The name of this CloudProxyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudProxyCreateParams.

        A unique friendly name for this proxy configuration  # noqa: E501

        :param name: The name of this CloudProxyCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def password(self):
        """Gets the password of this CloudProxyCreateParams.  # noqa: E501

        The password to connect to this proxy if required (write-only)  # noqa: E501

        :return: The password of this CloudProxyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CloudProxyCreateParams.

        The password to connect to this proxy if required (write-only)  # noqa: E501

        :param password: The password of this CloudProxyCreateParams.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def port(self):
        """Gets the port of this CloudProxyCreateParams.  # noqa: E501

        The port used to connect to this proxy  # noqa: E501

        :return: The port of this CloudProxyCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this CloudProxyCreateParams.

        The port used to connect to this proxy  # noqa: E501

        :param port: The port of this CloudProxyCreateParams.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def type(self):
        """Gets the type of this CloudProxyCreateParams.  # noqa: E501

        The type of connection used to connect to this proxy  # noqa: E501

        :return: The type of this CloudProxyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudProxyCreateParams.

        The type of connection used to connect to this proxy  # noqa: E501

        :param type: The type of this CloudProxyCreateParams.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["socks_4", "socks_5", "http"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def username(self):
        """Gets the username of this CloudProxyCreateParams.  # noqa: E501

        The username to connect to this proxy if required  # noqa: E501

        :return: The username of this CloudProxyCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CloudProxyCreateParams.

        The username to connect to this proxy if required  # noqa: E501

        :param username: The username of this CloudProxyCreateParams.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if not isinstance(other, CloudProxyCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
