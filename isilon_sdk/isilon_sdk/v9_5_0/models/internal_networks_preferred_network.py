# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 16
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InternalNetworksPreferredNetwork(object):
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
        'high_lnn': 'int',
        'low_lnn': 'int',
        'preferred_network': 'str'
    }

    attribute_map = {
        'high_lnn': 'high_lnn',
        'low_lnn': 'low_lnn',
        'preferred_network': 'preferred_network'
    }

    def __init__(self, high_lnn=None, low_lnn=None, preferred_network=None):  # noqa: E501
        """InternalNetworksPreferredNetwork - a model defined in Swagger"""  # noqa: E501

        self._high_lnn = None
        self._low_lnn = None
        self._preferred_network = None
        self.discriminator = None

        self.high_lnn = high_lnn
        self.low_lnn = low_lnn
        self.preferred_network = preferred_network

    @property
    def high_lnn(self):
        """Gets the high_lnn of this InternalNetworksPreferredNetwork.  # noqa: E501

        Low-numbered LNN of node pair  # noqa: E501

        :return: The high_lnn of this InternalNetworksPreferredNetwork.  # noqa: E501
        :rtype: int
        """
        return self._high_lnn

    @high_lnn.setter
    def high_lnn(self, high_lnn):
        """Sets the high_lnn of this InternalNetworksPreferredNetwork.

        Low-numbered LNN of node pair  # noqa: E501

        :param high_lnn: The high_lnn of this InternalNetworksPreferredNetwork.  # noqa: E501
        :type: int
        """
        if high_lnn is None:
            raise ValueError("Invalid value for `high_lnn`, must not be `None`")  # noqa: E501
        if high_lnn is not None and high_lnn > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `high_lnn`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if high_lnn is not None and high_lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `high_lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._high_lnn = high_lnn

    @property
    def low_lnn(self):
        """Gets the low_lnn of this InternalNetworksPreferredNetwork.  # noqa: E501

        Low-numbered LNN of node pair  # noqa: E501

        :return: The low_lnn of this InternalNetworksPreferredNetwork.  # noqa: E501
        :rtype: int
        """
        return self._low_lnn

    @low_lnn.setter
    def low_lnn(self, low_lnn):
        """Sets the low_lnn of this InternalNetworksPreferredNetwork.

        Low-numbered LNN of node pair  # noqa: E501

        :param low_lnn: The low_lnn of this InternalNetworksPreferredNetwork.  # noqa: E501
        :type: int
        """
        if low_lnn is None:
            raise ValueError("Invalid value for `low_lnn`, must not be `None`")  # noqa: E501
        if low_lnn is not None and low_lnn > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `low_lnn`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if low_lnn is not None and low_lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `low_lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._low_lnn = low_lnn

    @property
    def preferred_network(self):
        """Gets the preferred_network of this InternalNetworksPreferredNetwork.  # noqa: E501

        Backend network fabric primary network int-a and secondary network int-b  # noqa: E501

        :return: The preferred_network of this InternalNetworksPreferredNetwork.  # noqa: E501
        :rtype: str
        """
        return self._preferred_network

    @preferred_network.setter
    def preferred_network(self, preferred_network):
        """Sets the preferred_network of this InternalNetworksPreferredNetwork.

        Backend network fabric primary network int-a and secondary network int-b  # noqa: E501

        :param preferred_network: The preferred_network of this InternalNetworksPreferredNetwork.  # noqa: E501
        :type: str
        """
        if preferred_network is None:
            raise ValueError("Invalid value for `preferred_network`, must not be `None`")  # noqa: E501
        allowed_values = ["int-a", "int-b"]  # noqa: E501
        if preferred_network not in allowed_values:
            raise ValueError(
                "Invalid value for `preferred_network` ({0}), must be one of {1}"  # noqa: E501
                .format(preferred_network, allowed_values)
            )

        self._preferred_network = preferred_network

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
        if not isinstance(other, InternalNetworksPreferredNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other