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


class CatalogReadme(object):
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
        'readme': 'str'
    }

    attribute_map = {
        'readme': 'readme'
    }

    def __init__(self, readme=None):  # noqa: E501
        """CatalogReadme - a model defined in Swagger"""  # noqa: E501

        self._readme = None
        self.discriminator = None

        self.readme = readme

    @property
    def readme(self):
        """Gets the readme of this CatalogReadme.  # noqa: E501

        The README of the file stored in catalog  # noqa: E501

        :return: The readme of this CatalogReadme.  # noqa: E501
        :rtype: str
        """
        return self._readme

    @readme.setter
    def readme(self, readme):
        """Sets the readme of this CatalogReadme.

        The README of the file stored in catalog  # noqa: E501

        :param readme: The readme of this CatalogReadme.  # noqa: E501
        :type: str
        """
        if readme is None:
            raise ValueError("Invalid value for `readme`, must not be `None`")  # noqa: E501
        if readme is not None and len(readme) > 8192:
            raise ValueError("Invalid value for `readme`, length must be less than or equal to `8192`")  # noqa: E501
        if readme is not None and len(readme) < 0:
            raise ValueError("Invalid value for `readme`, length must be greater than or equal to `0`")  # noqa: E501

        self._readme = readme

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
        if not isinstance(other, CatalogReadme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other