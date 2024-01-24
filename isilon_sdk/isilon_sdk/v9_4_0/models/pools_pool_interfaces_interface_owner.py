# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PoolsPoolInterfacesInterfaceOwner(object):
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
        'groupnet': 'str',
        'ip_addrs': 'list[str]',
        'pool': 'str',
        'subnet': 'str'
    }

    attribute_map = {
        'groupnet': 'groupnet',
        'ip_addrs': 'ip_addrs',
        'pool': 'pool',
        'subnet': 'subnet'
    }

    def __init__(self, groupnet=None, ip_addrs=None, pool=None, subnet=None):  # noqa: E501
        """PoolsPoolInterfacesInterfaceOwner - a model defined in Swagger"""  # noqa: E501

        self._groupnet = None
        self._ip_addrs = None
        self._pool = None
        self._subnet = None
        self.discriminator = None

        if groupnet is not None:
            self.groupnet = groupnet
        if ip_addrs is not None:
            self.ip_addrs = ip_addrs
        if pool is not None:
            self.pool = pool
        if subnet is not None:
            self.subnet = subnet

    @property
    def groupnet(self):
        """Gets the groupnet of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501


        :return: The groupnet of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """Sets the groupnet of this PoolsPoolInterfacesInterfaceOwner.


        :param groupnet: The groupnet of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501
        :type: str
        """
        if groupnet is not None and len(groupnet) > 32:
            raise ValueError("Invalid value for `groupnet`, length must be less than or equal to `32`")  # noqa: E501
        if groupnet is not None and len(groupnet) < 1:
            raise ValueError("Invalid value for `groupnet`, length must be greater than or equal to `1`")  # noqa: E501

        self._groupnet = groupnet

    @property
    def ip_addrs(self):
        """Gets the ip_addrs of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501

        List of IP addresses in this owner  # noqa: E501

        :return: The ip_addrs of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addrs

    @ip_addrs.setter
    def ip_addrs(self, ip_addrs):
        """Sets the ip_addrs of this PoolsPoolInterfacesInterfaceOwner.

        List of IP addresses in this owner  # noqa: E501

        :param ip_addrs: The ip_addrs of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501
        :type: list[str]
        """

        self._ip_addrs = ip_addrs

    @property
    def pool(self):
        """Gets the pool of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501


        :return: The pool of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this PoolsPoolInterfacesInterfaceOwner.


        :param pool: The pool of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501
        :type: str
        """
        if pool is not None and len(pool) > 32:
            raise ValueError("Invalid value for `pool`, length must be less than or equal to `32`")  # noqa: E501
        if pool is not None and len(pool) < 1:
            raise ValueError("Invalid value for `pool`, length must be greater than or equal to `1`")  # noqa: E501

        self._pool = pool

    @property
    def subnet(self):
        """Gets the subnet of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501


        :return: The subnet of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501
        :rtype: str
        """
        return self._subnet

    @subnet.setter
    def subnet(self, subnet):
        """Sets the subnet of this PoolsPoolInterfacesInterfaceOwner.


        :param subnet: The subnet of this PoolsPoolInterfacesInterfaceOwner.  # noqa: E501
        :type: str
        """
        if subnet is not None and len(subnet) > 32:
            raise ValueError("Invalid value for `subnet`, length must be less than or equal to `32`")  # noqa: E501
        if subnet is not None and len(subnet) < 1:
            raise ValueError("Invalid value for `subnet`, length must be greater than or equal to `1`")  # noqa: E501

        self._subnet = subnet

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
        if not isinstance(other, PoolsPoolInterfacesInterfaceOwner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other