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


class SyncJobPhase(object):
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
        'end_time': 'int',
        'phase': 'str',
        'start_time': 'int'
    }

    attribute_map = {
        'end_time': 'end_time',
        'phase': 'phase',
        'start_time': 'start_time'
    }

    def __init__(self, end_time=None, phase=None, start_time=None):  # noqa: E501
        """SyncJobPhase - a model defined in Swagger"""  # noqa: E501

        self._end_time = None
        self._phase = None
        self._start_time = None
        self.discriminator = None

        if end_time is not None:
            self.end_time = end_time
        if phase is not None:
            self.phase = phase
        if start_time is not None:
            self.start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this SyncJobPhase.  # noqa: E501

        The time the job ended this phase.  # noqa: E501

        :return: The end_time of this SyncJobPhase.  # noqa: E501
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this SyncJobPhase.

        The time the job ended this phase.  # noqa: E501

        :param end_time: The end_time of this SyncJobPhase.  # noqa: E501
        :type: int
        """
        if end_time is not None and end_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `end_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if end_time is not None and end_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `end_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._end_time = end_time

    @property
    def phase(self):
        """Gets the phase of this SyncJobPhase.  # noqa: E501

        The phase that the job was in.  # noqa: E501

        :return: The phase of this SyncJobPhase.  # noqa: E501
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this SyncJobPhase.

        The phase that the job was in.  # noqa: E501

        :param phase: The phase of this SyncJobPhase.  # noqa: E501
        :type: str
        """
        if phase is not None and len(phase) > 255:
            raise ValueError("Invalid value for `phase`, length must be less than or equal to `255`")  # noqa: E501
        if phase is not None and len(phase) < 0:
            raise ValueError("Invalid value for `phase`, length must be greater than or equal to `0`")  # noqa: E501

        self._phase = phase

    @property
    def start_time(self):
        """Gets the start_time of this SyncJobPhase.  # noqa: E501

        The time the job began this phase.  # noqa: E501

        :return: The start_time of this SyncJobPhase.  # noqa: E501
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this SyncJobPhase.

        The time the job began this phase.  # noqa: E501

        :param start_time: The start_time of this SyncJobPhase.  # noqa: E501
        :type: int
        """
        if start_time is not None and start_time > 9223372036854775807:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must be a value less than or equal to `9223372036854775807`")  # noqa: E501
        if start_time is not None and start_time < 0:  # noqa: E501
            raise ValueError("Invalid value for `start_time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_time = start_time

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
        if not isinstance(other, SyncJobPhase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
