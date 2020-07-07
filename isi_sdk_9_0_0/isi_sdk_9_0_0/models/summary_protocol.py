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

from isi_sdk_9_0_0.models.summary_protocol_protocol_item import SummaryProtocolProtocolItem  # noqa: F401,E501


class SummaryProtocol(object):
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
        'protocol': 'list[SummaryProtocolProtocolItem]'
    }

    attribute_map = {
        'protocol': 'protocol'
    }

    def __init__(self, protocol=None):  # noqa: E501
        """SummaryProtocol - a model defined in Swagger"""  # noqa: E501

        self._protocol = None
        self.discriminator = None

        if protocol is not None:
            self.protocol = protocol

    @property
    def protocol(self):
        """Gets the protocol of this SummaryProtocol.  # noqa: E501


        :return: The protocol of this SummaryProtocol.  # noqa: E501
        :rtype: list[SummaryProtocolProtocolItem]
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SummaryProtocol.


        :param protocol: The protocol of this SummaryProtocol.  # noqa: E501
        :type: list[SummaryProtocolProtocolItem]
        """

        self._protocol = protocol

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
        if not isinstance(other, SummaryProtocol):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
