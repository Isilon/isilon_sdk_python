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


class ClusterFirmwareUpgradeItem(object):
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
        'exclude_device': 'str',
        'exclude_type': 'str',
        'fw_pkg': 'str',
        'include_device': 'str',
        'include_type': 'str',
        'no_burn': 'bool',
        'no_reboot': 'bool',
        'nodes_to_upgrade': 'list[int]',
        'simultaneous': 'bool'
    }

    attribute_map = {
        'exclude_device': 'exclude_device',
        'exclude_type': 'exclude_type',
        'fw_pkg': 'fw_pkg',
        'include_device': 'include_device',
        'include_type': 'include_type',
        'no_burn': 'no_burn',
        'no_reboot': 'no_reboot',
        'nodes_to_upgrade': 'nodes_to_upgrade',
        'simultaneous': 'simultaneous'
    }

    def __init__(self, exclude_device=None, exclude_type=None, fw_pkg=None, include_device=None, include_type=None, no_burn=None, no_reboot=None, nodes_to_upgrade=None, simultaneous=None):  # noqa: E501
        """ClusterFirmwareUpgradeItem - a model defined in Swagger"""  # noqa: E501

        self._exclude_device = None
        self._exclude_type = None
        self._fw_pkg = None
        self._include_device = None
        self._include_type = None
        self._no_burn = None
        self._no_reboot = None
        self._nodes_to_upgrade = None
        self._simultaneous = None
        self.discriminator = None

        if exclude_device is not None:
            self.exclude_device = exclude_device
        if exclude_type is not None:
            self.exclude_type = exclude_type
        if fw_pkg is not None:
            self.fw_pkg = fw_pkg
        if include_device is not None:
            self.include_device = include_device
        if include_type is not None:
            self.include_type = include_type
        if no_burn is not None:
            self.no_burn = no_burn
        if no_reboot is not None:
            self.no_reboot = no_reboot
        if nodes_to_upgrade is not None:
            self.nodes_to_upgrade = nodes_to_upgrade
        if simultaneous is not None:
            self.simultaneous = simultaneous

    @property
    def exclude_device(self):
        """Gets the exclude_device of this ClusterFirmwareUpgradeItem.  # noqa: E501

        Exclude the specified devices in the firmware upgrade.  # noqa: E501

        :return: The exclude_device of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: str
        """
        return self._exclude_device

    @exclude_device.setter
    def exclude_device(self, exclude_device):
        """Sets the exclude_device of this ClusterFirmwareUpgradeItem.

        Exclude the specified devices in the firmware upgrade.  # noqa: E501

        :param exclude_device: The exclude_device of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: str
        """
        if exclude_device is not None and len(exclude_device) > 128:
            raise ValueError("Invalid value for `exclude_device`, length must be less than or equal to `128`")  # noqa: E501
        if exclude_device is not None and len(exclude_device) < 1:
            raise ValueError("Invalid value for `exclude_device`, length must be greater than or equal to `1`")  # noqa: E501

        self._exclude_device = exclude_device

    @property
    def exclude_type(self):
        """Gets the exclude_type of this ClusterFirmwareUpgradeItem.  # noqa: E501

        Exclude the specified device type in the firmware upgrade.  # noqa: E501

        :return: The exclude_type of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: str
        """
        return self._exclude_type

    @exclude_type.setter
    def exclude_type(self, exclude_type):
        """Sets the exclude_type of this ClusterFirmwareUpgradeItem.

        Exclude the specified device type in the firmware upgrade.  # noqa: E501

        :param exclude_type: The exclude_type of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: str
        """
        if exclude_type is not None and len(exclude_type) > 128:
            raise ValueError("Invalid value for `exclude_type`, length must be less than or equal to `128`")  # noqa: E501
        if exclude_type is not None and len(exclude_type) < 1:
            raise ValueError("Invalid value for `exclude_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._exclude_type = exclude_type

    @property
    def fw_pkg(self):
        """Gets the fw_pkg of this ClusterFirmwareUpgradeItem.  # noqa: E501

        The location (path) of the firmware package which must be within /ifs.  # noqa: E501

        :return: The fw_pkg of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: str
        """
        return self._fw_pkg

    @fw_pkg.setter
    def fw_pkg(self, fw_pkg):
        """Sets the fw_pkg of this ClusterFirmwareUpgradeItem.

        The location (path) of the firmware package which must be within /ifs.  # noqa: E501

        :param fw_pkg: The fw_pkg of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: str
        """
        if fw_pkg is not None and len(fw_pkg) > 4096:
            raise ValueError("Invalid value for `fw_pkg`, length must be less than or equal to `4096`")  # noqa: E501
        if fw_pkg is not None and len(fw_pkg) < 3:
            raise ValueError("Invalid value for `fw_pkg`, length must be greater than or equal to `3`")  # noqa: E501

        self._fw_pkg = fw_pkg

    @property
    def include_device(self):
        """Gets the include_device of this ClusterFirmwareUpgradeItem.  # noqa: E501

        Include the specified devices in the firmware upgrade.  # noqa: E501

        :return: The include_device of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: str
        """
        return self._include_device

    @include_device.setter
    def include_device(self, include_device):
        """Sets the include_device of this ClusterFirmwareUpgradeItem.

        Include the specified devices in the firmware upgrade.  # noqa: E501

        :param include_device: The include_device of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: str
        """
        if include_device is not None and len(include_device) > 128:
            raise ValueError("Invalid value for `include_device`, length must be less than or equal to `128`")  # noqa: E501
        if include_device is not None and len(include_device) < 1:
            raise ValueError("Invalid value for `include_device`, length must be greater than or equal to `1`")  # noqa: E501

        self._include_device = include_device

    @property
    def include_type(self):
        """Gets the include_type of this ClusterFirmwareUpgradeItem.  # noqa: E501

        Include the specified device type in the firmware upgrade.  # noqa: E501

        :return: The include_type of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: str
        """
        return self._include_type

    @include_type.setter
    def include_type(self, include_type):
        """Sets the include_type of this ClusterFirmwareUpgradeItem.

        Include the specified device type in the firmware upgrade.  # noqa: E501

        :param include_type: The include_type of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: str
        """
        if include_type is not None and len(include_type) > 128:
            raise ValueError("Invalid value for `include_type`, length must be less than or equal to `128`")  # noqa: E501
        if include_type is not None and len(include_type) < 1:
            raise ValueError("Invalid value for `include_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._include_type = include_type

    @property
    def no_burn(self):
        """Gets the no_burn of this ClusterFirmwareUpgradeItem.  # noqa: E501

        Do not burn the firmware.  # noqa: E501

        :return: The no_burn of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: bool
        """
        return self._no_burn

    @no_burn.setter
    def no_burn(self, no_burn):
        """Sets the no_burn of this ClusterFirmwareUpgradeItem.

        Do not burn the firmware.  # noqa: E501

        :param no_burn: The no_burn of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: bool
        """

        self._no_burn = no_burn

    @property
    def no_reboot(self):
        """Gets the no_reboot of this ClusterFirmwareUpgradeItem.  # noqa: E501

        Do not reboot the node after an upgrade  # noqa: E501

        :return: The no_reboot of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: bool
        """
        return self._no_reboot

    @no_reboot.setter
    def no_reboot(self, no_reboot):
        """Sets the no_reboot of this ClusterFirmwareUpgradeItem.

        Do not reboot the node after an upgrade  # noqa: E501

        :param no_reboot: The no_reboot of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: bool
        """

        self._no_reboot = no_reboot

    @property
    def nodes_to_upgrade(self):
        """Gets the nodes_to_upgrade of this ClusterFirmwareUpgradeItem.  # noqa: E501

        The nodes scheduled for upgrade. Order in array determines queue position number. 'all' and null option will upgrade firmware on all nodes in <lnn> order (Note: 'all' and null options do not apply to simultaneous firmware upgrade).  # noqa: E501

        :return: The nodes_to_upgrade of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._nodes_to_upgrade

    @nodes_to_upgrade.setter
    def nodes_to_upgrade(self, nodes_to_upgrade):
        """Sets the nodes_to_upgrade of this ClusterFirmwareUpgradeItem.

        The nodes scheduled for upgrade. Order in array determines queue position number. 'all' and null option will upgrade firmware on all nodes in <lnn> order (Note: 'all' and null options do not apply to simultaneous firmware upgrade).  # noqa: E501

        :param nodes_to_upgrade: The nodes_to_upgrade of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: list[int]
        """

        self._nodes_to_upgrade = nodes_to_upgrade

    @property
    def simultaneous(self):
        """Gets the simultaneous of this ClusterFirmwareUpgradeItem.  # noqa: E501

        Upgrade Firmware on multiple nodes concurrently  # noqa: E501

        :return: The simultaneous of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :rtype: bool
        """
        return self._simultaneous

    @simultaneous.setter
    def simultaneous(self, simultaneous):
        """Sets the simultaneous of this ClusterFirmwareUpgradeItem.

        Upgrade Firmware on multiple nodes concurrently  # noqa: E501

        :param simultaneous: The simultaneous of this ClusterFirmwareUpgradeItem.  # noqa: E501
        :type: bool
        """

        self._simultaneous = simultaneous

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
        if not isinstance(other, ClusterFirmwareUpgradeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
