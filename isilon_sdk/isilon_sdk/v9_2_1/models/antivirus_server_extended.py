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

from isilon_sdk.v9_2_1.models.antivirus_server import AntivirusServer  # noqa: F401,E501


class AntivirusServerExtended(object):
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
        'enabled': 'bool',
        'url': 'str',
        'definitions': 'str',
        'id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'url': 'url',
        'definitions': 'definitions',
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, description=None, enabled=None, url=None, definitions=None, id=None, status=None):  # noqa: E501
        """AntivirusServerExtended - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._enabled = None
        self._url = None
        self._definitions = None
        self._id = None
        self._status = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if url is not None:
            self.url = url
        if definitions is not None:
            self.definitions = definitions
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status

    @property
    def description(self):
        """Gets the description of this AntivirusServerExtended.  # noqa: E501

        A description for the server.  # noqa: E501

        :return: The description of this AntivirusServerExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AntivirusServerExtended.

        A description for the server.  # noqa: E501

        :param description: The description of this AntivirusServerExtended.  # noqa: E501
        :type: str
        """
        if description is not None and len(description) > 255:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this AntivirusServerExtended.  # noqa: E501

        Whether the server is enabled.  # noqa: E501

        :return: The enabled of this AntivirusServerExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AntivirusServerExtended.

        Whether the server is enabled.  # noqa: E501

        :param enabled: The enabled of this AntivirusServerExtended.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def url(self):
        """Gets the url of this AntivirusServerExtended.  # noqa: E501

        The icap url for the server.  This should have a format of: icap://host.domain:port/path  # noqa: E501

        :return: The url of this AntivirusServerExtended.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AntivirusServerExtended.

        The icap url for the server.  This should have a format of: icap://host.domain:port/path  # noqa: E501

        :param url: The url of this AntivirusServerExtended.  # noqa: E501
        :type: str
        """
        if url is not None and len(url) > 2048:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `2048`")  # noqa: E501
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

    @property
    def definitions(self):
        """Gets the definitions of this AntivirusServerExtended.  # noqa: E501


        :return: The definitions of this AntivirusServerExtended.  # noqa: E501
        :rtype: str
        """
        return self._definitions

    @definitions.setter
    def definitions(self, definitions):
        """Sets the definitions of this AntivirusServerExtended.


        :param definitions: The definitions of this AntivirusServerExtended.  # noqa: E501
        :type: str
        """
        if definitions is not None and len(definitions) > 255:
            raise ValueError("Invalid value for `definitions`, length must be less than or equal to `255`")  # noqa: E501
        if definitions is not None and len(definitions) < 0:
            raise ValueError("Invalid value for `definitions`, length must be greater than or equal to `0`")  # noqa: E501

        self._definitions = definitions

    @property
    def id(self):
        """Gets the id of this AntivirusServerExtended.  # noqa: E501

        A unique identifier for the server.  # noqa: E501

        :return: The id of this AntivirusServerExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AntivirusServerExtended.

        A unique identifier for the server.  # noqa: E501

        :param id: The id of this AntivirusServerExtended.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this AntivirusServerExtended.  # noqa: E501

        The status of the server.  # noqa: E501

        :return: The status of this AntivirusServerExtended.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AntivirusServerExtended.

        The status of the server.  # noqa: E501

        :param status: The status of this AntivirusServerExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["active", "inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if not isinstance(other, AntivirusServerExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
