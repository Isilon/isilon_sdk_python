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

from isi_sdk_8_2_0.models.cluster_node_drive_d_config import ClusterNodeDriveDConfig  # noqa: F401,E501
from isi_sdk_8_2_0.models.cluster_node_drive_extended import ClusterNodeDriveExtended  # noqa: F401,E501
from isi_sdk_8_2_0.models.cluster_node_hardware import ClusterNodeHardware  # noqa: F401,E501
from isi_sdk_8_2_0.models.cluster_node_partitions import ClusterNodePartitions  # noqa: F401,E501
from isi_sdk_8_2_0.models.cluster_node_sensors import ClusterNodeSensors  # noqa: F401,E501
from isi_sdk_8_2_0.models.cluster_node_state_extended import ClusterNodeStateExtended  # noqa: F401,E501
from isi_sdk_8_2_0.models.cluster_node_status import ClusterNodeStatus  # noqa: F401,E501
from isi_sdk_8_2_0.models.node_sleds_node_sled import NodeSledsNodeSled  # noqa: F401,E501


class ClusterNodeExtended(object):
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
        'drive_d_config': 'ClusterNodeDriveDConfig',
        'drives': 'list[ClusterNodeDriveExtended]',
        'hardware': 'ClusterNodeHardware',
        'id': 'int',
        'internal_ip_address': 'str',
        'lnn': 'int',
        'partitions': 'ClusterNodePartitions',
        'sensors': 'ClusterNodeSensors',
        'sleds': 'list[NodeSledsNodeSled]',
        'state': 'ClusterNodeStateExtended',
        'status': 'ClusterNodeStatus'
    }

    attribute_map = {
        'drive_d_config': 'drive_d_config',
        'drives': 'drives',
        'hardware': 'hardware',
        'id': 'id',
        'internal_ip_address': 'internal_ip_address',
        'lnn': 'lnn',
        'partitions': 'partitions',
        'sensors': 'sensors',
        'sleds': 'sleds',
        'state': 'state',
        'status': 'status'
    }

    def __init__(self, drive_d_config=None, drives=None, hardware=None, id=None, internal_ip_address=None, lnn=None, partitions=None, sensors=None, sleds=None, state=None, status=None):  # noqa: E501
        """ClusterNodeExtended - a model defined in Swagger"""  # noqa: E501

        self._drive_d_config = None
        self._drives = None
        self._hardware = None
        self._id = None
        self._internal_ip_address = None
        self._lnn = None
        self._partitions = None
        self._sensors = None
        self._sleds = None
        self._state = None
        self._status = None
        self.discriminator = None

        if drive_d_config is not None:
            self.drive_d_config = drive_d_config
        if drives is not None:
            self.drives = drives
        if hardware is not None:
            self.hardware = hardware
        if id is not None:
            self.id = id
        self.internal_ip_address = internal_ip_address
        if lnn is not None:
            self.lnn = lnn
        if partitions is not None:
            self.partitions = partitions
        if sensors is not None:
            self.sensors = sensors
        if sleds is not None:
            self.sleds = sleds
        if state is not None:
            self.state = state
        if status is not None:
            self.status = status

    @property
    def drive_d_config(self):
        """Gets the drive_d_config of this ClusterNodeExtended.  # noqa: E501

        An object containing a node's drive subsystem XML configuration file.  # noqa: E501

        :return: The drive_d_config of this ClusterNodeExtended.  # noqa: E501
        :rtype: ClusterNodeDriveDConfig
        """
        return self._drive_d_config

    @drive_d_config.setter
    def drive_d_config(self, drive_d_config):
        """Sets the drive_d_config of this ClusterNodeExtended.

        An object containing a node's drive subsystem XML configuration file.  # noqa: E501

        :param drive_d_config: The drive_d_config of this ClusterNodeExtended.  # noqa: E501
        :type: ClusterNodeDriveDConfig
        """

        self._drive_d_config = drive_d_config

    @property
    def drives(self):
        """Gets the drives of this ClusterNodeExtended.  # noqa: E501

        List of the drives in this node.  # noqa: E501

        :return: The drives of this ClusterNodeExtended.  # noqa: E501
        :rtype: list[ClusterNodeDriveExtended]
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """Sets the drives of this ClusterNodeExtended.

        List of the drives in this node.  # noqa: E501

        :param drives: The drives of this ClusterNodeExtended.  # noqa: E501
        :type: list[ClusterNodeDriveExtended]
        """

        self._drives = drives

    @property
    def hardware(self):
        """Gets the hardware of this ClusterNodeExtended.  # noqa: E501

        Node hardware identifying information (static).  # noqa: E501

        :return: The hardware of this ClusterNodeExtended.  # noqa: E501
        :rtype: ClusterNodeHardware
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this ClusterNodeExtended.

        Node hardware identifying information (static).  # noqa: E501

        :param hardware: The hardware of this ClusterNodeExtended.  # noqa: E501
        :type: ClusterNodeHardware
        """

        self._hardware = hardware

    @property
    def id(self):
        """Gets the id of this ClusterNodeExtended.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this ClusterNodeExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClusterNodeExtended.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this ClusterNodeExtended.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def internal_ip_address(self):
        """Gets the internal_ip_address of this ClusterNodeExtended.  # noqa: E501

        IPv4 address in the format: xxx.xxx.xxx.xxx  # noqa: E501

        :return: The internal_ip_address of this ClusterNodeExtended.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip_address

    @internal_ip_address.setter
    def internal_ip_address(self, internal_ip_address):
        """Sets the internal_ip_address of this ClusterNodeExtended.

        IPv4 address in the format: xxx.xxx.xxx.xxx  # noqa: E501

        :param internal_ip_address: The internal_ip_address of this ClusterNodeExtended.  # noqa: E501
        :type: str
        """
        if internal_ip_address is None:
            raise ValueError("Invalid value for `internal_ip_address`, must not be `None`")  # noqa: E501
        if internal_ip_address is not None and len(internal_ip_address) > 45:
            raise ValueError("Invalid value for `internal_ip_address`, length must be less than or equal to `45`")  # noqa: E501
        if internal_ip_address is not None and len(internal_ip_address) < 2:
            raise ValueError("Invalid value for `internal_ip_address`, length must be greater than or equal to `2`")  # noqa: E501
        if internal_ip_address is not None and not re.search('^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$', internal_ip_address):  # noqa: E501
            raise ValueError("Invalid value for `internal_ip_address`, must be a follow pattern or equal to `/^([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\\.([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])){3}$/`")  # noqa: E501

        self._internal_ip_address = internal_ip_address

    @property
    def lnn(self):
        """Gets the lnn of this ClusterNodeExtended.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this ClusterNodeExtended.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this ClusterNodeExtended.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this ClusterNodeExtended.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def partitions(self):
        """Gets the partitions of this ClusterNodeExtended.  # noqa: E501

        Node partition information.  # noqa: E501

        :return: The partitions of this ClusterNodeExtended.  # noqa: E501
        :rtype: ClusterNodePartitions
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions):
        """Sets the partitions of this ClusterNodeExtended.

        Node partition information.  # noqa: E501

        :param partitions: The partitions of this ClusterNodeExtended.  # noqa: E501
        :type: ClusterNodePartitions
        """

        self._partitions = partitions

    @property
    def sensors(self):
        """Gets the sensors of this ClusterNodeExtended.  # noqa: E501

        Node sensor information (hardware reported).  # noqa: E501

        :return: The sensors of this ClusterNodeExtended.  # noqa: E501
        :rtype: ClusterNodeSensors
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this ClusterNodeExtended.

        Node sensor information (hardware reported).  # noqa: E501

        :param sensors: The sensors of this ClusterNodeExtended.  # noqa: E501
        :type: ClusterNodeSensors
        """

        self._sensors = sensors

    @property
    def sleds(self):
        """Gets the sleds of this ClusterNodeExtended.  # noqa: E501

        List of the sleds in this node.  # noqa: E501

        :return: The sleds of this ClusterNodeExtended.  # noqa: E501
        :rtype: list[NodeSledsNodeSled]
        """
        return self._sleds

    @sleds.setter
    def sleds(self, sleds):
        """Sets the sleds of this ClusterNodeExtended.

        List of the sleds in this node.  # noqa: E501

        :param sleds: The sleds of this ClusterNodeExtended.  # noqa: E501
        :type: list[NodeSledsNodeSled]
        """

        self._sleds = sleds

    @property
    def state(self):
        """Gets the state of this ClusterNodeExtended.  # noqa: E501

        Node state information (reported and modifiable).  # noqa: E501

        :return: The state of this ClusterNodeExtended.  # noqa: E501
        :rtype: ClusterNodeStateExtended
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ClusterNodeExtended.

        Node state information (reported and modifiable).  # noqa: E501

        :param state: The state of this ClusterNodeExtended.  # noqa: E501
        :type: ClusterNodeStateExtended
        """

        self._state = state

    @property
    def status(self):
        """Gets the status of this ClusterNodeExtended.  # noqa: E501

        Node status information (hardware reported).  # noqa: E501

        :return: The status of this ClusterNodeExtended.  # noqa: E501
        :rtype: ClusterNodeStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ClusterNodeExtended.

        Node status information (hardware reported).  # noqa: E501

        :param status: The status of this ClusterNodeExtended.  # noqa: E501
        :type: ClusterNodeStatus
        """

        self._status = status

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
        if not isinstance(other, ClusterNodeExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
