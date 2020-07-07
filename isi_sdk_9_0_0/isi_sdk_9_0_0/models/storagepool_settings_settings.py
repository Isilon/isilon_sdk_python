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

from isi_sdk_9_0_0.models.storagepool_settings_settings_spillover_target import StoragepoolSettingsSettingsSpilloverTarget  # noqa: F401,E501


class StoragepoolSettingsSettings(object):
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
        'automatically_manage_io_optimization': 'str',
        'automatically_manage_protection': 'str',
        'global_namespace_acceleration_enabled': 'bool',
        'global_namespace_acceleration_state': 'str',
        'protect_directories_one_level_higher': 'bool',
        'spillover_enabled': 'bool',
        'spillover_target': 'StoragepoolSettingsSettingsSpilloverTarget',
        'ssd_l3_cache_default_enabled': 'bool',
        'ssd_qab_mirrors': 'str',
        'ssd_system_btree_mirrors': 'str',
        'ssd_system_delta_mirrors': 'str',
        'virtual_hot_spare_deny_writes': 'bool',
        'virtual_hot_spare_hide_spare': 'bool',
        'virtual_hot_spare_limit_drives': 'int',
        'virtual_hot_spare_limit_percent': 'int'
    }

    attribute_map = {
        'automatically_manage_io_optimization': 'automatically_manage_io_optimization',
        'automatically_manage_protection': 'automatically_manage_protection',
        'global_namespace_acceleration_enabled': 'global_namespace_acceleration_enabled',
        'global_namespace_acceleration_state': 'global_namespace_acceleration_state',
        'protect_directories_one_level_higher': 'protect_directories_one_level_higher',
        'spillover_enabled': 'spillover_enabled',
        'spillover_target': 'spillover_target',
        'ssd_l3_cache_default_enabled': 'ssd_l3_cache_default_enabled',
        'ssd_qab_mirrors': 'ssd_qab_mirrors',
        'ssd_system_btree_mirrors': 'ssd_system_btree_mirrors',
        'ssd_system_delta_mirrors': 'ssd_system_delta_mirrors',
        'virtual_hot_spare_deny_writes': 'virtual_hot_spare_deny_writes',
        'virtual_hot_spare_hide_spare': 'virtual_hot_spare_hide_spare',
        'virtual_hot_spare_limit_drives': 'virtual_hot_spare_limit_drives',
        'virtual_hot_spare_limit_percent': 'virtual_hot_spare_limit_percent'
    }

    def __init__(self, automatically_manage_io_optimization=None, automatically_manage_protection=None, global_namespace_acceleration_enabled=None, global_namespace_acceleration_state=None, protect_directories_one_level_higher=None, spillover_enabled=None, spillover_target=None, ssd_l3_cache_default_enabled=None, ssd_qab_mirrors=None, ssd_system_btree_mirrors=None, ssd_system_delta_mirrors=None, virtual_hot_spare_deny_writes=None, virtual_hot_spare_hide_spare=None, virtual_hot_spare_limit_drives=None, virtual_hot_spare_limit_percent=None):  # noqa: E501
        """StoragepoolSettingsSettings - a model defined in Swagger"""  # noqa: E501

        self._automatically_manage_io_optimization = None
        self._automatically_manage_protection = None
        self._global_namespace_acceleration_enabled = None
        self._global_namespace_acceleration_state = None
        self._protect_directories_one_level_higher = None
        self._spillover_enabled = None
        self._spillover_target = None
        self._ssd_l3_cache_default_enabled = None
        self._ssd_qab_mirrors = None
        self._ssd_system_btree_mirrors = None
        self._ssd_system_delta_mirrors = None
        self._virtual_hot_spare_deny_writes = None
        self._virtual_hot_spare_hide_spare = None
        self._virtual_hot_spare_limit_drives = None
        self._virtual_hot_spare_limit_percent = None
        self.discriminator = None

        self.automatically_manage_io_optimization = automatically_manage_io_optimization
        self.automatically_manage_protection = automatically_manage_protection
        self.global_namespace_acceleration_enabled = global_namespace_acceleration_enabled
        self.global_namespace_acceleration_state = global_namespace_acceleration_state
        self.protect_directories_one_level_higher = protect_directories_one_level_higher
        self.spillover_enabled = spillover_enabled
        self.spillover_target = spillover_target
        self.ssd_l3_cache_default_enabled = ssd_l3_cache_default_enabled
        self.ssd_qab_mirrors = ssd_qab_mirrors
        self.ssd_system_btree_mirrors = ssd_system_btree_mirrors
        self.ssd_system_delta_mirrors = ssd_system_delta_mirrors
        self.virtual_hot_spare_deny_writes = virtual_hot_spare_deny_writes
        self.virtual_hot_spare_hide_spare = virtual_hot_spare_hide_spare
        self.virtual_hot_spare_limit_drives = virtual_hot_spare_limit_drives
        self.virtual_hot_spare_limit_percent = virtual_hot_spare_limit_percent

    @property
    def automatically_manage_io_optimization(self):
        """Gets the automatically_manage_io_optimization of this StoragepoolSettingsSettings.  # noqa: E501

        Automatically manage IO optimization settings on files.  # noqa: E501

        :return: The automatically_manage_io_optimization of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._automatically_manage_io_optimization

    @automatically_manage_io_optimization.setter
    def automatically_manage_io_optimization(self, automatically_manage_io_optimization):
        """Sets the automatically_manage_io_optimization of this StoragepoolSettingsSettings.

        Automatically manage IO optimization settings on files.  # noqa: E501

        :param automatically_manage_io_optimization: The automatically_manage_io_optimization of this StoragepoolSettingsSettings.  # noqa: E501
        :type: str
        """
        if automatically_manage_io_optimization is None:
            raise ValueError("Invalid value for `automatically_manage_io_optimization`, must not be `None`")  # noqa: E501
        allowed_values = ["all", "files_at_default", "none"]  # noqa: E501
        if automatically_manage_io_optimization not in allowed_values:
            raise ValueError(
                "Invalid value for `automatically_manage_io_optimization` ({0}), must be one of {1}"  # noqa: E501
                .format(automatically_manage_io_optimization, allowed_values)
            )

        self._automatically_manage_io_optimization = automatically_manage_io_optimization

    @property
    def automatically_manage_protection(self):
        """Gets the automatically_manage_protection of this StoragepoolSettingsSettings.  # noqa: E501

        Automatically manage protection settings on files.  # noqa: E501

        :return: The automatically_manage_protection of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._automatically_manage_protection

    @automatically_manage_protection.setter
    def automatically_manage_protection(self, automatically_manage_protection):
        """Sets the automatically_manage_protection of this StoragepoolSettingsSettings.

        Automatically manage protection settings on files.  # noqa: E501

        :param automatically_manage_protection: The automatically_manage_protection of this StoragepoolSettingsSettings.  # noqa: E501
        :type: str
        """
        if automatically_manage_protection is None:
            raise ValueError("Invalid value for `automatically_manage_protection`, must not be `None`")  # noqa: E501
        allowed_values = ["all", "files_at_default", "none"]  # noqa: E501
        if automatically_manage_protection not in allowed_values:
            raise ValueError(
                "Invalid value for `automatically_manage_protection` ({0}), must be one of {1}"  # noqa: E501
                .format(automatically_manage_protection, allowed_values)
            )

        self._automatically_manage_protection = automatically_manage_protection

    @property
    def global_namespace_acceleration_enabled(self):
        """Gets the global_namespace_acceleration_enabled of this StoragepoolSettingsSettings.  # noqa: E501

        Optimize namespace operations by storing metadata on SSDs.  # noqa: E501

        :return: The global_namespace_acceleration_enabled of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._global_namespace_acceleration_enabled

    @global_namespace_acceleration_enabled.setter
    def global_namespace_acceleration_enabled(self, global_namespace_acceleration_enabled):
        """Sets the global_namespace_acceleration_enabled of this StoragepoolSettingsSettings.

        Optimize namespace operations by storing metadata on SSDs.  # noqa: E501

        :param global_namespace_acceleration_enabled: The global_namespace_acceleration_enabled of this StoragepoolSettingsSettings.  # noqa: E501
        :type: bool
        """
        if global_namespace_acceleration_enabled is None:
            raise ValueError("Invalid value for `global_namespace_acceleration_enabled`, must not be `None`")  # noqa: E501

        self._global_namespace_acceleration_enabled = global_namespace_acceleration_enabled

    @property
    def global_namespace_acceleration_state(self):
        """Gets the global_namespace_acceleration_state of this StoragepoolSettingsSettings.  # noqa: E501

        Whether or not namespace operation optimizations are currently in effect.  # noqa: E501

        :return: The global_namespace_acceleration_state of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._global_namespace_acceleration_state

    @global_namespace_acceleration_state.setter
    def global_namespace_acceleration_state(self, global_namespace_acceleration_state):
        """Sets the global_namespace_acceleration_state of this StoragepoolSettingsSettings.

        Whether or not namespace operation optimizations are currently in effect.  # noqa: E501

        :param global_namespace_acceleration_state: The global_namespace_acceleration_state of this StoragepoolSettingsSettings.  # noqa: E501
        :type: str
        """
        if global_namespace_acceleration_state is None:
            raise ValueError("Invalid value for `global_namespace_acceleration_state`, must not be `None`")  # noqa: E501
        allowed_values = ["honored", "inactive"]  # noqa: E501
        if global_namespace_acceleration_state not in allowed_values:
            raise ValueError(
                "Invalid value for `global_namespace_acceleration_state` ({0}), must be one of {1}"  # noqa: E501
                .format(global_namespace_acceleration_state, allowed_values)
            )

        self._global_namespace_acceleration_state = global_namespace_acceleration_state

    @property
    def protect_directories_one_level_higher(self):
        """Gets the protect_directories_one_level_higher of this StoragepoolSettingsSettings.  # noqa: E501

        Automatically add additional protection level to all directories.  # noqa: E501

        :return: The protect_directories_one_level_higher of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._protect_directories_one_level_higher

    @protect_directories_one_level_higher.setter
    def protect_directories_one_level_higher(self, protect_directories_one_level_higher):
        """Sets the protect_directories_one_level_higher of this StoragepoolSettingsSettings.

        Automatically add additional protection level to all directories.  # noqa: E501

        :param protect_directories_one_level_higher: The protect_directories_one_level_higher of this StoragepoolSettingsSettings.  # noqa: E501
        :type: bool
        """
        if protect_directories_one_level_higher is None:
            raise ValueError("Invalid value for `protect_directories_one_level_higher`, must not be `None`")  # noqa: E501

        self._protect_directories_one_level_higher = protect_directories_one_level_higher

    @property
    def spillover_enabled(self):
        """Gets the spillover_enabled of this StoragepoolSettingsSettings.  # noqa: E501

        Spill writes into other pools as needed.  # noqa: E501

        :return: The spillover_enabled of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._spillover_enabled

    @spillover_enabled.setter
    def spillover_enabled(self, spillover_enabled):
        """Sets the spillover_enabled of this StoragepoolSettingsSettings.

        Spill writes into other pools as needed.  # noqa: E501

        :param spillover_enabled: The spillover_enabled of this StoragepoolSettingsSettings.  # noqa: E501
        :type: bool
        """
        if spillover_enabled is None:
            raise ValueError("Invalid value for `spillover_enabled`, must not be `None`")  # noqa: E501

        self._spillover_enabled = spillover_enabled

    @property
    def spillover_target(self):
        """Gets the spillover_target of this StoragepoolSettingsSettings.  # noqa: E501

        Target pool for spilled writes.  # noqa: E501

        :return: The spillover_target of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: StoragepoolSettingsSettingsSpilloverTarget
        """
        return self._spillover_target

    @spillover_target.setter
    def spillover_target(self, spillover_target):
        """Sets the spillover_target of this StoragepoolSettingsSettings.

        Target pool for spilled writes.  # noqa: E501

        :param spillover_target: The spillover_target of this StoragepoolSettingsSettings.  # noqa: E501
        :type: StoragepoolSettingsSettingsSpilloverTarget
        """
        if spillover_target is None:
            raise ValueError("Invalid value for `spillover_target`, must not be `None`")  # noqa: E501

        self._spillover_target = spillover_target

    @property
    def ssd_l3_cache_default_enabled(self):
        """Gets the ssd_l3_cache_default_enabled of this StoragepoolSettingsSettings.  # noqa: E501

        The L3 Cache default enabled state. This specifies whether L3 Cache should be enabled on new node pools.  # noqa: E501

        :return: The ssd_l3_cache_default_enabled of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._ssd_l3_cache_default_enabled

    @ssd_l3_cache_default_enabled.setter
    def ssd_l3_cache_default_enabled(self, ssd_l3_cache_default_enabled):
        """Sets the ssd_l3_cache_default_enabled of this StoragepoolSettingsSettings.

        The L3 Cache default enabled state. This specifies whether L3 Cache should be enabled on new node pools.  # noqa: E501

        :param ssd_l3_cache_default_enabled: The ssd_l3_cache_default_enabled of this StoragepoolSettingsSettings.  # noqa: E501
        :type: bool
        """
        if ssd_l3_cache_default_enabled is None:
            raise ValueError("Invalid value for `ssd_l3_cache_default_enabled`, must not be `None`")  # noqa: E501

        self._ssd_l3_cache_default_enabled = ssd_l3_cache_default_enabled

    @property
    def ssd_qab_mirrors(self):
        """Gets the ssd_qab_mirrors of this StoragepoolSettingsSettings.  # noqa: E501

        Controls number of mirrors of QAB blocks to place on SSDs.  # noqa: E501

        :return: The ssd_qab_mirrors of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ssd_qab_mirrors

    @ssd_qab_mirrors.setter
    def ssd_qab_mirrors(self, ssd_qab_mirrors):
        """Sets the ssd_qab_mirrors of this StoragepoolSettingsSettings.

        Controls number of mirrors of QAB blocks to place on SSDs.  # noqa: E501

        :param ssd_qab_mirrors: The ssd_qab_mirrors of this StoragepoolSettingsSettings.  # noqa: E501
        :type: str
        """
        if ssd_qab_mirrors is None:
            raise ValueError("Invalid value for `ssd_qab_mirrors`, must not be `None`")  # noqa: E501
        allowed_values = ["one", "all", "disabled", "invalid", "none"]  # noqa: E501
        if ssd_qab_mirrors not in allowed_values:
            raise ValueError(
                "Invalid value for `ssd_qab_mirrors` ({0}), must be one of {1}"  # noqa: E501
                .format(ssd_qab_mirrors, allowed_values)
            )

        self._ssd_qab_mirrors = ssd_qab_mirrors

    @property
    def ssd_system_btree_mirrors(self):
        """Gets the ssd_system_btree_mirrors of this StoragepoolSettingsSettings.  # noqa: E501

        Controls number of mirrors of system B-tree blocks to place on SSDs.  # noqa: E501

        :return: The ssd_system_btree_mirrors of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ssd_system_btree_mirrors

    @ssd_system_btree_mirrors.setter
    def ssd_system_btree_mirrors(self, ssd_system_btree_mirrors):
        """Sets the ssd_system_btree_mirrors of this StoragepoolSettingsSettings.

        Controls number of mirrors of system B-tree blocks to place on SSDs.  # noqa: E501

        :param ssd_system_btree_mirrors: The ssd_system_btree_mirrors of this StoragepoolSettingsSettings.  # noqa: E501
        :type: str
        """
        if ssd_system_btree_mirrors is None:
            raise ValueError("Invalid value for `ssd_system_btree_mirrors`, must not be `None`")  # noqa: E501
        allowed_values = ["one", "all", "disabled", "invalid", "none"]  # noqa: E501
        if ssd_system_btree_mirrors not in allowed_values:
            raise ValueError(
                "Invalid value for `ssd_system_btree_mirrors` ({0}), must be one of {1}"  # noqa: E501
                .format(ssd_system_btree_mirrors, allowed_values)
            )

        self._ssd_system_btree_mirrors = ssd_system_btree_mirrors

    @property
    def ssd_system_delta_mirrors(self):
        """Gets the ssd_system_delta_mirrors of this StoragepoolSettingsSettings.  # noqa: E501

        Controls number of mirrors of system delta blocks to place on SSDs.  # noqa: E501

        :return: The ssd_system_delta_mirrors of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ssd_system_delta_mirrors

    @ssd_system_delta_mirrors.setter
    def ssd_system_delta_mirrors(self, ssd_system_delta_mirrors):
        """Sets the ssd_system_delta_mirrors of this StoragepoolSettingsSettings.

        Controls number of mirrors of system delta blocks to place on SSDs.  # noqa: E501

        :param ssd_system_delta_mirrors: The ssd_system_delta_mirrors of this StoragepoolSettingsSettings.  # noqa: E501
        :type: str
        """
        if ssd_system_delta_mirrors is None:
            raise ValueError("Invalid value for `ssd_system_delta_mirrors`, must not be `None`")  # noqa: E501
        allowed_values = ["one", "all", "disabled", "invalid", "none"]  # noqa: E501
        if ssd_system_delta_mirrors not in allowed_values:
            raise ValueError(
                "Invalid value for `ssd_system_delta_mirrors` ({0}), must be one of {1}"  # noqa: E501
                .format(ssd_system_delta_mirrors, allowed_values)
            )

        self._ssd_system_delta_mirrors = ssd_system_delta_mirrors

    @property
    def virtual_hot_spare_deny_writes(self):
        """Gets the virtual_hot_spare_deny_writes of this StoragepoolSettingsSettings.  # noqa: E501

        Deny writes into reserved virtual hot spare space.  # noqa: E501

        :return: The virtual_hot_spare_deny_writes of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._virtual_hot_spare_deny_writes

    @virtual_hot_spare_deny_writes.setter
    def virtual_hot_spare_deny_writes(self, virtual_hot_spare_deny_writes):
        """Sets the virtual_hot_spare_deny_writes of this StoragepoolSettingsSettings.

        Deny writes into reserved virtual hot spare space.  # noqa: E501

        :param virtual_hot_spare_deny_writes: The virtual_hot_spare_deny_writes of this StoragepoolSettingsSettings.  # noqa: E501
        :type: bool
        """
        if virtual_hot_spare_deny_writes is None:
            raise ValueError("Invalid value for `virtual_hot_spare_deny_writes`, must not be `None`")  # noqa: E501

        self._virtual_hot_spare_deny_writes = virtual_hot_spare_deny_writes

    @property
    def virtual_hot_spare_hide_spare(self):
        """Gets the virtual_hot_spare_hide_spare of this StoragepoolSettingsSettings.  # noqa: E501

        Hide reserved virtual hot spare space from free space counts.  # noqa: E501

        :return: The virtual_hot_spare_hide_spare of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._virtual_hot_spare_hide_spare

    @virtual_hot_spare_hide_spare.setter
    def virtual_hot_spare_hide_spare(self, virtual_hot_spare_hide_spare):
        """Sets the virtual_hot_spare_hide_spare of this StoragepoolSettingsSettings.

        Hide reserved virtual hot spare space from free space counts.  # noqa: E501

        :param virtual_hot_spare_hide_spare: The virtual_hot_spare_hide_spare of this StoragepoolSettingsSettings.  # noqa: E501
        :type: bool
        """
        if virtual_hot_spare_hide_spare is None:
            raise ValueError("Invalid value for `virtual_hot_spare_hide_spare`, must not be `None`")  # noqa: E501

        self._virtual_hot_spare_hide_spare = virtual_hot_spare_hide_spare

    @property
    def virtual_hot_spare_limit_drives(self):
        """Gets the virtual_hot_spare_limit_drives of this StoragepoolSettingsSettings.  # noqa: E501

        The number of drives to reserve for the virtual hot spare, from 0-4.  # noqa: E501

        :return: The virtual_hot_spare_limit_drives of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._virtual_hot_spare_limit_drives

    @virtual_hot_spare_limit_drives.setter
    def virtual_hot_spare_limit_drives(self, virtual_hot_spare_limit_drives):
        """Sets the virtual_hot_spare_limit_drives of this StoragepoolSettingsSettings.

        The number of drives to reserve for the virtual hot spare, from 0-4.  # noqa: E501

        :param virtual_hot_spare_limit_drives: The virtual_hot_spare_limit_drives of this StoragepoolSettingsSettings.  # noqa: E501
        :type: int
        """
        if virtual_hot_spare_limit_drives is None:
            raise ValueError("Invalid value for `virtual_hot_spare_limit_drives`, must not be `None`")  # noqa: E501
        if virtual_hot_spare_limit_drives is not None and virtual_hot_spare_limit_drives > 4:  # noqa: E501
            raise ValueError("Invalid value for `virtual_hot_spare_limit_drives`, must be a value less than or equal to `4`")  # noqa: E501
        if virtual_hot_spare_limit_drives is not None and virtual_hot_spare_limit_drives < 0:  # noqa: E501
            raise ValueError("Invalid value for `virtual_hot_spare_limit_drives`, must be a value greater than or equal to `0`")  # noqa: E501

        self._virtual_hot_spare_limit_drives = virtual_hot_spare_limit_drives

    @property
    def virtual_hot_spare_limit_percent(self):
        """Gets the virtual_hot_spare_limit_percent of this StoragepoolSettingsSettings.  # noqa: E501

        The percent space to reserve for the virtual hot spare, from 0-20.  # noqa: E501

        :return: The virtual_hot_spare_limit_percent of this StoragepoolSettingsSettings.  # noqa: E501
        :rtype: int
        """
        return self._virtual_hot_spare_limit_percent

    @virtual_hot_spare_limit_percent.setter
    def virtual_hot_spare_limit_percent(self, virtual_hot_spare_limit_percent):
        """Sets the virtual_hot_spare_limit_percent of this StoragepoolSettingsSettings.

        The percent space to reserve for the virtual hot spare, from 0-20.  # noqa: E501

        :param virtual_hot_spare_limit_percent: The virtual_hot_spare_limit_percent of this StoragepoolSettingsSettings.  # noqa: E501
        :type: int
        """
        if virtual_hot_spare_limit_percent is None:
            raise ValueError("Invalid value for `virtual_hot_spare_limit_percent`, must not be `None`")  # noqa: E501
        if virtual_hot_spare_limit_percent is not None and virtual_hot_spare_limit_percent > 20:  # noqa: E501
            raise ValueError("Invalid value for `virtual_hot_spare_limit_percent`, must be a value less than or equal to `20`")  # noqa: E501
        if virtual_hot_spare_limit_percent is not None and virtual_hot_spare_limit_percent < 0:  # noqa: E501
            raise ValueError("Invalid value for `virtual_hot_spare_limit_percent`, must be a value greater than or equal to `0`")  # noqa: E501

        self._virtual_hot_spare_limit_percent = virtual_hot_spare_limit_percent

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
        if not isinstance(other, StoragepoolSettingsSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
