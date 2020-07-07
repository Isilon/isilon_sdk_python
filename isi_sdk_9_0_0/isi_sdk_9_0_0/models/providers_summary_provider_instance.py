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

from isi_sdk_9_0_0.models.providers_summary_provider_instance_connection import ProvidersSummaryProviderInstanceConnection  # noqa: F401,E501


class ProvidersSummaryProviderInstance(object):
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
        'active_server': 'str',
        'client_site': 'str',
        'connections': 'list[ProvidersSummaryProviderInstanceConnection]',
        'dc_site': 'str',
        'forest': 'str',
        'groupnet': 'str',
        'id': 'str',
        'name': 'str',
        'status': 'str',
        'type': 'str',
        'zone_name': 'str'
    }

    attribute_map = {
        'active_server': 'active_server',
        'client_site': 'client_site',
        'connections': 'connections',
        'dc_site': 'dc_site',
        'forest': 'forest',
        'groupnet': 'groupnet',
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'type': 'type',
        'zone_name': 'zone_name'
    }

    def __init__(self, active_server=None, client_site=None, connections=None, dc_site=None, forest=None, groupnet=None, id=None, name=None, status=None, type=None, zone_name=None):  # noqa: E501
        """ProvidersSummaryProviderInstance - a model defined in Swagger"""  # noqa: E501

        self._active_server = None
        self._client_site = None
        self._connections = None
        self._dc_site = None
        self._forest = None
        self._groupnet = None
        self._id = None
        self._name = None
        self._status = None
        self._type = None
        self._zone_name = None
        self.discriminator = None

        if active_server is not None:
            self.active_server = active_server
        if client_site is not None:
            self.client_site = client_site
        if connections is not None:
            self.connections = connections
        if dc_site is not None:
            self.dc_site = dc_site
        if forest is not None:
            self.forest = forest
        if groupnet is not None:
            self.groupnet = groupnet
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if zone_name is not None:
            self.zone_name = zone_name

    @property
    def active_server(self):
        """Gets the active_server of this ProvidersSummaryProviderInstance.  # noqa: E501


        :return: The active_server of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._active_server

    @active_server.setter
    def active_server(self, active_server):
        """Sets the active_server of this ProvidersSummaryProviderInstance.


        :param active_server: The active_server of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        if active_server is not None and len(active_server) > 255:
            raise ValueError("Invalid value for `active_server`, length must be less than or equal to `255`")  # noqa: E501
        if active_server is not None and len(active_server) < 0:
            raise ValueError("Invalid value for `active_server`, length must be greater than or equal to `0`")  # noqa: E501

        self._active_server = active_server

    @property
    def client_site(self):
        """Gets the client_site of this ProvidersSummaryProviderInstance.  # noqa: E501


        :return: The client_site of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._client_site

    @client_site.setter
    def client_site(self, client_site):
        """Sets the client_site of this ProvidersSummaryProviderInstance.


        :param client_site: The client_site of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        if client_site is not None and len(client_site) > 255:
            raise ValueError("Invalid value for `client_site`, length must be less than or equal to `255`")  # noqa: E501
        if client_site is not None and len(client_site) < 0:
            raise ValueError("Invalid value for `client_site`, length must be greater than or equal to `0`")  # noqa: E501

        self._client_site = client_site

    @property
    def connections(self):
        """Gets the connections of this ProvidersSummaryProviderInstance.  # noqa: E501


        :return: The connections of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: list[ProvidersSummaryProviderInstanceConnection]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this ProvidersSummaryProviderInstance.


        :param connections: The connections of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: list[ProvidersSummaryProviderInstanceConnection]
        """

        self._connections = connections

    @property
    def dc_site(self):
        """Gets the dc_site of this ProvidersSummaryProviderInstance.  # noqa: E501


        :return: The dc_site of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._dc_site

    @dc_site.setter
    def dc_site(self, dc_site):
        """Sets the dc_site of this ProvidersSummaryProviderInstance.


        :param dc_site: The dc_site of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        if dc_site is not None and len(dc_site) > 255:
            raise ValueError("Invalid value for `dc_site`, length must be less than or equal to `255`")  # noqa: E501
        if dc_site is not None and len(dc_site) < 0:
            raise ValueError("Invalid value for `dc_site`, length must be greater than or equal to `0`")  # noqa: E501

        self._dc_site = dc_site

    @property
    def forest(self):
        """Gets the forest of this ProvidersSummaryProviderInstance.  # noqa: E501


        :return: The forest of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._forest

    @forest.setter
    def forest(self, forest):
        """Sets the forest of this ProvidersSummaryProviderInstance.


        :param forest: The forest of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        if forest is not None and len(forest) > 255:
            raise ValueError("Invalid value for `forest`, length must be less than or equal to `255`")  # noqa: E501
        if forest is not None and len(forest) < 0:
            raise ValueError("Invalid value for `forest`, length must be greater than or equal to `0`")  # noqa: E501

        self._forest = forest

    @property
    def groupnet(self):
        """Gets the groupnet of this ProvidersSummaryProviderInstance.  # noqa: E501


        :return: The groupnet of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._groupnet

    @groupnet.setter
    def groupnet(self, groupnet):
        """Sets the groupnet of this ProvidersSummaryProviderInstance.


        :param groupnet: The groupnet of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        if groupnet is not None and len(groupnet) > 255:
            raise ValueError("Invalid value for `groupnet`, length must be less than or equal to `255`")  # noqa: E501
        if groupnet is not None and len(groupnet) < 0:
            raise ValueError("Invalid value for `groupnet`, length must be greater than or equal to `0`")  # noqa: E501

        self._groupnet = groupnet

    @property
    def id(self):
        """Gets the id of this ProvidersSummaryProviderInstance.  # noqa: E501

        Specifies the ID of the provider.  # noqa: E501

        :return: The id of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProvidersSummaryProviderInstance.

        Specifies the ID of the provider.  # noqa: E501

        :param id: The id of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        if id is not None and len(id) > 255:
            raise ValueError("Invalid value for `id`, length must be less than or equal to `255`")  # noqa: E501
        if id is not None and len(id) < 0:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `0`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ProvidersSummaryProviderInstance.  # noqa: E501

        Specifies the name of the provider.  # noqa: E501

        :return: The name of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProvidersSummaryProviderInstance.

        Specifies the name of the provider.  # noqa: E501

        :param name: The name of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this ProvidersSummaryProviderInstance.  # noqa: E501

        Indicates the status of the provider.  # noqa: E501

        :return: The status of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProvidersSummaryProviderInstance.

        Indicates the status of the provider.  # noqa: E501

        :param status: The status of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["offline", "active", "online", "initializing", "joining", "disabled"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this ProvidersSummaryProviderInstance.  # noqa: E501

        Specifies the type of provider.  # noqa: E501

        :return: The type of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProvidersSummaryProviderInstance.

        Specifies the type of provider.  # noqa: E501

        :param type: The type of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        allowed_values = ["file", "ldap", "local", "nis", "ads", "krb5", "unknown"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def zone_name(self):
        """Gets the zone_name of this ProvidersSummaryProviderInstance.  # noqa: E501


        :return: The zone_name of this ProvidersSummaryProviderInstance.  # noqa: E501
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this ProvidersSummaryProviderInstance.


        :param zone_name: The zone_name of this ProvidersSummaryProviderInstance.  # noqa: E501
        :type: str
        """
        if zone_name is not None and len(zone_name) > 255:
            raise ValueError("Invalid value for `zone_name`, length must be less than or equal to `255`")  # noqa: E501
        if zone_name is not None and len(zone_name) < 0:
            raise ValueError("Invalid value for `zone_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._zone_name = zone_name

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
        if not isinstance(other, ProvidersSummaryProviderInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
