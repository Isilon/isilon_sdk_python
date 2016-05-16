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


class NetworkDnscacheSetting(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NetworkDnscacheSetting - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cache_entry_limit': 'int',
            'cluster_timeout': 'int',
            'dns_timeout': 'int',
            'eager_refresh': 'int',
            'testping_delta': 'int',
            'ttl_max_noerror': 'int',
            'ttl_max_nxdomain': 'int',
            'ttl_max_other': 'int',
            'ttl_max_servfail': 'int',
            'ttl_min_noerror': 'int',
            'ttl_min_nxdomain': 'int',
            'ttl_min_other': 'int',
            'ttl_min_servfail': 'int'
        }

        self.attribute_map = {
            'cache_entry_limit': 'cache_entry_limit',
            'cluster_timeout': 'cluster_timeout',
            'dns_timeout': 'dns_timeout',
            'eager_refresh': 'eager_refresh',
            'testping_delta': 'testping_delta',
            'ttl_max_noerror': 'ttl_max_noerror',
            'ttl_max_nxdomain': 'ttl_max_nxdomain',
            'ttl_max_other': 'ttl_max_other',
            'ttl_max_servfail': 'ttl_max_servfail',
            'ttl_min_noerror': 'ttl_min_noerror',
            'ttl_min_nxdomain': 'ttl_min_nxdomain',
            'ttl_min_other': 'ttl_min_other',
            'ttl_min_servfail': 'ttl_min_servfail'
        }

        self._cache_entry_limit = None
        self._cluster_timeout = None
        self._dns_timeout = None
        self._eager_refresh = None
        self._testping_delta = None
        self._ttl_max_noerror = None
        self._ttl_max_nxdomain = None
        self._ttl_max_other = None
        self._ttl_max_servfail = None
        self._ttl_min_noerror = None
        self._ttl_min_nxdomain = None
        self._ttl_min_other = None
        self._ttl_min_servfail = None

    @property
    def cache_entry_limit(self):
        """
        Gets the cache_entry_limit of this NetworkDnscacheSetting.
        DNS cache entry limit

        :return: The cache_entry_limit of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._cache_entry_limit

    @cache_entry_limit.setter
    def cache_entry_limit(self, cache_entry_limit):
        """
        Sets the cache_entry_limit of this NetworkDnscacheSetting.
        DNS cache entry limit

        :param cache_entry_limit: The cache_entry_limit of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not cache_entry_limit:
            raise ValueError("Invalid value for `cache_entry_limit`, must not be `None`")
        if cache_entry_limit > 1048576.0: 
            raise ValueError("Invalid value for `cache_entry_limit`, must be a value less than or equal to `1048576.0`")
        if cache_entry_limit < 1024.0: 
            raise ValueError("Invalid value for `cache_entry_limit`, must be a value greater than or equal to `1024.0`")

        self._cache_entry_limit = cache_entry_limit

    @property
    def cluster_timeout(self):
        """
        Gets the cluster_timeout of this NetworkDnscacheSetting.
        Timeout value for calls made to other nodes in the cluster

        :return: The cluster_timeout of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._cluster_timeout

    @cluster_timeout.setter
    def cluster_timeout(self, cluster_timeout):
        """
        Sets the cluster_timeout of this NetworkDnscacheSetting.
        Timeout value for calls made to other nodes in the cluster

        :param cluster_timeout: The cluster_timeout of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not cluster_timeout:
            raise ValueError("Invalid value for `cluster_timeout`, must not be `None`")
        if cluster_timeout > 30.0: 
            raise ValueError("Invalid value for `cluster_timeout`, must be a value less than or equal to `30.0`")
        if cluster_timeout < 1.0: 
            raise ValueError("Invalid value for `cluster_timeout`, must be a value greater than or equal to `1.0`")

        self._cluster_timeout = cluster_timeout

    @property
    def dns_timeout(self):
        """
        Gets the dns_timeout of this NetworkDnscacheSetting.
        Timeout value for calls made to the dns resolvers

        :return: The dns_timeout of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._dns_timeout

    @dns_timeout.setter
    def dns_timeout(self, dns_timeout):
        """
        Sets the dns_timeout of this NetworkDnscacheSetting.
        Timeout value for calls made to the dns resolvers

        :param dns_timeout: The dns_timeout of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not dns_timeout:
            raise ValueError("Invalid value for `dns_timeout`, must not be `None`")
        if dns_timeout > 30.0: 
            raise ValueError("Invalid value for `dns_timeout`, must be a value less than or equal to `30.0`")
        if dns_timeout < 1.0: 
            raise ValueError("Invalid value for `dns_timeout`, must be a value greater than or equal to `1.0`")

        self._dns_timeout = dns_timeout

    @property
    def eager_refresh(self):
        """
        Gets the eager_refresh of this NetworkDnscacheSetting.
        Lead time to refresh cache entries nearing expiration

        :return: The eager_refresh of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._eager_refresh

    @eager_refresh.setter
    def eager_refresh(self, eager_refresh):
        """
        Sets the eager_refresh of this NetworkDnscacheSetting.
        Lead time to refresh cache entries nearing expiration

        :param eager_refresh: The eager_refresh of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not eager_refresh:
            raise ValueError("Invalid value for `eager_refresh`, must not be `None`")
        if eager_refresh > 60.0: 
            raise ValueError("Invalid value for `eager_refresh`, must be a value less than or equal to `60.0`")
        if eager_refresh < 0.0: 
            raise ValueError("Invalid value for `eager_refresh`, must be a value greater than or equal to `0.0`")

        self._eager_refresh = eager_refresh

    @property
    def testping_delta(self):
        """
        Gets the testping_delta of this NetworkDnscacheSetting.
        Deltas for checking cbind cluster health

        :return: The testping_delta of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._testping_delta

    @testping_delta.setter
    def testping_delta(self, testping_delta):
        """
        Sets the testping_delta of this NetworkDnscacheSetting.
        Deltas for checking cbind cluster health

        :param testping_delta: The testping_delta of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not testping_delta:
            raise ValueError("Invalid value for `testping_delta`, must not be `None`")
        if testping_delta > 60.0: 
            raise ValueError("Invalid value for `testping_delta`, must be a value less than or equal to `60.0`")
        if testping_delta < 0.0: 
            raise ValueError("Invalid value for `testping_delta`, must be a value greater than or equal to `0.0`")

        self._testping_delta = testping_delta

    @property
    def ttl_max_noerror(self):
        """
        Gets the ttl_max_noerror of this NetworkDnscacheSetting.
        Upper bound on ttl for cache hits

        :return: The ttl_max_noerror of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._ttl_max_noerror

    @ttl_max_noerror.setter
    def ttl_max_noerror(self, ttl_max_noerror):
        """
        Sets the ttl_max_noerror of this NetworkDnscacheSetting.
        Upper bound on ttl for cache hits

        :param ttl_max_noerror: The ttl_max_noerror of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not ttl_max_noerror:
            raise ValueError("Invalid value for `ttl_max_noerror`, must not be `None`")
        if ttl_max_noerror > 3600.0: 
            raise ValueError("Invalid value for `ttl_max_noerror`, must be a value less than or equal to `3600.0`")
        if ttl_max_noerror < 0.0: 
            raise ValueError("Invalid value for `ttl_max_noerror`, must be a value greater than or equal to `0.0`")

        self._ttl_max_noerror = ttl_max_noerror

    @property
    def ttl_max_nxdomain(self):
        """
        Gets the ttl_max_nxdomain of this NetworkDnscacheSetting.
        Upper bound on ttl for nxdomain

        :return: The ttl_max_nxdomain of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._ttl_max_nxdomain

    @ttl_max_nxdomain.setter
    def ttl_max_nxdomain(self, ttl_max_nxdomain):
        """
        Sets the ttl_max_nxdomain of this NetworkDnscacheSetting.
        Upper bound on ttl for nxdomain

        :param ttl_max_nxdomain: The ttl_max_nxdomain of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not ttl_max_nxdomain:
            raise ValueError("Invalid value for `ttl_max_nxdomain`, must not be `None`")
        if ttl_max_nxdomain > 3600.0: 
            raise ValueError("Invalid value for `ttl_max_nxdomain`, must be a value less than or equal to `3600.0`")
        if ttl_max_nxdomain < 0.0: 
            raise ValueError("Invalid value for `ttl_max_nxdomain`, must be a value greater than or equal to `0.0`")

        self._ttl_max_nxdomain = ttl_max_nxdomain

    @property
    def ttl_max_other(self):
        """
        Gets the ttl_max_other of this NetworkDnscacheSetting.
        Upper bound on ttl for non-nxdomain failures

        :return: The ttl_max_other of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._ttl_max_other

    @ttl_max_other.setter
    def ttl_max_other(self, ttl_max_other):
        """
        Sets the ttl_max_other of this NetworkDnscacheSetting.
        Upper bound on ttl for non-nxdomain failures

        :param ttl_max_other: The ttl_max_other of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not ttl_max_other:
            raise ValueError("Invalid value for `ttl_max_other`, must not be `None`")
        if ttl_max_other > 3600.0: 
            raise ValueError("Invalid value for `ttl_max_other`, must be a value less than or equal to `3600.0`")
        if ttl_max_other < 0.0: 
            raise ValueError("Invalid value for `ttl_max_other`, must be a value greater than or equal to `0.0`")

        self._ttl_max_other = ttl_max_other

    @property
    def ttl_max_servfail(self):
        """
        Gets the ttl_max_servfail of this NetworkDnscacheSetting.
        Upper bound on ttl for server failures

        :return: The ttl_max_servfail of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._ttl_max_servfail

    @ttl_max_servfail.setter
    def ttl_max_servfail(self, ttl_max_servfail):
        """
        Sets the ttl_max_servfail of this NetworkDnscacheSetting.
        Upper bound on ttl for server failures

        :param ttl_max_servfail: The ttl_max_servfail of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not ttl_max_servfail:
            raise ValueError("Invalid value for `ttl_max_servfail`, must not be `None`")
        if ttl_max_servfail > 3600.0: 
            raise ValueError("Invalid value for `ttl_max_servfail`, must be a value less than or equal to `3600.0`")
        if ttl_max_servfail < 0.0: 
            raise ValueError("Invalid value for `ttl_max_servfail`, must be a value greater than or equal to `0.0`")

        self._ttl_max_servfail = ttl_max_servfail

    @property
    def ttl_min_noerror(self):
        """
        Gets the ttl_min_noerror of this NetworkDnscacheSetting.
        Lower bound on ttl for cache hits

        :return: The ttl_min_noerror of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._ttl_min_noerror

    @ttl_min_noerror.setter
    def ttl_min_noerror(self, ttl_min_noerror):
        """
        Sets the ttl_min_noerror of this NetworkDnscacheSetting.
        Lower bound on ttl for cache hits

        :param ttl_min_noerror: The ttl_min_noerror of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not ttl_min_noerror:
            raise ValueError("Invalid value for `ttl_min_noerror`, must not be `None`")
        if ttl_min_noerror > 3600.0: 
            raise ValueError("Invalid value for `ttl_min_noerror`, must be a value less than or equal to `3600.0`")
        if ttl_min_noerror < 0.0: 
            raise ValueError("Invalid value for `ttl_min_noerror`, must be a value greater than or equal to `0.0`")

        self._ttl_min_noerror = ttl_min_noerror

    @property
    def ttl_min_nxdomain(self):
        """
        Gets the ttl_min_nxdomain of this NetworkDnscacheSetting.
        Lower bound on ttl for nxdomain

        :return: The ttl_min_nxdomain of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._ttl_min_nxdomain

    @ttl_min_nxdomain.setter
    def ttl_min_nxdomain(self, ttl_min_nxdomain):
        """
        Sets the ttl_min_nxdomain of this NetworkDnscacheSetting.
        Lower bound on ttl for nxdomain

        :param ttl_min_nxdomain: The ttl_min_nxdomain of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not ttl_min_nxdomain:
            raise ValueError("Invalid value for `ttl_min_nxdomain`, must not be `None`")
        if ttl_min_nxdomain > 3600.0: 
            raise ValueError("Invalid value for `ttl_min_nxdomain`, must be a value less than or equal to `3600.0`")
        if ttl_min_nxdomain < 0.0: 
            raise ValueError("Invalid value for `ttl_min_nxdomain`, must be a value greater than or equal to `0.0`")

        self._ttl_min_nxdomain = ttl_min_nxdomain

    @property
    def ttl_min_other(self):
        """
        Gets the ttl_min_other of this NetworkDnscacheSetting.
        Lower bound on ttl for non-nxdomain failures

        :return: The ttl_min_other of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._ttl_min_other

    @ttl_min_other.setter
    def ttl_min_other(self, ttl_min_other):
        """
        Sets the ttl_min_other of this NetworkDnscacheSetting.
        Lower bound on ttl for non-nxdomain failures

        :param ttl_min_other: The ttl_min_other of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not ttl_min_other:
            raise ValueError("Invalid value for `ttl_min_other`, must not be `None`")
        if ttl_min_other > 3600.0: 
            raise ValueError("Invalid value for `ttl_min_other`, must be a value less than or equal to `3600.0`")
        if ttl_min_other < 0.0: 
            raise ValueError("Invalid value for `ttl_min_other`, must be a value greater than or equal to `0.0`")

        self._ttl_min_other = ttl_min_other

    @property
    def ttl_min_servfail(self):
        """
        Gets the ttl_min_servfail of this NetworkDnscacheSetting.
        Lower bound on ttl for server failures

        :return: The ttl_min_servfail of this NetworkDnscacheSetting.
        :rtype: int
        """
        return self._ttl_min_servfail

    @ttl_min_servfail.setter
    def ttl_min_servfail(self, ttl_min_servfail):
        """
        Sets the ttl_min_servfail of this NetworkDnscacheSetting.
        Lower bound on ttl for server failures

        :param ttl_min_servfail: The ttl_min_servfail of this NetworkDnscacheSetting.
        :type: int
        """
        
        if not ttl_min_servfail:
            raise ValueError("Invalid value for `ttl_min_servfail`, must not be `None`")
        if ttl_min_servfail > 3600.0: 
            raise ValueError("Invalid value for `ttl_min_servfail`, must be a value less than or equal to `3600.0`")
        if ttl_min_servfail < 0.0: 
            raise ValueError("Invalid value for `ttl_min_servfail`, must be a value greater than or equal to `0.0`")

        self._ttl_min_servfail = ttl_min_servfail

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

