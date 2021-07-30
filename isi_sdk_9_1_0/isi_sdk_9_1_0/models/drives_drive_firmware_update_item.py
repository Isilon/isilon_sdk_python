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


class DrivesDriveFirmwareUpdateItem(object):
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
        'cluster_wide': 'bool'
    }

    attribute_map = {
        'cluster_wide': 'cluster_wide'
    }

    def __init__(self, cluster_wide=None):  # noqa: E501
        """DrivesDriveFirmwareUpdateItem - a model defined in Swagger"""  # noqa: E501

        self._cluster_wide = None
        self.discriminator = None

        self.cluster_wide = cluster_wide

    @property
    def cluster_wide(self):
        """Gets the cluster_wide of this DrivesDriveFirmwareUpdateItem.  # noqa: E501

        Indicates whether this is a cluster wide drive firmware update or not  # noqa: E501

        :return: The cluster_wide of this DrivesDriveFirmwareUpdateItem.  # noqa: E501
        :rtype: bool
        """
        return self._cluster_wide

    @cluster_wide.setter
    def cluster_wide(self, cluster_wide):
        """Sets the cluster_wide of this DrivesDriveFirmwareUpdateItem.

        Indicates whether this is a cluster wide drive firmware update or not  # noqa: E501

        :param cluster_wide: The cluster_wide of this DrivesDriveFirmwareUpdateItem.  # noqa: E501
        :type: bool
        """
        if cluster_wide is None:
            raise ValueError("Invalid value for `cluster_wide`, must not be `None`")  # noqa: E501

        self._cluster_wide = cluster_wide

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
        if not isinstance(other, DrivesDriveFirmwareUpdateItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
