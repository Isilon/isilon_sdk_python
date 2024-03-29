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


class SubnetsSubnetPoolIface(object):
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
        'iface': 'str',
        'lnn': 'int'
    }

    attribute_map = {
        'iface': 'iface',
        'lnn': 'lnn'
    }

    def __init__(self, iface=None, lnn=None):  # noqa: E501
        """SubnetsSubnetPoolIface - a model defined in Swagger"""  # noqa: E501

        self._iface = None
        self._lnn = None
        self.discriminator = None

        if iface is not None:
            self.iface = iface
        if lnn is not None:
            self.lnn = lnn

    @property
    def iface(self):
        """Gets the iface of this SubnetsSubnetPoolIface.  # noqa: E501

        A string that defines an interface name.  # noqa: E501

        :return: The iface of this SubnetsSubnetPoolIface.  # noqa: E501
        :rtype: str
        """
        return self._iface

    @iface.setter
    def iface(self, iface):
        """Sets the iface of this SubnetsSubnetPoolIface.

        A string that defines an interface name.  # noqa: E501

        :param iface: The iface of this SubnetsSubnetPoolIface.  # noqa: E501
        :type: str
        """
        if iface is not None and len(iface) > 32:
            raise ValueError("Invalid value for `iface`, length must be less than or equal to `32`")  # noqa: E501
        if iface is not None and len(iface) < 1:
            raise ValueError("Invalid value for `iface`, length must be greater than or equal to `1`")  # noqa: E501

        self._iface = iface

    @property
    def lnn(self):
        """Gets the lnn of this SubnetsSubnetPoolIface.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this SubnetsSubnetPoolIface.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this SubnetsSubnetPoolIface.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this SubnetsSubnetPoolIface.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

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
        if not isinstance(other, SubnetsSubnetPoolIface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
