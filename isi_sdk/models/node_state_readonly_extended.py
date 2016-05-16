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


class NodeStateReadonlyExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodeStateReadonlyExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allowed': 'bool',
            'enabled': 'bool',
            'mode': 'bool',
            'status': 'str',
            'valid': 'bool',
            'value': 'int'
        }

        self.attribute_map = {
            'allowed': 'allowed',
            'enabled': 'enabled',
            'mode': 'mode',
            'status': 'status',
            'valid': 'valid',
            'value': 'value'
        }

        self._allowed = None
        self._enabled = None
        self._mode = None
        self._status = None
        self._valid = None
        self._value = None

    @property
    def allowed(self):
        """
        Gets the allowed of this NodeStateReadonlyExtended.
        The current read-only mode allowed status for the node.

        :return: The allowed of this NodeStateReadonlyExtended.
        :rtype: bool
        """
        return self._allowed

    @allowed.setter
    def allowed(self, allowed):
        """
        Sets the allowed of this NodeStateReadonlyExtended.
        The current read-only mode allowed status for the node.

        :param allowed: The allowed of this NodeStateReadonlyExtended.
        :type: bool
        """
        
        self._allowed = allowed

    @property
    def enabled(self):
        """
        Gets the enabled of this NodeStateReadonlyExtended.
        The current read-only user mode status for the node. NOTE: If read-only mode is currently disallowed for this node, it will remain read/write until read-only mode is allowed again. This value only sets or clears any user-specified requests for read-only mode. If the node has been placed into read-only mode by the system, it will remain in read-only mode until the system conditions which triggered read-only mode have cleared.

        :return: The enabled of this NodeStateReadonlyExtended.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this NodeStateReadonlyExtended.
        The current read-only user mode status for the node. NOTE: If read-only mode is currently disallowed for this node, it will remain read/write until read-only mode is allowed again. This value only sets or clears any user-specified requests for read-only mode. If the node has been placed into read-only mode by the system, it will remain in read-only mode until the system conditions which triggered read-only mode have cleared.

        :param enabled: The enabled of this NodeStateReadonlyExtended.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def mode(self):
        """
        Gets the mode of this NodeStateReadonlyExtended.
        The current read-only mode status for the node.

        :return: The mode of this NodeStateReadonlyExtended.
        :rtype: bool
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this NodeStateReadonlyExtended.
        The current read-only mode status for the node.

        :param mode: The mode of this NodeStateReadonlyExtended.
        :type: bool
        """
        
        self._mode = mode

    @property
    def status(self):
        """
        Gets the status of this NodeStateReadonlyExtended.
        The current read-only mode status description for the node.

        :return: The status of this NodeStateReadonlyExtended.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this NodeStateReadonlyExtended.
        The current read-only mode status description for the node.

        :param status: The status of this NodeStateReadonlyExtended.
        :type: str
        """
        
        self._status = status

    @property
    def valid(self):
        """
        Gets the valid of this NodeStateReadonlyExtended.
        The read-only state values are valid (False = Error).

        :return: The valid of this NodeStateReadonlyExtended.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """
        Sets the valid of this NodeStateReadonlyExtended.
        The read-only state values are valid (False = Error).

        :param valid: The valid of this NodeStateReadonlyExtended.
        :type: bool
        """
        
        self._valid = valid

    @property
    def value(self):
        """
        Gets the value of this NodeStateReadonlyExtended.
        The current read-only value (enumerated bitfield) for the node.

        :return: The value of this NodeStateReadonlyExtended.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this NodeStateReadonlyExtended.
        The current read-only value (enumerated bitfield) for the node.

        :param value: The value of this NodeStateReadonlyExtended.
        :type: int
        """
        
        self._value = value

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

