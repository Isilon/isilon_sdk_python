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


class JobJobFilepolicyParams(object):
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
        'directory_only': 'bool',
        'nop': 'bool',
        'policy_only': 'bool'
    }

    attribute_map = {
        'directory_only': 'directory_only',
        'nop': 'nop',
        'policy_only': 'policy_only'
    }

    def __init__(self, directory_only=None, nop=None, policy_only=None):  # noqa: E501
        """JobJobFilepolicyParams - a model defined in Swagger"""  # noqa: E501

        self._directory_only = None
        self._nop = None
        self._policy_only = None
        self.discriminator = None

        if directory_only is not None:
            self.directory_only = directory_only
        if nop is not None:
            self.nop = nop
        if policy_only is not None:
            self.policy_only = policy_only

    @property
    def directory_only(self):
        """Gets the directory_only of this JobJobFilepolicyParams.  # noqa: E501

        Skip processing of regular files.  # noqa: E501

        :return: The directory_only of this JobJobFilepolicyParams.  # noqa: E501
        :rtype: bool
        """
        return self._directory_only

    @directory_only.setter
    def directory_only(self, directory_only):
        """Sets the directory_only of this JobJobFilepolicyParams.

        Skip processing of regular files.  # noqa: E501

        :param directory_only: The directory_only of this JobJobFilepolicyParams.  # noqa: E501
        :type: bool
        """

        self._directory_only = directory_only

    @property
    def nop(self):
        """Gets the nop of this JobJobFilepolicyParams.  # noqa: E501

        Calculate what would be done (dry run).  # noqa: E501

        :return: The nop of this JobJobFilepolicyParams.  # noqa: E501
        :rtype: bool
        """
        return self._nop

    @nop.setter
    def nop(self, nop):
        """Sets the nop of this JobJobFilepolicyParams.

        Calculate what would be done (dry run).  # noqa: E501

        :param nop: The nop of this JobJobFilepolicyParams.  # noqa: E501
        :type: bool
        """

        self._nop = nop

    @property
    def policy_only(self):
        """Gets the policy_only of this JobJobFilepolicyParams.  # noqa: E501

        Apply policies but skip restriping.  # noqa: E501

        :return: The policy_only of this JobJobFilepolicyParams.  # noqa: E501
        :rtype: bool
        """
        return self._policy_only

    @policy_only.setter
    def policy_only(self, policy_only):
        """Sets the policy_only of this JobJobFilepolicyParams.

        Apply policies but skip restriping.  # noqa: E501

        :param policy_only: The policy_only of this JobJobFilepolicyParams.  # noqa: E501
        :type: bool
        """

        self._policy_only = policy_only

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
        if not isinstance(other, JobJobFilepolicyParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
