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


class ConfigUserUser(object):
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
        'id': 'int',
        'password': 'str',
        'username': 'str'
    }

    attribute_map = {
        'id': 'id',
        'password': 'password',
        'username': 'username'
    }

    def __init__(self, id=None, password=None, username=None):  # noqa: E501
        """ConfigUserUser - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._password = None
        self._username = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if password is not None:
            self.password = password
        if username is not None:
            self.username = username

    @property
    def id(self):
        """Gets the id of this ConfigUserUser.  # noqa: E501

        The numeric User ID associated with the username.  # noqa: E501

        :return: The id of this ConfigUserUser.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConfigUserUser.

        The numeric User ID associated with the username.  # noqa: E501

        :param id: The id of this ConfigUserUser.  # noqa: E501
        :type: int
        """
        if id is not None and id > 16:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `16`")  # noqa: E501
        if id is not None and id < 3:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `3`")  # noqa: E501

        self._id = id

    @property
    def password(self):
        """Gets the password of this ConfigUserUser.  # noqa: E501

        Represents the password that customers will use with the IPMI username when authenticating remote IPMI requests.  # noqa: E501

        :return: The password of this ConfigUserUser.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ConfigUserUser.

        Represents the password that customers will use with the IPMI username when authenticating remote IPMI requests.  # noqa: E501

        :param password: The password of this ConfigUserUser.  # noqa: E501
        :type: str
        """
        if password is not None and len(password) > 20:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `20`")  # noqa: E501
        if password is not None and len(password) < 16:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `16`")  # noqa: E501

        self._password = password

    @property
    def username(self):
        """Gets the username of this ConfigUserUser.  # noqa: E501

        Represents the username that customers will use when authenticating remote IPMI requests.  # noqa: E501

        :return: The username of this ConfigUserUser.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ConfigUserUser.

        Represents the username that customers will use when authenticating remote IPMI requests.  # noqa: E501

        :param username: The username of this ConfigUserUser.  # noqa: E501
        :type: str
        """
        if username is not None and len(username) > 16:
            raise ValueError("Invalid value for `username`, length must be less than or equal to `16`")  # noqa: E501
        if username is not None and len(username) < 1:
            raise ValueError("Invalid value for `username`, length must be greater than or equal to `1`")  # noqa: E501

        self._username = username

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
        if not isinstance(other, ConfigUserUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
