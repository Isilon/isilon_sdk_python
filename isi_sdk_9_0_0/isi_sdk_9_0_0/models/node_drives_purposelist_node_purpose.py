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


class NodeDrivesPurposelistNodePurpose(object):
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
        'purpose': 'str',
        'purpose_description': 'str'
    }

    attribute_map = {
        'purpose': 'purpose',
        'purpose_description': 'purpose_description'
    }

    def __init__(self, purpose=None, purpose_description=None):  # noqa: E501
        """NodeDrivesPurposelistNodePurpose - a model defined in Swagger"""  # noqa: E501

        self._purpose = None
        self._purpose_description = None
        self.discriminator = None

        if purpose is not None:
            self.purpose = purpose
        if purpose_description is not None:
            self.purpose_description = purpose_description

    @property
    def purpose(self):
        """Gets the purpose of this NodeDrivesPurposelistNodePurpose.  # noqa: E501

        String representation of this purpose for API use.  # noqa: E501

        :return: The purpose of this NodeDrivesPurposelistNodePurpose.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this NodeDrivesPurposelistNodePurpose.

        String representation of this purpose for API use.  # noqa: E501

        :param purpose: The purpose of this NodeDrivesPurposelistNodePurpose.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def purpose_description(self):
        """Gets the purpose_description of this NodeDrivesPurposelistNodePurpose.  # noqa: E501

        A description of this purpose.  # noqa: E501

        :return: The purpose_description of this NodeDrivesPurposelistNodePurpose.  # noqa: E501
        :rtype: str
        """
        return self._purpose_description

    @purpose_description.setter
    def purpose_description(self, purpose_description):
        """Sets the purpose_description of this NodeDrivesPurposelistNodePurpose.

        A description of this purpose.  # noqa: E501

        :param purpose_description: The purpose_description of this NodeDrivesPurposelistNodePurpose.  # noqa: E501
        :type: str
        """

        self._purpose_description = purpose_description

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
        if not isinstance(other, NodeDrivesPurposelistNodePurpose):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
