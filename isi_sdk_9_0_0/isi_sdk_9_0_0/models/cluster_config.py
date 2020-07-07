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

from isi_sdk_9_0_0.models.cluster_config_device import ClusterConfigDevice  # noqa: F401,E501
from isi_sdk_9_0_0.models.cluster_config_onefs_version import ClusterConfigOnefsVersion  # noqa: F401,E501
from isi_sdk_9_0_0.models.cluster_config_timezone import ClusterConfigTimezone  # noqa: F401,E501


class ClusterConfig(object):
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
        'description': 'str',
        'devices': 'list[ClusterConfigDevice]',
        'encoding': 'str',
        'guid': 'str',
        'has_quorum': 'bool',
        'is_compliance': 'bool',
        'is_virtual': 'bool',
        'is_vonefs': 'bool',
        'join_mode': 'str',
        'local_devid': 'int',
        'local_lnn': 'int',
        'local_serial': 'str',
        'name': 'str',
        'onefs_version': 'ClusterConfigOnefsVersion',
        'timezone': 'ClusterConfigTimezone',
        'upgrade_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'devices': 'devices',
        'encoding': 'encoding',
        'guid': 'guid',
        'has_quorum': 'has_quorum',
        'is_compliance': 'is_compliance',
        'is_virtual': 'is_virtual',
        'is_vonefs': 'is_vonefs',
        'join_mode': 'join_mode',
        'local_devid': 'local_devid',
        'local_lnn': 'local_lnn',
        'local_serial': 'local_serial',
        'name': 'name',
        'onefs_version': 'onefs_version',
        'timezone': 'timezone',
        'upgrade_type': 'upgrade_type'
    }

    def __init__(self, description=None, devices=None, encoding=None, guid=None, has_quorum=None, is_compliance=None, is_virtual=None, is_vonefs=None, join_mode=None, local_devid=None, local_lnn=None, local_serial=None, name=None, onefs_version=None, timezone=None, upgrade_type=None):  # noqa: E501
        """ClusterConfig - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._devices = None
        self._encoding = None
        self._guid = None
        self._has_quorum = None
        self._is_compliance = None
        self._is_virtual = None
        self._is_vonefs = None
        self._join_mode = None
        self._local_devid = None
        self._local_lnn = None
        self._local_serial = None
        self._name = None
        self._onefs_version = None
        self._timezone = None
        self._upgrade_type = None
        self.discriminator = None

        self.description = description
        self.devices = devices
        self.encoding = encoding
        self.guid = guid
        self.has_quorum = has_quorum
        self.is_compliance = is_compliance
        self.is_virtual = is_virtual
        self.is_vonefs = is_vonefs
        self.join_mode = join_mode
        self.local_devid = local_devid
        self.local_lnn = local_lnn
        self.local_serial = local_serial
        self.name = name
        if onefs_version is not None:
            self.onefs_version = onefs_version
        if timezone is not None:
            self.timezone = timezone
        if upgrade_type is not None:
            self.upgrade_type = upgrade_type

    @property
    def description(self):
        """Gets the description of this ClusterConfig.  # noqa: E501

        Customer configurable description.  # noqa: E501

        :return: The description of this ClusterConfig.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterConfig.

        Customer configurable description.  # noqa: E501

        :param description: The description of this ClusterConfig.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def devices(self):
        """Gets the devices of this ClusterConfig.  # noqa: E501


        :return: The devices of this ClusterConfig.  # noqa: E501
        :rtype: list[ClusterConfigDevice]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this ClusterConfig.


        :param devices: The devices of this ClusterConfig.  # noqa: E501
        :type: list[ClusterConfigDevice]
        """
        if devices is None:
            raise ValueError("Invalid value for `devices`, must not be `None`")  # noqa: E501

        self._devices = devices

    @property
    def encoding(self):
        """Gets the encoding of this ClusterConfig.  # noqa: E501

        Default encoding.  # noqa: E501

        :return: The encoding of this ClusterConfig.  # noqa: E501
        :rtype: str
        """
        return self._encoding

    @encoding.setter
    def encoding(self, encoding):
        """Sets the encoding of this ClusterConfig.

        Default encoding.  # noqa: E501

        :param encoding: The encoding of this ClusterConfig.  # noqa: E501
        :type: str
        """
        if encoding is None:
            raise ValueError("Invalid value for `encoding`, must not be `None`")  # noqa: E501

        self._encoding = encoding

    @property
    def guid(self):
        """Gets the guid of this ClusterConfig.  # noqa: E501

        Cluster GUID.  # noqa: E501

        :return: The guid of this ClusterConfig.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this ClusterConfig.

        Cluster GUID.  # noqa: E501

        :param guid: The guid of this ClusterConfig.  # noqa: E501
        :type: str
        """
        if guid is None:
            raise ValueError("Invalid value for `guid`, must not be `None`")  # noqa: E501

        self._guid = guid

    @property
    def has_quorum(self):
        """Gets the has_quorum of this ClusterConfig.  # noqa: E501

        If true, the local node is in a group with quorum: It is communicating, storing, and protecting data normally with other nodes in its group.  Under normal circumstances, every node in the cluster is part of one group.  # noqa: E501

        :return: The has_quorum of this ClusterConfig.  # noqa: E501
        :rtype: bool
        """
        return self._has_quorum

    @has_quorum.setter
    def has_quorum(self, has_quorum):
        """Sets the has_quorum of this ClusterConfig.

        If true, the local node is in a group with quorum: It is communicating, storing, and protecting data normally with other nodes in its group.  Under normal circumstances, every node in the cluster is part of one group.  # noqa: E501

        :param has_quorum: The has_quorum of this ClusterConfig.  # noqa: E501
        :type: bool
        """
        if has_quorum is None:
            raise ValueError("Invalid value for `has_quorum`, must not be `None`")  # noqa: E501

        self._has_quorum = has_quorum

    @property
    def is_compliance(self):
        """Gets the is_compliance of this ClusterConfig.  # noqa: E501

        If true, the cluster is in compliance mode.  Compliance mode clusters do not allow root access and have stricter WORM (Write Once Read Many) features for retaining data in compliance with U.S. Securities and Exchange Commission rule 17a-4.  # noqa: E501

        :return: The is_compliance of this ClusterConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_compliance

    @is_compliance.setter
    def is_compliance(self, is_compliance):
        """Sets the is_compliance of this ClusterConfig.

        If true, the cluster is in compliance mode.  Compliance mode clusters do not allow root access and have stricter WORM (Write Once Read Many) features for retaining data in compliance with U.S. Securities and Exchange Commission rule 17a-4.  # noqa: E501

        :param is_compliance: The is_compliance of this ClusterConfig.  # noqa: E501
        :type: bool
        """
        if is_compliance is None:
            raise ValueError("Invalid value for `is_compliance`, must not be `None`")  # noqa: E501

        self._is_compliance = is_compliance

    @property
    def is_virtual(self):
        """Gets the is_virtual of this ClusterConfig.  # noqa: E501

        true if the cluster is deployed on a desktop VMWorkstation  # noqa: E501

        :return: The is_virtual of this ClusterConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_virtual

    @is_virtual.setter
    def is_virtual(self, is_virtual):
        """Sets the is_virtual of this ClusterConfig.

        true if the cluster is deployed on a desktop VMWorkstation  # noqa: E501

        :param is_virtual: The is_virtual of this ClusterConfig.  # noqa: E501
        :type: bool
        """
        if is_virtual is None:
            raise ValueError("Invalid value for `is_virtual`, must not be `None`")  # noqa: E501

        self._is_virtual = is_virtual

    @property
    def is_vonefs(self):
        """Gets the is_vonefs of this ClusterConfig.  # noqa: E501

        true if this is a vOneFS cluster on an ESXi  # noqa: E501

        :return: The is_vonefs of this ClusterConfig.  # noqa: E501
        :rtype: bool
        """
        return self._is_vonefs

    @is_vonefs.setter
    def is_vonefs(self, is_vonefs):
        """Sets the is_vonefs of this ClusterConfig.

        true if this is a vOneFS cluster on an ESXi  # noqa: E501

        :param is_vonefs: The is_vonefs of this ClusterConfig.  # noqa: E501
        :type: bool
        """
        if is_vonefs is None:
            raise ValueError("Invalid value for `is_vonefs`, must not be `None`")  # noqa: E501

        self._is_vonefs = is_vonefs

    @property
    def join_mode(self):
        """Gets the join_mode of this ClusterConfig.  # noqa: E501

        Node join mode: 'manual' or 'secure'.  # noqa: E501

        :return: The join_mode of this ClusterConfig.  # noqa: E501
        :rtype: str
        """
        return self._join_mode

    @join_mode.setter
    def join_mode(self, join_mode):
        """Sets the join_mode of this ClusterConfig.

        Node join mode: 'manual' or 'secure'.  # noqa: E501

        :param join_mode: The join_mode of this ClusterConfig.  # noqa: E501
        :type: str
        """
        if join_mode is None:
            raise ValueError("Invalid value for `join_mode`, must not be `None`")  # noqa: E501

        self._join_mode = join_mode

    @property
    def local_devid(self):
        """Gets the local_devid of this ClusterConfig.  # noqa: E501

        Device ID of the queried node.  # noqa: E501

        :return: The local_devid of this ClusterConfig.  # noqa: E501
        :rtype: int
        """
        return self._local_devid

    @local_devid.setter
    def local_devid(self, local_devid):
        """Sets the local_devid of this ClusterConfig.

        Device ID of the queried node.  # noqa: E501

        :param local_devid: The local_devid of this ClusterConfig.  # noqa: E501
        :type: int
        """
        if local_devid is None:
            raise ValueError("Invalid value for `local_devid`, must not be `None`")  # noqa: E501

        self._local_devid = local_devid

    @property
    def local_lnn(self):
        """Gets the local_lnn of this ClusterConfig.  # noqa: E501

        Device logical node number of the queried node.  # noqa: E501

        :return: The local_lnn of this ClusterConfig.  # noqa: E501
        :rtype: int
        """
        return self._local_lnn

    @local_lnn.setter
    def local_lnn(self, local_lnn):
        """Sets the local_lnn of this ClusterConfig.

        Device logical node number of the queried node.  # noqa: E501

        :param local_lnn: The local_lnn of this ClusterConfig.  # noqa: E501
        :type: int
        """
        if local_lnn is None:
            raise ValueError("Invalid value for `local_lnn`, must not be `None`")  # noqa: E501

        self._local_lnn = local_lnn

    @property
    def local_serial(self):
        """Gets the local_serial of this ClusterConfig.  # noqa: E501

        Device serial number of the queried node.  # noqa: E501

        :return: The local_serial of this ClusterConfig.  # noqa: E501
        :rtype: str
        """
        return self._local_serial

    @local_serial.setter
    def local_serial(self, local_serial):
        """Sets the local_serial of this ClusterConfig.

        Device serial number of the queried node.  # noqa: E501

        :param local_serial: The local_serial of this ClusterConfig.  # noqa: E501
        :type: str
        """
        if local_serial is None:
            raise ValueError("Invalid value for `local_serial`, must not be `None`")  # noqa: E501

        self._local_serial = local_serial

    @property
    def name(self):
        """Gets the name of this ClusterConfig.  # noqa: E501

        Cluster name.  # noqa: E501

        :return: The name of this ClusterConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterConfig.

        Cluster name.  # noqa: E501

        :param name: The name of this ClusterConfig.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def onefs_version(self):
        """Gets the onefs_version of this ClusterConfig.  # noqa: E501

          # noqa: E501

        :return: The onefs_version of this ClusterConfig.  # noqa: E501
        :rtype: ClusterConfigOnefsVersion
        """
        return self._onefs_version

    @onefs_version.setter
    def onefs_version(self, onefs_version):
        """Sets the onefs_version of this ClusterConfig.

          # noqa: E501

        :param onefs_version: The onefs_version of this ClusterConfig.  # noqa: E501
        :type: ClusterConfigOnefsVersion
        """

        self._onefs_version = onefs_version

    @property
    def timezone(self):
        """Gets the timezone of this ClusterConfig.  # noqa: E501

        The cluster timezone settings.  # noqa: E501

        :return: The timezone of this ClusterConfig.  # noqa: E501
        :rtype: ClusterConfigTimezone
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this ClusterConfig.

        The cluster timezone settings.  # noqa: E501

        :param timezone: The timezone of this ClusterConfig.  # noqa: E501
        :type: ClusterConfigTimezone
        """

        self._timezone = timezone

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this ClusterConfig.  # noqa: E501


        :return: The upgrade_type of this ClusterConfig.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this ClusterConfig.


        :param upgrade_type: The upgrade_type of this ClusterConfig.  # noqa: E501
        :type: str
        """

        self._upgrade_type = upgrade_type

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
        if not isinstance(other, ClusterConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
