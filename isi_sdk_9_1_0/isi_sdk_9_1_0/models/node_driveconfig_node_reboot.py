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


class NodeDriveconfigNodeReboot(object):
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
        'chassis_loss': 'bool',
        'none_present': 'bool'
    }

    attribute_map = {
        'chassis_loss': 'chassis_loss',
        'none_present': 'none_present'
    }

    def __init__(self, chassis_loss=True, none_present=True):  # noqa: E501
        """NodeDriveconfigNodeReboot - a model defined in Swagger"""  # noqa: E501

        self._chassis_loss = None
        self._none_present = None
        self.discriminator = None

        if chassis_loss is not None:
            self.chassis_loss = chassis_loss
        if none_present is not None:
            self.none_present = none_present

    @property
    def chassis_loss(self):
        """Gets the chassis_loss of this NodeDriveconfigNodeReboot.  # noqa: E501

        Indicates whether or not to reboot the node due to a lost chassis.  # noqa: E501

        :return: The chassis_loss of this NodeDriveconfigNodeReboot.  # noqa: E501
        :rtype: bool
        """
        return self._chassis_loss

    @chassis_loss.setter
    def chassis_loss(self, chassis_loss):
        """Sets the chassis_loss of this NodeDriveconfigNodeReboot.

        Indicates whether or not to reboot the node due to a lost chassis.  # noqa: E501

        :param chassis_loss: The chassis_loss of this NodeDriveconfigNodeReboot.  # noqa: E501
        :type: bool
        """

        self._chassis_loss = chassis_loss

    @property
    def none_present(self):
        """Gets the none_present of this NodeDriveconfigNodeReboot.  # noqa: E501

        Indicates whether or not to reboot the node if no drives are present.  # noqa: E501

        :return: The none_present of this NodeDriveconfigNodeReboot.  # noqa: E501
        :rtype: bool
        """
        return self._none_present

    @none_present.setter
    def none_present(self, none_present):
        """Sets the none_present of this NodeDriveconfigNodeReboot.

        Indicates whether or not to reboot the node if no drives are present.  # noqa: E501

        :param none_present: The none_present of this NodeDriveconfigNodeReboot.  # noqa: E501
        :type: bool
        """

        self._none_present = none_present

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
        if not isinstance(other, NodeDriveconfigNodeReboot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
