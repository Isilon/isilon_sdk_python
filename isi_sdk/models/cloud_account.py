# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class CloudAccount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CloudAccount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'account_id': 'str',
            'account_username': 'str',
            'birth_cluster_id': 'str',
            'enabled': 'bool',
            'key': 'str',
            'name': 'str',
            'skip_ssl_validation': 'bool',
            'storage_region': 'str',
            'telemetry_bucket': 'str',
            'uri': 'str'
        }

        self.attribute_map = {
            'account_id': 'account_id',
            'account_username': 'account_username',
            'birth_cluster_id': 'birth_cluster_id',
            'enabled': 'enabled',
            'key': 'key',
            'name': 'name',
            'skip_ssl_validation': 'skip_ssl_validation',
            'storage_region': 'storage_region',
            'telemetry_bucket': 'telemetry_bucket',
            'uri': 'uri'
        }

        self._account_id = None
        self._account_username = None
        self._birth_cluster_id = None
        self._enabled = None
        self._key = None
        self._name = None
        self._skip_ssl_validation = None
        self._storage_region = None
        self._telemetry_bucket = None
        self._uri = None

    @property
    def account_id(self):
        """
        Gets the account_id of this CloudAccount.
        (S3 only) The user id of the S3 account

        :return: The account_id of this CloudAccount.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this CloudAccount.
        (S3 only) The user id of the S3 account

        :param account_id: The account_id of this CloudAccount.
        :type: str
        """
        
        self._account_id = account_id

    @property
    def account_username(self):
        """
        Gets the account_username of this CloudAccount.
        The username required to authenticate against the cloud service

        :return: The account_username of this CloudAccount.
        :rtype: str
        """
        return self._account_username

    @account_username.setter
    def account_username(self, account_username):
        """
        Sets the account_username of this CloudAccount.
        The username required to authenticate against the cloud service

        :param account_username: The account_username of this CloudAccount.
        :type: str
        """
        
        self._account_username = account_username

    @property
    def birth_cluster_id(self):
        """
        Gets the birth_cluster_id of this CloudAccount.
        The guid of the cluster where this account was created

        :return: The birth_cluster_id of this CloudAccount.
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """
        Sets the birth_cluster_id of this CloudAccount.
        The guid of the cluster where this account was created

        :param birth_cluster_id: The birth_cluster_id of this CloudAccount.
        :type: str
        """
        
        self._birth_cluster_id = birth_cluster_id

    @property
    def enabled(self):
        """
        Gets the enabled of this CloudAccount.
        Whether this account is explicitly enabled or disabled by a user

        :return: The enabled of this CloudAccount.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CloudAccount.
        Whether this account is explicitly enabled or disabled by a user

        :param enabled: The enabled of this CloudAccount.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def key(self):
        """
        Gets the key of this CloudAccount.
        A valid authentication key for connecting to the cloud

        :return: The key of this CloudAccount.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CloudAccount.
        A valid authentication key for connecting to the cloud

        :param key: The key of this CloudAccount.
        :type: str
        """
        
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this CloudAccount.
        A unique name for this account

        :return: The name of this CloudAccount.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudAccount.
        A unique name for this account

        :param name: The name of this CloudAccount.
        :type: str
        """
        
        self._name = name

    @property
    def skip_ssl_validation(self):
        """
        Gets the skip_ssl_validation of this CloudAccount.
        Indicates whether to skip SSL certificate validation when connecting to the cloud

        :return: The skip_ssl_validation of this CloudAccount.
        :rtype: bool
        """
        return self._skip_ssl_validation

    @skip_ssl_validation.setter
    def skip_ssl_validation(self, skip_ssl_validation):
        """
        Sets the skip_ssl_validation of this CloudAccount.
        Indicates whether to skip SSL certificate validation when connecting to the cloud

        :param skip_ssl_validation: The skip_ssl_validation of this CloudAccount.
        :type: bool
        """
        
        self._skip_ssl_validation = skip_ssl_validation

    @property
    def storage_region(self):
        """
        Gets the storage_region of this CloudAccount.
        (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region

        :return: The storage_region of this CloudAccount.
        :rtype: str
        """
        return self._storage_region

    @storage_region.setter
    def storage_region(self, storage_region):
        """
        Sets the storage_region of this CloudAccount.
        (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region

        :param storage_region: The storage_region of this CloudAccount.
        :type: str
        """
        
        self._storage_region = storage_region

    @property
    def telemetry_bucket(self):
        """
        Gets the telemetry_bucket of this CloudAccount.
        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider

        :return: The telemetry_bucket of this CloudAccount.
        :rtype: str
        """
        return self._telemetry_bucket

    @telemetry_bucket.setter
    def telemetry_bucket(self, telemetry_bucket):
        """
        Sets the telemetry_bucket of this CloudAccount.
        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider

        :param telemetry_bucket: The telemetry_bucket of this CloudAccount.
        :type: str
        """
        
        self._telemetry_bucket = telemetry_bucket

    @property
    def uri(self):
        """
        Gets the uri of this CloudAccount.
        A valid URI pointing to the location of the cloud storage

        :return: The uri of this CloudAccount.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this CloudAccount.
        A valid URI pointing to the location of the cloud storage

        :param uri: The uri of this CloudAccount.
        :type: str
        """
        
        self._uri = uri

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

