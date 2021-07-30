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

from isi_sdk_9_1_0.models.node_status_nvram_node_battery import NodeStatusNvramNodeBattery  # noqa: F401,E501


class NodeStatusNvramNode(object):
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
        'batteries': 'list[NodeStatusNvramNodeBattery]',
        'battery_count': 'int',
        'charge_status': 'str',
        'charge_status_number': 'int',
        'device': 'str',
        'error': 'str',
        'id': 'int',
        'lnn': 'int',
        'present': 'bool',
        'present_flash': 'bool',
        'present_size': 'int',
        'present_type': 'str',
        'ship_mode': 'int',
        'status': 'int',
        'supported': 'bool',
        'supported_flash': 'bool',
        'supported_size': 'int',
        'supported_type': 'str'
    }

    attribute_map = {
        'batteries': 'batteries',
        'battery_count': 'battery_count',
        'charge_status': 'charge_status',
        'charge_status_number': 'charge_status_number',
        'device': 'device',
        'error': 'error',
        'id': 'id',
        'lnn': 'lnn',
        'present': 'present',
        'present_flash': 'present_flash',
        'present_size': 'present_size',
        'present_type': 'present_type',
        'ship_mode': 'ship_mode',
        'status': 'status',
        'supported': 'supported',
        'supported_flash': 'supported_flash',
        'supported_size': 'supported_size',
        'supported_type': 'supported_type'
    }

    def __init__(self, batteries=None, battery_count=None, charge_status=None, charge_status_number=None, device=None, error=None, id=None, lnn=None, present=None, present_flash=None, present_size=None, present_type=None, ship_mode=None, status=None, supported=None, supported_flash=None, supported_size=None, supported_type=None):  # noqa: E501
        """NodeStatusNvramNode - a model defined in Swagger"""  # noqa: E501

        self._batteries = None
        self._battery_count = None
        self._charge_status = None
        self._charge_status_number = None
        self._device = None
        self._error = None
        self._id = None
        self._lnn = None
        self._present = None
        self._present_flash = None
        self._present_size = None
        self._present_type = None
        self._ship_mode = None
        self._status = None
        self._supported = None
        self._supported_flash = None
        self._supported_size = None
        self._supported_type = None
        self.discriminator = None

        if batteries is not None:
            self.batteries = batteries
        if battery_count is not None:
            self.battery_count = battery_count
        if charge_status is not None:
            self.charge_status = charge_status
        if charge_status_number is not None:
            self.charge_status_number = charge_status_number
        if device is not None:
            self.device = device
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if present is not None:
            self.present = present
        if present_flash is not None:
            self.present_flash = present_flash
        if present_size is not None:
            self.present_size = present_size
        if present_type is not None:
            self.present_type = present_type
        if ship_mode is not None:
            self.ship_mode = ship_mode
        if status is not None:
            self.status = status
        if supported is not None:
            self.supported = supported
        if supported_flash is not None:
            self.supported_flash = supported_flash
        if supported_size is not None:
            self.supported_size = supported_size
        if supported_type is not None:
            self.supported_type = supported_type

    @property
    def batteries(self):
        """Gets the batteries of this NodeStatusNvramNode.  # noqa: E501

        This node's NVRAM battery status information.  # noqa: E501

        :return: The batteries of this NodeStatusNvramNode.  # noqa: E501
        :rtype: list[NodeStatusNvramNodeBattery]
        """
        return self._batteries

    @batteries.setter
    def batteries(self, batteries):
        """Sets the batteries of this NodeStatusNvramNode.

        This node's NVRAM battery status information.  # noqa: E501

        :param batteries: The batteries of this NodeStatusNvramNode.  # noqa: E501
        :type: list[NodeStatusNvramNodeBattery]
        """

        self._batteries = batteries

    @property
    def battery_count(self):
        """Gets the battery_count of this NodeStatusNvramNode.  # noqa: E501

        This node's NVRAM battery count. On failure: -1, otherwise 1 or 2.  # noqa: E501

        :return: The battery_count of this NodeStatusNvramNode.  # noqa: E501
        :rtype: int
        """
        return self._battery_count

    @battery_count.setter
    def battery_count(self, battery_count):
        """Sets the battery_count of this NodeStatusNvramNode.

        This node's NVRAM battery count. On failure: -1, otherwise 1 or 2.  # noqa: E501

        :param battery_count: The battery_count of this NodeStatusNvramNode.  # noqa: E501
        :type: int
        """
        if battery_count is not None and battery_count > 2:  # noqa: E501
            raise ValueError("Invalid value for `battery_count`, must be a value less than or equal to `2`")  # noqa: E501
        if battery_count is not None and battery_count < -1:  # noqa: E501
            raise ValueError("Invalid value for `battery_count`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._battery_count = battery_count

    @property
    def charge_status(self):
        """Gets the charge_status of this NodeStatusNvramNode.  # noqa: E501

        This node's NVRAM battery charge status, as a color.  # noqa: E501

        :return: The charge_status of this NodeStatusNvramNode.  # noqa: E501
        :rtype: str
        """
        return self._charge_status

    @charge_status.setter
    def charge_status(self, charge_status):
        """Sets the charge_status of this NodeStatusNvramNode.

        This node's NVRAM battery charge status, as a color.  # noqa: E501

        :param charge_status: The charge_status of this NodeStatusNvramNode.  # noqa: E501
        :type: str
        """
        allowed_values = ["BLACK", "GREEN", "YELLOW", "RED", "UNKNOWN", "Not supported"]  # noqa: E501
        if charge_status not in allowed_values:
            raise ValueError(
                "Invalid value for `charge_status` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_status, allowed_values)
            )

        self._charge_status = charge_status

    @property
    def charge_status_number(self):
        """Gets the charge_status_number of this NodeStatusNvramNode.  # noqa: E501

        This node's NVRAM battery charge status, as a number. Error or not supported: -1. BR_BLACK: 0. BR_GREEN: 1. BR_YELLOW: 2. BR_RED: 3.  # noqa: E501

        :return: The charge_status_number of this NodeStatusNvramNode.  # noqa: E501
        :rtype: int
        """
        return self._charge_status_number

    @charge_status_number.setter
    def charge_status_number(self, charge_status_number):
        """Sets the charge_status_number of this NodeStatusNvramNode.

        This node's NVRAM battery charge status, as a number. Error or not supported: -1. BR_BLACK: 0. BR_GREEN: 1. BR_YELLOW: 2. BR_RED: 3.  # noqa: E501

        :param charge_status_number: The charge_status_number of this NodeStatusNvramNode.  # noqa: E501
        :type: int
        """
        if charge_status_number is not None and charge_status_number > 3:  # noqa: E501
            raise ValueError("Invalid value for `charge_status_number`, must be a value less than or equal to `3`")  # noqa: E501
        if charge_status_number is not None and charge_status_number < -1:  # noqa: E501
            raise ValueError("Invalid value for `charge_status_number`, must be a value greater than or equal to `-1`")  # noqa: E501

        self._charge_status_number = charge_status_number

    @property
    def device(self):
        """Gets the device of this NodeStatusNvramNode.  # noqa: E501

        This node's NVRAM device name with path.  # noqa: E501

        :return: The device of this NodeStatusNvramNode.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this NodeStatusNvramNode.

        This node's NVRAM device name with path.  # noqa: E501

        :param device: The device of this NodeStatusNvramNode.  # noqa: E501
        :type: str
        """
        if device is not None and len(device) > 255:
            raise ValueError("Invalid value for `device`, length must be less than or equal to `255`")  # noqa: E501
        if device is not None and len(device) < 0:
            raise ValueError("Invalid value for `device`, length must be greater than or equal to `0`")  # noqa: E501

        self._device = device

    @property
    def error(self):
        """Gets the error of this NodeStatusNvramNode.  # noqa: E501

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :return: The error of this NodeStatusNvramNode.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this NodeStatusNvramNode.

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :param error: The error of this NodeStatusNvramNode.  # noqa: E501
        :type: str
        """
        if error is not None and len(error) > 8192:
            raise ValueError("Invalid value for `error`, length must be less than or equal to `8192`")  # noqa: E501
        if error is not None and len(error) < 0:
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `0`")  # noqa: E501

        self._error = error

    @property
    def id(self):
        """Gets the id of this NodeStatusNvramNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeStatusNvramNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeStatusNvramNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeStatusNvramNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NodeStatusNvramNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeStatusNvramNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeStatusNvramNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeStatusNvramNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def present(self):
        """Gets the present of this NodeStatusNvramNode.  # noqa: E501

        This node has NVRAM.  # noqa: E501

        :return: The present of this NodeStatusNvramNode.  # noqa: E501
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """Sets the present of this NodeStatusNvramNode.

        This node has NVRAM.  # noqa: E501

        :param present: The present of this NodeStatusNvramNode.  # noqa: E501
        :type: bool
        """

        self._present = present

    @property
    def present_flash(self):
        """Gets the present_flash of this NodeStatusNvramNode.  # noqa: E501

        This node has NVRAM with flash storage.  # noqa: E501

        :return: The present_flash of this NodeStatusNvramNode.  # noqa: E501
        :rtype: bool
        """
        return self._present_flash

    @present_flash.setter
    def present_flash(self, present_flash):
        """Sets the present_flash of this NodeStatusNvramNode.

        This node has NVRAM with flash storage.  # noqa: E501

        :param present_flash: The present_flash of this NodeStatusNvramNode.  # noqa: E501
        :type: bool
        """

        self._present_flash = present_flash

    @property
    def present_size(self):
        """Gets the present_size of this NodeStatusNvramNode.  # noqa: E501

        The size of the NVRAM, in bytes.  # noqa: E501

        :return: The present_size of this NodeStatusNvramNode.  # noqa: E501
        :rtype: int
        """
        return self._present_size

    @present_size.setter
    def present_size(self, present_size):
        """Sets the present_size of this NodeStatusNvramNode.

        The size of the NVRAM, in bytes.  # noqa: E501

        :param present_size: The present_size of this NodeStatusNvramNode.  # noqa: E501
        :type: int
        """
        if present_size is not None and present_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `present_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if present_size is not None and present_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `present_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._present_size = present_size

    @property
    def present_type(self):
        """Gets the present_type of this NodeStatusNvramNode.  # noqa: E501

        This node's NVRAM type.  # noqa: E501

        :return: The present_type of this NodeStatusNvramNode.  # noqa: E501
        :rtype: str
        """
        return self._present_type

    @present_type.setter
    def present_type(self, present_type):
        """Sets the present_type of this NodeStatusNvramNode.

        This node's NVRAM type.  # noqa: E501

        :param present_type: The present_type of this NodeStatusNvramNode.  # noqa: E501
        :type: str
        """
        if present_type is not None and len(present_type) > 255:
            raise ValueError("Invalid value for `present_type`, length must be less than or equal to `255`")  # noqa: E501
        if present_type is not None and len(present_type) < 0:
            raise ValueError("Invalid value for `present_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._present_type = present_type

    @property
    def ship_mode(self):
        """Gets the ship_mode of this NodeStatusNvramNode.  # noqa: E501

        This node's current ship mode state for NVRAM batteries. If not supported or on failure: -1. Disabled: 0. Enabled: 1.  # noqa: E501

        :return: The ship_mode of this NodeStatusNvramNode.  # noqa: E501
        :rtype: int
        """
        return self._ship_mode

    @ship_mode.setter
    def ship_mode(self, ship_mode):
        """Sets the ship_mode of this NodeStatusNvramNode.

        This node's current ship mode state for NVRAM batteries. If not supported or on failure: -1. Disabled: 0. Enabled: 1.  # noqa: E501

        :param ship_mode: The ship_mode of this NodeStatusNvramNode.  # noqa: E501
        :type: int
        """

        self._ship_mode = ship_mode

    @property
    def status(self):
        """Gets the status of this NodeStatusNvramNode.  # noqa: E501

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :return: The status of this NodeStatusNvramNode.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeStatusNvramNode.

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :param status: The status of this NodeStatusNvramNode.  # noqa: E501
        :type: int
        """
        if status is not None and status > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if status is not None and status < 0:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0`")  # noqa: E501

        self._status = status

    @property
    def supported(self):
        """Gets the supported of this NodeStatusNvramNode.  # noqa: E501

        This node supports NVRAM.  # noqa: E501

        :return: The supported of this NodeStatusNvramNode.  # noqa: E501
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """Sets the supported of this NodeStatusNvramNode.

        This node supports NVRAM.  # noqa: E501

        :param supported: The supported of this NodeStatusNvramNode.  # noqa: E501
        :type: bool
        """

        self._supported = supported

    @property
    def supported_flash(self):
        """Gets the supported_flash of this NodeStatusNvramNode.  # noqa: E501

        This node supports NVRAM with flash storage.  # noqa: E501

        :return: The supported_flash of this NodeStatusNvramNode.  # noqa: E501
        :rtype: bool
        """
        return self._supported_flash

    @supported_flash.setter
    def supported_flash(self, supported_flash):
        """Sets the supported_flash of this NodeStatusNvramNode.

        This node supports NVRAM with flash storage.  # noqa: E501

        :param supported_flash: The supported_flash of this NodeStatusNvramNode.  # noqa: E501
        :type: bool
        """

        self._supported_flash = supported_flash

    @property
    def supported_size(self):
        """Gets the supported_size of this NodeStatusNvramNode.  # noqa: E501

        The maximum size of the NVRAM, in bytes.  # noqa: E501

        :return: The supported_size of this NodeStatusNvramNode.  # noqa: E501
        :rtype: int
        """
        return self._supported_size

    @supported_size.setter
    def supported_size(self, supported_size):
        """Sets the supported_size of this NodeStatusNvramNode.

        The maximum size of the NVRAM, in bytes.  # noqa: E501

        :param supported_size: The supported_size of this NodeStatusNvramNode.  # noqa: E501
        :type: int
        """
        if supported_size is not None and supported_size > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `supported_size`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if supported_size is not None and supported_size < 0:  # noqa: E501
            raise ValueError("Invalid value for `supported_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._supported_size = supported_size

    @property
    def supported_type(self):
        """Gets the supported_type of this NodeStatusNvramNode.  # noqa: E501

        This node's supported NVRAM type.  # noqa: E501

        :return: The supported_type of this NodeStatusNvramNode.  # noqa: E501
        :rtype: str
        """
        return self._supported_type

    @supported_type.setter
    def supported_type(self, supported_type):
        """Sets the supported_type of this NodeStatusNvramNode.

        This node's supported NVRAM type.  # noqa: E501

        :param supported_type: The supported_type of this NodeStatusNvramNode.  # noqa: E501
        :type: str
        """
        if supported_type is not None and len(supported_type) > 255:
            raise ValueError("Invalid value for `supported_type`, length must be less than or equal to `255`")  # noqa: E501
        if supported_type is not None and len(supported_type) < 0:
            raise ValueError("Invalid value for `supported_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._supported_type = supported_type

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
        if not isinstance(other, NodeStatusNvramNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
