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


class StoragepoolNodepool(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StoragepoolNodepool - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'l3': 'bool',
            'lnns': 'list[int]',
            'name': 'str',
            'protection_policy': 'str',
            'tier': 'str'
        }

        self.attribute_map = {
            'l3': 'l3',
            'lnns': 'lnns',
            'name': 'name',
            'protection_policy': 'protection_policy',
            'tier': 'tier'
        }

        self._l3 = None
        self._lnns = None
        self._name = None
        self._protection_policy = None
        self._tier = None

    @property
    def l3(self):
        """
        Gets the l3 of this StoragepoolNodepool.
        Use SSDs in this node pool for L3 cache.

        :return: The l3 of this StoragepoolNodepool.
        :rtype: bool
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """
        Sets the l3 of this StoragepoolNodepool.
        Use SSDs in this node pool for L3 cache.

        :param l3: The l3 of this StoragepoolNodepool.
        :type: bool
        """
        
        self._l3 = l3

    @property
    def lnns(self):
        """
        Gets the lnns of this StoragepoolNodepool.
        The nodes that are part of this node pool.

        :return: The lnns of this StoragepoolNodepool.
        :rtype: list[int]
        """
        return self._lnns

    @lnns.setter
    def lnns(self, lnns):
        """
        Sets the lnns of this StoragepoolNodepool.
        The nodes that are part of this node pool.

        :param lnns: The lnns of this StoragepoolNodepool.
        :type: list[int]
        """
        
        self._lnns = lnns

    @property
    def name(self):
        """
        Gets the name of this StoragepoolNodepool.
        The node pool name.

        :return: The name of this StoragepoolNodepool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragepoolNodepool.
        The node pool name.

        :param name: The name of this StoragepoolNodepool.
        :type: str
        """
        
        self._name = name

    @property
    def protection_policy(self):
        """
        Gets the protection_policy of this StoragepoolNodepool.
        The node pool protection policy.

        :return: The protection_policy of this StoragepoolNodepool.
        :rtype: str
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """
        Sets the protection_policy of this StoragepoolNodepool.
        The node pool protection policy.

        :param protection_policy: The protection_policy of this StoragepoolNodepool.
        :type: str
        """
        
        self._protection_policy = protection_policy

    @property
    def tier(self):
        """
        Gets the tier of this StoragepoolNodepool.
        The name or ID of the node pool's tier, if it is in a tier.

        :return: The tier of this StoragepoolNodepool.
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """
        Sets the tier of this StoragepoolNodepool.
        The name or ID of the node pool's tier, if it is in a tier.

        :param tier: The tier of this StoragepoolNodepool.
        :type: str
        """
        
        self._tier = tier

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

