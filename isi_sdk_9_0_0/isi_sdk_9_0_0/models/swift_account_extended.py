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


class SwiftAccountExtended(object):
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
        'id': 'str',
        'name': 'str',
        'path': 'str',
        'swiftgroup': 'str',
        'swiftuser': 'str',
        'users': 'list[str]',
        'zone': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'path': 'path',
        'swiftgroup': 'swiftgroup',
        'swiftuser': 'swiftuser',
        'users': 'users',
        'zone': 'zone'
    }

    def __init__(self, id=None, name=None, path=None, swiftgroup=None, swiftuser=None, users=None, zone=None):  # noqa: E501
        """SwiftAccountExtended - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._path = None
        self._swiftgroup = None
        self._swiftuser = None
        self._users = None
        self._zone = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if swiftgroup is not None:
            self.swiftgroup = swiftgroup
        if swiftuser is not None:
            self.swiftuser = swiftuser
        if users is not None:
            self.users = users
        if zone is not None:
            self.zone = zone

    @property
    def id(self):
        """Gets the id of this SwiftAccountExtended.  # noqa: E501

        Unique id of swift account  # noqa: E501

        :return: The id of this SwiftAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SwiftAccountExtended.

        Unique id of swift account  # noqa: E501

        :param id: The id of this SwiftAccountExtended.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SwiftAccountExtended.  # noqa: E501

        Name of Swift account  # noqa: E501

        :return: The name of this SwiftAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SwiftAccountExtended.

        Name of Swift account  # noqa: E501

        :param name: The name of this SwiftAccountExtended.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """Gets the path of this SwiftAccountExtended.  # noqa: E501

        Path to root of Swift account  # noqa: E501

        :return: The path of this SwiftAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SwiftAccountExtended.

        Path to root of Swift account  # noqa: E501

        :param path: The path of this SwiftAccountExtended.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def swiftgroup(self):
        """Gets the swiftgroup of this SwiftAccountExtended.  # noqa: E501

        Group with filesystem ownership of this account  # noqa: E501

        :return: The swiftgroup of this SwiftAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._swiftgroup

    @swiftgroup.setter
    def swiftgroup(self, swiftgroup):
        """Sets the swiftgroup of this SwiftAccountExtended.

        Group with filesystem ownership of this account  # noqa: E501

        :param swiftgroup: The swiftgroup of this SwiftAccountExtended.  # noqa: E501
        :type: str
        """

        self._swiftgroup = swiftgroup

    @property
    def swiftuser(self):
        """Gets the swiftuser of this SwiftAccountExtended.  # noqa: E501

        User with filesystem ownership of this account  # noqa: E501

        :return: The swiftuser of this SwiftAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._swiftuser

    @swiftuser.setter
    def swiftuser(self, swiftuser):
        """Sets the swiftuser of this SwiftAccountExtended.

        User with filesystem ownership of this account  # noqa: E501

        :param swiftuser: The swiftuser of this SwiftAccountExtended.  # noqa: E501
        :type: str
        """

        self._swiftuser = swiftuser

    @property
    def users(self):
        """Gets the users of this SwiftAccountExtended.  # noqa: E501

        Users who are allowed to access Swift account  # noqa: E501

        :return: The users of this SwiftAccountExtended.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this SwiftAccountExtended.

        Users who are allowed to access Swift account  # noqa: E501

        :param users: The users of this SwiftAccountExtended.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def zone(self):
        """Gets the zone of this SwiftAccountExtended.  # noqa: E501

        Name of access zone for account  # noqa: E501

        :return: The zone of this SwiftAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._zone

    @zone.setter
    def zone(self, zone):
        """Sets the zone of this SwiftAccountExtended.

        Name of access zone for account  # noqa: E501

        :param zone: The zone of this SwiftAccountExtended.  # noqa: E501
        :type: str
        """

        self._zone = zone

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
        if not isinstance(other, SwiftAccountExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
