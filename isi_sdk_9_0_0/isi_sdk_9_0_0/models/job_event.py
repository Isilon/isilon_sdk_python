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


class JobEvent(object):
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
        'flags': 'str',
        'fmt_type': 'str',
        'id': 'int',
        'job_id': 'int',
        'job_type': 'str',
        'key': 'str',
        'phase': 'int',
        'raw_type': 'int',
        'time': 'int',
        'value': 'str'
    }

    attribute_map = {
        'flags': 'flags',
        'fmt_type': 'fmt_type',
        'id': 'id',
        'job_id': 'job_id',
        'job_type': 'job_type',
        'key': 'key',
        'phase': 'phase',
        'raw_type': 'raw_type',
        'time': 'time',
        'value': 'value'
    }

    def __init__(self, flags=None, fmt_type=None, id=None, job_id=None, job_type=None, key=None, phase=None, raw_type=None, time=None, value=None):  # noqa: E501
        """JobEvent - a model defined in Swagger"""  # noqa: E501

        self._flags = None
        self._fmt_type = None
        self._id = None
        self._job_id = None
        self._job_type = None
        self._key = None
        self._phase = None
        self._raw_type = None
        self._time = None
        self._value = None
        self.discriminator = None

        self.flags = flags
        self.fmt_type = fmt_type
        self.id = id
        self.job_id = job_id
        self.job_type = job_type
        self.key = key
        self.phase = phase
        self.raw_type = raw_type
        self.time = time
        if value is not None:
            self.value = value

    @property
    def flags(self):
        """Gets the flags of this JobEvent.  # noqa: E501

        Event flags.  # noqa: E501

        :return: The flags of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this JobEvent.

        Event flags.  # noqa: E501

        :param flags: The flags of this JobEvent.  # noqa: E501
        :type: str
        """
        if flags is None:
            raise ValueError("Invalid value for `flags`, must not be `None`")  # noqa: E501

        self._flags = flags

    @property
    def fmt_type(self):
        """Gets the fmt_type of this JobEvent.  # noqa: E501

        A string representation of the type of the data value.  # noqa: E501

        :return: The fmt_type of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._fmt_type

    @fmt_type.setter
    def fmt_type(self, fmt_type):
        """Sets the fmt_type of this JobEvent.

        A string representation of the type of the data value.  # noqa: E501

        :param fmt_type: The fmt_type of this JobEvent.  # noqa: E501
        :type: str
        """
        if fmt_type is None:
            raise ValueError("Invalid value for `fmt_type`, must not be `None`")  # noqa: E501

        self._fmt_type = fmt_type

    @property
    def id(self):
        """Gets the id of this JobEvent.  # noqa: E501

        Job event ID.  # noqa: E501

        :return: The id of this JobEvent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobEvent.

        Job event ID.  # noqa: E501

        :param id: The id of this JobEvent.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def job_id(self):
        """Gets the job_id of this JobEvent.  # noqa: E501

        Job ID.  # noqa: E501

        :return: The job_id of this JobEvent.  # noqa: E501
        :rtype: int
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this JobEvent.

        Job ID.  # noqa: E501

        :param job_id: The job_id of this JobEvent.  # noqa: E501
        :type: int
        """
        if job_id is None:
            raise ValueError("Invalid value for `job_id`, must not be `None`")  # noqa: E501
        if job_id is not None and job_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `job_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._job_id = job_id

    @property
    def job_type(self):
        """Gets the job_type of this JobEvent.  # noqa: E501

        Job Type.  # noqa: E501

        :return: The job_type of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this JobEvent.

        Job Type.  # noqa: E501

        :param job_type: The job_type of this JobEvent.  # noqa: E501
        :type: str
        """
        if job_type is None:
            raise ValueError("Invalid value for `job_type`, must not be `None`")  # noqa: E501

        self._job_type = job_type

    @property
    def key(self):
        """Gets the key of this JobEvent.  # noqa: E501

        Event key name.  # noqa: E501

        :return: The key of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this JobEvent.

        Event key name.  # noqa: E501

        :param key: The key of this JobEvent.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def phase(self):
        """Gets the phase of this JobEvent.  # noqa: E501

        Job phase number at time of event.  # noqa: E501

        :return: The phase of this JobEvent.  # noqa: E501
        :rtype: int
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """Sets the phase of this JobEvent.

        Job phase number at time of event.  # noqa: E501

        :param phase: The phase of this JobEvent.  # noqa: E501
        :type: int
        """
        if phase is None:
            raise ValueError("Invalid value for `phase`, must not be `None`")  # noqa: E501

        self._phase = phase

    @property
    def raw_type(self):
        """Gets the raw_type of this JobEvent.  # noqa: E501

        An integer representation of the type of the data value.  # noqa: E501

        :return: The raw_type of this JobEvent.  # noqa: E501
        :rtype: int
        """
        return self._raw_type

    @raw_type.setter
    def raw_type(self, raw_type):
        """Sets the raw_type of this JobEvent.

        An integer representation of the type of the data value.  # noqa: E501

        :param raw_type: The raw_type of this JobEvent.  # noqa: E501
        :type: int
        """
        if raw_type is None:
            raise ValueError("Invalid value for `raw_type`, must not be `None`")  # noqa: E501

        self._raw_type = raw_type

    @property
    def time(self):
        """Gets the time of this JobEvent.  # noqa: E501

        Time of event in Unix epoch seconds.  # noqa: E501

        :return: The time of this JobEvent.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this JobEvent.

        Time of event in Unix epoch seconds.  # noqa: E501

        :param time: The time of this JobEvent.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def value(self):
        """Gets the value of this JobEvent.  # noqa: E501

        Event value.  # noqa: E501

        :return: The value of this JobEvent.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this JobEvent.

        Event value.  # noqa: E501

        :param value: The value of this JobEvent.  # noqa: E501
        :type: str
        """

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
        if not isinstance(other, JobEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
