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


class CertificateServerCertificateFingerprint(object):
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
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None):  # noqa: E501
        """CertificateServerCertificateFingerprint - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._value = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value

    @property
    def type(self):
        """Gets the type of this CertificateServerCertificateFingerprint.  # noqa: E501

        Fingerprint hash algorithm  # noqa: E501

        :return: The type of this CertificateServerCertificateFingerprint.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CertificateServerCertificateFingerprint.

        Fingerprint hash algorithm  # noqa: E501

        :param type: The type of this CertificateServerCertificateFingerprint.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) > 100:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `100`")  # noqa: E501
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this CertificateServerCertificateFingerprint.  # noqa: E501

        Fingerprint value  # noqa: E501

        :return: The value of this CertificateServerCertificateFingerprint.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CertificateServerCertificateFingerprint.

        Fingerprint value  # noqa: E501

        :param value: The value of this CertificateServerCertificateFingerprint.  # noqa: E501
        :type: str
        """
        if value is not None and len(value) > 512:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `512`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

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
        if not isinstance(other, CertificateServerCertificateFingerprint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
