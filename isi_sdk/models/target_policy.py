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


class TargetPolicy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TargetPolicy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'failover_failback_state': 'str',
            'id': 'str',
            'last_job_state': 'str',
            'last_source_coordinator_ip': 'str',
            'last_update_from_source': 'int',
            'legacy_policy': 'bool',
            'name': 'str',
            'source_cluster_guid': 'str',
            'source_host': 'str',
            'target_path': 'str'
        }

        self.attribute_map = {
            'failover_failback_state': 'failover_failback_state',
            'id': 'id',
            'last_job_state': 'last_job_state',
            'last_source_coordinator_ip': 'last_source_coordinator_ip',
            'last_update_from_source': 'last_update_from_source',
            'legacy_policy': 'legacy_policy',
            'name': 'name',
            'source_cluster_guid': 'source_cluster_guid',
            'source_host': 'source_host',
            'target_path': 'target_path'
        }

        self._failover_failback_state = None
        self._id = None
        self._last_job_state = None
        self._last_source_coordinator_ip = None
        self._last_update_from_source = None
        self._legacy_policy = None
        self._name = None
        self._source_cluster_guid = None
        self._source_host = None
        self._target_path = None

    @property
    def failover_failback_state(self):
        """
        Gets the failover_failback_state of this TargetPolicy.
        The condition of this policy with respect to sync failover/failback.

        :return: The failover_failback_state of this TargetPolicy.
        :rtype: str
        """
        return self._failover_failback_state

    @failover_failback_state.setter
    def failover_failback_state(self, failover_failback_state):
        """
        Sets the failover_failback_state of this TargetPolicy.
        The condition of this policy with respect to sync failover/failback.

        :param failover_failback_state: The failover_failback_state of this TargetPolicy.
        :type: str
        """
        allowed_values = ["writes_disabled", "enabling_writes", "writes_enabled", "disabling_writes", "creating_resync_policy", "resync_policy_created"]
        if failover_failback_state not in allowed_values:
            raise ValueError(
                "Invalid value for `failover_failback_state`, must be one of {0}"
                .format(allowed_values)
            )

        self._failover_failback_state = failover_failback_state

    @property
    def id(self):
        """
        Gets the id of this TargetPolicy.
        The system ID given to this sync policy.

        :return: The id of this TargetPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetPolicy.
        The system ID given to this sync policy.

        :param id: The id of this TargetPolicy.
        :type: str
        """
        
        self._id = id

    @property
    def last_job_state(self):
        """
        Gets the last_job_state of this TargetPolicy.
        The state of the last job run for this policy.

        :return: The last_job_state of this TargetPolicy.
        :rtype: str
        """
        return self._last_job_state

    @last_job_state.setter
    def last_job_state(self, last_job_state):
        """
        Sets the last_job_state of this TargetPolicy.
        The state of the last job run for this policy.

        :param last_job_state: The last_job_state of this TargetPolicy.
        :type: str
        """
        allowed_values = ["scheduled", "running", "paused", "finished", "failed", "canceled", "needs_attention", "skipped", "pending", "unknown"]
        if last_job_state not in allowed_values:
            raise ValueError(
                "Invalid value for `last_job_state`, must be one of {0}"
                .format(allowed_values)
            )

        self._last_job_state = last_job_state

    @property
    def last_source_coordinator_ip(self):
        """
        Gets the last_source_coordinator_ip of this TargetPolicy.
        The IP address from which a SyncIQ coordinator daemon most recently connected to this cluster to update it about the progress of a job for this policy.

        :return: The last_source_coordinator_ip of this TargetPolicy.
        :rtype: str
        """
        return self._last_source_coordinator_ip

    @last_source_coordinator_ip.setter
    def last_source_coordinator_ip(self, last_source_coordinator_ip):
        """
        Sets the last_source_coordinator_ip of this TargetPolicy.
        The IP address from which a SyncIQ coordinator daemon most recently connected to this cluster to update it about the progress of a job for this policy.

        :param last_source_coordinator_ip: The last_source_coordinator_ip of this TargetPolicy.
        :type: str
        """
        
        self._last_source_coordinator_ip = last_source_coordinator_ip

    @property
    def last_update_from_source(self):
        """
        Gets the last_update_from_source of this TargetPolicy.
        The last time this cluster was updated with sync information from the source cluster for this policy, in unix epoch seconds.  Null if no such update has occurred yet.

        :return: The last_update_from_source of this TargetPolicy.
        :rtype: int
        """
        return self._last_update_from_source

    @last_update_from_source.setter
    def last_update_from_source(self, last_update_from_source):
        """
        Sets the last_update_from_source of this TargetPolicy.
        The last time this cluster was updated with sync information from the source cluster for this policy, in unix epoch seconds.  Null if no such update has occurred yet.

        :param last_update_from_source: The last_update_from_source of this TargetPolicy.
        :type: int
        """
        
        self._last_update_from_source = last_update_from_source

    @property
    def legacy_policy(self):
        """
        Gets the legacy_policy of this TargetPolicy.
        Was this policy defined by a OneFS version earlier than 6.0? (Pre-6.0 policies did not have the target policy concept and canceling from the target side will not be available.)

        :return: The legacy_policy of this TargetPolicy.
        :rtype: bool
        """
        return self._legacy_policy

    @legacy_policy.setter
    def legacy_policy(self, legacy_policy):
        """
        Sets the legacy_policy of this TargetPolicy.
        Was this policy defined by a OneFS version earlier than 6.0? (Pre-6.0 policies did not have the target policy concept and canceling from the target side will not be available.)

        :param legacy_policy: The legacy_policy of this TargetPolicy.
        :type: bool
        """
        
        self._legacy_policy = legacy_policy

    @property
    def name(self):
        """
        Gets the name of this TargetPolicy.
        User-assigned name of this sync policy.

        :return: The name of this TargetPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TargetPolicy.
        User-assigned name of this sync policy.

        :param name: The name of this TargetPolicy.
        :type: str
        """
        
        self._name = name

    @property
    def source_cluster_guid(self):
        """
        Gets the source_cluster_guid of this TargetPolicy.
        Unique identifier for the source cluster.

        :return: The source_cluster_guid of this TargetPolicy.
        :rtype: str
        """
        return self._source_cluster_guid

    @source_cluster_guid.setter
    def source_cluster_guid(self, source_cluster_guid):
        """
        Sets the source_cluster_guid of this TargetPolicy.
        Unique identifier for the source cluster.

        :param source_cluster_guid: The source_cluster_guid of this TargetPolicy.
        :type: str
        """
        
        self._source_cluster_guid = source_cluster_guid

    @property
    def source_host(self):
        """
        Gets the source_host of this TargetPolicy.
        Hostname or IP address of sync source cluster.

        :return: The source_host of this TargetPolicy.
        :rtype: str
        """
        return self._source_host

    @source_host.setter
    def source_host(self, source_host):
        """
        Sets the source_host of this TargetPolicy.
        Hostname or IP address of sync source cluster.

        :param source_host: The source_host of this TargetPolicy.
        :type: str
        """
        
        self._source_host = source_host

    @property
    def target_path(self):
        """
        Gets the target_path of this TargetPolicy.
        Absolute filesystem path on the target cluster for the sync destination.

        :return: The target_path of this TargetPolicy.
        :rtype: str
        """
        return self._target_path

    @target_path.setter
    def target_path(self, target_path):
        """
        Sets the target_path of this TargetPolicy.
        Absolute filesystem path on the target cluster for the sync destination.

        :param target_path: The target_path of this TargetPolicy.
        :type: str
        """
        
        self._target_path = target_path

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

