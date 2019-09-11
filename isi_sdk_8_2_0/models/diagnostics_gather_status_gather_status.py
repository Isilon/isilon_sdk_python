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


class DiagnosticsGatherStatusGatherStatus(object):
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
        'active_status': 'str',
        'last_status': 'str'
    }

    attribute_map = {
        'active_status': 'Active_Status',
        'last_status': 'Last_Status'
    }

    def __init__(self, active_status=None, last_status=None):  # noqa: E501
        """DiagnosticsGatherStatusGatherStatus - a model defined in Swagger"""  # noqa: E501

        self._active_status = None
        self._last_status = None
        self.discriminator = None

        self.active_status = active_status
        self.last_status = last_status

    @property
    def active_status(self):
        """Gets the active_status of this DiagnosticsGatherStatusGatherStatus.  # noqa: E501

        The current status of the process  # noqa: E501

        :return: The active_status of this DiagnosticsGatherStatusGatherStatus.  # noqa: E501
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this DiagnosticsGatherStatusGatherStatus.

        The current status of the process  # noqa: E501

        :param active_status: The active_status of this DiagnosticsGatherStatusGatherStatus.  # noqa: E501
        :type: str
        """
        if active_status is None:
            raise ValueError("Invalid value for `active_status`, must not be `None`")  # noqa: E501
        allowed_values = ["NOT_RUNNING", "RUNNING", "FINISHED", "STOPPING", "STOPPED"]  # noqa: E501
        if active_status not in allowed_values:
            raise ValueError(
                "Invalid value for `active_status` ({0}), must be one of {1}"  # noqa: E501
                .format(active_status, allowed_values)
            )

        self._active_status = active_status

    @property
    def last_status(self):
        """Gets the last_status of this DiagnosticsGatherStatusGatherStatus.  # noqa: E501

        The previous status of the process  # noqa: E501

        :return: The last_status of this DiagnosticsGatherStatusGatherStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_status

    @last_status.setter
    def last_status(self, last_status):
        """Sets the last_status of this DiagnosticsGatherStatusGatherStatus.

        The previous status of the process  # noqa: E501

        :param last_status: The last_status of this DiagnosticsGatherStatusGatherStatus.  # noqa: E501
        :type: str
        """
        if last_status is None:
            raise ValueError("Invalid value for `last_status`, must not be `None`")  # noqa: E501
        allowed_values = ["NOT_RUNNING", "RUNNING", "FINISHED", "STOPPING", "STOPPED"]  # noqa: E501
        if last_status not in allowed_values:
            raise ValueError(
                "Invalid value for `last_status` ({0}), must be one of {1}"  # noqa: E501
                .format(last_status, allowed_values)
            )

        self._last_status = last_status

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
        if not isinstance(other, DiagnosticsGatherStatusGatherStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
