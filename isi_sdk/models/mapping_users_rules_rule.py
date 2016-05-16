# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class MappingUsersRulesRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        MappingUsersRulesRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'operator': 'str',
            'options': 'MappingUsersRulesRuleOptions',
            'user1': 'MappingUsersRulesRuleUser2',
            'user2': 'MappingUsersRulesRuleUser2'
        }

        self.attribute_map = {
            'operator': 'operator',
            'options': 'options',
            'user1': 'user1',
            'user2': 'user2'
        }

        self._operator = None
        self._options = None
        self._user1 = None
        self._user2 = None

    @property
    def operator(self):
        """
        Gets the operator of this MappingUsersRulesRule.
        Specifies the operator to make rules on specified users or groups.

        :return: The operator of this MappingUsersRulesRule.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """
        Sets the operator of this MappingUsersRulesRule.
        Specifies the operator to make rules on specified users or groups.

        :param operator: The operator of this MappingUsersRulesRule.
        :type: str
        """
        allowed_values = ["append", "insert", "replace", "trim", "union"]
        if operator not in allowed_values:
            raise ValueError(
                "Invalid value for `operator`, must be one of {0}"
                .format(allowed_values)
            )

        self._operator = operator

    @property
    def options(self):
        """
        Gets the options of this MappingUsersRulesRule.
        Specifies the properties for user mapping rules.

        :return: The options of this MappingUsersRulesRule.
        :rtype: MappingUsersRulesRuleOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this MappingUsersRulesRule.
        Specifies the properties for user mapping rules.

        :param options: The options of this MappingUsersRulesRule.
        :type: MappingUsersRulesRuleOptions
        """
        
        self._options = options

    @property
    def user1(self):
        """
        Gets the user1 of this MappingUsersRulesRule.
        

        :return: The user1 of this MappingUsersRulesRule.
        :rtype: MappingUsersRulesRuleUser2
        """
        return self._user1

    @user1.setter
    def user1(self, user1):
        """
        Sets the user1 of this MappingUsersRulesRule.
        

        :param user1: The user1 of this MappingUsersRulesRule.
        :type: MappingUsersRulesRuleUser2
        """
        
        self._user1 = user1

    @property
    def user2(self):
        """
        Gets the user2 of this MappingUsersRulesRule.
        

        :return: The user2 of this MappingUsersRulesRule.
        :rtype: MappingUsersRulesRuleUser2
        """
        return self._user2

    @user2.setter
    def user2(self, user2):
        """
        Sets the user2 of this MappingUsersRulesRule.
        

        :param user2: The user2 of this MappingUsersRulesRule.
        :type: MappingUsersRulesRuleUser2
        """
        
        self._user2 = user2

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

