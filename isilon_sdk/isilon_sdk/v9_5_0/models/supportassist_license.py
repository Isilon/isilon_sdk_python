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

from isilon_sdk.v9_5_0.models.supportassist_license_task import SupportassistLicenseTask  # noqa: F401,E501


class SupportassistLicense(object):
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
        'task': 'SupportassistLicenseTask',
        'warning': 'str'
    }

    attribute_map = {
        'task': 'task',
        'warning': 'warning'
    }

    def __init__(self, task=None, warning=None):  # noqa: E501
        """SupportassistLicense - a model defined in Swagger"""  # noqa: E501

        self._task = None
        self._warning = None
        self.discriminator = None

        if task is not None:
            self.task = task
        if warning is not None:
            self.warning = warning

    @property
    def task(self):
        """Gets the task of this SupportassistLicense.  # noqa: E501

          # noqa: E501

        :return: The task of this SupportassistLicense.  # noqa: E501
        :rtype: SupportassistLicenseTask
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this SupportassistLicense.

          # noqa: E501

        :param task: The task of this SupportassistLicense.  # noqa: E501
        :type: SupportassistLicenseTask
        """

        self._task = task

    @property
    def warning(self):
        """Gets the warning of this SupportassistLicense.  # noqa: E501

        Error message when license not found  # noqa: E501

        :return: The warning of this SupportassistLicense.  # noqa: E501
        :rtype: str
        """
        return self._warning

    @warning.setter
    def warning(self, warning):
        """Sets the warning of this SupportassistLicense.

        Error message when license not found  # noqa: E501

        :param warning: The warning of this SupportassistLicense.  # noqa: E501
        :type: str
        """
        if warning is not None and len(warning) > 255:
            raise ValueError("Invalid value for `warning`, length must be less than or equal to `255`")  # noqa: E501
        if warning is not None and len(warning) < 0:
            raise ValueError("Invalid value for `warning`, length must be greater than or equal to `0`")  # noqa: E501

        self._warning = warning

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
        if not isinstance(other, SupportassistLicense):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other