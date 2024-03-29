# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 15
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isilon_sdk.v9_4_0.models.datamover_account_credentials import DatamoverAccountCredentials  # noqa: F401,E501


class DatamoverAccountCreateParams(object):
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
        'account_type': 'str',
        'briefcase': 'str',
        'credentials': 'DatamoverAccountCredentials',
        'local_network_pool': 'str',
        'name': 'str',
        'remote_network_pool': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'account_type': 'account_type',
        'briefcase': 'briefcase',
        'credentials': 'credentials',
        'local_network_pool': 'local_network_pool',
        'name': 'name',
        'remote_network_pool': 'remote_network_pool',
        'uri': 'uri'
    }

    def __init__(self, account_type=None, briefcase=None, credentials=None, local_network_pool=None, name=None, remote_network_pool=None, uri=None):  # noqa: E501
        """DatamoverAccountCreateParams - a model defined in Swagger"""  # noqa: E501

        self._account_type = None
        self._briefcase = None
        self._credentials = None
        self._local_network_pool = None
        self._name = None
        self._remote_network_pool = None
        self._uri = None
        self.discriminator = None

        self.account_type = account_type
        if briefcase is not None:
            self.briefcase = briefcase
        if credentials is not None:
            self.credentials = credentials
        if local_network_pool is not None:
            self.local_network_pool = local_network_pool
        self.name = name
        if remote_network_pool is not None:
            self.remote_network_pool = remote_network_pool
        self.uri = uri

    @property
    def account_type(self):
        """Gets the account_type of this DatamoverAccountCreateParams.  # noqa: E501

        Type of the data storage account  # noqa: E501

        :return: The account_type of this DatamoverAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this DatamoverAccountCreateParams.

        Type of the data storage account  # noqa: E501

        :param account_type: The account_type of this DatamoverAccountCreateParams.  # noqa: E501
        :type: str
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DM", "AWS_S3", "ECS_S3", "AZURE"]  # noqa: E501
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"  # noqa: E501
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def briefcase(self):
        """Gets the briefcase of this DatamoverAccountCreateParams.  # noqa: E501

        An opaque container for storing additional data in this object, e.g. key-value pairs  # noqa: E501

        :return: The briefcase of this DatamoverAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._briefcase

    @briefcase.setter
    def briefcase(self, briefcase):
        """Sets the briefcase of this DatamoverAccountCreateParams.

        An opaque container for storing additional data in this object, e.g. key-value pairs  # noqa: E501

        :param briefcase: The briefcase of this DatamoverAccountCreateParams.  # noqa: E501
        :type: str
        """
        if briefcase is not None and len(briefcase) > 512:
            raise ValueError("Invalid value for `briefcase`, length must be less than or equal to `512`")  # noqa: E501
        if briefcase is not None and len(briefcase) < 0:
            raise ValueError("Invalid value for `briefcase`, length must be greater than or equal to `0`")  # noqa: E501

        self._briefcase = briefcase

    @property
    def credentials(self):
        """Gets the credentials of this DatamoverAccountCreateParams.  # noqa: E501

          # noqa: E501

        :return: The credentials of this DatamoverAccountCreateParams.  # noqa: E501
        :rtype: DatamoverAccountCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this DatamoverAccountCreateParams.

          # noqa: E501

        :param credentials: The credentials of this DatamoverAccountCreateParams.  # noqa: E501
        :type: DatamoverAccountCredentials
        """

        self._credentials = credentials

    @property
    def local_network_pool(self):
        """Gets the local_network_pool of this DatamoverAccountCreateParams.  # noqa: E501

        Local platform-specific network restriction  # noqa: E501

        :return: The local_network_pool of this DatamoverAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._local_network_pool

    @local_network_pool.setter
    def local_network_pool(self, local_network_pool):
        """Sets the local_network_pool of this DatamoverAccountCreateParams.

        Local platform-specific network restriction  # noqa: E501

        :param local_network_pool: The local_network_pool of this DatamoverAccountCreateParams.  # noqa: E501
        :type: str
        """
        if local_network_pool is not None and len(local_network_pool) > 255:
            raise ValueError("Invalid value for `local_network_pool`, length must be less than or equal to `255`")  # noqa: E501
        if local_network_pool is not None and len(local_network_pool) < 1:
            raise ValueError("Invalid value for `local_network_pool`, length must be greater than or equal to `1`")  # noqa: E501

        self._local_network_pool = local_network_pool

    @property
    def name(self):
        """Gets the name of this DatamoverAccountCreateParams.  # noqa: E501

        Name for this Data Mover account  # noqa: E501

        :return: The name of this DatamoverAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatamoverAccountCreateParams.

        Name for this Data Mover account  # noqa: E501

        :param name: The name of this DatamoverAccountCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def remote_network_pool(self):
        """Gets the remote_network_pool of this DatamoverAccountCreateParams.  # noqa: E501

        Remote platform-specific network restriction  # noqa: E501

        :return: The remote_network_pool of this DatamoverAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._remote_network_pool

    @remote_network_pool.setter
    def remote_network_pool(self, remote_network_pool):
        """Sets the remote_network_pool of this DatamoverAccountCreateParams.

        Remote platform-specific network restriction  # noqa: E501

        :param remote_network_pool: The remote_network_pool of this DatamoverAccountCreateParams.  # noqa: E501
        :type: str
        """
        if remote_network_pool is not None and len(remote_network_pool) > 255:
            raise ValueError("Invalid value for `remote_network_pool`, length must be less than or equal to `255`")  # noqa: E501
        if remote_network_pool is not None and len(remote_network_pool) < 1:
            raise ValueError("Invalid value for `remote_network_pool`, length must be greater than or equal to `1`")  # noqa: E501

        self._remote_network_pool = remote_network_pool

    @property
    def uri(self):
        """Gets the uri of this DatamoverAccountCreateParams.  # noqa: E501

        A valid URI pointing to the data storage  # noqa: E501

        :return: The uri of this DatamoverAccountCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this DatamoverAccountCreateParams.

        A valid URI pointing to the data storage  # noqa: E501

        :param uri: The uri of this DatamoverAccountCreateParams.  # noqa: E501
        :type: str
        """
        if uri is None:
            raise ValueError("Invalid value for `uri`, must not be `None`")  # noqa: E501
        if uri is not None and len(uri) > 2048:
            raise ValueError("Invalid value for `uri`, length must be less than or equal to `2048`")  # noqa: E501
        if uri is not None and len(uri) < 1:
            raise ValueError("Invalid value for `uri`, length must be greater than or equal to `1`")  # noqa: E501

        self._uri = uri

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
        if not isinstance(other, DatamoverAccountCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
