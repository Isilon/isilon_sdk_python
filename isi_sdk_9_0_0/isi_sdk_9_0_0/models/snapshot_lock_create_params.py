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

from isi_sdk_9_0_0.models.snapshot_lock import SnapshotLock  # noqa: F401,E501


class SnapshotLockCreateParams(object):
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
        'expires': 'int',
        'comment': 'str'
    }

    attribute_map = {
        'expires': 'expires',
        'comment': 'comment'
    }

    def __init__(self, expires=None, comment=None):  # noqa: E501
        """SnapshotLockCreateParams - a model defined in Swagger"""  # noqa: E501

        self._expires = None
        self._comment = None
        self.discriminator = None

        if expires is not None:
            self.expires = expires
        if comment is not None:
            self.comment = comment

    @property
    def expires(self):
        """Gets the expires of this SnapshotLockCreateParams.  # noqa: E501

        The Unix Epoch time the snapshot lock will expire and be eligible for automatic deletion.  # noqa: E501

        :return: The expires of this SnapshotLockCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this SnapshotLockCreateParams.

        The Unix Epoch time the snapshot lock will expire and be eligible for automatic deletion.  # noqa: E501

        :param expires: The expires of this SnapshotLockCreateParams.  # noqa: E501
        :type: int
        """
        if expires is not None and expires > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `expires`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if expires is not None and expires < 1:  # noqa: E501
            raise ValueError("Invalid value for `expires`, must be a value greater than or equal to `1`")  # noqa: E501

        self._expires = expires

    @property
    def comment(self):
        """Gets the comment of this SnapshotLockCreateParams.  # noqa: E501

        Free form comment.  # noqa: E501

        :return: The comment of this SnapshotLockCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this SnapshotLockCreateParams.

        Free form comment.  # noqa: E501

        :param comment: The comment of this SnapshotLockCreateParams.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if not isinstance(other, SnapshotLockCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
