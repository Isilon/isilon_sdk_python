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

from isilon_sdk.v9_5_0.models.cluster_identity_logon import ClusterIdentityLogon  # noqa: F401,E501


class ClusterIdentity(object):
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
        'description': 'str',
        'logon': 'ClusterIdentityLogon',
        'mttdl_level_msg': 'str',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'logon': 'logon',
        'mttdl_level_msg': 'mttdl_level_msg',
        'name': 'name'
    }

    def __init__(self, description=None, logon=None, mttdl_level_msg=None, name=None):  # noqa: E501
        """ClusterIdentity - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._logon = None
        self._mttdl_level_msg = None
        self._name = None
        self.discriminator = None

        self.description = description
        self.logon = logon
        self.mttdl_level_msg = mttdl_level_msg
        self.name = name

    @property
    def description(self):
        """Gets the description of this ClusterIdentity.  # noqa: E501

        A description of the cluster.  # noqa: E501

        :return: The description of this ClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ClusterIdentity.

        A description of the cluster.  # noqa: E501

        :param description: The description of this ClusterIdentity.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def logon(self):
        """Gets the logon of this ClusterIdentity.  # noqa: E501

        The information displayed when a user logs in to the cluster.  # noqa: E501

        :return: The logon of this ClusterIdentity.  # noqa: E501
        :rtype: ClusterIdentityLogon
        """
        return self._logon

    @logon.setter
    def logon(self, logon):
        """Sets the logon of this ClusterIdentity.

        The information displayed when a user logs in to the cluster.  # noqa: E501

        :param logon: The logon of this ClusterIdentity.  # noqa: E501
        :type: ClusterIdentityLogon
        """
        if logon is None:
            raise ValueError("Invalid value for `logon`, must not be `None`")  # noqa: E501

        self._logon = logon

    @property
    def mttdl_level_msg(self):
        """Gets the mttdl_level_msg of this ClusterIdentity.  # noqa: E501

        Enum to control the display message about the MTTDL of the cluster. This does NOT change the MTTDL of a cluster in anyway, and is purely a value for displaying messages.  # noqa: E501

        :return: The mttdl_level_msg of this ClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._mttdl_level_msg

    @mttdl_level_msg.setter
    def mttdl_level_msg(self, mttdl_level_msg):
        """Sets the mttdl_level_msg of this ClusterIdentity.

        Enum to control the display message about the MTTDL of the cluster. This does NOT change the MTTDL of a cluster in anyway, and is purely a value for displaying messages.  # noqa: E501

        :param mttdl_level_msg: The mttdl_level_msg of this ClusterIdentity.  # noqa: E501
        :type: str
        """
        if mttdl_level_msg is None:
            raise ValueError("Invalid value for `mttdl_level_msg`, must not be `None`")  # noqa: E501
        allowed_values = ["warn", "none"]  # noqa: E501
        if mttdl_level_msg not in allowed_values:
            raise ValueError(
                "Invalid value for `mttdl_level_msg` ({0}), must be one of {1}"  # noqa: E501
                .format(mttdl_level_msg, allowed_values)
            )

        self._mttdl_level_msg = mttdl_level_msg

    @property
    def name(self):
        """Gets the name of this ClusterIdentity.  # noqa: E501

        The name of the cluster.  # noqa: E501

        :return: The name of this ClusterIdentity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterIdentity.

        The name of the cluster.  # noqa: E501

        :param name: The name of this ClusterIdentity.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, ClusterIdentity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other