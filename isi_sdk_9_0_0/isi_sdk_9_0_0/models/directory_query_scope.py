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

from isi_sdk_9_0_0.models.directory_query_scope_conditions import DirectoryQueryScopeConditions  # noqa: F401,E501


class DirectoryQueryScope(object):
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
        'conditions': 'list[DirectoryQueryScopeConditions]',
        'logic': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'logic': 'logic'
    }

    def __init__(self, conditions=None, logic=None):  # noqa: E501
        """DirectoryQueryScope - a model defined in Swagger"""  # noqa: E501

        self._conditions = None
        self._logic = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if logic is not None:
            self.logic = logic

    @property
    def conditions(self):
        """Gets the conditions of this DirectoryQueryScope.  # noqa: E501


        :return: The conditions of this DirectoryQueryScope.  # noqa: E501
        :rtype: list[DirectoryQueryScopeConditions]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this DirectoryQueryScope.


        :param conditions: The conditions of this DirectoryQueryScope.  # noqa: E501
        :type: list[DirectoryQueryScopeConditions]
        """

        self._conditions = conditions

    @property
    def logic(self):
        """Gets the logic of this DirectoryQueryScope.  # noqa: E501


        :return: The logic of this DirectoryQueryScope.  # noqa: E501
        :rtype: str
        """
        return self._logic

    @logic.setter
    def logic(self, logic):
        """Sets the logic of this DirectoryQueryScope.


        :param logic: The logic of this DirectoryQueryScope.  # noqa: E501
        :type: str
        """

        self._logic = logic

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
        if not isinstance(other, DirectoryQueryScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
