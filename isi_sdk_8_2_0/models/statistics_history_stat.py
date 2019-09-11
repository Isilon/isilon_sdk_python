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

from isi_sdk_8_2_0.models.statistics_history_stat_value import StatisticsHistoryStatValue  # noqa: F401,E501


class StatisticsHistoryStat(object):
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
        'devid': 'int',
        'error': 'str',
        'error_code': 'int',
        'key': 'str',
        'resolution': 'int',
        'values': 'list[StatisticsHistoryStatValue]'
    }

    attribute_map = {
        'devid': 'devid',
        'error': 'error',
        'error_code': 'error_code',
        'key': 'key',
        'resolution': 'resolution',
        'values': 'values'
    }

    def __init__(self, devid=None, error=None, error_code=None, key=None, resolution=None, values=None):  # noqa: E501
        """StatisticsHistoryStat - a model defined in Swagger"""  # noqa: E501

        self._devid = None
        self._error = None
        self._error_code = None
        self._key = None
        self._resolution = None
        self._values = None
        self.discriminator = None

        self.devid = devid
        if error is not None:
            self.error = error
        if error_code is not None:
            self.error_code = error_code
        self.key = key
        self.resolution = resolution
        if values is not None:
            self.values = values

    @property
    def devid(self):
        """Gets the devid of this StatisticsHistoryStat.  # noqa: E501

        Devid of node of statistic or 0 for cluster scoped statistics.  # noqa: E501

        :return: The devid of this StatisticsHistoryStat.  # noqa: E501
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """Sets the devid of this StatisticsHistoryStat.

        Devid of node of statistic or 0 for cluster scoped statistics.  # noqa: E501

        :param devid: The devid of this StatisticsHistoryStat.  # noqa: E501
        :type: int
        """
        if devid is None:
            raise ValueError("Invalid value for `devid`, must not be `None`")  # noqa: E501

        self._devid = devid

    @property
    def error(self):
        """Gets the error of this StatisticsHistoryStat.  # noqa: E501

        Key specific error string, if applicable.  # noqa: E501

        :return: The error of this StatisticsHistoryStat.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this StatisticsHistoryStat.

        Key specific error string, if applicable.  # noqa: E501

        :param error: The error of this StatisticsHistoryStat.  # noqa: E501
        :type: str
        """

        self._error = error

    @property
    def error_code(self):
        """Gets the error_code of this StatisticsHistoryStat.  # noqa: E501

        Key specific error number, if applicable.  # noqa: E501

        :return: The error_code of this StatisticsHistoryStat.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this StatisticsHistoryStat.

        Key specific error number, if applicable.  # noqa: E501

        :param error_code: The error_code of this StatisticsHistoryStat.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def key(self):
        """Gets the key of this StatisticsHistoryStat.  # noqa: E501

        Key name of statistic.  # noqa: E501

        :return: The key of this StatisticsHistoryStat.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this StatisticsHistoryStat.

        Key name of statistic.  # noqa: E501

        :param key: The key of this StatisticsHistoryStat.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def resolution(self):
        """Gets the resolution of this StatisticsHistoryStat.  # noqa: E501

        The interval for which these results were figured (averaged against.)  # noqa: E501

        :return: The resolution of this StatisticsHistoryStat.  # noqa: E501
        :rtype: int
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this StatisticsHistoryStat.

        The interval for which these results were figured (averaged against.)  # noqa: E501

        :param resolution: The resolution of this StatisticsHistoryStat.  # noqa: E501
        :type: int
        """
        if resolution is None:
            raise ValueError("Invalid value for `resolution`, must not be `None`")  # noqa: E501

        self._resolution = resolution

    @property
    def values(self):
        """Gets the values of this StatisticsHistoryStat.  # noqa: E501

        Time-series values.  # noqa: E501

        :return: The values of this StatisticsHistoryStat.  # noqa: E501
        :rtype: list[StatisticsHistoryStatValue]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this StatisticsHistoryStat.

        Time-series values.  # noqa: E501

        :param values: The values of this StatisticsHistoryStat.  # noqa: E501
        :type: list[StatisticsHistoryStatValue]
        """

        self._values = values

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
        if not isinstance(other, StatisticsHistoryStat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
