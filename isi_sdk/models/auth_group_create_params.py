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


class AuthGroupCreateParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuthGroupCreateParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'gid': 'int',
            'members': 'list[GroupMember]',
            'name': 'str',
            'sid': 'str'
        }

        self.attribute_map = {
            'gid': 'gid',
            'members': 'members',
            'name': 'name',
            'sid': 'sid'
        }

        self._gid = None
        self._members = None
        self._name = None
        self._sid = None

    @property
    def gid(self):
        """
        Gets the gid of this AuthGroupCreateParams.
        Specifies the numeric group identifier.

        :return: The gid of this AuthGroupCreateParams.
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """
        Sets the gid of this AuthGroupCreateParams.
        Specifies the numeric group identifier.

        :param gid: The gid of this AuthGroupCreateParams.
        :type: int
        """
        
        self._gid = gid

    @property
    def members(self):
        """
        Gets the members of this AuthGroupCreateParams.
        Specifies the members of the group.

        :return: The members of this AuthGroupCreateParams.
        :rtype: list[GroupMember]
        """
        return self._members

    @members.setter
    def members(self, members):
        """
        Sets the members of this AuthGroupCreateParams.
        Specifies the members of the group.

        :param members: The members of this AuthGroupCreateParams.
        :type: list[GroupMember]
        """
        
        self._members = members

    @property
    def name(self):
        """
        Gets the name of this AuthGroupCreateParams.
        Specifies the group name.

        :return: The name of this AuthGroupCreateParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AuthGroupCreateParams.
        Specifies the group name.

        :param name: The name of this AuthGroupCreateParams.
        :type: str
        """
        
        self._name = name

    @property
    def sid(self):
        """
        Gets the sid of this AuthGroupCreateParams.
        Specifies the security identifier.

        :return: The sid of this AuthGroupCreateParams.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this AuthGroupCreateParams.
        Specifies the security identifier.

        :param sid: The sid of this AuthGroupCreateParams.
        :type: str
        """
        
        self._sid = sid

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

