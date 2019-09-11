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

from isi_sdk_8_2_0.models.pools_pool_interfaces_interface_owner import PoolsPoolInterfacesInterfaceOwner  # noqa: F401,E501


class PoolsPoolInterfacesInterface(object):
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
        'id': 'str',
        'ip_addrs': 'list[str]',
        'lnn': 'int',
        'name': 'str',
        'nic_name': 'str',
        'owners': 'list[PoolsPoolInterfacesInterfaceOwner]',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'ip_addrs': 'ip_addrs',
        'lnn': 'lnn',
        'name': 'name',
        'nic_name': 'nic_name',
        'owners': 'owners',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, id=None, ip_addrs=None, lnn=None, name=None, nic_name=None, owners=None, status=None, type=None):  # noqa: E501
        """PoolsPoolInterfacesInterface - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._ip_addrs = None
        self._lnn = None
        self._name = None
        self._nic_name = None
        self._owners = None
        self._status = None
        self._type = None
        self.discriminator = None

        self.id = id
        self.ip_addrs = ip_addrs
        self.lnn = lnn
        self.name = name
        self.nic_name = nic_name
        self.owners = owners
        self.status = status
        self.type = type

    @property
    def id(self):
        """Gets the id of this PoolsPoolInterfacesInterface.  # noqa: E501

        Unique interface ID.  # noqa: E501

        :return: The id of this PoolsPoolInterfacesInterface.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PoolsPoolInterfacesInterface.

        Unique interface ID.  # noqa: E501

        :param id: The id of this PoolsPoolInterfacesInterface.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 32:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `32`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def ip_addrs(self):
        """Gets the ip_addrs of this PoolsPoolInterfacesInterface.  # noqa: E501

        List of IP addresses  # noqa: E501

        :return: The ip_addrs of this PoolsPoolInterfacesInterface.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_addrs

    @ip_addrs.setter
    def ip_addrs(self, ip_addrs):
        """Sets the ip_addrs of this PoolsPoolInterfacesInterface.

        List of IP addresses  # noqa: E501

        :param ip_addrs: The ip_addrs of this PoolsPoolInterfacesInterface.  # noqa: E501
        :type: list[str]
        """
        if ip_addrs is None:
            raise ValueError("Invalid value for `ip_addrs`, must not be `None`")  # noqa: E501

        self._ip_addrs = ip_addrs

    @property
    def lnn(self):
        """Gets the lnn of this PoolsPoolInterfacesInterface.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this PoolsPoolInterfacesInterface.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this PoolsPoolInterfacesInterface.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this PoolsPoolInterfacesInterface.  # noqa: E501
        :type: int
        """
        if lnn is None:
            raise ValueError("Invalid value for `lnn`, must not be `None`")  # noqa: E501
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def name(self):
        """Gets the name of this PoolsPoolInterfacesInterface.  # noqa: E501

        The name of the interface.  # noqa: E501

        :return: The name of this PoolsPoolInterfacesInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PoolsPoolInterfacesInterface.

        The name of the interface.  # noqa: E501

        :param name: The name of this PoolsPoolInterfacesInterface.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 32:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `32`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def nic_name(self):
        """Gets the nic_name of this PoolsPoolInterfacesInterface.  # noqa: E501

        NIC name  # noqa: E501

        :return: The nic_name of this PoolsPoolInterfacesInterface.  # noqa: E501
        :rtype: str
        """
        return self._nic_name

    @nic_name.setter
    def nic_name(self, nic_name):
        """Sets the nic_name of this PoolsPoolInterfacesInterface.

        NIC name  # noqa: E501

        :param nic_name: The nic_name of this PoolsPoolInterfacesInterface.  # noqa: E501
        :type: str
        """
        if nic_name is None:
            raise ValueError("Invalid value for `nic_name`, must not be `None`")  # noqa: E501
        if nic_name is not None and len(nic_name) > 32:
            raise ValueError("Invalid value for `nic_name`, length must be less than or equal to `32`")  # noqa: E501
        if nic_name is not None and len(nic_name) < 1:
            raise ValueError("Invalid value for `nic_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._nic_name = nic_name

    @property
    def owners(self):
        """Gets the owners of this PoolsPoolInterfacesInterface.  # noqa: E501

        List of owners (membership)  # noqa: E501

        :return: The owners of this PoolsPoolInterfacesInterface.  # noqa: E501
        :rtype: list[PoolsPoolInterfacesInterfaceOwner]
        """
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Sets the owners of this PoolsPoolInterfacesInterface.

        List of owners (membership)  # noqa: E501

        :param owners: The owners of this PoolsPoolInterfacesInterface.  # noqa: E501
        :type: list[PoolsPoolInterfacesInterfaceOwner]
        """
        if owners is None:
            raise ValueError("Invalid value for `owners`, must not be `None`")  # noqa: E501

        self._owners = owners

    @property
    def status(self):
        """Gets the status of this PoolsPoolInterfacesInterface.  # noqa: E501

        Status of the interface  # noqa: E501

        :return: The status of this PoolsPoolInterfacesInterface.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PoolsPoolInterfacesInterface.

        Status of the interface  # noqa: E501

        :param status: The status of this PoolsPoolInterfacesInterface.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this PoolsPoolInterfacesInterface.  # noqa: E501

        Interface type.  The '*gige' types stand for 'gigabit ethernet'.  'gige' itself is occasionally also referred to in other places as 'ext' for 'external'.  'ib' and 'ib_qdr' are internal Infiniband interface types.  'vlan' and 'vmxnet3' are virtual interface types that appear on virtual nodes.  'loopback' is an interface for failover addresses and should only appear if failover is configured.  # noqa: E501

        :return: The type of this PoolsPoolInterfacesInterface.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PoolsPoolInterfacesInterface.

        Interface type.  The '*gige' types stand for 'gigabit ethernet'.  'gige' itself is occasionally also referred to in other places as 'ext' for 'external'.  'ib' and 'ib_qdr' are internal Infiniband interface types.  'vlan' and 'vmxnet3' are virtual interface types that appear on virtual nodes.  'loopback' is an interface for failover addresses and should only appear if failover is configured.  # noqa: E501

        :param type: The type of this PoolsPoolInterfacesInterface.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["any", "gige", "fastgige", "10gige", "40gige", "mgmt", "ib", "ib_qdr", "ib_fdr", "aggregated", "vlan", "vmxnet3", "loopback"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, PoolsPoolInterfacesInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
