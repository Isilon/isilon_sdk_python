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


class ClusterTime(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ClusterTime - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'errors': 'list[ClusterTimeError]',
            'nodes': 'list[ClusterTimeNode]',
            'total': 'int'
        }

        self.attribute_map = {
            'errors': 'errors',
            'nodes': 'nodes',
            'total': 'total'
        }

        self._errors = None
        self._nodes = None
        self._total = None

    @property
    def errors(self):
        """
        Gets the errors of this ClusterTime.
        A list of errors encountered by the individual nodes involved in this request, or an empty list if there were no errors.

        :return: The errors of this ClusterTime.
        :rtype: list[ClusterTimeError]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """
        Sets the errors of this ClusterTime.
        A list of errors encountered by the individual nodes involved in this request, or an empty list if there were no errors.

        :param errors: The errors of this ClusterTime.
        :type: list[ClusterTimeError]
        """
        
        self._errors = errors

    @property
    def nodes(self):
        """
        Gets the nodes of this ClusterTime.
        The responses from the individual nodes involved in this request.

        :return: The nodes of this ClusterTime.
        :rtype: list[ClusterTimeNode]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """
        Sets the nodes of this ClusterTime.
        The responses from the individual nodes involved in this request.

        :param nodes: The nodes of this ClusterTime.
        :type: list[ClusterTimeNode]
        """
        
        self._nodes = nodes

    @property
    def total(self):
        """
        Gets the total of this ClusterTime.
        The total number of nodes responding.

        :return: The total of this ClusterTime.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this ClusterTime.
        The total number of nodes responding.

        :param total: The total of this ClusterTime.
        :type: int
        """
        
        self._total = total

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

