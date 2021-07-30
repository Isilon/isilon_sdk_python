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


class DirectoryQueryScopeConditions(object):
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
        'attr': 'str',
        'operator': 'str',
        'value': 'str'
    }

    attribute_map = {
        'attr': 'attr',
        'operator': 'operator',
        'value': 'value'
    }

    def __init__(self, attr=None, operator=None, value=None):  # noqa: E501
        """DirectoryQueryScopeConditions - a model defined in Swagger"""  # noqa: E501

        self._attr = None
        self._operator = None
        self._value = None
        self.discriminator = None

        if attr is not None:
            self.attr = attr
        if operator is not None:
            self.operator = operator
        if value is not None:
            self.value = value

    @property
    def attr(self):
        """Gets the attr of this DirectoryQueryScopeConditions.  # noqa: E501


        :return: The attr of this DirectoryQueryScopeConditions.  # noqa: E501
        :rtype: str
        """
        return self._attr

    @attr.setter
    def attr(self, attr):
        """Sets the attr of this DirectoryQueryScopeConditions.


        :param attr: The attr of this DirectoryQueryScopeConditions.  # noqa: E501
        :type: str
        """

        self._attr = attr

    @property
    def operator(self):
        """Gets the operator of this DirectoryQueryScopeConditions.  # noqa: E501


        :return: The operator of this DirectoryQueryScopeConditions.  # noqa: E501
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this DirectoryQueryScopeConditions.


        :param operator: The operator of this DirectoryQueryScopeConditions.  # noqa: E501
        :type: str
        """

        self._operator = operator

    @property
    def value(self):
        """Gets the value of this DirectoryQueryScopeConditions.  # noqa: E501


        :return: The value of this DirectoryQueryScopeConditions.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this DirectoryQueryScopeConditions.


        :param value: The value of this DirectoryQueryScopeConditions.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, DirectoryQueryScopeConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
