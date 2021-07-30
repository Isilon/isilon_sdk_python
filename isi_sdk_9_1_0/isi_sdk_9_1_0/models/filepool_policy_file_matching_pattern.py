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

from isi_sdk_9_1_0.models.filepool_policy_file_matching_pattern_or_criteria_item import FilepoolPolicyFileMatchingPatternOrCriteriaItem  # noqa: F401,E501


class FilepoolPolicyFileMatchingPattern(object):
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
        'or_criteria': 'list[FilepoolPolicyFileMatchingPatternOrCriteriaItem]'
    }

    attribute_map = {
        'or_criteria': 'or_criteria'
    }

    def __init__(self, or_criteria=None):  # noqa: E501
        """FilepoolPolicyFileMatchingPattern - a model defined in Swagger"""  # noqa: E501

        self._or_criteria = None
        self.discriminator = None

        self.or_criteria = or_criteria

    @property
    def or_criteria(self):
        """Gets the or_criteria of this FilepoolPolicyFileMatchingPattern.  # noqa: E501


        :return: The or_criteria of this FilepoolPolicyFileMatchingPattern.  # noqa: E501
        :rtype: list[FilepoolPolicyFileMatchingPatternOrCriteriaItem]
        """
        return self._or_criteria

    @or_criteria.setter
    def or_criteria(self, or_criteria):
        """Sets the or_criteria of this FilepoolPolicyFileMatchingPattern.


        :param or_criteria: The or_criteria of this FilepoolPolicyFileMatchingPattern.  # noqa: E501
        :type: list[FilepoolPolicyFileMatchingPatternOrCriteriaItem]
        """
        if or_criteria is None:
            raise ValueError("Invalid value for `or_criteria`, must not be `None`")  # noqa: E501

        self._or_criteria = or_criteria

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
        if not isinstance(other, FilepoolPolicyFileMatchingPattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
