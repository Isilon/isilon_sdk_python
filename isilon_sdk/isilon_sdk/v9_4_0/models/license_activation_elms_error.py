# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LicenseActivationElmsError(object):
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
        'code': 'str',
        'error': 'str'
    }

    attribute_map = {
        'code': 'code',
        'error': 'error'
    }

    def __init__(self, code=None, error=None):  # noqa: E501
        """LicenseActivationElmsError - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._error = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if error is not None:
            self.error = error

    @property
    def code(self):
        """Gets the code of this LicenseActivationElmsError.  # noqa: E501

        An error code corresponding to an error returned from the SRS ELMS rest call.  # noqa: E501

        :return: The code of this LicenseActivationElmsError.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LicenseActivationElmsError.

        An error code corresponding to an error returned from the SRS ELMS rest call.  # noqa: E501

        :param code: The code of this LicenseActivationElmsError.  # noqa: E501
        :type: str
        """
        if code is not None and len(code) > 50:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `50`")  # noqa: E501
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def error(self):
        """Gets the error of this LicenseActivationElmsError.  # noqa: E501

        An error string retured from the SRS ELMS rest call  # noqa: E501

        :return: The error of this LicenseActivationElmsError.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this LicenseActivationElmsError.

        An error string retured from the SRS ELMS rest call  # noqa: E501

        :param error: The error of this LicenseActivationElmsError.  # noqa: E501
        :type: str
        """
        if error is not None and len(error) > 50:
            raise ValueError("Invalid value for `error`, length must be less than or equal to `50`")  # noqa: E501
        if error is not None and len(error) < 1:
            raise ValueError("Invalid value for `error`, length must be greater than or equal to `1`")  # noqa: E501

        self._error = error

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
        if not isinstance(other, LicenseActivationElmsError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other