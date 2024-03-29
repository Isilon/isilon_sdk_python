# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 16
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_5_0.models.supportassist_license_task_audit_state import SupportassistLicenseTaskAuditState  # noqa: F401,E501
from isilon_sdk.v9_5_0.models.supportassist_license_task_audit_sub_state import SupportassistLicenseTaskAuditSubState  # noqa: F401,E501


class SupportassistLicenseTaskAudit(object):
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
        'state': 'SupportassistLicenseTaskAuditState',
        'sub_state': 'SupportassistLicenseTaskAuditSubState'
    }

    attribute_map = {
        'state': 'state',
        'sub_state': 'sub_state'
    }

    def __init__(self, state=None, sub_state=None):  # noqa: E501
        """SupportassistLicenseTaskAudit - a model defined in Swagger"""  # noqa: E501

        self._state = None
        self._sub_state = None
        self.discriminator = None

        self.state = state
        self.sub_state = sub_state

    @property
    def state(self):
        """Gets the state of this SupportassistLicenseTaskAudit.  # noqa: E501

        The timestamps of when a task entered a new state  # noqa: E501

        :return: The state of this SupportassistLicenseTaskAudit.  # noqa: E501
        :rtype: SupportassistLicenseTaskAuditState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SupportassistLicenseTaskAudit.

        The timestamps of when a task entered a new state  # noqa: E501

        :param state: The state of this SupportassistLicenseTaskAudit.  # noqa: E501
        :type: SupportassistLicenseTaskAuditState
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def sub_state(self):
        """Gets the sub_state of this SupportassistLicenseTaskAudit.  # noqa: E501

        The sub state audit trail of the task  # noqa: E501

        :return: The sub_state of this SupportassistLicenseTaskAudit.  # noqa: E501
        :rtype: SupportassistLicenseTaskAuditSubState
        """
        return self._sub_state

    @sub_state.setter
    def sub_state(self, sub_state):
        """Sets the sub_state of this SupportassistLicenseTaskAudit.

        The sub state audit trail of the task  # noqa: E501

        :param sub_state: The sub_state of this SupportassistLicenseTaskAudit.  # noqa: E501
        :type: SupportassistLicenseTaskAuditSubState
        """
        if sub_state is None:
            raise ValueError("Invalid value for `sub_state`, must not be `None`")  # noqa: E501

        self._sub_state = sub_state

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
        if not isinstance(other, SupportassistLicenseTaskAudit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
