# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 12
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_2_1.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isilon_sdk.v9_2_1.models.auth_group import AuthGroup  # noqa: F401,E501


class AuthGroupCreateParams(object):
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
        'gid': 'int',
        'members': 'list[AuthAccessAccessItemFileGroup]',
        'name': 'str',
        'sid': 'str'
    }

    attribute_map = {
        'gid': 'gid',
        'members': 'members',
        'name': 'name',
        'sid': 'sid'
    }

    def __init__(self, gid=None, members=None, name=None, sid=None):  # noqa: E501
        """AuthGroupCreateParams - a model defined in Swagger"""  # noqa: E501

        self._gid = None
        self._members = None
        self._name = None
        self._sid = None
        self.discriminator = None

        if gid is not None:
            self.gid = gid
        if members is not None:
            self.members = members
        self.name = name
        if sid is not None:
            self.sid = sid

    @property
    def gid(self):
        """Gets the gid of this AuthGroupCreateParams.  # noqa: E501

        Specifies the numeric group identifier.  # noqa: E501

        :return: The gid of this AuthGroupCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this AuthGroupCreateParams.

        Specifies the numeric group identifier.  # noqa: E501

        :param gid: The gid of this AuthGroupCreateParams.  # noqa: E501
        :type: int
        """
        if gid is not None and gid > 4294967295:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must be a value less than or equal to `4294967295`")  # noqa: E501
        if gid is not None and gid < 0:  # noqa: E501
            raise ValueError("Invalid value for `gid`, must be a value greater than or equal to `0`")  # noqa: E501

        self._gid = gid

    @property
    def members(self):
        """Gets the members of this AuthGroupCreateParams.  # noqa: E501

        Specifies the members of the group.  # noqa: E501

        :return: The members of this AuthGroupCreateParams.  # noqa: E501
        :rtype: list[AuthAccessAccessItemFileGroup]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this AuthGroupCreateParams.

        Specifies the members of the group.  # noqa: E501

        :param members: The members of this AuthGroupCreateParams.  # noqa: E501
        :type: list[AuthAccessAccessItemFileGroup]
        """

        self._members = members

    @property
    def name(self):
        """Gets the name of this AuthGroupCreateParams.  # noqa: E501

        Specifies the group name.  # noqa: E501

        :return: The name of this AuthGroupCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthGroupCreateParams.

        Specifies the group name.  # noqa: E501

        :param name: The name of this AuthGroupCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def sid(self):
        """Gets the sid of this AuthGroupCreateParams.  # noqa: E501

        Specifies the security identifier.  # noqa: E501

        :return: The sid of this AuthGroupCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this AuthGroupCreateParams.

        Specifies the security identifier.  # noqa: E501

        :param sid: The sid of this AuthGroupCreateParams.  # noqa: E501
        :type: str
        """
        if sid is not None and len(sid) > 255:
            raise ValueError("Invalid value for `sid`, length must be less than or equal to `255`")  # noqa: E501
        if sid is not None and len(sid) < 0:
            raise ValueError("Invalid value for `sid`, length must be greater than or equal to `0`")  # noqa: E501

        self._sid = sid

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
        if not isinstance(other, AuthGroupCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
