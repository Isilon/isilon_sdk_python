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


class ClusterServicesNodeService(object):
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
        'name': 'str',
        'state': 'str'
    }

    attribute_map = {
        'name': 'name',
        'state': 'state'
    }

    def __init__(self, name=None, state=None):  # noqa: E501
        """ClusterServicesNodeService - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._state = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if state is not None:
            self.state = state

    @property
    def name(self):
        """Gets the name of this ClusterServicesNodeService.  # noqa: E501

        Service name.  # noqa: E501

        :return: The name of this ClusterServicesNodeService.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterServicesNodeService.

        Service name.  # noqa: E501

        :param name: The name of this ClusterServicesNodeService.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def state(self):
        """Gets the state of this ClusterServicesNodeService.  # noqa: E501

        Service state.  # noqa: E501

        :return: The state of this ClusterServicesNodeService.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ClusterServicesNodeService.

        Service state.  # noqa: E501

        :param state: The state of this ClusterServicesNodeService.  # noqa: E501
        :type: str
        """
        if state is not None and len(state) > 255:
            raise ValueError("Invalid value for `state`, length must be less than or equal to `255`")  # noqa: E501
        if state is not None and len(state) < 1:
            raise ValueError("Invalid value for `state`, length must be greater than or equal to `1`")  # noqa: E501

        self._state = state

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
        if not isinstance(other, ClusterServicesNodeService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other