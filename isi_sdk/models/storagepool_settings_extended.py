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


class StoragepoolSettingsExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        StoragepoolSettingsExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'automatically_manage_io_optimization': 'str',
            'automatically_manage_protection': 'str',
            'global_namespace_acceleration_enabled': 'bool',
            'protect_directories_one_level_higher': 'bool',
            'spillover_enabled': 'bool',
            'spillover_target': 'StoragepoolSettingsSpilloverTarget',
            'ssd_l3_cache_default_enabled': 'bool',
            'virtual_hot_spare_deny_writes': 'bool',
            'virtual_hot_spare_hide_spare': 'bool',
            'virtual_hot_spare_limit_drives': 'int',
            'virtual_hot_spare_limit_percent': 'int'
        }

        self.attribute_map = {
            'automatically_manage_io_optimization': 'automatically_manage_io_optimization',
            'automatically_manage_protection': 'automatically_manage_protection',
            'global_namespace_acceleration_enabled': 'global_namespace_acceleration_enabled',
            'protect_directories_one_level_higher': 'protect_directories_one_level_higher',
            'spillover_enabled': 'spillover_enabled',
            'spillover_target': 'spillover_target',
            'ssd_l3_cache_default_enabled': 'ssd_l3_cache_default_enabled',
            'virtual_hot_spare_deny_writes': 'virtual_hot_spare_deny_writes',
            'virtual_hot_spare_hide_spare': 'virtual_hot_spare_hide_spare',
            'virtual_hot_spare_limit_drives': 'virtual_hot_spare_limit_drives',
            'virtual_hot_spare_limit_percent': 'virtual_hot_spare_limit_percent'
        }

        self._automatically_manage_io_optimization = None
        self._automatically_manage_protection = None
        self._global_namespace_acceleration_enabled = None
        self._protect_directories_one_level_higher = None
        self._spillover_enabled = None
        self._spillover_target = None
        self._ssd_l3_cache_default_enabled = None
        self._virtual_hot_spare_deny_writes = None
        self._virtual_hot_spare_hide_spare = None
        self._virtual_hot_spare_limit_drives = None
        self._virtual_hot_spare_limit_percent = None

    @property
    def automatically_manage_io_optimization(self):
        """
        Gets the automatically_manage_io_optimization of this StoragepoolSettingsExtended.
        Automatically manage IO optimization settings on files.

        :return: The automatically_manage_io_optimization of this StoragepoolSettingsExtended.
        :rtype: str
        """
        return self._automatically_manage_io_optimization

    @automatically_manage_io_optimization.setter
    def automatically_manage_io_optimization(self, automatically_manage_io_optimization):
        """
        Sets the automatically_manage_io_optimization of this StoragepoolSettingsExtended.
        Automatically manage IO optimization settings on files.

        :param automatically_manage_io_optimization: The automatically_manage_io_optimization of this StoragepoolSettingsExtended.
        :type: str
        """
        allowed_values = ["all", "files_at_default", "none"]
        if automatically_manage_io_optimization not in allowed_values:
            raise ValueError(
                "Invalid value for `automatically_manage_io_optimization`, must be one of {0}"
                .format(allowed_values)
            )

        self._automatically_manage_io_optimization = automatically_manage_io_optimization

    @property
    def automatically_manage_protection(self):
        """
        Gets the automatically_manage_protection of this StoragepoolSettingsExtended.
        Automatically manage protection settings on files.

        :return: The automatically_manage_protection of this StoragepoolSettingsExtended.
        :rtype: str
        """
        return self._automatically_manage_protection

    @automatically_manage_protection.setter
    def automatically_manage_protection(self, automatically_manage_protection):
        """
        Sets the automatically_manage_protection of this StoragepoolSettingsExtended.
        Automatically manage protection settings on files.

        :param automatically_manage_protection: The automatically_manage_protection of this StoragepoolSettingsExtended.
        :type: str
        """
        allowed_values = ["all", "files_at_default", "none"]
        if automatically_manage_protection not in allowed_values:
            raise ValueError(
                "Invalid value for `automatically_manage_protection`, must be one of {0}"
                .format(allowed_values)
            )

        self._automatically_manage_protection = automatically_manage_protection

    @property
    def global_namespace_acceleration_enabled(self):
        """
        Gets the global_namespace_acceleration_enabled of this StoragepoolSettingsExtended.
        Optimize namespace operations by storing metadata on SSDs.

        :return: The global_namespace_acceleration_enabled of this StoragepoolSettingsExtended.
        :rtype: bool
        """
        return self._global_namespace_acceleration_enabled

    @global_namespace_acceleration_enabled.setter
    def global_namespace_acceleration_enabled(self, global_namespace_acceleration_enabled):
        """
        Sets the global_namespace_acceleration_enabled of this StoragepoolSettingsExtended.
        Optimize namespace operations by storing metadata on SSDs.

        :param global_namespace_acceleration_enabled: The global_namespace_acceleration_enabled of this StoragepoolSettingsExtended.
        :type: bool
        """
        
        self._global_namespace_acceleration_enabled = global_namespace_acceleration_enabled

    @property
    def protect_directories_one_level_higher(self):
        """
        Gets the protect_directories_one_level_higher of this StoragepoolSettingsExtended.
        Automatically add additional protection level to all directories.

        :return: The protect_directories_one_level_higher of this StoragepoolSettingsExtended.
        :rtype: bool
        """
        return self._protect_directories_one_level_higher

    @protect_directories_one_level_higher.setter
    def protect_directories_one_level_higher(self, protect_directories_one_level_higher):
        """
        Sets the protect_directories_one_level_higher of this StoragepoolSettingsExtended.
        Automatically add additional protection level to all directories.

        :param protect_directories_one_level_higher: The protect_directories_one_level_higher of this StoragepoolSettingsExtended.
        :type: bool
        """
        
        self._protect_directories_one_level_higher = protect_directories_one_level_higher

    @property
    def spillover_enabled(self):
        """
        Gets the spillover_enabled of this StoragepoolSettingsExtended.
        Spill writes into other pools as needed.

        :return: The spillover_enabled of this StoragepoolSettingsExtended.
        :rtype: bool
        """
        return self._spillover_enabled

    @spillover_enabled.setter
    def spillover_enabled(self, spillover_enabled):
        """
        Sets the spillover_enabled of this StoragepoolSettingsExtended.
        Spill writes into other pools as needed.

        :param spillover_enabled: The spillover_enabled of this StoragepoolSettingsExtended.
        :type: bool
        """
        
        self._spillover_enabled = spillover_enabled

    @property
    def spillover_target(self):
        """
        Gets the spillover_target of this StoragepoolSettingsExtended.
        Target pool for spilled writes.

        :return: The spillover_target of this StoragepoolSettingsExtended.
        :rtype: StoragepoolSettingsSpilloverTarget
        """
        return self._spillover_target

    @spillover_target.setter
    def spillover_target(self, spillover_target):
        """
        Sets the spillover_target of this StoragepoolSettingsExtended.
        Target pool for spilled writes.

        :param spillover_target: The spillover_target of this StoragepoolSettingsExtended.
        :type: StoragepoolSettingsSpilloverTarget
        """
        
        self._spillover_target = spillover_target

    @property
    def ssd_l3_cache_default_enabled(self):
        """
        Gets the ssd_l3_cache_default_enabled of this StoragepoolSettingsExtended.
        The L3 Cache default enabled state. This specifies whether L3 Cache should be enabled on new node pools

        :return: The ssd_l3_cache_default_enabled of this StoragepoolSettingsExtended.
        :rtype: bool
        """
        return self._ssd_l3_cache_default_enabled

    @ssd_l3_cache_default_enabled.setter
    def ssd_l3_cache_default_enabled(self, ssd_l3_cache_default_enabled):
        """
        Sets the ssd_l3_cache_default_enabled of this StoragepoolSettingsExtended.
        The L3 Cache default enabled state. This specifies whether L3 Cache should be enabled on new node pools

        :param ssd_l3_cache_default_enabled: The ssd_l3_cache_default_enabled of this StoragepoolSettingsExtended.
        :type: bool
        """
        
        self._ssd_l3_cache_default_enabled = ssd_l3_cache_default_enabled

    @property
    def virtual_hot_spare_deny_writes(self):
        """
        Gets the virtual_hot_spare_deny_writes of this StoragepoolSettingsExtended.
        Deny writes into reserved virtual hot spare space.

        :return: The virtual_hot_spare_deny_writes of this StoragepoolSettingsExtended.
        :rtype: bool
        """
        return self._virtual_hot_spare_deny_writes

    @virtual_hot_spare_deny_writes.setter
    def virtual_hot_spare_deny_writes(self, virtual_hot_spare_deny_writes):
        """
        Sets the virtual_hot_spare_deny_writes of this StoragepoolSettingsExtended.
        Deny writes into reserved virtual hot spare space.

        :param virtual_hot_spare_deny_writes: The virtual_hot_spare_deny_writes of this StoragepoolSettingsExtended.
        :type: bool
        """
        
        self._virtual_hot_spare_deny_writes = virtual_hot_spare_deny_writes

    @property
    def virtual_hot_spare_hide_spare(self):
        """
        Gets the virtual_hot_spare_hide_spare of this StoragepoolSettingsExtended.
        Hide reserved virtual hot spare space from free space counts.

        :return: The virtual_hot_spare_hide_spare of this StoragepoolSettingsExtended.
        :rtype: bool
        """
        return self._virtual_hot_spare_hide_spare

    @virtual_hot_spare_hide_spare.setter
    def virtual_hot_spare_hide_spare(self, virtual_hot_spare_hide_spare):
        """
        Sets the virtual_hot_spare_hide_spare of this StoragepoolSettingsExtended.
        Hide reserved virtual hot spare space from free space counts.

        :param virtual_hot_spare_hide_spare: The virtual_hot_spare_hide_spare of this StoragepoolSettingsExtended.
        :type: bool
        """
        
        self._virtual_hot_spare_hide_spare = virtual_hot_spare_hide_spare

    @property
    def virtual_hot_spare_limit_drives(self):
        """
        Gets the virtual_hot_spare_limit_drives of this StoragepoolSettingsExtended.
        The number of drives to reserve for the virtual hot spare, from 0-4.

        :return: The virtual_hot_spare_limit_drives of this StoragepoolSettingsExtended.
        :rtype: int
        """
        return self._virtual_hot_spare_limit_drives

    @virtual_hot_spare_limit_drives.setter
    def virtual_hot_spare_limit_drives(self, virtual_hot_spare_limit_drives):
        """
        Sets the virtual_hot_spare_limit_drives of this StoragepoolSettingsExtended.
        The number of drives to reserve for the virtual hot spare, from 0-4.

        :param virtual_hot_spare_limit_drives: The virtual_hot_spare_limit_drives of this StoragepoolSettingsExtended.
        :type: int
        """
        
        if not virtual_hot_spare_limit_drives:
            raise ValueError("Invalid value for `virtual_hot_spare_limit_drives`, must not be `None`")
        if virtual_hot_spare_limit_drives > 4.0: 
            raise ValueError("Invalid value for `virtual_hot_spare_limit_drives`, must be a value less than or equal to `4.0`")
        if virtual_hot_spare_limit_drives < 0.0: 
            raise ValueError("Invalid value for `virtual_hot_spare_limit_drives`, must be a value greater than or equal to `0.0`")

        self._virtual_hot_spare_limit_drives = virtual_hot_spare_limit_drives

    @property
    def virtual_hot_spare_limit_percent(self):
        """
        Gets the virtual_hot_spare_limit_percent of this StoragepoolSettingsExtended.
        The percent space to reserve for the virtual hot spare, from 0-20.

        :return: The virtual_hot_spare_limit_percent of this StoragepoolSettingsExtended.
        :rtype: int
        """
        return self._virtual_hot_spare_limit_percent

    @virtual_hot_spare_limit_percent.setter
    def virtual_hot_spare_limit_percent(self, virtual_hot_spare_limit_percent):
        """
        Sets the virtual_hot_spare_limit_percent of this StoragepoolSettingsExtended.
        The percent space to reserve for the virtual hot spare, from 0-20.

        :param virtual_hot_spare_limit_percent: The virtual_hot_spare_limit_percent of this StoragepoolSettingsExtended.
        :type: int
        """
        
        if not virtual_hot_spare_limit_percent:
            raise ValueError("Invalid value for `virtual_hot_spare_limit_percent`, must not be `None`")
        if virtual_hot_spare_limit_percent > 20.0: 
            raise ValueError("Invalid value for `virtual_hot_spare_limit_percent`, must be a value less than or equal to `20.0`")
        if virtual_hot_spare_limit_percent < 0.0: 
            raise ValueError("Invalid value for `virtual_hot_spare_limit_percent`, must be a value greater than or equal to `0.0`")

        self._virtual_hot_spare_limit_percent = virtual_hot_spare_limit_percent

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

