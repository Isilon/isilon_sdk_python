# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 7
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MappingUsersRulesRuleUser2(object):
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
        'domain': 'str',
        'user': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'user': 'user'
    }

    def __init__(self, domain=None, user=None):  # noqa: E501
        """MappingUsersRulesRuleUser2 - a model defined in Swagger"""  # noqa: E501

        self._domain = None
        self._user = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if user is not None:
            self.user = user

    @property
    def domain(self):
        """Gets the domain of this MappingUsersRulesRuleUser2.  # noqa: E501


        :return: The domain of this MappingUsersRulesRuleUser2.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this MappingUsersRulesRuleUser2.


        :param domain: The domain of this MappingUsersRulesRuleUser2.  # noqa: E501
        :type: str
        """
        if domain is not None and len(domain) > 255:
            raise ValueError("Invalid value for `domain`, length must be less than or equal to `255`")  # noqa: E501
        if domain is not None and len(domain) < 0:
            raise ValueError("Invalid value for `domain`, length must be greater than or equal to `0`")  # noqa: E501

        self._domain = domain

    @property
    def user(self):
        """Gets the user of this MappingUsersRulesRuleUser2.  # noqa: E501


        :return: The user of this MappingUsersRulesRuleUser2.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this MappingUsersRulesRuleUser2.


        :param user: The user of this MappingUsersRulesRuleUser2.  # noqa: E501
        :type: str
        """
        if user is not None and len(user) > 255:
            raise ValueError("Invalid value for `user`, length must be less than or equal to `255`")  # noqa: E501
        if user is not None and len(user) < 0:
            raise ValueError("Invalid value for `user`, length must be greater than or equal to `0`")  # noqa: E501

        self._user = user

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
        if not isinstance(other, MappingUsersRulesRuleUser2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
