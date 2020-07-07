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


class DrivesDriveFirmwareUpdateNodeStatus(object):
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
        'failed': 'int',
        'finish_time': 'str',
        'remaining': 'int',
        'start_time': 'str',
        'status': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'failed': 'failed',
        'finish_time': 'finish_time',
        'remaining': 'remaining',
        'start_time': 'start_time',
        'status': 'status',
        'updated': 'updated'
    }

    def __init__(self, failed=None, finish_time=None, remaining=None, start_time=None, status=None, updated=None):  # noqa: E501
        """DrivesDriveFirmwareUpdateNodeStatus - a model defined in Swagger"""  # noqa: E501

        self._failed = None
        self._finish_time = None
        self._remaining = None
        self._start_time = None
        self._status = None
        self._updated = None
        self.discriminator = None

        if failed is not None:
            self.failed = failed
        if finish_time is not None:
            self.finish_time = finish_time
        if remaining is not None:
            self.remaining = remaining
        if start_time is not None:
            self.start_time = start_time
        if status is not None:
            self.status = status
        if updated is not None:
            self.updated = updated

    @property
    def failed(self):
        """Gets the failed of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501

        The number of drives that did not successfully complete firmware updates update on the node.  # noqa: E501

        :return: The failed of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this DrivesDriveFirmwareUpdateNodeStatus.

        The number of drives that did not successfully complete firmware updates update on the node.  # noqa: E501

        :param failed: The failed of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def finish_time(self):
        """Gets the finish_time of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501

        Time when drive firmware update finished on node.  # noqa: E501

        :return: The finish_time of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._finish_time

    @finish_time.setter
    def finish_time(self, finish_time):
        """Sets the finish_time of this DrivesDriveFirmwareUpdateNodeStatus.

        Time when drive firmware update finished on node.  # noqa: E501

        :param finish_time: The finish_time of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :type: str
        """

        self._finish_time = finish_time

    @property
    def remaining(self):
        """Gets the remaining of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501

        Number of drives remaining to be updated on node.  # noqa: E501

        :return: The remaining of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :rtype: int
        """
        return self._remaining

    @remaining.setter
    def remaining(self, remaining):
        """Sets the remaining of this DrivesDriveFirmwareUpdateNodeStatus.

        Number of drives remaining to be updated on node.  # noqa: E501

        :param remaining: The remaining of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :type: int
        """

        self._remaining = remaining

    @property
    def start_time(self):
        """Gets the start_time of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501

        Time when drive firmware update started on node.  # noqa: E501

        :return: The start_time of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this DrivesDriveFirmwareUpdateNodeStatus.

        Time when drive firmware update started on node.  # noqa: E501

        :param start_time: The start_time of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def status(self):
        """Gets the status of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501

        Overall status of this nodes firmware updates.  # noqa: E501

        :return: The status of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DrivesDriveFirmwareUpdateNodeStatus.

        Overall status of this nodes firmware updates.  # noqa: E501

        :param status: The status of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def updated(self):
        """Gets the updated of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501

        The number of drives that completed firmware updates on the node.  # noqa: E501

        :return: The updated of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this DrivesDriveFirmwareUpdateNodeStatus.

        The number of drives that completed firmware updates on the node.  # noqa: E501

        :param updated: The updated of this DrivesDriveFirmwareUpdateNodeStatus.  # noqa: E501
        :type: int
        """

        self._updated = updated

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
        if not isinstance(other, DrivesDriveFirmwareUpdateNodeStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
