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

from isi_sdk_9_0_0.models.summary_protocol_stats_protocol_stats_cpu import SummaryProtocolStatsProtocolStatsCpu  # noqa: F401,E501
from isi_sdk_9_0_0.models.summary_protocol_stats_protocol_stats_disk import SummaryProtocolStatsProtocolStatsDisk  # noqa: F401,E501
from isi_sdk_9_0_0.models.summary_protocol_stats_protocol_stats_network import SummaryProtocolStatsProtocolStatsNetwork  # noqa: F401,E501
from isi_sdk_9_0_0.models.summary_protocol_stats_protocol_stats_onefs import SummaryProtocolStatsProtocolStatsOnefs  # noqa: F401,E501
from isi_sdk_9_0_0.models.summary_protocol_stats_protocol_stats_protocol import SummaryProtocolStatsProtocolStatsProtocol  # noqa: F401,E501


class SummaryProtocolStatsProtocolStats(object):
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
        'cpu': 'SummaryProtocolStatsProtocolStatsCpu',
        'disk': 'SummaryProtocolStatsProtocolStatsDisk',
        'network': 'SummaryProtocolStatsProtocolStatsNetwork',
        'onefs': 'SummaryProtocolStatsProtocolStatsOnefs',
        'protocol': 'SummaryProtocolStatsProtocolStatsProtocol',
        'time': 'int'
    }

    attribute_map = {
        'cpu': 'cpu',
        'disk': 'disk',
        'network': 'network',
        'onefs': 'onefs',
        'protocol': 'protocol',
        'time': 'time'
    }

    def __init__(self, cpu=None, disk=None, network=None, onefs=None, protocol=None, time=None):  # noqa: E501
        """SummaryProtocolStatsProtocolStats - a model defined in Swagger"""  # noqa: E501

        self._cpu = None
        self._disk = None
        self._network = None
        self._onefs = None
        self._protocol = None
        self._time = None
        self.discriminator = None

        if cpu is not None:
            self.cpu = cpu
        if disk is not None:
            self.disk = disk
        if network is not None:
            self.network = network
        if onefs is not None:
            self.onefs = onefs
        if protocol is not None:
            self.protocol = protocol
        self.time = time

    @property
    def cpu(self):
        """Gets the cpu of this SummaryProtocolStatsProtocolStats.  # noqa: E501

          # noqa: E501

        :return: The cpu of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :rtype: SummaryProtocolStatsProtocolStatsCpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this SummaryProtocolStatsProtocolStats.

          # noqa: E501

        :param cpu: The cpu of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :type: SummaryProtocolStatsProtocolStatsCpu
        """

        self._cpu = cpu

    @property
    def disk(self):
        """Gets the disk of this SummaryProtocolStatsProtocolStats.  # noqa: E501

          # noqa: E501

        :return: The disk of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :rtype: SummaryProtocolStatsProtocolStatsDisk
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this SummaryProtocolStatsProtocolStats.

          # noqa: E501

        :param disk: The disk of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :type: SummaryProtocolStatsProtocolStatsDisk
        """

        self._disk = disk

    @property
    def network(self):
        """Gets the network of this SummaryProtocolStatsProtocolStats.  # noqa: E501

          # noqa: E501

        :return: The network of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :rtype: SummaryProtocolStatsProtocolStatsNetwork
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this SummaryProtocolStatsProtocolStats.

          # noqa: E501

        :param network: The network of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :type: SummaryProtocolStatsProtocolStatsNetwork
        """

        self._network = network

    @property
    def onefs(self):
        """Gets the onefs of this SummaryProtocolStatsProtocolStats.  # noqa: E501

          # noqa: E501

        :return: The onefs of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :rtype: SummaryProtocolStatsProtocolStatsOnefs
        """
        return self._onefs

    @onefs.setter
    def onefs(self, onefs):
        """Sets the onefs of this SummaryProtocolStatsProtocolStats.

          # noqa: E501

        :param onefs: The onefs of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :type: SummaryProtocolStatsProtocolStatsOnefs
        """

        self._onefs = onefs

    @property
    def protocol(self):
        """Gets the protocol of this SummaryProtocolStatsProtocolStats.  # noqa: E501

        A single protocol for which statistics should be reported.  # noqa: E501

        :return: The protocol of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :rtype: SummaryProtocolStatsProtocolStatsProtocol
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this SummaryProtocolStatsProtocolStats.

        A single protocol for which statistics should be reported.  # noqa: E501

        :param protocol: The protocol of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :type: SummaryProtocolStatsProtocolStatsProtocol
        """

        self._protocol = protocol

    @property
    def time(self):
        """Gets the time of this SummaryProtocolStatsProtocolStats.  # noqa: E501

        Unix Epoch time in seconds of the request.  # noqa: E501

        :return: The time of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SummaryProtocolStatsProtocolStats.

        Unix Epoch time in seconds of the request.  # noqa: E501

        :param time: The time of this SummaryProtocolStatsProtocolStats.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

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
        if not isinstance(other, SummaryProtocolStatsProtocolStats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
