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

from isi_sdk_9_0_0.models.auth_access_access_item_share_share_permissions_share_relevant_ace import AuthAccessAccessItemShareSharePermissionsShareRelevantAce  # noqa: F401,E501


class AuthAccessAccessItemFileFilePermissions(object):
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
        'delete_child': 'bool',
        'expected': 'str',
        'mode': 'str',
        'ownership': 'bool',
        'relevant_aces': 'list[AuthAccessAccessItemShareSharePermissionsShareRelevantAce]',
        'relevant_mode': 'str',
        'sticky': 'bool'
    }

    attribute_map = {
        'delete_child': 'delete_child',
        'expected': 'expected',
        'mode': 'mode',
        'ownership': 'ownership',
        'relevant_aces': 'relevant_aces',
        'relevant_mode': 'relevant_mode',
        'sticky': 'sticky'
    }

    def __init__(self, delete_child=None, expected=None, mode=None, ownership=None, relevant_aces=None, relevant_mode=None, sticky=None):  # noqa: E501
        """AuthAccessAccessItemFileFilePermissions - a model defined in Swagger"""  # noqa: E501

        self._delete_child = None
        self._expected = None
        self._mode = None
        self._ownership = None
        self._relevant_aces = None
        self._relevant_mode = None
        self._sticky = None
        self.discriminator = None

        if delete_child is not None:
            self.delete_child = delete_child
        if expected is not None:
            self.expected = expected
        if mode is not None:
            self.mode = mode
        if ownership is not None:
            self.ownership = ownership
        if relevant_aces is not None:
            self.relevant_aces = relevant_aces
        if relevant_mode is not None:
            self.relevant_mode = relevant_mode
        if sticky is not None:
            self.sticky = sticky

    @property
    def delete_child(self):
        """Gets the delete_child of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501

        Specifies if the parent directory has the delete_child property set for the user.  If the delete_child property is set for a user, that user is able to delete the file.  # noqa: E501

        :return: The delete_child of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._delete_child

    @delete_child.setter
    def delete_child(self, delete_child):
        """Sets the delete_child of this AuthAccessAccessItemFileFilePermissions.

        Specifies if the parent directory has the delete_child property set for the user.  If the delete_child property is set for a user, that user is able to delete the file.  # noqa: E501

        :param delete_child: The delete_child of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :type: bool
        """

        self._delete_child = delete_child

    @property
    def expected(self):
        """Gets the expected of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501

        Specifies the expected access rights for the user on the file.  # noqa: E501

        :return: The expected of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :rtype: str
        """
        return self._expected

    @expected.setter
    def expected(self, expected):
        """Sets the expected of this AuthAccessAccessItemFileFilePermissions.

        Specifies the expected access rights for the user on the file.  # noqa: E501

        :param expected: The expected of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :type: str
        """
        if expected is not None and len(expected) > 255:
            raise ValueError("Invalid value for `expected`, length must be less than or equal to `255`")  # noqa: E501
        if expected is not None and len(expected) < 0:
            raise ValueError("Invalid value for `expected`, length must be greater than or equal to `0`")  # noqa: E501

        self._expected = expected

    @property
    def mode(self):
        """Gets the mode of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501

        Specifies the mode bits on the file.  # noqa: E501

        :return: The mode of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this AuthAccessAccessItemFileFilePermissions.

        Specifies the mode bits on the file.  # noqa: E501

        :param mode: The mode of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :type: str
        """
        if mode is not None and len(mode) > 255:
            raise ValueError("Invalid value for `mode`, length must be less than or equal to `255`")  # noqa: E501
        if mode is not None and len(mode) < 0:
            raise ValueError("Invalid value for `mode`, length must be greater than or equal to `0`")  # noqa: E501

        self._mode = mode

    @property
    def ownership(self):
        """Gets the ownership of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501

        True if the user owns the file.  # noqa: E501

        :return: The ownership of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        """Sets the ownership of this AuthAccessAccessItemFileFilePermissions.

        True if the user owns the file.  # noqa: E501

        :param ownership: The ownership of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :type: bool
        """

        self._ownership = ownership

    @property
    def relevant_aces(self):
        """Gets the relevant_aces of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501

        Specifies a list of the relevant Access Control Entrieswith respect to the user in the share.  # noqa: E501

        :return: The relevant_aces of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :rtype: list[AuthAccessAccessItemShareSharePermissionsShareRelevantAce]
        """
        return self._relevant_aces

    @relevant_aces.setter
    def relevant_aces(self, relevant_aces):
        """Sets the relevant_aces of this AuthAccessAccessItemFileFilePermissions.

        Specifies a list of the relevant Access Control Entrieswith respect to the user in the share.  # noqa: E501

        :param relevant_aces: The relevant_aces of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :type: list[AuthAccessAccessItemShareSharePermissionsShareRelevantAce]
        """

        self._relevant_aces = relevant_aces

    @property
    def relevant_mode(self):
        """Gets the relevant_mode of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501

        Specifies the mode bits that are related to the user.  # noqa: E501

        :return: The relevant_mode of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :rtype: str
        """
        return self._relevant_mode

    @relevant_mode.setter
    def relevant_mode(self, relevant_mode):
        """Sets the relevant_mode of this AuthAccessAccessItemFileFilePermissions.

        Specifies the mode bits that are related to the user.  # noqa: E501

        :param relevant_mode: The relevant_mode of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :type: str
        """
        if relevant_mode is not None and len(relevant_mode) > 255:
            raise ValueError("Invalid value for `relevant_mode`, length must be less than or equal to `255`")  # noqa: E501
        if relevant_mode is not None and len(relevant_mode) < 0:
            raise ValueError("Invalid value for `relevant_mode`, length must be greater than or equal to `0`")  # noqa: E501

        self._relevant_mode = relevant_mode

    @property
    def sticky(self):
        """Gets the sticky of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501

        Specifies if the parent directory has the sticky bit property set indicating only the file's owner may delete the file.  # noqa: E501

        :return: The sticky of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :rtype: bool
        """
        return self._sticky

    @sticky.setter
    def sticky(self, sticky):
        """Sets the sticky of this AuthAccessAccessItemFileFilePermissions.

        Specifies if the parent directory has the sticky bit property set indicating only the file's owner may delete the file.  # noqa: E501

        :param sticky: The sticky of this AuthAccessAccessItemFileFilePermissions.  # noqa: E501
        :type: bool
        """

        self._sticky = sticky

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
        if not isinstance(other, AuthAccessAccessItemFileFilePermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
