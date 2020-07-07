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

from isi_sdk_9_0_0.models.timezone_region_timezone import TimezoneRegionTimezone  # noqa: F401,E501


class TimezoneRegion(object):
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
        'comments': 'str',
        'id': 'str',
        'region': 'str',
        'timezone': 'TimezoneRegionTimezone'
    }

    attribute_map = {
        'comments': 'comments',
        'id': 'id',
        'region': 'region',
        'timezone': 'timezone'
    }

    def __init__(self, comments=None, id=None, region=None, timezone=None):  # noqa: E501
        """TimezoneRegion - a model defined in Swagger"""  # noqa: E501

        self._comments = None
        self._id = None
        self._region = None
        self._timezone = None
        self.discriminator = None

        if comments is not None:
            self.comments = comments
        if id is not None:
            self.id = id
        if region is not None:
            self.region = region
        if timezone is not None:
            self.timezone = timezone

    @property
    def comments(self):
        """Gets the comments of this TimezoneRegion.  # noqa: E501

        Clarifying comments on the region or timezone.  # noqa: E501

        :return: The comments of this TimezoneRegion.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this TimezoneRegion.

        Clarifying comments on the region or timezone.  # noqa: E501

        :param comments: The comments of this TimezoneRegion.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def id(self):
        """Gets the id of this TimezoneRegion.  # noqa: E501

        A unique identifier for the timezone region.  # noqa: E501

        :return: The id of this TimezoneRegion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimezoneRegion.

        A unique identifier for the timezone region.  # noqa: E501

        :param id: The id of this TimezoneRegion.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def region(self):
        """Gets the region of this TimezoneRegion.  # noqa: E501

        The name of the region.  # noqa: E501

        :return: The region of this TimezoneRegion.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TimezoneRegion.

        The name of the region.  # noqa: E501

        :param region: The region of this TimezoneRegion.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def timezone(self):
        """Gets the timezone of this TimezoneRegion.  # noqa: E501

        A timezone.  # noqa: E501

        :return: The timezone of this TimezoneRegion.  # noqa: E501
        :rtype: TimezoneRegionTimezone
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this TimezoneRegion.

        A timezone.  # noqa: E501

        :param timezone: The timezone of this TimezoneRegion.  # noqa: E501
        :type: TimezoneRegionTimezone
        """

        self._timezone = timezone

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
        if not isinstance(other, TimezoneRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
