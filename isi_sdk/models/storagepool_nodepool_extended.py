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


class StoragepoolNodepoolExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StoragepoolNodepoolExtended - a model defined in Swagger

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
            'tier': 'str',
            'can_enable_l3': 'bool',
            'id': 'int',
            'l3_status': 'str',
            'manual': 'bool',
            'usage': 'StoragepoolTierUsage'
        }

        self.attribute_map = {
            'l3': 'l3',
            'lnns': 'lnns',
            'name': 'name',
            'protection_policy': 'protection_policy',
            'tier': 'tier',
            'can_enable_l3': 'can_enable_l3',
            'id': 'id',
            'l3_status': 'l3_status',
            'manual': 'manual',
            'usage': 'usage'
        }

        self._l3 = None
        self._lnns = None
        self._name = None
        self._protection_policy = None
        self._tier = None
        self._can_enable_l3 = None
        self._id = None
        self._l3_status = None
        self._manual = None
        self._usage = None

    @property
    def l3(self):
        """
        Gets the l3 of this StoragepoolNodepoolExtended.
        Use SSDs in this node pool for L3 cache.

        :return: The l3 of this StoragepoolNodepoolExtended.
        :rtype: bool
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """
        Sets the l3 of this StoragepoolNodepoolExtended.
        Use SSDs in this node pool for L3 cache.

        :param l3: The l3 of this StoragepoolNodepoolExtended.
        :type: bool
        """
        
        self._l3 = l3

    @property
    def lnns(self):
        """
        Gets the lnns of this StoragepoolNodepoolExtended.
        The nodes that are part of this node pool.

        :return: The lnns of this StoragepoolNodepoolExtended.
        :rtype: list[int]
        """
        return self._lnns

    @lnns.setter
    def lnns(self, lnns):
        """
        Sets the lnns of this StoragepoolNodepoolExtended.
        The nodes that are part of this node pool.

        :param lnns: The lnns of this StoragepoolNodepoolExtended.
        :type: list[int]
        """
        
        self._lnns = lnns

    @property
    def name(self):
        """
        Gets the name of this StoragepoolNodepoolExtended.
        The node pool name.

        :return: The name of this StoragepoolNodepoolExtended.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoragepoolNodepoolExtended.
        The node pool name.

        :param name: The name of this StoragepoolNodepoolExtended.
        :type: str
        """
        
        self._name = name

    @property
    def protection_policy(self):
        """
        Gets the protection_policy of this StoragepoolNodepoolExtended.
        The node pool protection policy.

        :return: The protection_policy of this StoragepoolNodepoolExtended.
        :rtype: str
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """
        Sets the protection_policy of this StoragepoolNodepoolExtended.
        The node pool protection policy.

        :param protection_policy: The protection_policy of this StoragepoolNodepoolExtended.
        :type: str
        """
        
        self._protection_policy = protection_policy

    @property
    def tier(self):
        """
        Gets the tier of this StoragepoolNodepoolExtended.
        The name or ID of the node pool's tier, if it is in a tier.

        :return: The tier of this StoragepoolNodepoolExtended.
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """
        Sets the tier of this StoragepoolNodepoolExtended.
        The name or ID of the node pool's tier, if it is in a tier.

        :param tier: The tier of this StoragepoolNodepoolExtended.
        :type: str
        """
        
        self._tier = tier

    @property
    def can_enable_l3(self):
        """
        Gets the can_enable_l3 of this StoragepoolNodepoolExtended.
        Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives.

        :return: The can_enable_l3 of this StoragepoolNodepoolExtended.
        :rtype: bool
        """
        return self._can_enable_l3

    @can_enable_l3.setter
    def can_enable_l3(self, can_enable_l3):
        """
        Sets the can_enable_l3 of this StoragepoolNodepoolExtended.
        Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives.

        :param can_enable_l3: The can_enable_l3 of this StoragepoolNodepoolExtended.
        :type: bool
        """
        
        self._can_enable_l3 = can_enable_l3

    @property
    def id(self):
        """
        Gets the id of this StoragepoolNodepoolExtended.
        The system ID given to the node pool.

        :return: The id of this StoragepoolNodepoolExtended.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StoragepoolNodepoolExtended.
        The system ID given to the node pool.

        :param id: The id of this StoragepoolNodepoolExtended.
        :type: int
        """
        
        self._id = id

    @property
    def l3_status(self):
        """
        Gets the l3_status of this StoragepoolNodepoolExtended.
        'storage' if the 'l3' option is disabled. If the l3 option is enabled, 'migrating' if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, 'l3'.

        :return: The l3_status of this StoragepoolNodepoolExtended.
        :rtype: str
        """
        return self._l3_status

    @l3_status.setter
    def l3_status(self, l3_status):
        """
        Sets the l3_status of this StoragepoolNodepoolExtended.
        'storage' if the 'l3' option is disabled. If the l3 option is enabled, 'migrating' if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, 'l3'.

        :param l3_status: The l3_status of this StoragepoolNodepoolExtended.
        :type: str
        """
        allowed_values = ["l3", "storage", "migrating"]
        if l3_status not in allowed_values:
            raise ValueError(
                "Invalid value for `l3_status`, must be one of {0}"
                .format(allowed_values)
            )

        self._l3_status = l3_status

    @property
    def manual(self):
        """
        Gets the manual of this StoragepoolNodepoolExtended.
        Whether or not the node pool is manually managed.

        :return: The manual of this StoragepoolNodepoolExtended.
        :rtype: bool
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        """
        Sets the manual of this StoragepoolNodepoolExtended.
        Whether or not the node pool is manually managed.

        :param manual: The manual of this StoragepoolNodepoolExtended.
        :type: bool
        """
        
        self._manual = manual

    @property
    def usage(self):
        """
        Gets the usage of this StoragepoolNodepoolExtended.
        Total pool usage.

        :return: The usage of this StoragepoolNodepoolExtended.
        :rtype: StoragepoolTierUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """
        Sets the usage of this StoragepoolNodepoolExtended.
        Total pool usage.

        :param usage: The usage of this StoragepoolNodepoolExtended.
        :type: StoragepoolTierUsage
        """
        
        self._usage = usage

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

