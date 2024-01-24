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

from isilon_sdk.v9_1_0.models.auth_access_access_item_file_group import AuthAccessAccessItemFileGroup  # noqa: F401,E501
from isilon_sdk.v9_1_0.models.mapping_identity_target import MappingIdentityTarget  # noqa: F401,E501


class MappingIdentity(object):
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
        'source': 'AuthAccessAccessItemFileGroup',
        'targets': 'list[MappingIdentityTarget]'
    }

    attribute_map = {
        'id': 'id',
        'source': 'source',
        'targets': 'targets'
    }

    def __init__(self, id=None, source=None, targets=None):  # noqa: E501
        """MappingIdentity - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._source = None
        self._targets = None
        self.discriminator = None

        self.id = id
        if source is not None:
            self.source = source
        self.targets = targets

    @property
    def id(self):
        """Gets the id of this MappingIdentity.  # noqa: E501

        Specifies the identity mapping entry id.  # noqa: E501

        :return: The id of this MappingIdentity.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MappingIdentity.

        Specifies the identity mapping entry id.  # noqa: E501

        :param id: The id of this MappingIdentity.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def source(self):
        """Gets the source of this MappingIdentity.  # noqa: E501

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :return: The source of this MappingIdentity.  # noqa: E501
        :rtype: AuthAccessAccessItemFileGroup
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this MappingIdentity.

        Specifies properties for a persona, which consists of either a 'type' and a 'name' or an 'ID'.  # noqa: E501

        :param source: The source of this MappingIdentity.  # noqa: E501
        :type: AuthAccessAccessItemFileGroup
        """

        self._source = source

    @property
    def targets(self):
        """Gets the targets of this MappingIdentity.  # noqa: E501


        :return: The targets of this MappingIdentity.  # noqa: E501
        :rtype: list[MappingIdentityTarget]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        """Sets the targets of this MappingIdentity.


        :param targets: The targets of this MappingIdentity.  # noqa: E501
        :type: list[MappingIdentityTarget]
        """
        if targets is None:
            raise ValueError("Invalid value for `targets`, must not be `None`")  # noqa: E501

        self._targets = targets

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
        if not isinstance(other, MappingIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other