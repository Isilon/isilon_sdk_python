# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 16
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_5_0.models.ndmp_settings_preferred_ip_data_subnet import NdmpSettingsPreferredIpDataSubnet  # noqa: F401,E501


class NdmpSettingsPreferredIpsPreference(object):
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
        'data_subnets': 'list[NdmpSettingsPreferredIpDataSubnet]',
        'id': 'str',
        'scope': 'str'
    }

    attribute_map = {
        'data_subnets': 'data_subnets',
        'id': 'id',
        'scope': 'scope'
    }

    def __init__(self, data_subnets=None, id=None, scope=None):  # noqa: E501
        """NdmpSettingsPreferredIpsPreference - a model defined in Swagger"""  # noqa: E501

        self._data_subnets = None
        self._id = None
        self._scope = None
        self.discriminator = None

        if data_subnets is not None:
            self.data_subnets = data_subnets
        if id is not None:
            self.id = id
        if scope is not None:
            self.scope = scope

    @property
    def data_subnets(self):
        """Gets the data_subnets of this NdmpSettingsPreferredIpsPreference.  # noqa: E501


        :return: The data_subnets of this NdmpSettingsPreferredIpsPreference.  # noqa: E501
        :rtype: list[NdmpSettingsPreferredIpDataSubnet]
        """
        return self._data_subnets

    @data_subnets.setter
    def data_subnets(self, data_subnets):
        """Sets the data_subnets of this NdmpSettingsPreferredIpsPreference.


        :param data_subnets: The data_subnets of this NdmpSettingsPreferredIpsPreference.  # noqa: E501
        :type: list[NdmpSettingsPreferredIpDataSubnet]
        """

        self._data_subnets = data_subnets

    @property
    def id(self):
        """Gets the id of this NdmpSettingsPreferredIpsPreference.  # noqa: E501

        The unique display id, same as scope  # noqa: E501

        :return: The id of this NdmpSettingsPreferredIpsPreference.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NdmpSettingsPreferredIpsPreference.

        The unique display id, same as scope  # noqa: E501

        :param id: The id of this NdmpSettingsPreferredIpsPreference.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def scope(self):
        """Gets the scope of this NdmpSettingsPreferredIpsPreference.  # noqa: E501

        Either cluster or a network subnet defined in OneFS.  # noqa: E501

        :return: The scope of this NdmpSettingsPreferredIpsPreference.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this NdmpSettingsPreferredIpsPreference.

        Either cluster or a network subnet defined in OneFS.  # noqa: E501

        :param scope: The scope of this NdmpSettingsPreferredIpsPreference.  # noqa: E501
        :type: str
        """

        self._scope = scope

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
        if not isinstance(other, NdmpSettingsPreferredIpsPreference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other