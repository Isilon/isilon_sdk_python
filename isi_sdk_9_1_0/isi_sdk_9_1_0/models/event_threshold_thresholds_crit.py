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


class EventThresholdThresholdsCrit(object):
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
        'level': 'str',
        'value': 'str'
    }

    attribute_map = {
        'level': 'level',
        'value': 'value'
    }

    def __init__(self, level=None, value=None):  # noqa: E501
        """EventThresholdThresholdsCrit - a model defined in Swagger"""  # noqa: E501

        self._level = None
        self._value = None
        self.discriminator = None

        if level is not None:
            self.level = level
        if value is not None:
            self.value = value

    @property
    def level(self):
        """Gets the level of this EventThresholdThresholdsCrit.  # noqa: E501


        :return: The level of this EventThresholdThresholdsCrit.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this EventThresholdThresholdsCrit.


        :param level: The level of this EventThresholdThresholdsCrit.  # noqa: E501
        :type: str
        """
        if level is not None and len(level) > 255:
            raise ValueError("Invalid value for `level`, length must be less than or equal to `255`")  # noqa: E501
        if level is not None and len(level) < 0:
            raise ValueError("Invalid value for `level`, length must be greater than or equal to `0`")  # noqa: E501

        self._level = level

    @property
    def value(self):
        """Gets the value of this EventThresholdThresholdsCrit.  # noqa: E501


        :return: The value of this EventThresholdThresholdsCrit.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EventThresholdThresholdsCrit.


        :param value: The value of this EventThresholdThresholdsCrit.  # noqa: E501
        :type: str
        """
        if value is not None and len(value) > 255:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `255`")  # noqa: E501
        if value is not None and len(value) < 0:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `0`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, EventThresholdThresholdsCrit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
