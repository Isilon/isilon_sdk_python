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


class JobJob(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        JobJob - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'policy': 'str',
            'priority': 'int',
            'state': 'str'
        }

        self.attribute_map = {
            'policy': 'policy',
            'priority': 'priority',
            'state': 'state'
        }

        self._policy = None
        self._priority = None
        self._state = None

    @property
    def policy(self):
        """
        Gets the policy of this JobJob.
        Impact policy of this job instance.

        :return: The policy of this JobJob.
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """
        Sets the policy of this JobJob.
        Impact policy of this job instance.

        :param policy: The policy of this JobJob.
        :type: str
        """
        
        self._policy = policy

    @property
    def priority(self):
        """
        Gets the priority of this JobJob.
        Priority of this job instance; lower numbers preempt higher numbers.

        :return: The priority of this JobJob.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this JobJob.
        Priority of this job instance; lower numbers preempt higher numbers.

        :param priority: The priority of this JobJob.
        :type: int
        """
        
        if not priority:
            raise ValueError("Invalid value for `priority`, must not be `None`")
        if priority > 10.0: 
            raise ValueError("Invalid value for `priority`, must be a value less than or equal to `10.0`")
        if priority < 1.0: 
            raise ValueError("Invalid value for `priority`, must be a value greater than or equal to `1.0`")

        self._priority = priority

    @property
    def state(self):
        """
        Gets the state of this JobJob.
        Desired new state of this job instance.

        :return: The state of this JobJob.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this JobJob.
        Desired new state of this job instance.

        :param state: The state of this JobJob.
        :type: str
        """
        allowed_values = ["run", "pause", "cancel"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state`, must be one of {0}"
                .format(allowed_values)
            )

        self._state = state

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

