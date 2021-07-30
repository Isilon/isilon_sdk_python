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

from isi_sdk_9_1_0.models.node_drives_purposelist_node_purpose import NodeDrivesPurposelistNodePurpose  # noqa: F401,E501


class NodeDrivesPurposelistNode(object):
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
        'error': 'str',
        'id': 'int',
        'lnn': 'int',
        'purposes': 'list[NodeDrivesPurposelistNodePurpose]',
        'status': 'int'
    }

    attribute_map = {
        'error': 'error',
        'id': 'id',
        'lnn': 'lnn',
        'purposes': 'purposes',
        'status': 'status'
    }

    def __init__(self, error=None, id=None, lnn=None, purposes=None, status=None):  # noqa: E501
        """NodeDrivesPurposelistNode - a model defined in Swagger"""  # noqa: E501

        self._error = None
        self._id = None
        self._lnn = None
        self._purposes = None
        self._status = None
        self.discriminator = None

        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if purposes is not None:
            self.purposes = purposes
        if status is not None:
            self.status = status

    @property
    def error(self):
        """Gets the error of this NodeDrivesPurposelistNode.  # noqa: E501

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :return: The error of this NodeDrivesPurposelistNode.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this NodeDrivesPurposelistNode.

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :param error: The error of this NodeDrivesPurposelistNode.  # noqa: E501
        :type: str
        """
        if error is not None and len(error) > 8192:
            raise ValueError("Invalid value for `error`, length must be less than or equal to `8192`")  # noqa: E501
        if error is not None and len(error) < 0:
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `0`")  # noqa: E501

        self._error = error

    @property
    def id(self):
        """Gets the id of this NodeDrivesPurposelistNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeDrivesPurposelistNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeDrivesPurposelistNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeDrivesPurposelistNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NodeDrivesPurposelistNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeDrivesPurposelistNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeDrivesPurposelistNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeDrivesPurposelistNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def purposes(self):
        """Gets the purposes of this NodeDrivesPurposelistNode.  # noqa: E501

        List of the drive purposes available on this node.  # noqa: E501

        :return: The purposes of this NodeDrivesPurposelistNode.  # noqa: E501
        :rtype: list[NodeDrivesPurposelistNodePurpose]
        """
        return self._purposes

    @purposes.setter
    def purposes(self, purposes):
        """Sets the purposes of this NodeDrivesPurposelistNode.

        List of the drive purposes available on this node.  # noqa: E501

        :param purposes: The purposes of this NodeDrivesPurposelistNode.  # noqa: E501
        :type: list[NodeDrivesPurposelistNodePurpose]
        """

        self._purposes = purposes

    @property
    def status(self):
        """Gets the status of this NodeDrivesPurposelistNode.  # noqa: E501

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :return: The status of this NodeDrivesPurposelistNode.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeDrivesPurposelistNode.

        Status of the HTTP response from this node if not 200.  If 200, this field does not appear.  # noqa: E501

        :param status: The status of this NodeDrivesPurposelistNode.  # noqa: E501
        :type: int
        """
        if status is not None and status > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if status is not None and status < 0:  # noqa: E501
            raise ValueError("Invalid value for `status`, must be a value greater than or equal to `0`")  # noqa: E501

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
        if not isinstance(other, NodeDrivesPurposelistNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
