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


class HealthcheckItemParameter(object):
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
        'default': 'str',
        'description': 'str',
        'mandatory': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'default': 'default',
        'description': 'description',
        'mandatory': 'mandatory',
        'name': 'name'
    }

    def __init__(self, default=None, description=None, mandatory=None, name=None):  # noqa: E501
        """HealthcheckItemParameter - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._description = None
        self._mandatory = None
        self._name = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if description is not None:
            self.description = description
        if mandatory is not None:
            self.mandatory = mandatory
        if name is not None:
            self.name = name

    @property
    def default(self):
        """Gets the default of this HealthcheckItemParameter.  # noqa: E501

        Default value of parameter  # noqa: E501

        :return: The default of this HealthcheckItemParameter.  # noqa: E501
        :rtype: str
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this HealthcheckItemParameter.

        Default value of parameter  # noqa: E501

        :param default: The default of this HealthcheckItemParameter.  # noqa: E501
        :type: str
        """

        self._default = default

    @property
    def description(self):
        """Gets the description of this HealthcheckItemParameter.  # noqa: E501

        Parameter description including value structure  # noqa: E501

        :return: The description of this HealthcheckItemParameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this HealthcheckItemParameter.

        Parameter description including value structure  # noqa: E501

        :param description: The description of this HealthcheckItemParameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mandatory(self):
        """Gets the mandatory of this HealthcheckItemParameter.  # noqa: E501

        True if parameter must be supplied  # noqa: E501

        :return: The mandatory of this HealthcheckItemParameter.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this HealthcheckItemParameter.

        True if parameter must be supplied  # noqa: E501

        :param mandatory: The mandatory of this HealthcheckItemParameter.  # noqa: E501
        :type: bool
        """

        self._mandatory = mandatory

    @property
    def name(self):
        """Gets the name of this HealthcheckItemParameter.  # noqa: E501

        Parameter name  # noqa: E501

        :return: The name of this HealthcheckItemParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HealthcheckItemParameter.

        Parameter name  # noqa: E501

        :param name: The name of this HealthcheckItemParameter.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if not isinstance(other, HealthcheckItemParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
