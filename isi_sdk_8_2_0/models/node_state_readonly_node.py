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


class NodeStateReadonlyNode(object):
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
        'allowed': 'bool',
        'enabled': 'bool',
        'error': 'str',
        'id': 'int',
        'lnn': 'int',
        'mode': 'bool',
        'status': 'str',
        'valid': 'bool',
        'value': 'int'
    }

    attribute_map = {
        'allowed': 'allowed',
        'enabled': 'enabled',
        'error': 'error',
        'id': 'id',
        'lnn': 'lnn',
        'mode': 'mode',
        'status': 'status',
        'valid': 'valid',
        'value': 'value'
    }

    def __init__(self, allowed=None, enabled=None, error=None, id=None, lnn=None, mode=None, status=None, valid=None, value=None):  # noqa: E501
        """NodeStateReadonlyNode - a model defined in Swagger"""  # noqa: E501

        self._allowed = None
        self._enabled = None
        self._error = None
        self._id = None
        self._lnn = None
        self._mode = None
        self._status = None
        self._valid = None
        self._value = None
        self.discriminator = None

        if allowed is not None:
            self.allowed = allowed
        if enabled is not None:
            self.enabled = enabled
        if error is not None:
            self.error = error
        if id is not None:
            self.id = id
        if lnn is not None:
            self.lnn = lnn
        if mode is not None:
            self.mode = mode
        if status is not None:
            self.status = status
        if valid is not None:
            self.valid = valid
        if value is not None:
            self.value = value

    @property
    def allowed(self):
        """Gets the allowed of this NodeStateReadonlyNode.  # noqa: E501

        The current read-only mode allowed status for the node.  # noqa: E501

        :return: The allowed of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: bool
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """Sets the allowed of this NodeStateReadonlyNode.

        The current read-only mode allowed status for the node.  # noqa: E501

        :param allowed: The allowed of this NodeStateReadonlyNode.  # noqa: E501
        :type: bool
        """

        self._allowed = allowed

    @property
    def enabled(self):
        """Gets the enabled of this NodeStateReadonlyNode.  # noqa: E501

        The current read-only user mode status for the node. NOTE: If read-only mode is currently disallowed for this node, it will remain read/write until read-only mode is allowed again. This value only sets or clears any user-specified requests for read-only mode. If the node has been placed into read-only mode by the system, it will remain in read-only mode until the system conditions which triggered read-only mode have cleared.  # noqa: E501

        :return: The enabled of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NodeStateReadonlyNode.

        The current read-only user mode status for the node. NOTE: If read-only mode is currently disallowed for this node, it will remain read/write until read-only mode is allowed again. This value only sets or clears any user-specified requests for read-only mode. If the node has been placed into read-only mode by the system, it will remain in read-only mode until the system conditions which triggered read-only mode have cleared.  # noqa: E501

        :param enabled: The enabled of this NodeStateReadonlyNode.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def error(self):
        """Gets the error of this NodeStateReadonlyNode.  # noqa: E501

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :return: The error of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this NodeStateReadonlyNode.

        Error message, if the HTTP status returned from this node was not 200.  # noqa: E501

        :param error: The error of this NodeStateReadonlyNode.  # noqa: E501
        :type: str
        """
        if error is not None and len(error) > 8192:
            raise ValueError("Invalid value for `error`, length must be less than or equal to `8192`")  # noqa: E501
        if error is not None and len(error) < 0:
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `0`")  # noqa: E501

        self._error = error

    @property
    def id(self):
        """Gets the id of this NodeStateReadonlyNode.  # noqa: E501

        Node ID (Device Number) of a node.  # noqa: E501

        :return: The id of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NodeStateReadonlyNode.

        Node ID (Device Number) of a node.  # noqa: E501

        :param id: The id of this NodeStateReadonlyNode.  # noqa: E501
        :type: int
        """
        if id is not None and id > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if id is not None and id < 0:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def lnn(self):
        """Gets the lnn of this NodeStateReadonlyNode.  # noqa: E501

        Logical Node Number (LNN) of a node.  # noqa: E501

        :return: The lnn of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: int
        """
        return self._lnn

    @lnn.setter
    def lnn(self, lnn):
        """Sets the lnn of this NodeStateReadonlyNode.

        Logical Node Number (LNN) of a node.  # noqa: E501

        :param lnn: The lnn of this NodeStateReadonlyNode.  # noqa: E501
        :type: int
        """
        if lnn is not None and lnn > 65535:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value less than or equal to `65535`")  # noqa: E501
        if lnn is not None and lnn < 1:  # noqa: E501
            raise ValueError("Invalid value for `lnn`, must be a value greater than or equal to `1`")  # noqa: E501

        self._lnn = lnn

    @property
    def mode(self):
        """Gets the mode of this NodeStateReadonlyNode.  # noqa: E501

        The current read-only mode status for the node.  # noqa: E501

        :return: The mode of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: bool
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this NodeStateReadonlyNode.

        The current read-only mode status for the node.  # noqa: E501

        :param mode: The mode of this NodeStateReadonlyNode.  # noqa: E501
        :type: bool
        """

        self._mode = mode

    @property
    def status(self):
        """Gets the status of this NodeStateReadonlyNode.  # noqa: E501

        The current read-only mode status description for the node.  # noqa: E501

        :return: The status of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NodeStateReadonlyNode.

        The current read-only mode status description for the node.  # noqa: E501

        :param status: The status of this NodeStateReadonlyNode.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def valid(self):
        """Gets the valid of this NodeStateReadonlyNode.  # noqa: E501

        The read-only state values are valid (False = Error).  # noqa: E501

        :return: The valid of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this NodeStateReadonlyNode.

        The read-only state values are valid (False = Error).  # noqa: E501

        :param valid: The valid of this NodeStateReadonlyNode.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def value(self):
        """Gets the value of this NodeStateReadonlyNode.  # noqa: E501

        The current read-only value (enumerated bitfield) for the node.  # noqa: E501

        :return: The value of this NodeStateReadonlyNode.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this NodeStateReadonlyNode.

        The current read-only value (enumerated bitfield) for the node.  # noqa: E501

        :param value: The value of this NodeStateReadonlyNode.  # noqa: E501
        :type: int
        """
        if value is not None and value > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if value is not None and value < 0:  # noqa: E501
            raise ValueError("Invalid value for `value`, must be a value greater than or equal to `0`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, NodeStateReadonlyNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
