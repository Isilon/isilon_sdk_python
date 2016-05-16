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


class CloudAccountExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CloudAccountExtended - a model defined in Swagger

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
            'uri': 'str',
            'bucket': 'str',
            'id': 'str',
            'metadata_bucket': 'str',
            'pool': 'str',
            'state': 'str',
            'state_details': 'str',
            'type': 'str'
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
            'uri': 'uri',
            'bucket': 'bucket',
            'id': 'id',
            'metadata_bucket': 'metadata_bucket',
            'pool': 'pool',
            'state': 'state',
            'state_details': 'state_details',
            'type': 'type'
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
        self._bucket = None
        self._id = None
        self._metadata_bucket = None
        self._pool = None
        self._state = None
        self._state_details = None
        self._type = None

    @property
    def account_id(self):
        """
        Gets the account_id of this CloudAccountExtended.
        (S3 only) The user id of the S3 account

        :return: The account_id of this CloudAccountExtended.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """
        Sets the account_id of this CloudAccountExtended.
        (S3 only) The user id of the S3 account

        :param account_id: The account_id of this CloudAccountExtended.
        :type: str
        """
        
        self._account_id = account_id

    @property
    def account_username(self):
        """
        Gets the account_username of this CloudAccountExtended.
        The username required to authenticate against the cloud service

        :return: The account_username of this CloudAccountExtended.
        :rtype: str
        """
        return self._account_username

    @account_username.setter
    def account_username(self, account_username):
        """
        Sets the account_username of this CloudAccountExtended.
        The username required to authenticate against the cloud service

        :param account_username: The account_username of this CloudAccountExtended.
        :type: str
        """
        
        self._account_username = account_username

    @property
    def birth_cluster_id(self):
        """
        Gets the birth_cluster_id of this CloudAccountExtended.
        The guid of the cluster where this account was created

        :return: The birth_cluster_id of this CloudAccountExtended.
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """
        Sets the birth_cluster_id of this CloudAccountExtended.
        The guid of the cluster where this account was created

        :param birth_cluster_id: The birth_cluster_id of this CloudAccountExtended.
        :type: str
        """
        
        self._birth_cluster_id = birth_cluster_id

    @property
    def enabled(self):
        """
        Gets the enabled of this CloudAccountExtended.
        Whether this account is explicitly enabled or disabled by a user

        :return: The enabled of this CloudAccountExtended.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this CloudAccountExtended.
        Whether this account is explicitly enabled or disabled by a user

        :param enabled: The enabled of this CloudAccountExtended.
        :type: bool
        """
        
        self._enabled = enabled

    @property
    def key(self):
        """
        Gets the key of this CloudAccountExtended.
        A valid authentication key for connecting to the cloud

        :return: The key of this CloudAccountExtended.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this CloudAccountExtended.
        A valid authentication key for connecting to the cloud

        :param key: The key of this CloudAccountExtended.
        :type: str
        """
        
        self._key = key

    @property
    def name(self):
        """
        Gets the name of this CloudAccountExtended.
        A unique name for this account

        :return: The name of this CloudAccountExtended.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CloudAccountExtended.
        A unique name for this account

        :param name: The name of this CloudAccountExtended.
        :type: str
        """
        
        self._name = name

    @property
    def skip_ssl_validation(self):
        """
        Gets the skip_ssl_validation of this CloudAccountExtended.
        Indicates whether to skip SSL certificate validation when connecting to the cloud

        :return: The skip_ssl_validation of this CloudAccountExtended.
        :rtype: bool
        """
        return self._skip_ssl_validation

    @skip_ssl_validation.setter
    def skip_ssl_validation(self, skip_ssl_validation):
        """
        Sets the skip_ssl_validation of this CloudAccountExtended.
        Indicates whether to skip SSL certificate validation when connecting to the cloud

        :param skip_ssl_validation: The skip_ssl_validation of this CloudAccountExtended.
        :type: bool
        """
        
        self._skip_ssl_validation = skip_ssl_validation

    @property
    def storage_region(self):
        """
        Gets the storage_region of this CloudAccountExtended.
        (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region

        :return: The storage_region of this CloudAccountExtended.
        :rtype: str
        """
        return self._storage_region

    @storage_region.setter
    def storage_region(self, storage_region):
        """
        Sets the storage_region of this CloudAccountExtended.
        (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region

        :param storage_region: The storage_region of this CloudAccountExtended.
        :type: str
        """
        
        self._storage_region = storage_region

    @property
    def telemetry_bucket(self):
        """
        Gets the telemetry_bucket of this CloudAccountExtended.
        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider

        :return: The telemetry_bucket of this CloudAccountExtended.
        :rtype: str
        """
        return self._telemetry_bucket

    @telemetry_bucket.setter
    def telemetry_bucket(self, telemetry_bucket):
        """
        Sets the telemetry_bucket of this CloudAccountExtended.
        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider

        :param telemetry_bucket: The telemetry_bucket of this CloudAccountExtended.
        :type: str
        """
        
        self._telemetry_bucket = telemetry_bucket

    @property
    def uri(self):
        """
        Gets the uri of this CloudAccountExtended.
        A valid URI pointing to the location of the cloud storage

        :return: The uri of this CloudAccountExtended.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this CloudAccountExtended.
        A valid URI pointing to the location of the cloud storage

        :param uri: The uri of this CloudAccountExtended.
        :type: str
        """
        
        self._uri = uri

    @property
    def bucket(self):
        """
        Gets the bucket of this CloudAccountExtended.
        The machine generated name of the account bucket to store data

        :return: The bucket of this CloudAccountExtended.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """
        Sets the bucket of this CloudAccountExtended.
        The machine generated name of the account bucket to store data

        :param bucket: The bucket of this CloudAccountExtended.
        :type: str
        """
        
        self._bucket = bucket

    @property
    def id(self):
        """
        Gets the id of this CloudAccountExtended.
        A globally unique name for this account

        :return: The id of this CloudAccountExtended.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudAccountExtended.
        A globally unique name for this account

        :param id: The id of this CloudAccountExtended.
        :type: str
        """
        
        self._id = id

    @property
    def metadata_bucket(self):
        """
        Gets the metadata_bucket of this CloudAccountExtended.
        The machine generated name of the account bucket to store metadata

        :return: The metadata_bucket of this CloudAccountExtended.
        :rtype: str
        """
        return self._metadata_bucket

    @metadata_bucket.setter
    def metadata_bucket(self, metadata_bucket):
        """
        Sets the metadata_bucket of this CloudAccountExtended.
        The machine generated name of the account bucket to store metadata

        :param metadata_bucket: The metadata_bucket of this CloudAccountExtended.
        :type: str
        """
        
        self._metadata_bucket = metadata_bucket

    @property
    def pool(self):
        """
        Gets the pool of this CloudAccountExtended.
        Name of the pool referencing this account.  Empty if none.

        :return: The pool of this CloudAccountExtended.
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """
        Sets the pool of this CloudAccountExtended.
        Name of the pool referencing this account.  Empty if none.

        :param pool: The pool of this CloudAccountExtended.
        :type: str
        """
        
        self._pool = pool

    @property
    def state(self):
        """
        Gets the state of this CloudAccountExtended.
        Indicates whether this account is in a good state (\"OK\"), disabled (\"disabled\") or inaccessible via the network (\"unreachable\")

        :return: The state of this CloudAccountExtended.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this CloudAccountExtended.
        Indicates whether this account is in a good state (\"OK\"), disabled (\"disabled\") or inaccessible via the network (\"unreachable\")

        :param state: The state of this CloudAccountExtended.
        :type: str
        """
        allowed_values = ["OK", "disabled", "unreachable"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )

        self._state = state

    @property
    def state_details(self):
        """
        Gets the state_details of this CloudAccountExtended.
        Gives further information to describe the state of this account

        :return: The state_details of this CloudAccountExtended.
        :rtype: str
        """
        return self._state_details

    @state_details.setter
    def state_details(self, state_details):
        """
        Sets the state_details of this CloudAccountExtended.
        Gives further information to describe the state of this account

        :param state_details: The state_details of this CloudAccountExtended.
        :type: str
        """
        
        self._state_details = state_details

    @property
    def type(self):
        """
        Gets the type of this CloudAccountExtended.
        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"ecs2\" for EMC Elastic Cloud Storage Service, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3

        :return: The type of this CloudAccountExtended.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CloudAccountExtended.
        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"ecs2\" for EMC Elastic Cloud Storage Service, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3

        :param type: The type of this CloudAccountExtended.
        :type: str
        """
        allowed_values = ["isilon", "ecs", "ecs2", "azure", "s3", "ran"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )

        self._type = type

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

