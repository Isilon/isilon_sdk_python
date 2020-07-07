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

from isi_sdk_9_0_0.models.storagepool_tier_usage import StoragepoolTierUsage  # noqa: F401,E501


class StoragepoolStoragepool(object):
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
        'can_disable_l3': 'bool',
        'can_enable_l3': 'bool',
        'children': 'list[str]',
        'health_flags': 'list[str]',
        'id': 'int',
        'l3': 'bool',
        'l3_status': 'str',
        'lnns': 'list[int]',
        'manual': 'bool',
        'name': 'str',
        'node_type_ids': 'list[int]',
        'protection_policy': 'str',
        'type': 'str',
        'usage': 'StoragepoolTierUsage'
    }

    attribute_map = {
        'can_disable_l3': 'can_disable_l3',
        'can_enable_l3': 'can_enable_l3',
        'children': 'children',
        'health_flags': 'health_flags',
        'id': 'id',
        'l3': 'l3',
        'l3_status': 'l3_status',
        'lnns': 'lnns',
        'manual': 'manual',
        'name': 'name',
        'node_type_ids': 'node_type_ids',
        'protection_policy': 'protection_policy',
        'type': 'type',
        'usage': 'usage'
    }

    def __init__(self, can_disable_l3=None, can_enable_l3=None, children=None, health_flags=None, id=None, l3=None, l3_status=None, lnns=None, manual=None, name=None, node_type_ids=None, protection_policy=None, type=None, usage=None):  # noqa: E501
        """StoragepoolStoragepool - a model defined in Swagger"""  # noqa: E501

        self._can_disable_l3 = None
        self._can_enable_l3 = None
        self._children = None
        self._health_flags = None
        self._id = None
        self._l3 = None
        self._l3_status = None
        self._lnns = None
        self._manual = None
        self._name = None
        self._node_type_ids = None
        self._protection_policy = None
        self._type = None
        self._usage = None
        self.discriminator = None

        if can_disable_l3 is not None:
            self.can_disable_l3 = can_disable_l3
        if can_enable_l3 is not None:
            self.can_enable_l3 = can_enable_l3
        if children is not None:
            self.children = children
        if health_flags is not None:
            self.health_flags = health_flags
        self.id = id
        if l3 is not None:
            self.l3 = l3
        if l3_status is not None:
            self.l3_status = l3_status
        self.lnns = lnns
        if manual is not None:
            self.manual = manual
        self.name = name
        self.node_type_ids = node_type_ids
        if protection_policy is not None:
            self.protection_policy = protection_policy
        self.type = type
        self.usage = usage

    @property
    def can_disable_l3(self):
        """Gets the can_disable_l3 of this StoragepoolStoragepool.  # noqa: E501

        Indicates if disabling L3 is possible.  # noqa: E501

        :return: The can_disable_l3 of this StoragepoolStoragepool.  # noqa: E501
        :rtype: bool
        """
        return self._can_disable_l3

    @can_disable_l3.setter
    def can_disable_l3(self, can_disable_l3):
        """Sets the can_disable_l3 of this StoragepoolStoragepool.

        Indicates if disabling L3 is possible.  # noqa: E501

        :param can_disable_l3: The can_disable_l3 of this StoragepoolStoragepool.  # noqa: E501
        :type: bool
        """

        self._can_disable_l3 = can_disable_l3

    @property
    def can_enable_l3(self):
        """Gets the can_enable_l3 of this StoragepoolStoragepool.  # noqa: E501

        Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives.  # noqa: E501

        :return: The can_enable_l3 of this StoragepoolStoragepool.  # noqa: E501
        :rtype: bool
        """
        return self._can_enable_l3

    @can_enable_l3.setter
    def can_enable_l3(self, can_enable_l3):
        """Sets the can_enable_l3 of this StoragepoolStoragepool.

        Indicates if enabling L3 is possible. L3 cannot be enabled if there are unprovisioned drives.  # noqa: E501

        :param can_enable_l3: The can_enable_l3 of this StoragepoolStoragepool.  # noqa: E501
        :type: bool
        """

        self._can_enable_l3 = can_enable_l3

    @property
    def children(self):
        """Gets the children of this StoragepoolStoragepool.  # noqa: E501

        The names or IDs of the pool's children.  # noqa: E501

        :return: The children of this StoragepoolStoragepool.  # noqa: E501
        :rtype: list[str]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this StoragepoolStoragepool.

        The names or IDs of the pool's children.  # noqa: E501

        :param children: The children of this StoragepoolStoragepool.  # noqa: E501
        :type: list[str]
        """

        self._children = children

    @property
    def health_flags(self):
        """Gets the health_flags of this StoragepoolStoragepool.  # noqa: E501

        An array of containing any health issues with this pool.  If the pool is healthy, the list is empty.  Only appears on 'nodepool' type storagepools.  # noqa: E501

        :return: The health_flags of this StoragepoolStoragepool.  # noqa: E501
        :rtype: list[str]
        """
        return self._health_flags

    @health_flags.setter
    def health_flags(self, health_flags):
        """Sets the health_flags of this StoragepoolStoragepool.

        An array of containing any health issues with this pool.  If the pool is healthy, the list is empty.  Only appears on 'nodepool' type storagepools.  # noqa: E501

        :param health_flags: The health_flags of this StoragepoolStoragepool.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["underprovisioned", "missing_drives", "devices_down", "devices_smartfailed", "waiting_repair"]  # noqa: E501
        if not set(health_flags).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `health_flags` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(health_flags) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._health_flags = health_flags

    @property
    def id(self):
        """Gets the id of this StoragepoolStoragepool.  # noqa: E501

        The system ID given to the pool.  # noqa: E501

        :return: The id of this StoragepoolStoragepool.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StoragepoolStoragepool.

        The system ID given to the pool.  # noqa: E501

        :param id: The id of this StoragepoolStoragepool.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 1:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def l3(self):
        """Gets the l3 of this StoragepoolStoragepool.  # noqa: E501

        Use SSDs in this node pool for L3 cache.  # noqa: E501

        :return: The l3 of this StoragepoolStoragepool.  # noqa: E501
        :rtype: bool
        """
        return self._l3

    @l3.setter
    def l3(self, l3):
        """Sets the l3 of this StoragepoolStoragepool.

        Use SSDs in this node pool for L3 cache.  # noqa: E501

        :param l3: The l3 of this StoragepoolStoragepool.  # noqa: E501
        :type: bool
        """

        self._l3 = l3

    @property
    def l3_status(self):
        """Gets the l3_status of this StoragepoolStoragepool.  # noqa: E501

        'storage' if the 'l3' option is disabled. If the l3 option is enabled, 'migrating' if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, 'l3'.  # noqa: E501

        :return: The l3_status of this StoragepoolStoragepool.  # noqa: E501
        :rtype: str
        """
        return self._l3_status

    @l3_status.setter
    def l3_status(self, l3_status):
        """Sets the l3_status of this StoragepoolStoragepool.

        'storage' if the 'l3' option is disabled. If the l3 option is enabled, 'migrating' if any SSDs in this node pool have not yet been migrated to L3. If all SSDs have been migrated, 'l3'.  # noqa: E501

        :param l3_status: The l3_status of this StoragepoolStoragepool.  # noqa: E501
        :type: str
        """
        allowed_values = ["l3", "storage", "migrating"]  # noqa: E501
        if l3_status not in allowed_values:
            raise ValueError(
                "Invalid value for `l3_status` ({0}), must be one of {1}"  # noqa: E501
                .format(l3_status, allowed_values)
            )

        self._l3_status = l3_status

    @property
    def lnns(self):
        """Gets the lnns of this StoragepoolStoragepool.  # noqa: E501

        The nodes that are part of this pool.  # noqa: E501

        :return: The lnns of this StoragepoolStoragepool.  # noqa: E501
        :rtype: list[int]
        """
        return self._lnns

    @lnns.setter
    def lnns(self, lnns):
        """Sets the lnns of this StoragepoolStoragepool.

        The nodes that are part of this pool.  # noqa: E501

        :param lnns: The lnns of this StoragepoolStoragepool.  # noqa: E501
        :type: list[int]
        """
        if lnns is None:
            raise ValueError("Invalid value for `lnns`, must not be `None`")  # noqa: E501

        self._lnns = lnns

    @property
    def manual(self):
        """Gets the manual of this StoragepoolStoragepool.  # noqa: E501

        Whether or not the node pool is manually managed.  # noqa: E501

        :return: The manual of this StoragepoolStoragepool.  # noqa: E501
        :rtype: bool
        """
        return self._manual

    @manual.setter
    def manual(self, manual):
        """Sets the manual of this StoragepoolStoragepool.

        Whether or not the node pool is manually managed.  # noqa: E501

        :param manual: The manual of this StoragepoolStoragepool.  # noqa: E501
        :type: bool
        """

        self._manual = manual

    @property
    def name(self):
        """Gets the name of this StoragepoolStoragepool.  # noqa: E501

        The pool name.  # noqa: E501

        :return: The name of this StoragepoolStoragepool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoragepoolStoragepool.

        The pool name.  # noqa: E501

        :param name: The name of this StoragepoolStoragepool.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def node_type_ids(self):
        """Gets the node_type_ids of this StoragepoolStoragepool.  # noqa: E501

        The node types that are part of this pool.  # noqa: E501

        :return: The node_type_ids of this StoragepoolStoragepool.  # noqa: E501
        :rtype: list[int]
        """
        return self._node_type_ids

    @node_type_ids.setter
    def node_type_ids(self, node_type_ids):
        """Sets the node_type_ids of this StoragepoolStoragepool.

        The node types that are part of this pool.  # noqa: E501

        :param node_type_ids: The node_type_ids of this StoragepoolStoragepool.  # noqa: E501
        :type: list[int]
        """
        if node_type_ids is None:
            raise ValueError("Invalid value for `node_type_ids`, must not be `None`")  # noqa: E501

        self._node_type_ids = node_type_ids

    @property
    def protection_policy(self):
        """Gets the protection_policy of this StoragepoolStoragepool.  # noqa: E501

        The underlying protection policy.  # noqa: E501

        :return: The protection_policy of this StoragepoolStoragepool.  # noqa: E501
        :rtype: str
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this StoragepoolStoragepool.

        The underlying protection policy.  # noqa: E501

        :param protection_policy: The protection_policy of this StoragepoolStoragepool.  # noqa: E501
        :type: str
        """
        if protection_policy is not None and len(protection_policy) > 255:
            raise ValueError("Invalid value for `protection_policy`, length must be less than or equal to `255`")  # noqa: E501
        if protection_policy is not None and len(protection_policy) < 1:
            raise ValueError("Invalid value for `protection_policy`, length must be greater than or equal to `1`")  # noqa: E501

        self._protection_policy = protection_policy

    @property
    def type(self):
        """Gets the type of this StoragepoolStoragepool.  # noqa: E501

        The pool type.  # noqa: E501

        :return: The type of this StoragepoolStoragepool.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoragepoolStoragepool.

        The pool type.  # noqa: E501

        :param type: The type of this StoragepoolStoragepool.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["tier", "nodepool"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def usage(self):
        """Gets the usage of this StoragepoolStoragepool.  # noqa: E501

        Total pool usage.  # noqa: E501

        :return: The usage of this StoragepoolStoragepool.  # noqa: E501
        :rtype: StoragepoolTierUsage
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this StoragepoolStoragepool.

        Total pool usage.  # noqa: E501

        :param usage: The usage of this StoragepoolStoragepool.  # noqa: E501
        :type: StoragepoolTierUsage
        """
        if usage is None:
            raise ValueError("Invalid value for `usage`, must not be `None`")  # noqa: E501

        self._usage = usage

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
        if not isinstance(other, StoragepoolStoragepool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
