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


class IdResolutionZone(object):
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
        'zone_id': 'int',
        'zone_name': 'str'
    }

    attribute_map = {
        'zone_id': 'zone_id',
        'zone_name': 'zone_name'
    }

    def __init__(self, zone_id=None, zone_name=None):  # noqa: E501
        """IdResolutionZone - a model defined in Swagger"""  # noqa: E501

        self._zone_id = None
        self._zone_name = None
        self.discriminator = None

        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def zone_id(self):
        """Gets the zone_id of this IdResolutionZone.  # noqa: E501

        Zone ID.  # noqa: E501

        :return: The zone_id of this IdResolutionZone.  # noqa: E501
        :rtype: int
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this IdResolutionZone.

        Zone ID.  # noqa: E501

        :param zone_id: The zone_id of this IdResolutionZone.  # noqa: E501
        :type: int
        """
        if zone_id is not None and zone_id > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `zone_id`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if zone_id is not None and zone_id < 0:  # noqa: E501
            raise ValueError("Invalid value for `zone_id`, must be a value greater than or equal to `0`")  # noqa: E501

        self._zone_id = zone_id

    @property
    def zone_name(self):
        """Gets the zone_name of this IdResolutionZone.  # noqa: E501

        The zone name.  # noqa: E501

        :return: The zone_name of this IdResolutionZone.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this IdResolutionZone.

        The zone name.  # noqa: E501

        :param zone_name: The zone_name of this IdResolutionZone.  # noqa: E501
        :type: str
        """
        if zone_name is not None and len(zone_name) > 255:
            raise ValueError("Invalid value for `zone_name`, length must be less than or equal to `255`")  # noqa: E501
        if zone_name is not None and len(zone_name) < 0:
            raise ValueError("Invalid value for `zone_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._zone_name = zone_name

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
        if not isinstance(other, IdResolutionZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
